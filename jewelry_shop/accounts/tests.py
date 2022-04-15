from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from jewelry_shop.accounts.models import Profile

UserModel = get_user_model()


class ProfileDetailsViewTests(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@gmail.com',
        'password': '12345',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'user',
        'email': 'test@gmail.com',
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile.details.html')

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_when_user_has_no_orders__orders_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()

        response = self.__get_response_for_profile(profile)
        self.assertListEqual(
            [],
            response.context['products'],
        )


class AddShippingAddressView(django_test.TestCase):
    VALID_ADDRESS_CREDENTIALS = {
        'address': 'bul. Patriarh Evtimi',
        'city': 'Sofia',
        'zip_code': '1111',
        'phone_number': '1234567890',
    }
    VALID_USER_CREDENTIALS = {
        'email': 'test@gmail.com',
        'password': '12345',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'user',
        'email': 'test@gmail.com',
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def test_expect_correct_template(self):
        response = self.client.get(reverse('shipping address'))

        self.assertTemplateUsed(response, 'accounts/shipping_address.html')

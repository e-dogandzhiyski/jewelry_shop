from django import test as django_tests
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.test import Client
from jewelry_shop.accounts.models import AppUser, Profile
from jewelry_shop.shop.models import Product
from django.test import RequestFactory

from jewelry_shop.shop.views import ProductDetailsView

UserModel = get_user_model()


class ProductDetailsViewTests(django_tests.TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = AppUser.objects.create(
            email='test2@gmail.com',
            password='1234qwe',
        )

        self.profile = Profile.objects.create(
            first_name='test',
            last_name='user',
            user_id='3',
            email='test2@gmail.com',
        )

        self.product = Product.objects.create(
            name='testproduct',
            type='Chain',
            description='TestProduct',
            image='http://ring.png',
            price='24.99'
        )
        self.client = Client()

    # def test_if_user_not_authenticated__redirect_to_login(self):
    #     request = self.factory.get('/product/details/')
    #     request.user = AnonymousUser()
    #     response = ProductDetailsView.as_view()(request)
    #     self.assertEqual(response.status_code, 302)

    def test_create_product(self):
        response = self.client.get('/product-create/')
        self.assertEqual(response.status_code, 302)

    def test_edit_product(self):
        AppUser.objects.create(email='testemail@gmail.com', password='1234qwe', is_staff=1, is_superuser=0)
        Product.objects.create(name='testproduct', type='Chain', description='TestDescription', image='http://ring.png',
                               price='24.99')

        response = self.client.get('/product/edit/1')
        self.assertEqual(response.status_code, 301)

    # def test_delete_product(self):
    #     delete_response = self.client.get('/product/delete/1')
    #     self.assertEqual(delete_response.status_code, 404)

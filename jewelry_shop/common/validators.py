from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def validate_only_numbers(value):
    for num in value:
        if not num.isdigit():
            raise ValidationError('Value must contain only numbers')


def validate_card_number_right_length(value):
    if not len(value) == 16:
        raise ValidationError('Card number must be 16 digits!')


def validate_cvv_number_right_length(value):
    if not len(value) == 3:
        raise ValidationError('Card number must be 16 digits!')


def validate_phone_number_len(value):
    if not len(value) == 10:
        raise ValidationError('Phone number is incorrect!')


def validate_zip_code(value):
    if not len(value) == 4:
        raise ValidationError('Incorrect Zip code! Zip codes have 4 numbers.')
from django.forms import ValidationError


def validate_value(value):
    if value < 0:
        raise ValidationError(f'Значение {value} не может быть отрицательным')
    return value

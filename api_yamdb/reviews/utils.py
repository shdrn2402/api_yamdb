from django.core.exceptions import ValidationError


def username_validation(username):
    if username == 'me':
        raise ValidationError("Username can't be 'me'")

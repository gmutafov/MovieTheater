from django.core.exceptions import ValidationError

def validate_capitalized(value):
    if not value[0].isupper():
        raise ValidationError("This field must start with a capital letter.")

def only_letters(value):
    if not value.isalpha():
        raise ValidationError("This field must contain only letters.")
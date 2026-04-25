import re

class ValidationError(Exception):
    pass

def validate_username(username):
    if not isinstance(username, str):
        raise ValidationError('Username must be a string')
    if len(username) < 3 or len(username) > 20:
        raise ValidationError('Username must be between 3 and 20 characters')
    if not re.match('^[a-zA-Z0-9_]*$', username):
        raise ValidationError('Username can only contain letters, numbers, and underscores')
    return True


def validate_email(email):
    if not isinstance(email, str):
        raise ValidationError('Email must be a string')
    if not re.match('^[\w\.-]+@[\w\.-]+\.\w+$', email):
        raise ValidationError('Invalid email format')
    return True


def validate_password(password):
    if not isinstance(password, str):
        raise ValidationError('Password must be a string')
    if len(password) < 8:
        raise ValidationError('Password must be at least 8 characters long')
    if not re.search('[A-Z]', password):
        raise ValidationError('Password must contain at least one uppercase letter')
    if not re.search('[a-z]', password):
        raise ValidationError('Password must contain at least one lowercase letter')
    if not re.search('[0-9]', password):
        raise ValidationError('Password must contain at least one digit')
    return True
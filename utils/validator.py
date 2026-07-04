import re


def is_valid_email(email):
    """
    Validate email format.
    """

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    """
    Pakistani mobile number validation.
    Example:
    03123456789
    """

    pattern = r'^03\d{9}$'

    return re.match(pattern, phone) is not None


def is_valid_status(status):
    """
    Validate customer status.
    """

    allowed = [
        "Active",
        "Inactive",
        "Suspended"
    ]

    return status in allowed
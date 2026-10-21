import re

def is_valid_phone_number(phone):
    pattern = re.match(r"^\d{3}-\d{3}-\d{4}$", phone)
    return bool(pattern)

is_valid_phone_number("123-456-7890")
is_valid_phone_number("1234567890")
is_valid_phone_number("123-45-6789")
is_valid_phone_number("abc-def-ghij")
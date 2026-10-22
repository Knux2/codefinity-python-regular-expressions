import re

def is_strong_password(password: str) -> bool:
     return bool(re.fullmatch(
         r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$',
         password
     ))

print(is_strong_password("Abcdef1!"))
print(is_strong_password("weakpass"))
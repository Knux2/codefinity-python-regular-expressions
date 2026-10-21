import re

def extract_dates(text):
    pattern = re.findall(r"\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b", text)
    return pattern

print(extract_dates("Important dates: 2025-10-23, 12/05/2024, and 1999-01-01."))
print(extract_dates("No valid date here, but maybe 31/12/2023 and 2024-07-04 are fine."))
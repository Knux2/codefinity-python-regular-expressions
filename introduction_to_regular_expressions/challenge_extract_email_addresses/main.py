import re

def extract_emails(text):
    email_address = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}", text)
    return email_address

print(extract_emails("Contact us at support@example.com or sales@shop.co.uk for details."))
print(extract_emails("Invalid: user@@example.com, correct: hello.world123@mail.io"))
import re

def find_words_starting_with_a(text):
    uppercase_letters = re.findall(r"\bA\w*", text)
    return uppercase_letters

print(find_words_starting_with_a("Alice and Bob met Amy at an Airport."))
print(find_words_starting_with_a("Amazing! An_underscore, A1, and A-B were noted; also an apple."))
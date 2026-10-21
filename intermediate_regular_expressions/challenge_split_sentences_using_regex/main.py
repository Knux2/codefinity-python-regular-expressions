import re

def split_sentences(paragraph):
    pattern = r"[^.!?]+[.!?]"
    return [s.strip() for s in re.findall(pattern, paragraph, re.DOTALL)]

print(split_sentences("Hello world. How are you? I'm fine!"))
print(split_sentences("First sentence across " + 
                      "multiple lines! Second one."))
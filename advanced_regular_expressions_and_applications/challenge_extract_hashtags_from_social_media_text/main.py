import re

def extract_hashtags(text):
    hashtags = re.findall(r'(?<!\w)#\w+|#+$', text)
    return hashtags

extract_hashtags("Excited for the #Python3_12 release! #coding #AI #100DaysOfCode")
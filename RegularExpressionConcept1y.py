import re

text = "Contact me at 123-456-7890"
print("Text:", text)
digits = re.findall(r"\d+", text)
print("Digits found:", digits)

updated_text = re.sub(r"\d", "X", text)
print("Updated text:", updated_text)
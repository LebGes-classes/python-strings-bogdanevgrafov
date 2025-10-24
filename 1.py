import re

text = input()
words = re.findall(r"\b\w+\b", text)

reversed_words = ''
reversed_text = ''

for word in words:
    reversed_words = word + ' ' + reversed_words

for ch in text:
    reversed_text = ch + reversed_text
    
print(reversed_words)
print(reversed_text)
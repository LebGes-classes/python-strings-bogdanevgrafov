import re

text = input("Введите текст:\n")

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
lower = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

converted = ""

for ch in text:
    if ch in upper:
        index = 0

        while index < len(upper) and upper[index] != ch:
            index += 1

        if index < len(lower):
            converted += lower[index]
        else:
            converted += ch
    else:
        converted += ch

str_lst = re.findall(r"\b\w+\b", converted)
words = {}

for word in str_lst:
    found = False
    for key in words:
        if key == word:
            words[key] += 1
            found = True
    if not found:
        words[word] = 1

words_srt = list(words.items())

for i in range(len(words_srt)):
    for j in range(len(words_srt)):
        if words_srt[i][1] > words_srt[j][1]:
            temp = words_srt[i]
            words_srt[i] = words_srt[j]
            words_srt[j] = temp

print(f'Топ {len(words_srt) if len(words_srt) < 5 else 5} самых частых слов:')

count = 0

while count != len(words_srt) and count != 5:
    print(words_srt[count])
    count += 1

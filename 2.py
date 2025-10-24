low_char = 'abcdefghijklmnopqrstuvwxyz'
high_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

tet = input()
text = ''

if '.' not in tet:
    tet = tet + '.'

CharNotDot = True
i = 0

while CharNotDot:
    text += tet[i]
    
    if tet[i] == '.':
        CharNotDot = False
        
    i += 1

K = 0
mx = 0

for ch in text:
    mx += 1
    if ch in " .":
        mx = 0
    if mx > K:
        K = mx
    
new_text = ''
DotInText = False
chars = 0
l = 0

while DotInText == False:
    for j in range(26):
        if text[l] == low_char[j]:
            new_text += low_char[(j+K)%26]
    
    for m in range(26):
        if text[l] == high_char[m]:
            new_text += high_char[(m+K)%26]
    
    if text[l] not in low_char + high_char:
        new_text += text[l]

    if text[l] == '.':
        DotInText = True
    
    if text[l] in (low_char + high_char):
        chars += 1
    else: 
        chars = 0
    
    if chars == 20:
        new_text += ' '
        chars = 0
    
    l += 1
    
print(new_text)
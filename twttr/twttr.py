text = input('Input: ')
no_vowel = []
for i in range(len(text)):
    if not text[i].lower() in ['a', 'e', 'i', 'o', 'u']: no_vowel.append(text[i])

print(''.join(no_vowel))

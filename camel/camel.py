text = input('Enter a camelCased Word: ')
snakeCased = []
for i in range(len(text)):
    if(text[i].isupper()): snakeCased.append('_' + text[i].lower())
    else: snakeCased.append(text[i])


print(''.join(snakeCased)) if len(snakeCased) > 0 else print(text)

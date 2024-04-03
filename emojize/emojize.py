import emoji
input = input('Input: ').strip()
print(f'Output: {emoji.emojize(input, language='alias')}')

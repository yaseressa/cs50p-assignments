text = input('What is the Great Question of Life, the Universe and Everything: ').strip()

if text == '42' or text.lower().replace('-', ' ') == 'forty two':
    print('Yes')
else:
    print('No')

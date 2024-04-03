text = input('Greet Me!!! ').strip().lower()
if text == 'hello':
    print('$0')
elif text == 'hello, newman':
    print('$0')
elif text.startswith('h'):
    print('$20')
else:
    print('$100')

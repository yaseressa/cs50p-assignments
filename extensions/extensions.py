text = input('Enter a File: ').strip().lower()

if text.endswith('.gif') or text.endswith('.jpg') or text.endswith('.jpeg') or text.endswith('.png') :
    if( text.split('.')[-1] == 'jpg'):
        print('image/jpeg')
    else:
        print('image/' + text.split('.')[-1])
elif text.endswith('.pdf') or text.endswith('.zip'):
    print('application/' + text.split('.')[-1])
elif text.endswith('.txt'):
    print('text/plain')
else:
    print('application/octet-stream')

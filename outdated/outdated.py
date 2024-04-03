m = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}

while True:
    try:
        date = input('Enter a Date: ')
        if len(date.split('/')) == 3 and 1 <= int(date.split('/')[0]) <= 12 and (1 <= int(date.split('/')[1]) <= 31) and (int(date.split('/')[2])) > 0:
            print(f'{int(date.split('/')[2]):04}-{int(date.split('/')[0]):02}-{int(date.split('/')[1]):02}'.strip())
            break
        elif len(date.split(' ')) == 3 and m[date.split(' ')[0].title()]  and (1 <= int(date.split(' ')[1][:-1]) <= 31) and (',' in date.split(' ')[1]) and (int(date.split(' ')[2])) > 0:
            print(f'{int(date.split(' ')[2]):04}-{int(m[date.split(' ')[0]]):02}-{int(date.split(' ')[1][:-1]):02}'.strip())
            break
        else: raise ValueError()
    except:
        pass







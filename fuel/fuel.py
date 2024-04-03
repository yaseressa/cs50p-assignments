from functools import reduce
while True:
    try:
        text = input('Fraction: ').split('/')
        expr = reduce(lambda x, y: int(x) / int(y), text)
        if(text[0].isnumeric() and text[1].isnumeric() and int(text[0]) <= int(text[1])):
            print(f'{round(expr * 100)}%') if 0.99 > expr > 0.1 else (print('F') if expr >= 0.99 else print('E'))
            break
    except:
        pass

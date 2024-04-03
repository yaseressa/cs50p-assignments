text = input('Enter an expression: ').split()

match text[1]:
    case '+' | '-' | '*' |  '/':
        print(float(eval(''.join(text))))

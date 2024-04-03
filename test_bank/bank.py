def main():
    print(value(input('Greet Me!!! ')))


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting == 'hello':
        return(0)
    elif greeting == 'hello, newman':
        return(0)
    elif greeting.startswith('h'):
        return(20)
    return(100)



if __name__ == "__main__":
    main()

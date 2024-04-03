from functools import reduce
def main():
    while True:
        try:
            gauge(convert(input('Fraction: ')))
        except:
            pass

def convert(fraction):
    fraction = fraction.strip().split('/')
    if int(fraction[1]) == 0:
        raise ZeroDivisionError()
    if int(fraction[0]) > int(fraction[1]):
        raise ValueError()
    return reduce(lambda x, y: int(x) / int(y), fraction)

def gauge(percentage):
    if 0.99 > percentage > 0.1:
        return (f'{round(percentage * 100)}%')
    else:
        if percentage >= 0.99: return('F')
        else: return('E')
if __name__ == "__main__":
    main()

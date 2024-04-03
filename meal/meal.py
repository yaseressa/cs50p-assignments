def main():
    time = convert(input('Enter a Time: ').strip())
    if time >= 7 and time <= 8:
        print('breakfast time')
    elif time >= 12 and time <= 13:
        print('lunch time')
    elif time >= 18 and time <= 19:
        print('dinner time')

def convert(time):
    x = float(time.split(':')[0])
    y = (float(time.split(':')[1]) / 60)
    return float('%.2f' % (x + y))


if __name__ == "__main__":
    main()

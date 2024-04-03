def main():
    coke_machine(50)

def coke_machine(n):
    while n > 0:
        print(f'Amount Due: {n}')
        coin = int(input('Insert Coin: '))
        if coin in [25, 10, 5]:
            n -= coin
    print(f'Change Owed: {-n}')

main()

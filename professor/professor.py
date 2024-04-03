import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y, i = generate_integer(level), generate_integer(level), 1
        r_sol = x + y
        while True:
            try:
                sol = int(input(f'{x} + {y} = ').strip())
                if sol != r_sol:
                    raise ValueError()
                score += 1
                break
            except:
                if i < 3:
                    print('EEE')
                    i += 1
                elif i >= 3 and sol != r_sol:
                    sol = r_sol
                    print(f'{x} + {y} = {sol}')
                    break
                pass
    print(f'Score: {score}')


def get_level():
    while True:
        try:
            lvl = int(input('Level: ').strip())
            if(not (lvl in [1, 2, 3])):
                raise ValueError()
            return lvl
        except:
            pass


def generate_integer(level):
    return random.randint(0, int('9' * level)) if level == 1 else random.randint(int('1' + '0' * (level - 1)), int('9' * level))


if __name__ == "__main__":
    main()

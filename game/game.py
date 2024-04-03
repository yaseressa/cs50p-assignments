import random
while True:
    try:
        to_g = random.randint(1, int(input('Level: ')))
        while True:
            try:
                guessed = int(input('Guess: '))
                if guessed == to_g:
                    print('Just right!')
                    break
                elif guessed < to_g:
                    print('Too small!')
                else:
                    print('Too large!')
            except ValueError:
                pass
        break
    except ValueError:
        pass



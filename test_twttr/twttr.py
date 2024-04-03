def main():
    print(shorten(input('Input: ').strip()))


def shorten(word):
    no_vowel = []
    for i in range(len(word)):
        if not word[i].lower() in ['a', 'e', 'i', 'o', 'u']: no_vowel.append(word[i])
    return ''.join(no_vowel)


if __name__ == "__main__":
    main()

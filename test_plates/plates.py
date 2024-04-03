import string

def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s: str):
    s = s.upper().strip()
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        i, l = False, True
        for j in s:
            if j not in string.punctuation:
                if i ^ l:
                    if j.isnumeric() and int(j) != 0:
                        i, l = True, False
                    elif j.isnumeric() and l and not i and int(j) == 0:
                        i = l = True
                    elif j.isalpha() and not i:
                        i, l = False, True
                    elif j.isalpha() and i:
                        i = l = True
            else:
                i = l = True
                break
        return not (i and l)
    return False

if __name__ == "__main__":
    main()

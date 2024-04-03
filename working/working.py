import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if match := re.search(r'^(?:([01]?[0-9])(\:[0-5]?[0-9])?\s(PM|AM)) to ([01]?[0-9])(\:[0-5]?[0-9])?\s(PM|AM)$', s, re.IGNORECASE):
        if match.group(2) and ':' in match.group(2) and match.group(5) and ':' in match.group(5):
            if not( int(match.group(1)) == 12 and int(match.group(2)[1:]) > 0) and not( int(match.group(4)) == 12 and int(match.group(5)[1:]) > 0 ) and int(match.group(1)) <= 12 and int(match.group(4)) <= 12:
                if match.group(3).lower() == 'pm' and match.group(6).lower() == 'pm':
                    pm1 = match.group(1)
                    pm2 = match.group(4)
                    return f'{str(int(pm1) + 12).zfill(2) if int(pm1) + 12 < 24 else '12'}{match.group(2)} to {str(int(pm2) + 12).zfill(2) if int(pm2) + 12 < 24 else '12'}{match.group(5)}'
                elif match.group(3).lower() == 'pm':
                    pm = match.group(1)
                    return f'{str(int(pm) + 12).zfill(2)  if int(pm) + 12 < 24 else '12'}{match.group(2)} to {str(int(match.group(4))).zfill(2) if int(match.group(4)) != 12 else '00'}{match.group(5)}'
                elif match.group(6).lower() == 'pm':
                    pm = match.group(4)
                    return f'{str(int(match.group(1))).zfill(2) if int(match.group(4)) != 12 else '00'}{match.group(2)} to {str(int(pm) + 12).zfill(2)  if int(pm) + 12 < 24 else '12'}{match.group(5)}'
            else: raise ValueError()
        else:
            if int(match.group(1)) <= 12 and int(match.group(4)) <= 12:
                if match.group(3).lower() == 'pm' and match.group(6).lower() == 'pm':
                    pm1 = match.group(1)
                    pm2 = match.group(4)
                    return f'{str(int(pm1) + 12).zfill(2) if int(pm1) + 12 < 24 else '12'}:00 to {str(int(pm2) + 12).zfill(2) if int(pm2) + 12 < 24 else '12'}:00'
                elif match.group(3).lower() == 'pm':
                    pm = match.group(1)
                    return f'{str(int(pm) + 12).zfill(2) if int(pm) + 12 < 24 else '12'}:00 to {str(int(match.group(4))).zfill(2) if int(match.group(1)) != 12 else '00'}:00'
                elif match.group(6).lower() == 'pm':
                    pm = match.group(4)
                    return f'{str(int(match.group(1))).zfill(2) if int(match.group(1)) != 12 else '00'}:00 to {str(int(pm) + 12).zfill(2) if int(pm) + 12 < 24 else '12'}:00'
            else: raise ValueError()
    else:
        raise ValueError()

if __name__ == "__main__":
    main()

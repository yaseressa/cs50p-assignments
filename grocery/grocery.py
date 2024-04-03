import operator
total = {}
while True:
    try:
        item = input().lower().strip()
        if total.get(item):
            total[item] += 1
        else: total[item] = 1
    except EOFError:
        for k, v in dict(sorted(total.items())).items():
            print(v, k.upper())
        break

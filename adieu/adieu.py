text_ = []
while True:
    try:
        text = input().strip()
        text_.append(text)
    except EOFError:
        s ='Adieu, adieu, to '
        for i in range(len(text_)):
            if i == len(text_) - 2:
                if len(text_) == 2:
                    s += text_[i] + ' and '
                    continue
                s += text_[i] + ', and '
                continue

            if i == len(text_) - 1:
                 s += text_[i]
                 continue
            s += text_[i] + ', '
        print(s)
        break


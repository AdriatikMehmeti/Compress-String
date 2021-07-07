def compress(a=list(a)):
    rez = ''
    count = 1
    for i in range(len(a)):
        try:
            old = a[i]
            new = a[i + 1]
            if old == new:
                count += 1
            else:
                rez = rez + old + str(count) if count > 1 else rez + old;
                count = 1
        except IndexError as e:
            rez = rez + old + str(count) if count > 1 else rez + old
    return rez

def perevod_v_desatichnuu(osnovanie, c):
    if osnovanie <= 10:
        result = 0
        lyst = list(c)
        length = len(lyst)-1
        for i in range(len(lyst)):
            lyst[i] = int(lyst[i])
            result = result+lyst[i]*osnovanie**length
            length = length-1
        return result
    elif osnovanie > 10:
        result = 0
        lyst = list(c)
        length = len(lyst)-1
        for i in range(len(lyst)):
            if lyst[i] == 'A':
                lyst[i] = '10'
            if lyst[i] == 'B':
                lyst[i] = '11'
            if lyst[i] == 'C':
                lyst[i] = '12'
            if lyst[i] == 'D':
                lyst[i] = '13'
            if lyst[i] == 'E':
                lyst[i] = '14'
            if lyst[i] == 'F':
                lyst[i] = '15'
            lyst[i] = int(lyst[i])
            result = result+lyst[i]*osnovanie**length
            length = length-1
        return result


def perevod_iz_desaticnoi(b, c):
    c = int(c)
    ost = c
    lyst = []
    while ost != 0:
        cifra = ost % b
        if cifra == 10:
            cifra = 'A'
        if cifra == 11:
            cifra = 'B'
        if cifra == 12:
            cifra = 'C'
        if cifra == 13:
            cifra = 'D'
        if cifra == 14:
            cifra = 'E'
        if cifra == 15:
            cifra = 'F'
        lyst.append(cifra)
        ost = ost//b
    lyst.reverse()
    for i in range(len(lyst)):
        lyst[i] = str(lyst[i])
    result = ''.join(lyst)
    return result


print('Из какой системы переводим?(Укажите основание системы: 1-16)')
osnovanie = int(input())
print('В какую систему переводим?(Укажите основание системы: 1-16)')
b = int(input())
print('Введите число')
c = input()
if b == 10:
    result = perevod_v_desatichnuu(osnovanie, c)
    print(result)
else:
    c = perevod_v_desatichnuu(osnovanie, c)
    result = perevod_iz_desaticnoi(b, c)
    print(result)

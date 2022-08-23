h = str(input('Digite um número Decimal ou Hexadecimal: ')).upper()
nc = n = total = dividendo = resto = quociente = 0
convertido = list()
r = list()
if h[1] == 'X':
    print('Você digitou um valor Hexadecimal que será convertido para Decimal')
    n = list(h)
    del n[:2]
    for i, e in enumerate(reversed(n)):
        if e == 'A':
            nc = 16 ** i * 10
            convertido.append(nc)
        elif e == 'B':
            nc = (16 ** i) * 11
            convertido.append(nc)
        elif e == 'C':
            nc = 16 ** i * 12
            convertido.append(nc)
        elif e == 'D':
            nc = 16 ** i * 13
            convertido.append(nc)
        elif e == 'E':
            nc = 16 ** i * 14
            convertido.append(nc)
        elif e == 'F':
            nc = 16 ** i * 15
            convertido.append(nc)
        else:
            e = int(e)
            nc = (16 ** i) * e
            convertido.append(nc)
    for g in convertido:
        total += g
    print(f'O valor {h} Hexadecimal corresponde a {total} Decimal')

else:
    print('Você digitou um valor Decimal que será convertido para Hexadecimal')
    n = int(h)
    while n >= 16:
        quociente = n // 16
        resto = n % 16
        r.append(resto)
        n = quociente
    r.append(n)
    print(f'O valor {h} em Decimal corresponde a 0x', end='')
    for e in reversed(r):
        if e > 9:
            if e == 10:
                print("A", end='')
            elif e == 11:
                print("B", end='')
            elif e == 12:
                print("C", end='')
            elif e == 13:
                print("D", end='')
            elif e == 14:
                print("E", end='')
            elif e == 15:
                print("F", end='')
        else:
            print(f'{e}', end='')
    print(" em Hexadecimal")
    

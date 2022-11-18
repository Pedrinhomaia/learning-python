import random
print('qual dado deseja rolar? ')
print('d100,d20,d10,d6,d4,dx, e digite 0 para parar')
while True:
    res = input('>>>>')
    if res == 'd100' or res == 'D100':
        d100 = random.randint(0,100)
        print(d100)
        if d100 == 1:
            print ('cagou demais')
        elif d100 == 100:
            print('se ferrou')
    elif res == 'd20' or res == 'D20':
        d20 = random.randint(0,20)
        print(d20)
        if d20 == 1:
            print('desastre')
        elif d20 == 20:
            print('critico')
    elif res == 'd10' or res == 'D10':
        d10 = random.randint(0,10)
        print(d10)
    elif res == 'd6' or res == 'D6':
        d6 = random.randint(0,6)
        print(d6)
    elif res == 'd4' or res == 'D4':
        d4 = random.randint(0,4)
        print(d4)
    elif res == 'dx' or res == 'Dx' or res == 'DX' or res == 'dX':
        d = int(input('qual o valor do dado que você deseja rolar? '))
        dx = random.randint(0,d)
        print(dx)
    elif res == 0:
        break
    else:
        print('desculpe não entendi')

import random
print('qual dado deseja rolar? ')

while True:
    print('d100,d20,d10,d6,d4,dx, e digite 0 para parar')
    res = input('>>>>')
    print('deseja adicionar algum valor no dado?')
    vald = int(input('>>>>'))
    if res == 'd100' or res == 'D100':
        d100 = random.randint(1,100)+vald
        print(d100)
        print(f'[{d100+vald}] <--- {d100} + {vald}')
        if d100 == 1:
            print ('cagou demais')
        elif d100 >= 100:
            print('se ferrou')
    elif res == 'd20' or res == 'D20':
        d20 = random.randint(1,20)
        print(d20+vald)
        print(f'[{d20+vald}] <--- {d20} + {vald}')
        if d20 == 1:
            print('desastre')
        elif d20 == 20:
            print('critico')
    elif res == 'd10' or res == 'D10':
        d10 = random.randint(1,10)

        print(d10+vald)
        print(f'[{d10+vald}] <--- {d10} + {vald}')
    elif res == 'd6' or res == 'D6':
        d6 = random.randint(1,6)
        print(d6)
        print(f'[{d6+vald}] <--- {d6} + {vald}')
    elif res == 'd4' or res == 'D4':
        d4 = random.randint(1,4)
        print(d4)
        print(f'[{d4+vald}] <--- {d4} + {vald}')
    elif res == 'dx' or res == 'Dx' or res == 'DX' or res == 'dX':
        d = int(input('qual o valor do dado que você deseja rolar? '))
        dx = random.randint(1,d)
        print(dx)
        print(f'[{dx+vald}] <--- {dx} + {vald}')
    elif res == 0:
        break
    else:
        print('desculpe não entendi')
        
        
        
        
        
        

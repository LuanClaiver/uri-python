p, j1, j2, r, a = input().split()

j1 = int(j1) + int(j2)
j1 %= 2
if((r == '1') and (a == '1')):
    print('Jogador 2 ganha!')
elif((r == '1') or (a == '1')):
    print('Jogador 1 ganha!')

else:
    if(j1 == 0):
        if(p == 1):
            print('Jogador 1 ganha!')
        else:
            print('Jogador 2 ganha!')
    elif(j1 == p):
        print('Jogador 2 ganha!')
    else:
        print('Jogador 1 ganha!')
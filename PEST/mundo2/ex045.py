import random
from time import sleep
o = ('pedra', 'papel', 'tesoura')
comp = random.randint(0, 2)

j = int(input('[0]: Pedra \n[1]: Papel \n[2]: Tesoura \nEscolha uma das opções: '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
sleep(0.5)

if j == comp:
    print('-'*20)
    print('Computador escolheu {} \nJogador escolheu {}'.format(o[comp], o[j]))
    print('-'*20)
    sleep(0.5)
    print('EMPATE')
elif j == 0 and comp == 2 or j == 1 and comp == 0 or j == 2 and comp == 1:
    print('-'*20)
    print('Computador escolheu {} \nJogador escolheu {}'.format(o[comp], o[j]))
    print('-'*20)
    sleep(0.5)
    print('JOGADOR VENCE')
elif comp == 0 and j == 2 or comp == 1 and j == 0 or comp == 2 and j == 1:
    print('-'*20)
    print('Computador escolheu {} \nJogador escolheu {}'.format(o[comp], o[j]))
    print('-'*20)
    sleep(0.5)
    print('COMPUTADOR VENCE')

import random
comp = random.randint(0, 5)
from time import sleep
print('Vou pensar em um numero entre 0 e 5.. tente adivinhar')
sleep(1)
adv = int(input('Adivinhe o numero: '))
print('processando..')
sleep(1)
if adv == comp:
    print('Parabens! Você ganhou')
else: 
    print('Você perdeu.. o numero certo era {}'.format(comp))
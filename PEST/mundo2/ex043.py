from re import A
from time import sleep
p = float(input('\033[4mCalculando seu IMC \nDigite o seu peso: '))
a = float(input('\033[4mDigite a sua altura: '))

aa = a*a 
imc = p/aa
print('Calculando..')
sleep(1)

if imc < 18.5:
    print('Seu IMC é {:.1f}: ABAIXO DO PESO'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.1f}: PESO IDEAL'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.1f}: SOBREPESO'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.1f}: OBESIDADE'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}: OBESIDADE MORBIDA'.format(imc))
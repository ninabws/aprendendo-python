nn = int(input('Digite um numero: '))
n = input('Conversao: \nDigite 1 para binario, 2 para octal ou 3 para hexadecimal: ')

if n == '1':
    print('Numero {} em binario: {}'.format(nn, format(nn, 'b')))
elif n == '2':
    print('Numero {} em octal: {}'.format(nn, format(nn, 'o')))
elif n == '3':
    print('Numero {} em hexadecimal: {}'.format(nn, format(nn, 'x')))
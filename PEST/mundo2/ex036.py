cs = float(input('Digite o valor da casa: '))
sc = float(input('Digite seu salario: '))
an = int(input('Digite em quantos anos você vai pagar a casa: '))

prest = cs/ (an*12)
min = sc*0.3
print('A prestaçao sera de {:.2f}'.format(prest))

if prest <= min:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: ')) 

if n1 > n2: 
    print('O primeiro numero é o maior')
elif n2 > n1:
    print('O segundo numero é o maior')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais')

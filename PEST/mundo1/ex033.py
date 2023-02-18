n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: ')) 
n3 = int(input('Terceiro valor: '))

if n1 < n2 and n1 < n3:
    print('{} é o menor numero'.format(n1))
elif n2 < n3 and n2 < n1:
    print('{} é o menor numero'.format(n2))
elif n3 < n2 and n3 < n1:
        print('{} é o menor numero'.format(n3))

if n1 > n2 and n1 > n3: 
    print('{} é o maior numero'.format(n1))
elif n2 > n3 and n2 > n1:
     print('{} é o maior numero'.format(n2))
elif n3 > n2 and n3 > n1:
     print('{} é o maior numero'.format(n3))


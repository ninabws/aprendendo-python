frase = input('Digite uma frase: ').strip()

f = frase.lower()
print('A letra A aparece {} vezes na frase'.format(f.count('a')))
print('A primeira letra A apareceu na posiçao {}'.format(f.find('a')+1)) 
print('A ultima letra A apareceu na posiçao {}'.format(f.rfind('a')+1))
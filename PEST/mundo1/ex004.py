a = input('Digite algo: ')
print('Tipo primitivo: {}'.format(type(a)))
print('Somente espaços?: {}'.format(a.isspace()))
print('É um número?: {}'.format(a.isnumeric()))
print('É alfabetico?: {}'.format(a.isalpha()))
print('É alfanúmerico?: {}'.format(a.isalnum()))
print('Esta em maiusculo?: {}'.format(a.isupper()))
print('Esta em minusculo?: {}'.format(a.islower()))
print('Esta capitalizada?: {}'.format(a.istitle()))
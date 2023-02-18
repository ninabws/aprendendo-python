nc = input('Digite seu nome completo: ').strip()

print('Nome em letras maiusculas: {}'.format(nc.upper()))
print('Nome em letras minusculas: {}'.format(nc.lower()))
print('Quantas letras ao todo tem o nome: {}'.format(len(nc) - nc.count(' ')))
print('Quantas letras tem o primeiro nome: {}'.format(nc.find(' ')))
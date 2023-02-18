km = float(input('Digite a quantidade de Km percorridos pelo carro alugado: '))
dias = int(input('Digite a quantidade de dias pelos quais ele foi alugado: '))

d = dias*60
k = km*0.15
t = d+k

print(f'O preço total a ser pago pelo carro alugado é {t}')
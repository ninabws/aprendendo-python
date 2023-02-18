d = int(input('Digite a distancia da sua viagem em km/h: '))

if d <= 200:
    print('O valor da sua passagem para sua viagem de {}km/h é R${:.2f}'.format(d, d*0.50))
else:
    print('O valor da sua passagem para uma viagem mais longa é R${:.2f}'.format(d*0.45))
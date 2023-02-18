vel = int(input('Digite a velocidade atual do seu carro: '))
mul = (vel-80) *7
if vel > 80:
    print('Você foi multado por dirijir ha mais de 80km/h. Terá que pagar R${} de multa'.format(mul))
else:
    print('Tudo ok, você esta cumprindo o limite de 80km/h.')
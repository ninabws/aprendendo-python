from datetime import date
ano = date.today().year
a = int(input('Digite o ano que você nasceu: '))
id = (ano - a)

if id == 18:
    print('Você ja tem 18 anos, ja esta na hora de se alistar')
elif id < 18:
    saldo = 18 - id
    al = saldo + ano
    print('Voce tem {} anos \nAinda faltam {} anos para o alistamento \nSeu alistamento sera em {}'.format(id, saldo, al))
elif id > 18:
    saldo = id - 18
    al = ano - saldo
    print('Voce tem {} anos \nJa se passaram {} anos do seu alistamento \nSeu alistamento foi em {}'.format(id, saldo, al))
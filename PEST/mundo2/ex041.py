from datetime import date
atual = date.today().year
at = int(input('Digite o ano de nascimento do atleta: '))

id = atual - at

if id <= 9:
    print('O atleta tem {} anos, portanto esta na categoria MIRIM'.format(id))
elif id > 9 and id <= 14:
    print('O atleta tem {} anos, portanto esta na categoria INFANTIL'.format(id))
elif id > 14 and id <= 19:
    print('O atleta tem {} anos, portanto esta na categoria JUNIOR'.format(id))
elif id > 19 and id <= 25:
    print('O atleta tem {} anos, portanto esta na categoria SENIOR'.format(id))
elif id > 25:
    print('O atleta tem {} anos, portanto esta na categoria MASTER'.format(id))

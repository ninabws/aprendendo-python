s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: ')) 
s3 = float(input('Terceiro segmento: '))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s1+s2: 
    print('Os segmentos podem se tornar um triangulo!')
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('Classificaçao: EQUILATERO')
    elif s1 != s2 != s3 != s1:
        print('Classificaçao: ESCALENO')
    else:
        print('Classificaçao: ISOSCELES')
else:
    print('Os segmentos nao podem se tornar um triangulo') 
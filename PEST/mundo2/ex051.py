print('-'*20)
print('10 TERMOS DE UMA P.A')
print('-'*20)

p = int(input('primeiro termo: '))
r = int(input('razao: '))
d = p +(10-1)*r
for c in range(p, d, r):
    print('{}'.format(c), end = ' → ')
print('fim')

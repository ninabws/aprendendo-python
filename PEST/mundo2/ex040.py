from time import sleep
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

m = n1+n2
mf = m/2
print('-'*20)
print('calculando..')
print('-'*20)
sleep(1)
print('Sua media ficou {:.1f}, resultado:'.format(mf))
sleep(0.5)
if mf < 5.0:
    print('\033[1;31mREPROVADO')
elif mf >= 5.0 and mf <= 6.9:
    print('\033[1;33mRECUPERAÇAO')
elif mf >= 7.0:
    print('\033[1;32mAPROVADO')
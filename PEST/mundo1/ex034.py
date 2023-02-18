sal = float(input('Digite o salario do funcionario: R$ '))

if sal > 1250.00:
    print('O salario de {:.2f} passou a ser {:.2f}'.format(sal, sal+sal*0.10))
elif sal <= 1250.00:
     print('O salario de {:.2f} passou a ser {:.2f}'.format(sal, sal+sal*0.15))
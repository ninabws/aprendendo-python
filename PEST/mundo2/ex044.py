p = float(input('Digite o valor da compra:'))
m = input('[1]: à vista dinheiro/cheque \n[2]: à vista no cartão \n[3]: em até 2x no cartão \n[4]: 3x ou mais no cartão \nQual seu metodo de pagamento?: ')

if m == '1':
    d = p-p*0.10
    print('O valor final da sua compra é de R${:.2f}'.format(d))
elif m == '2':
    d = p-p*0.05
    print('O valor final da sua compra é de R${:.2f}'.format(d))
elif m == '3':
    tot = p
    d = p/2
    print('O valor a pagar da sua compra parcelado em 2x é de R${:.2f}'.format(d))
    print('O valor da sua compra de R${:.2f} fica R${:.2f} no total'.format(p, tot))
elif m == '4':
    d = p+p*0.20
    tp = int(input('Em quantas vezes você deseja parcelar?: '))
    par = d/tp
    print('O valor a pagar da sua compra parcelado em {} vezes com juros de 20% é de R${:.2f}'.format(tp, par))
    print('O valor da sua compra de R${:.2f} fica R${:.2f} no total'.format(p, d))
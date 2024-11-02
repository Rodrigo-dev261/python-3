preco_produto = float(input('Qual o preco do produto? '))
desconto = (preco_produto / 100) * 5
preco_com_desconto = preco_produto - desconto
print('O preco desse produto ira ficar R${:.2f} com 5% de desconto.'.format(preco_com_desconto))

print()
valor = int(input('Quanto voce tem em sua carteira? R$'))
cotacao = 5.86
dollar_total = valor / cotacao
print('' * 38)
print('Com R${:.2f} voce pade comprar ${:.2f}'.format(valor, dollar_total))
print()
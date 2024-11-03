salario = float(input('Quanto foi seu salario este mes? R$ '))
novo_salario = (salario / 100) * 15 + salario
print('Seu novo salario a partir do mes que vem sera de R${:.2f}'.format(novo_salario))

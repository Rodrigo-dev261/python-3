largura = float(input('Qual a largura da sua parede em metros: ')) 
altura = float(input('Qual e a altura de sua parede em metros: '))
area = largura * altura
cobertura_tinta = 2 * 2
tinta_necessaria = area / cobertura_tinta
print('Para pintar sua parede voce ira precisar de {:.1f} litros de tinta.'.format(tinta_necessaria))
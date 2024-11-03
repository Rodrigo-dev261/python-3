largura = float(input('Qual a largura da sua parede em metros: ')) 
altura = float(input('Qual e a altura de sua parede em metros: '))
area = largura * altura
cobertura = area / 2 
print('Sua parede tem a dimensao de {} X {} e sua area e de {:.1f}m².'.format(largura, altura, area))
print('Para pintar essa parede voce vai precisasr de {}L de tinta.'.format(cobertura))
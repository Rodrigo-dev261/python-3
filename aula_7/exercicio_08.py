medida = float(input('Digite um valor em Metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
ect = 100
print('A conversao de {:.0f}m e {:.0f}cm e {:.0f}mm '.format(medida, cm, mm))
print('{:.0f}m equivale a {}km'.format(medida, km))
print('{:.0f}m e igual a {} ectometros'.format(medida, (medida / ect)))
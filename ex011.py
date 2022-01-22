#Faça um programa que leia a largura e a altura de uma parede em mestros, calcule a área e a quantitdade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
print('Sua parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(altura, largura, area))
tinta = area / 2
print('Essa parede precisa de {:.1f}l de tinta'.format(tinta))

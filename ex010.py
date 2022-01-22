#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considerando dolar à 3,27 reias
real = float(input('Quanto dinheiro em R$ você tem na carteira? R$ '))
dolar = real / 3.27
print ('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))


#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por
# dia e R$ 0,15 por KM rodado.
dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram percorridos? '))
pd = dias * 60
pkm = km * 0.15
total = pd + pkm
print('O carro foi alugado por {} dias e percorreu {}KM, o valor total a se pagar é R$ {:.2f}'.format(dias, km, total))
#também podia ser feito como:
#total = (dias * 60) + (km * 0.15)


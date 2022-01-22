#Faça um algoritmo que leia o preço de um produto e mostre sua novo preço, com 5% de descontos
preco = float(input('Digite o valor do produto: R$ '))
desc = preco * 0.05
np = preco - desc
#também poderia ser feito como: np = np - (preco * 5 / 100) ou np = np - (preco*0.05)
print("O valor do produto antes era R${:.2f}, com 5% de desconto (R${:.2f}) o novo valor é R${:.2f}".format(preco, desc, np))


#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor de {}, seu antecessor é {} e seu sucessor é {}'.format(n, a, s))
#Também pode tirar as variaveis s e a e fazer assim: .format (n-1), (n+1)
#Quanto menos variáveis, mais memória se economiza.




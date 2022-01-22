#Programa que mostre o dobro, o triplho e a raiz quadrada de um número
n = int(input('Digite algum número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro de {} é {};\nO triplo é {}; \nE a raiz quadrada é {:.2f}.'.format(n, dobro, triplo, raiz))

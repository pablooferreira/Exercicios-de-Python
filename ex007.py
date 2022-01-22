#Desenvolver um programa que leia as duas notas de um aluno e calcule a média das notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A primeira nota foi {:.1f}; \nA segunda foi {:.1f}; \nEntão a média é: {:.1f}.'.format(n1, n2, media))
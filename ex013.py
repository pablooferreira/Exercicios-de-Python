#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o salário: R$ '))
nsalario = salario * 1.15
print('O salário antigo era: R${:.2f} e com o aumento de 15% passa a ser: R${:.2f}'.format(salario, nsalario))


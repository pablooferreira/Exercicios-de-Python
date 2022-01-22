#Escreva um programa que leia um valor em mestro e o exiba convertir em centímetros e milímetros
m = float(input('Uma distância em metros: '))
mm = m *1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('{} METROS é {} MILÍMETROS,{} CENTÍMETROS, {} DECÍMETROS, {} DECÂMETROS, {} HECTROMETORS e {} KILÔMETROS'.format(m, mm, cm, dm, dam, hm, km))

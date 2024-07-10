# faça um programa que leia um numero 
# inteiro qualquer e mostre sua taboada.

numero = int(input("Digite um número inteiro: "))

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# crie um programa que leia um numero real qualquer pelo teclado e mostre na 
# tela a sua porção inteira.

from math import trunc
num = float(input("Digite um número real: "))
print("A parte inteira de {} é igual a {}".format(num, trunc(num)))


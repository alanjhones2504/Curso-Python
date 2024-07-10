# faça um programa que leia a largura e altura de uma pareide em 
# metros quadrado, e calcule sua area, e a quantidade de tinta 
# necessaria para pintala, sabendo que cada litro de tinta 
# pinta uma area de dois metros quadrados

largura = float(input("qual a largura?: "))
altura = float(input("qual a altura?: "))
pareide = largura * altura
litrosTintas = pareide / 4

print(f"A area da pareide é {pareide} metros")
print(f"A quantidade de tinta é {litrosTintas} litros")

#faça um algoritimo que leia o salario de um funcionario e mostre 
#seu novo salario, com 15% de almento


salario = float(input("qual o valor do salario? R$"))
novo = salario + (salario * 15 / 100)
print(f"O salario de {salario} mais 15% de reajuste fica {novo:.2f}")


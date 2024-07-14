# faça um algoritimo que leia um preço de um produto e mostre seu 
# novo preço, com cinco porcento de desconto

preco = float(input("digite o preço do produto? R$"))
novo = preco - (preco * 5 / 100)
print(f"O produto que custa R${preco:.2f}, na promoção de 5% desconto de R${novo:.2f}")
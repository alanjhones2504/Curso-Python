# escreva um programa que pergunte a quantidade de Km
# percorrido por um carro alugado e a quantidade de dias
# pelo qual ele foi alugado. calcule o preço a pagar, 
# sabendo que o carros custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("quantos Km percorridos? "))
diaria = int(input("e quantos dias? "))

pago = (km * 0.15) + (diaria * 60)

print(f"O valor dos km mais a diaria R$ {pago}")
# lista = [2,4,3,8,9,10]

# for item in lista:
#     print(item)

# palavra = 'alan'
# for letra in palavra:
#     print(letra)

# for numero in range(0,11):
#     print(numero)

# nome = input('digite seu nome: ')
# for x in range(1, 16):
#     print(f'{x+1} {nome}')

# range(valor inicial, valor final, encremento)

# for x in range(2,20,2):
#     print(x)

#  pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')
#  for pedra in pedras:
#     if pedra == 'Quartzo':
#         continue
#     print(pedra)

# for cont_ex in range(1,6):
#    print(f'\nRodada: {cont_ex}')
#    for cont_in in range(5, 0, -1):
#         print(f'valor: {cont_in}')

import random

for A in range(1, 6):
    print(f'\nconjunto {A}')
    for B in range(5):
        print(f'valor: {B}')
        num = random.randint(1, 100)
        print(f'valor: {num}')
        


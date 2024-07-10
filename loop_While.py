# while significa enquanto um numero X for menor ou igual Y faça

# num =  1

# while (num <= 100):
#     print(num)
#     num += 1 # isso chamamos de incremento
# print('laços encerrado')

nome = None

while True:
    print('digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}') 
print('Até logo!')

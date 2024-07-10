# Simples, Composto, Encadeado
# uma condicional simples é quando so existe uma condição no caso (if)
# e uma condição composta é quando existe duas no caso (if, else)
# e uma condição encadeado é quando existem tres condições (if, elif, else)

n1 = n2 = 0.0
media = 0.0

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

# calcular a media aritimetica das duas notas
media = (n1 + n2) / 2

if (media >= 7):
    print('resultado aprovado!')
    print('parabéns')
elif (media>= 5):
    print('você esta de recuperação')
else:
    print('Aluno reprovado.....')

print('a sua media é {}'.format(media))
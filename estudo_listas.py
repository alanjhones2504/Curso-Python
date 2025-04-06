# Estudo sobre listas em Python

# Criando uma lista
frutas = ["maçã", "banana", "laranja", "uva"]
print("Lista inicial:", frutas)

# Acessando elementos da lista (índices começam em 0)
print("Primeira fruta:", frutas[0])  # maçã
print("Última fruta:", frutas[-1])   # uva

# Adicionando um elemento ao final da lista
frutas.append("manga")
print("Após adicionar manga:", frutas)

# Removendo um elemento da lista
frutas.remove("banana")
print("Após remover banana:", frutas)

# Alterando um elemento da lista
frutas[1] = "abacaxi"
print("Após alterar laranja por abacaxi:", frutas)

# Tamanho da lista
print("Tamanho da lista:", len(frutas))

# Percorrendo a lista com um loop for
print("Frutas na lista:")
for fruta in frutas:
    print(fruta)

# Verificando se um elemento está na lista
if "uva" in frutas:
    print("Sim, uva está na lista!")
else:
    print("Não, uva não está na lista.")

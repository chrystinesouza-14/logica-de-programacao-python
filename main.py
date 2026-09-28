#Listas, Tuplas e Dicionários

#1. Listas
#Listas são utilizadas para armazenar vários valores dentro de uma única variável

nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)

#2. Acessando Elementos da Lista
print(nomes[1])

#Podemos acessar o último elemento usando o -1
print(nomes[-1])

#3. Alterando Elementos

nomes[0] = "Pedro"
print(nomes)

#4. Adicionar Elementos
#append() adiciona um elemento no final da lista

nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição específica.

nomes.insert(1, "Mariana")
print(nomes)

#5. Removendo Elementos
#remove() remove um elemento pelo valor

nomes.remove("João")
print(nomes)

#pop() remove um elemento pelo índice

nomes.pop(0)
print(nomes)

#6. Tamanho da Lista
#len() informa a quantidade de elementos
print(len(nomes))

#7. Percorrendo uma Lista
for nome in nomes:
    print(nome)

#8. Verificando se um elemento existe

if "Lucas" in nomes:
    print("Lucas está na lista")
else:
    print("Lucas não está na lista")

#9. Lista com diferentes tipos de dados
dados = ["João", 18, 1.75, True]
print(dados)

#10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"Média: {media}")

#11. Tuplas
#Tuplas são semelhantes às listas.
#As tuplas não podem ser alteradas.

coordenadas = (10, 20)
print(coordenadas)

print(coordenadas[0])

#12. Dicionários
#Dicionários armezenam informações no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)

# 13. acesssando valores do dicionario

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])

# 14. alterando valores

aluno["nota"] = 9.0
print(aluno)

# 15. Adicionando novos dados
aluno["curso"] = "Informática"
print(aluno)

# 16. Removendo dados
del aluno["curso"]
print(aluno)

# 17. Percorrendo um dicionário
for chave in aluno:
    print(chave)

# Podemos acessar a chave e valor ao mesmo tempo.
for chave, valor in aluno.itens():
    print("f{chave}: {valor}")

# 18. Verificando uma chave
if "nome" in aluno:
    print("A chave nome existe.")

# 19. Dicionário com lista
aluno = {
    "nome": "Maria",
    "notas": [8.0, 7.5, 9.0]
}

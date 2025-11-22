# Truth Value Testing
#   > Repare que os valores vazios ou zeros são considerado False, do contrário são considerados True.
bool(0)     # Retorna False
bool("")    # Retorna False
bool(None)  # Retorna False
bool(1)     # Retorna True
bool(-100)  # Retorna True
bool(13.5)  # Retorna True
bool("teste")  # Retorna True
bool(True)  # Retorna True

# Método Find
"""
A função find encontra a primeira ocorrência do texto que estamos procurando e devolve o índice. Lembrando também que o 
índice começa com 0.

para mais métodos que interagem com o tipo string, acessar: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

O find também aceita um segundo parâmetro, que define a partir de qual posição gostaríamos de começar, por exemplo:
"""
palavra = "aluracursos"
palavra.find("a", 1)  # procurando "a" a partir da segunda posição  →  Retorna: 4
palavra.capitalize()  # Retorna 'Aluracursos'
palavra.endswith("alu")  # A palavra começa com 'alu'? True or False; nesse caso Retorna True
palavra.endswith("os")  # A palavra termina com 'na'? True or False; nesse caso Retorna True
palavra.lower()  # Todas as letras ficam minúsculo
palavra.upper()  # Todas as letras ficam maiúsculas
palavra.strip()  # Tira espaços do início e do final da string

# OBS: Essas funções do tipo string retornam uma string, mas não alteram a variável original.
"""
O tipo str foi criado de tal maneira que é impossível alterá-lo, qualquer função de alteração devolve uma nova string, 
que representa a alteração. Esse principio também é chamado de imutabilidade. Strings são imutáveis, são sequências 
imutáveis!
"""


# Listas (sequência de dados que podem mudar)
lista = [1, 2, 3, 4, 5, 5]
print(6 in lista)  # Retornará False pois o número 6 não existe nesta lista
print(max(lista))
print(min(lista))
print(lista.count(5))  # Retorna 2  →  Conta o número de ocorrências de um determinado elemento em uma lista

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))  # retorna o índice da primeira ocorrência de um determinado elemento em uma lista
print(frutas.index('Melancia'))  # Retorna "ValueError: 'Melancia' is not in list"
print(frutas.pop())  # Retorna 'Uva', que é o último elemento da lista, mas também o deleta da lista

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
dias.append("Sábado2")  # ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Sábado2']


# Tuplas (sequência de dados que NÃO mudam)
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")
# dias.append("Sábado2")  # AttribiteError: 'tuple' object has no attribute 'append'

p1 = (3, 5)
p2 = (4, 6)
p3 = (5, 7)
line = [p1, p2, p3]
print(line)  # Retorna uma lista contendo tuplas

tuple(line)  # Converte a lista em tupla
list(line)   # Converte a tupla em lista


pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)
instrutores = [pessoa1, pessoa2, pessoa3]
instrutores[1][1]  # Retorna '37'

# Set (sequência de dados que não permite valores duplicados)
colecao = {11122233344, 22233344455, 33344455566}
colecao.add(44455566677)  # vai adicionar pois não existe ainda. É equivalente ao 'append()' de listas
# OBS: É importante notar que o set não é uma sequência, pois não tem um índice;
# Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos
# duplicados dentro do set.


# Dictionary
instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}


# List Comprehensions
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

# Refatorando:
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]  # List Comprehension


# Leitura de arquivos
"""
Como agora o arquivo palavras.txt está na pasta do projeto jogos, devemos executar o comando que abre o terminal do Python 3 na pasta do projeto.


# Abrir o arquivo no modo de leitura, 
# > basta passar o nome do arquivo e a letra r para a função open, como já vimos no vídeo anterior:

    arquivo = open("palavras.txt", "r")
    
# Como abrimos o arquivo no modo de leitura, a função write não funciona. 
# Para ler o arquivo inteiro, utilizamos a função read:

    arquivo.read()  # Retorna 'banana\nmelancia\nmorango\nmanga\n'

# Mas se executarmos a função novamente:

    arquivo.read()  # Retorna '', ou seja, nada. Nos é retornado uma string vazia. Por quê?

# > O arquivo é como um fluxo de linhas, que começa no início do arquivo, como se fosse o ponteiro. 
# > Ele vai descendo e lendo arquivo, após ler tudo, ele fica posicionado no final do arquivo, então quando chamamos a 
# função read() novamente, não há mais conteúdo, pois ele todo já foi lido. Ou seja, para ler o arquivo novamente, 
# devemos fechá-lo e abri-lo novamente.
"""


# Lendo linha por linha do arquivo
"""
# Não queremos ler todo o conteúdo do arquivo, e sim ler linha por linha. 
Como já foi visto, um arquivo é um fluxo de linhas, uma sequência de linhas, então como é uma sequência, 
podemos fazer um for nela:

>>> arquivo = open("palavras.txt", "r")
>>> for linha in arquivo:
...     print(linha)
... 
banana

melancia

morango

manga


# Mas podemos reparar que existe uma linha entre cada fruta. Por que isso acontece? 
# Para ver melhor, vamos ler somente uma linha do arquivo, com a função readLine():

>>> arquivo = open("palavras.txt", "r")
>>> linha = arquivo.readline()
>>> linha
'banana\n'

# Há um \n ao final da linha, porque a linha sabe que ao seu final deve ser ser feita uma nova linha. Mas anteriormente havíamos feito um print, que também quebra uma linha ao final da impressão, colocando também um \n! Assim, são criadas duas novas linhas, por isso havia uma linha em branco entre as frutas.
"""

# Limpando a linha
"""
Como vimos, há um \n ao final de cada linha, de cada palavra, mas queremos somente a palavra. Já vimos como tirar 
espaços em branco no início e no fim da string, basta utilizar a função strip(), que também remove caracteres especiais,
como o \n.
"""

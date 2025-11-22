print("Ola mundo doido")
# help(print)  # help é uma função do Python. Todas as funções em Python são acompanhadas de parênteses.

"""
Inicialmente, o que nos importa são os três primeiros valores que a função print pode receber:

"value" é o valor que queremos imprimir, as reticências indicam que a função pode receber mais de um valor, basta separá-los por vírgula.
"sep=" é o separador entre os valores, por padrão o separador é um espaço em branco.
"end=" é o que acontecerá ao final da função, por padrão há uma quebra de linha, uma nova linha (\n)

Podemos apertar a tecla Q** para sair da documentação da função e **CTRL + C ou CTRL + D para sair do console de ajuda.
"""
print("Brasil ganhou 5 títulos mundiais")
print("Brasil", "ganhou", 5, "titulos mundiais", sep="-")  # Retorna 'Brasil-ganhou-5-titulos mundiais'


# Agora vamos definir uma variável:
pais = "Itália"  # Definimos a variável "pais" e atribuímos o valor "Italia", da classe String. Variáveis podem variar em seus valores, como o próprio nome diz.
quantidade = 4
print(pais, "ganhou", quantidade, "titulos mundiais")


# Tipagem do Python
type(pais)  # Retorna <class 'str'>
type(quantidade)  # Retorna <class 'int'>

"""
Mas em nenhum local definimos explicitamente que a variável pais receberá valores do tipo string. Talvez você já tenha 
visto isso em outras linguagens, como C, C++, Java, em que definimos o tipo da variável na hora da sua declaração, 
algo como:

str pais = "Brasil"

Mas isso em Python não funciona. Ou seja, no mundo Python não somos obrigados a definir explicitamente o tipo da 
variável. Podemos até passar outros tipos de valores para a variável:

pais = "Brasil"
type(pais)  # Retorna <class 'str'>

OBS: A linguagem Python possui uma tipagem dinâmica, não sendo necessário declarar o tipo de uma variável antes de 
criá-la, diferentemente de outras linguagens.

Em Python, a variável só passa a existir quando atribuímos um valor a ela.
"""

# Imprimindo datas
dia = 15
mes = 10
ano = 2015
print(dia, mes, ano, sep="/")

"""
O Python utiliza por convenção o padrão Snake_Case para nomes de variáveis (ou identificadores).

Um exemplo de variáveis em Snake_Case são:
"""
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30

"""
Em outras linguagens também se usa o padrão CamelCase. O mesmo exemplo com CamelCase (que não é o padrão do Python):

idadeEsposa = 20
perfilVip = 'Flávio Almeida'
recibosEmAtraso = 30
"""

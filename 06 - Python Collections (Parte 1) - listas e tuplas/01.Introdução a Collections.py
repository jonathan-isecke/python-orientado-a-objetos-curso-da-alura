"""
Sim, o nome do arquivo possui espaços e caracteres especiais. Salvei assim mesmo porque o professor deste curso está
utilizando outra ferramenta diferente do Pycharm, o Google Collaboratory, ou Google Colabs.

Para acessar essa ferramenta de desenvolvimento online, acessar: https://colab.research.google.com/
"""


idades = [39, 30, 27, 18]  # Funciona como um array (a uma lista de elementos e podemos acessar cada um pela posição)
print(type(idades))  # Retorna <class 'list'>

# OBS: Não confundir o funcionamento 'array' com o 'tipo array'. Em Python, existem essas duas coisas diferentemente.

len(idades)
print(idades[0])
print(idades)

idades.append(15)  # append() adiciona elementos ao fim da lista.
print(idades)
# print(idades[5])  # Retorna 'IndexError: list index out of range' pois não existe um elemento de índice 5 na lista

for idade in idades:
    print(idade)

idades.remove(30)
print(idades)

# idades.remove(30)  # Não é possível remover itens inexistentes - ValueError: list.remove(x): x not in list

idades.append(27)
print(f'Olha o 27 aqui: {idades}')
idades.remove(27)
print(idades)  # Perceba que o Python remove a primeira aparição do 27 e não a mais recente que acabamos de adicionar

# idades.clear()  # Limpa toda a lista e a torna vazia

print(f'28 está em idades? {28 in idades}')

if 15 in idades:
    idades.remove(15)
    print(idades)
    idades.append(19)


idades.insert(0, 20)
print(idades)

idades = [20, 39, 18]

# idades.append(27, 19)  # TypeError: list.append() takes exactly one argument (2 given)
idades.append([27, 19])  # Fazendo uma gambiarra aqui pra usar o append para mais de 2 elementos. Boa prática? Não!

for elemento in idades:
    print("Recebi o elemento", elemento)

# O último elemento impresso do comando anterior será 'Recebi o elemento [27, 19]'. É possível inserir um elemento lista
# dentro de outra lista; no entanto para o exemplo anterior, isso não é uma boa prática, uma vez que costumamos utilizar
# elementos de mesmo tipo dentro de uma lista. No caso, nossa lista continha valores do tipo 'int' e acrescentamos um
# diferente, do tipo 'list'.

idades.remove(idades[3])
idades.extend([27, 19])  # Esse é o uso correto quando queremos adicionar mais de um item de mesmo tipo em uma lista.
print(idades)


# Um método antigo de iteração:
idades_no_ano_que_vem = []

for idade in idades:
    idades_no_ano_que_vem.append(idade + 1)

print(idades_no_ano_que_vem, "Novas idades depois de 1 ano")

# Um método melhor de iteração:
idades_no_ano_que_vem = [(idade+1) for idade in idades]             # List Comprehension
idades_no_ano_que_vem_filtrada = [idade for idade in idades if idade > 21]

print(idades_no_ano_que_vem_filtrada)

"""
def faz_processamento_de_visualizacao(lista):
    print(len(lista))
    # lista.append(13)
    # OBS: Se adicionássemos o 13 no final da lista com 5 elementos e mandássemos o Python imprimir o tamanho dessa
    # lista, ele imprimirá 5 elementos ao invés de 6 elementos, deixando o 13 de lado. Isso acontecesse porque já
    # criamos um objeto na memória que tem 5 elementos. Um objeto com 6 elementos será um novo objeto alocado na memória
    # Portanto é importante tomar cuidado quando utilizarmos objetos mutáveis...

    # Sempre que passamos um objeto mutavel como parametro, perdemos o controle do que aquilo pode se tornar, devido a
    # sua mutabilidade. Por isso, alguns desenvolvedores defendem que quanto mais imutável um objeto, melhor.

"""
idades = [16, 21, 29, 56, 43]
# faz_processamento_de_visualizacao(idades)
# print(idades)


# Refatorando para um jeito melhor:
def faz_processamento_de_visualizacao(lista=None):

    if lista is None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)


print("--" * 100)


class ContaCorrente:

    def __init__(self, codigo):  # Construtor
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):  # Método
        self.saldo += valor

    def __str__(self):  # Definição de String
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

print("--" * 100)
contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)


# Tuplas, objetos e anemia
# >> Usar tuplas quando queremos objetos imutáveis, onde a posição é importante e pode ter elementos diferentes.
def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])


guilherme = ('Guilherme', 37, 1981)  # Tupla
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))
print(usuarios)
print("--" * 100)


# Listas e polimorfismo
"""class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Código {} Saldo {} <<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):  # Classe ContaCorrente que herda da classe Conta

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01  # Soma mais 1% todo mês
        self._saldo -= 3     # Retira 3 reais todo mês


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(conta)

print("--"*100)"""

# Arrays e Numpy
#   > Arrays são muito utilizados em programação científica, Data Science
"""
import array as arr
#   >  os arrays padrão do Python (array puro), evitaremos usar

arr.array('d', [1, 2, 3.5])  # O array do Python tenta armazenar números de maneira mais eficiente
# Se você tentar passar uma string para a lista de números, não vai funcionar. Retorna um erro porque não é um número.


import numpy as np
#   > para precisão matemática ou qualquer tipo de trabalho numérico, usamos mais o numpy do que o array padrão do Python

numeros = np.array([1, 1.5])
print(numeros)
print(numeros + 3)

print("--"*100)"""


# (Refatorando) Método Abstrato e Igualdade com __eq__
from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):  # Quando queremos forçar a implementação de um método, transformamos a classe em abstrata dessa maneira (e importando o módulo ABC)

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        raise NotImplementedError  # Se chamarmos este método, descobrimos se há implementação desse método em subclasse

    def __str__(self):
        return "[>>Código {} Saldo {} <<]".format(self._codigo, self._saldo)


class ContaCorrente(Conta):  # Classe ContaCorrente que herda da classe Conta

    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01  # Soma mais 1% todo mês
        self._saldo -= 3     # Retira 3 reais todo mês


class ContaInvestimento(Conta):
    pass


from functools import total_ordering


@total_ordering
class ContaSalario:  # Essa conta aqui não vai herdar da classe Conta

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):
        return self._codigo == other._codigo

    """def __lt__(self, other):  # 'lt' significa Less Than (Método usado para Ordenação de objetos sem ordem natural)
        return self._saldo < other._saldo"""

    def __lt__(self, other):  # Alteração de __lt__ feita para a parte 'Ordenação completa e functools' do curso.
        if self._saldo != other._saldo:
            return self._saldo < other._saldo

        return self._codigo < other._codigo

    # Outra ideia de comparação:
    """if type(other) != ContaSalario:
        return False"""

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'>>Código {self._codigo} Saldo {self._saldo}<<'


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
print(conta1)
print(conta2)
print(conta1 == conta2)
# Apesar de conta1 e conta2 serem objetos diferentes alocados na memória, retornará True por causa do método '__eq__'
# que implementamos na classe mãe 'Conta'.

print(isinstance(ContaCorrente(34), ContaCorrente))
print(isinstance(ContaCorrente(34), Conta))


# Builtins como enumerated, range e desempacotamento automatico de tuplas
for valor in enumerate(idades):     # Neste caso em específico, estamos pedindo para a função retornar cada
    print(valor)                    # valor com seu respectivo índice em uma tupla
# Alternativamente
for indice, idade in enumerate(idades):
    print(indice, idade)            # Aqui ele faz um desempacotamento da tupla.


# OBS: O enumerate() é um gerador de iterável assim como o range(). Esses geradores são capazes de criar objetos na
# memória de modo que estão preparados para algum tipo de uso, mas não fazem nada até chamarmos alguma função que
# interaja com eles. Esses geradores iteráveis podem ser inseridos em listas e tuplas, por exemplo.


# Desempacotamento automático:
usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

# 1 - Ideal para legibilidade:
for nome, idade, nascimento in usuarios:
    print(nome)  # Desempacotamos todas as informações de 'usuários' e usamos só o que queríamos

# 2 - Alternativamente (não ideal em caso de colaboração com outros desenvolvedores):
for nome, _, _ in usuarios:  # Passando um underline no lugar da variável estamos falando para o Python ignorar variável
    print(nome)


# Ordenação Básica:
print("Idades:", idades)
print("Idades ao contrário:", list(reversed(idades)))  # Só tá ao contrário. Não em ordem decrescente
print("Idades em ordem crescente:", sorted(idades))
print("Idades em ordem decrescente:", sorted(idades, reverse=True))
print("Idades em ordem decrescente:", list(reversed(sorted(idades))))
print("##"*50)


# Ordenação natural
#       > Números possuem uma ordenação natural: 1, 2, 3, ... 44, 45... 1100, 1545...
#       > Strings também tem uma ordenação natural: Abacate, Banana, Cajamanga, Vinho...
#               >> Essa ordenação de strings é denominada lexicográfica.
#                   Essa ordem segue a ordenação do código de caracteres. Primeiro as maiúsulas A-Z, depois minúsculas


nomes = ['Guilherme', 'Daniela', 'Paulo']
print(sorted(nomes))
nomes = ['guilherme', 'Daniela', 'Paulo']
print(sorted(nomes))
print("--"*50)


# ###############################################################################################################
# Ordenação de objetos sem ordem natural
conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

# sorted(contas)  # Não vai funcionar porque os o Python não consegue comparar maior ou menor entre objetos;
# Ex: Conta > Conta OU Conta < Conta  →  O Python não consegue fazer essa ordenação


# Jeito ruim de fazer (ruim pq estamos fazendo acesso a um atributo privado):
"""def extrai_saldo(conta):
    return conta._saldo


for conta in sorted(contas, key=extrai_saldo):
    print(conta)"""

# Outro jeito ruim (que acessa dados privados):
"""from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)"""

# Melhor jeito (implementar a função __lt__) na classe ContaSalario (dá uma olhada lá):
#       > Desse jeito não quebramos o encapsulamento de atributos pois o acesso de atributos privados está sendo feito
#       dentro da própria classe.

print(conta_do_guilherme < conta_da_daniela)  # Retorna True
print(conta_do_guilherme > conta_da_daniela)  # Retorna False

print('\nContas')
for conta in sorted(contas):
    print(conta)

print('\nContas - Reversed')
for conta in sorted(contas, reverse=True):
    print(conta)


# Ordenação completa e functools
#           > Agora queremos que se as duas contas tiverem o mesmo saldo, ordenar pelo número da conta mais baixo

from operator import attrgetter


print('\nContas - Attrgetter')
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)


# Refatoração feita na parte __lt__ da classe ContaSalario...
print('\nRefatoração - __lt__')
for conta in sorted(contas):
    print(conta)
print()


# from functools import total_ordering - para fazer esse tipo de comparação aqui: '<=' OU '>='. Só o __lt__ não consegue
# Dá uma olhada em cima da classe ContaSalario!
# OBS: Para essa lógica funcionar, é necessário ter os métodos __eq__ e __lt__ implementados na classe.
print('After importing functools')
print(conta_do_guilherme <= conta_da_daniela)  # Retorna True
print(conta_do_guilherme <= conta_do_paulo)  # Retorna False; apesar de terem o mesmo saldo o nº da conta do gui é menor
print(conta_do_guilherme < conta_do_guilherme)  # Retorna False, pq são iguais
print(conta_do_guilherme == conta_do_guilherme)  # Retorna True, pq são iguais
print(conta_do_guilherme <= conta_do_guilherme)  # Retorna True, pq ou é uma coisa ou outra


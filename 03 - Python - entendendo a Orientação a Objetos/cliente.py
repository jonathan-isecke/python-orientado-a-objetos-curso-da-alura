"""class Cliente:

    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome.title()  # .title() - Retorna uma string com a primeira letra maiúscula
"""

# Contextualizando:
"""
Definimos a classe Cliente. Para acessarmos os atributos da classe Cliente, no terminal, precisamos sempre chamar o 
método usando um parêntese no final. Isso é padrão de qualquer método / função definida pelo desenvolvedor. Para o 
exemplo acima, se eu quiser chamar o nome de alguém, ficaria algo assim: >> cliente.get_nome(). Tudo certo. Nada demais

Mas eu não quero digitar o parênteses quando eu chamar essa função toda vez. Para fazer isso, é só 'dar uma dica' para o
Python, para que a linguagem nos dê acesso aos objetos de uma classe. Essa dica pode ser definida como uma 'Propriedade'
"""
# Refatorando com Properties


"""class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()"""


# Refatorando
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print('chamando setter nome()')
        self.__nome = nome


# Agora retorne para o arquivo 'conta.py' para continuar o raciocínio...

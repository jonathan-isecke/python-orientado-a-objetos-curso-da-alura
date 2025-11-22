"""
class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):  # R$1000,00 será o limite padrão para qualquer conta
        print("Construindo objeto ... {}".format(self))
        self.numero = numero        # Estamos definindo os atributos da classe. (Quais as características que ela tem?)
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta1 = Conta(1, "Fulano", 0.0)
conta2 = Conta(2, "Beltrano", 0.0)
conta3 = Conta(3, "Sicrano", 0.0, 2000.0)  # Conta especial com um limite maior que as demais. É só atribuir o valor

conta1.saldo()
"""

# Refatorando com Métodos Privados e Getters e Setters
"""
class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):  # R$1000,00 será o limite padrão para qualquer conta
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero      # Estamos definindo os atributos da classe. (Quais as características que ela tem?)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):  # pega_saldo() é um exemplo de método Getter. Get só devolve um valor. Faz mais nada.
        return self.__saldo

    def get_titular(self):  # Getter  → por convenção utilizamos o nome 'get' para definir um método: <get_método>
        return self.__titular

    def get_limite(self):  # Getter  →  'get' devolve; retorna;
        return self.__limite

    def set_limite(self, limite):  # Setter →  'set' recebe um valor; altera; define;
        self.__limite = limite


conta1 = Conta(189, "Jonathan", 2000)
conta2 = Conta(564, "Mario", 3000)
# conta1._Conta__saldo  →  equivalente ao: conta1.saldo() se os métodos fossem públicos.
#       > É o Python avisando que o método é Privado e que sua alteração não é recomendada.

conta1.transferir(200, conta2)
conta1.extrato()
conta2.extrato()
"""

# Anotações do professor no terminal
"""
>>> from conta import Conta
>>> conta = Conta(123, "Nico", 55.5, 1000.0)
Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
>>> conta2 = Conta(321, "Marcos", 100.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x7f82af89d400>
>>> conta.transfere(10.0, conta2)
>>> conta.extrato()
Saldo de 45.5 do titular Nico
>>> conta2.extrato()
Saldo de 110.0 do titular Marcos
"""


# Refatorando com Properties
#   > OBS: Para entender melhor sobre 'Properties', verifique as anotações feitas no arquivo 'cliente.py'.

"""class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):  # R$1000,00 será o limite padrão para qualquer conta
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero      # Estamos definindo os atributos da classe. (Quais as características que ela tem?)
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):  # pega_saldo() é um exemplo de método Getter. Get só devolve um valor. Faz mais nada.
        return self.__saldo

    def get_titular(self):  # Getter  → por convenção utilizamos o nome 'get' para definir um método: <get_método>
        return self.__titular

    @property
    def limite(self):  # Getter  →  'get' devolve; retorna;
        return self.__limite

    @limite.setter
    def limite(self, limite):  # Setter →  'set' recebe um valor; altera; define;
        self.__limite = limite


conta = Conta(123, 'Joshua', 100, 1500)
conta.limite  # Não precisamos mais colocar 'conta.limite()' para executar o método. Somente 'conta.limite' é suficiente
conta.limite = 2500     # Execução do método setter com o decorator '@limite.setter'
conta.limite  # Para retornar na tela o novo limite
"""

# Refatorando com Métodos Privados
"""class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):  # colocando '__' antes do nome de um método, o definimos como Método Privado
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel  # Retorna True or False

    def sacar(self, valor):
        if self.__pode_sacar(valor):    # Se pode sacar
            self.__saldo -= valor       # Então saca
        else:
            print('O valor {} ultrapassou o limite'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite"""

# Refatorando com Métodos Estáticos
# > Nos Métodos Estáticos, queremos fazer acesso a um atributo de classe sem ter criado um objeto / variável. Quero que
#   a função me retorne um valor só de chamá-la diretamente.


class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):  # colocando '__' antes do nome de um método, o definimos como Método Privado
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel  # Retorna True or False

    def sacar(self, valor):
        if self.__pode_sacar(valor):    # Se pode sacar
            self.__saldo -= valor       # Então saca
        else:
            print('O valor {} ultrapassou o limite'.format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_do_banco():
        return "001"

    @staticmethod
    def codigos_dos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


codigos = Conta.codigos_dos_bancos()

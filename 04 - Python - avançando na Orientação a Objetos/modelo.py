# Criando um atributo de Classe (<tamanho_cpf>)
"""class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False
        # necessário colocar '__class__' para acessar o atributo de classe <tamanho_cpf>.

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())"""

# Problemática:
# Repare que no código abaixo, estamos repetindo muitos atributos iguais em classes diferentes. Poderíamos aproveitar
# métodos e atributos em comum das duas classes sem precisar ficar copiando ou reescrevendo?


"""class Filme:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0
    # OBS: 'nome' e 'likes' estão definidos como Privados pois queremos proteger esses atributos contra alterações

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
"""
# Refatorando: Menos duplicação, mais reuso (HERANÇA)
"""class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # '_nome' com 1 underline, protegemos o atributo
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chamando o inicializador 'init' da classe mãe 'Programa' por meio do 'super'
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
# print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao}: {vingadores.likes} likes')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
# print(f'{atlanta.nome} - {atlanta.ano} - {atlanta.temporadas}: {atlanta.likes} likes')
"""
# Métodos de Classe
# São métodos declarados com @classmethod. Quando criamos um método de classe, temos acesso aos atributos da classe.
# Da mesma forma com os atributos de classe, podemos acessar estes métodos de dentro dos métodos de instância, a partir
# de __class__, se desejarmos:


class Funcionario:
    prefixo = 'Instrutor'

    @classmethod
    def info(cls):
        return f'Esse é um {cls.prefixo}'

# Perceba que, ao invés de self, passamos cls para o método, já que neste caso sempre recebemos uma instância da classe
# como primeiro argumento. O nome cls é uma convenção, assim como self."""


# Métodos Estáticos
# A outra forma de criar métodos ligados à classe é com a declaração @staticmethod. Veja abaixo:
class FolhaDePagamento:
    @staticmethod
    def log():
        return f'Isso é um log qualquer'

# Note que, no caso acima, não precisamos passar nenhum primeiro argumento fixo para o método estático. Nesse caso, não
# é possível acessar as informações da classe, porém o método estático é acessível a partir da classe e também
# da instância.


"""Cuidados a tomar...
Sempre que você usar métodos estáticos em classes que contém herança, observe se não está tentando acessar alguma 
informação da classe a partir do método estático, pois isso pode dar algumas dores de cabeça pra entender o motivo 
dos problemas.

Alguns pythonistas não aconselham o uso do @staticmethod, já que poderia ser substituído por uma simples função no corpo
do módulo. Outros mais puristas entendem que os métodos estáticos fazem sentido, sim, e que devem ser vistos como 
responsabilidade das classes."""


# Polimorfismo (porém não está Pythonico)
"""filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas  # <hasattr>= Se tem o atributo
    print(f'{programa.nome} - {detalhes}: {programa.likes}')"""

# Refatorando
"""class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # '_nome' com 1 underline, protegemos o atributo
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self._likes} Likes')


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # Chamando o inicializador 'init' da classe mãe 'Programa' por meio do 'super'
        self.duracao = duracao

    def imprime(self):  # Perceba que na classe mãe tbm temos um método chamado imprime. Aqui, estamos sobrescrevendo...
        print(f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} Likes')


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes')


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime()

print(str(12412))
"""
# Refatorando (Utilizando a representação textual de objetos)
"""
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # '_nome' com 1 underline, protegemos o atributo
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def __str__(self):      # Representação textual de um objeto <__str__>
        return f'{self._nome} - {self.ano} - {self._likes} Likes'  # Assim, mudamos o método de 'print' para 'return'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist(list):  # Sim, podemos herdar de classes internas do Python
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
vingadores.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

# for programa in filmes_e_series:
#     print(programa)  # Agora estamos chamando a função interna de representação de textos. <__str__>. Sempre que mandarmos imprimir a classe, será impresso essa representação textual contida neste método.

print(f'Tamanho a playlist: {len(playlist_fim_de_semana)}')  # Vai mostrar quantos programas estão na minha playlist
for programa in playlist_fim_de_semana:
    print(programa)

print(f'Está na minha playlist ou não? {demolidor in playlist_fim_de_semana}')
"""
# Refatorando (Fugindo da complexidade)
"""class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # '_nome' com 1 underline, protegemos o atributo
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def __str__(self):      # Representação textual de um objeto <__str__>
        return f'{self._nome} - {self.ano} - {self._likes} Likes'  # Assim, mudamos o método de 'print' para 'return'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
vingadores.dar_like()


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):      # Agora a nossa lista tem objetos iteráveis
        return self._programas[item]  # Estamos repassando um item para a lista de programas interna.
    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho a playlist: {len(playlist_fim_de_semana.listagem)}')  # Vai mostrar quantos programas estão na minha playlist
print(f'Demolidor está na minha playlist ou não? {demolidor in playlist_fim_de_semana}')
print(f'Vingadores está na minha playlist ou não? {vingadores in playlist_fim_de_semana}')
print(f'O primeiro da lista é: {playlist_fim_de_semana[0]}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

len(playlist_fim_de_semana)  # Não vai funcionar porque a playlist não tem o atributo len()"""


"""
Tipos de Herança:
    Interface vs. Reuso
        > Formas de Reuso
            Composição vs. Extensão
            
            
Duck Typing
> Utilizando Métodos Mágicos como o '__getitem__' podemos dar características para métodos de nossas classes sem precisar 
importar um método Built-In completamente. No caso do '__getitem__', damos aos objetos do método, características de 
iterável.

Python Data Model
    Inicialização:          __init__                                        → obj = Novo()               
    Representação:          __str__, __repr__                               → str(obj), repr(obj), print(obj)   
    Container, sequência:   __contains__, __iter__, __len__, __getitem__    → len(obj), iten in obj, for i in obj, obj[2:3]
    Numéricos:              __add__, __sub__, __mul__, __mod__              → obj + outro_obj, obj * obj    
"""
# Refatorando com Duck Typing

class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()  # '_nome' com 1 underline, protegemos o atributo
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def __str__(self):      # Representação textual de um objeto <__str__>
        return f'{self._nome} - {self.ano} - {self._likes} Likes'  # Assim, mudamos o método de 'print' para 'return'


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min. - {self._likes} Likes'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)

demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
vingadores.dar_like()


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):      # Agora a nossa lista tem objetos iteráveis
        return self._programas[item]  # Estamos repassando um item para a lista de programas interna.
    @property
    def listagem(self):
        return self._programas

    def __len__(self):  # Com este método mágico, podemos facilmente substituir o decorator '@property' e não precisamos definir uma função 'tamanho()'
        return len(self._programas)


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho a playlist: {len(playlist_fim_de_semana)}')
print(f'Demolidor está na minha playlist ou não? {demolidor in playlist_fim_de_semana}')
print(f'Vingadores está na minha playlist ou não? {vingadores in playlist_fim_de_semana}')
print(f'O primeiro da lista é: {playlist_fim_de_semana[0]}')

for programa in playlist_fim_de_semana.listagem:
    print(programa)

len(playlist_fim_de_semana)


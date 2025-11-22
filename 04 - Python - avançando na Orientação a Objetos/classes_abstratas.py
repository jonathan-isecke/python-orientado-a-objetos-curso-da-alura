# from abc import ABC  # Abstract Base Classes
"""
from collections.abc import MutableSequence
from numbers import Complex

class Playlist(MutableSequence):
    pass

filmes = Playlist()

class Numero(Complex):
    def __getitem__(self, item):
        super().__getitem__()
    pass
"""
# Atividade:
"""
from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self):
        return self.descricao


lista = MinhaListagem('Nova_lista')
print(lista)

# O código vai dar erro, pois faltou implementar um método.
# O método que faltou foi o __len__, que caracteriza a classe abstrata Sized.
"""

"""
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass
"""

from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    pass


objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)
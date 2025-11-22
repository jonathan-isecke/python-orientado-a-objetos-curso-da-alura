# Ordenando lista de strings no Python
# Disponível em: https://www.alura.com.br/artigos/ordenando-listas-no-python

class Produto(object):
  def __init__(self, nome, valor):
    self.__nome = nome
    self.__valor = valor

  def __repr__(self):
    return "nome:%s valor:%s" % (self.__nome, self.__valor)  # Esse %s é para concatenar Strings; se parece com .format

  def get_nome(self):
    return self.__nome

  def get_valor(self):
    return self.__valor


def lista_produtos():
  """Restante do código não compartilhado na matéria lida..."""
  pass

produtos = lista_produtos(produtos)
produtos_ordenados = sorted(produtos, key = Produto.get_valor, reverse=True)  # Ordenando pelo valor primeiro
produtos_ordenados = sorted(produtos, key = Produto.get_nome, reverse=True)  # Ordenando pelo nome primeiro


# O que o código deve retornar:
"""
[nome:chocolate valor:3.45,
nome:biscoito valor:2.49,
nome:cafe valor:3.45,
nome:suco valor:4.3,
nome:feijao valor:10.0,
nome:arroz valor:8.5] 

[nome:arroz valor:8.5,
nome:biscoito valor:2.49,
nome:cafe valor:3.45,
nome:chocolate valor:3.45,
nome:feijao valor:10.0,
nome:suco valor:4.3]
"""

"""
Vimos nesse post que quando queremos ordenar listas no Python, podemos utilizar a função sorted. Vimos, também, que ela
funciona perfeitamente para strings ou números, entretanto, quando queremos ordenar objetos, precisamos informar como 
ela deve ordenar o objeto, ou seja, enviando um atributo do objeto por meio do parâmetro key.
"""

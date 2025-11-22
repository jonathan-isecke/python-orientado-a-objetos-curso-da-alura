# Parâmetros em páginas da internet
# url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


# Fatiamento de strings (Slicing)
"""url1 = "bytebank.com/cambio?moedaOrigem=real"

url_base = url1[0:19]                       # Slicing  →  Neste caso: Imprima da string na posição zero, até a 18 (19-1)
print(url_base)                             # Retorna <bytebank.com/cambio>

url_parametros = url1[20:36]
print(url_parametros)                       # Retorna <moedaOrigem=real>
"""


# Método Find e Método Len
"""# O método find()     -     Mais info: https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=find#str.find
#                           Estrutura: str.find(sub[, start[, end]])
url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

#              Parte 1 - Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]  # '+1' para pular o índice '?'; vai até o final pq não passamos um limite
print(url_parametros)


# O método len()
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)

indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[indice_valor:]
print(valor)  # Retorna <real>, no entanto, se no 'parametro_busca' mudarmos para 'moedaDolar',
# retornará <dolar&moedaOrigem=real>, então o cógido ainda precisa de alguns ajustes"""


# (REFATORANDO) URL com múltiplos parâmetros
"""
url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"

# Sanitização da URL
url = url.replace(" ", "")

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")


indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]


#           Parte 2 - Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)


indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)  # busque '&' a partir de 'indice_valor'

if indice_e_comercial == -1:  # Se o índice do '&' não for encontrado, então...
    valor = url_parametros[indice_valor:]  # ...então vá até o final da string
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
"""

# (REFATORANDO com boas práticas) Criando nossa classe
# extrator_url.py
# Métodos da Classe str: https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods

# Expressões Regulares & Quantificadores e Intervalos
# extrator_cep.py

# Validando a nossa URL com RegEx
# validador_url.py
# RegEx: https://docs.python.org/pt-br/3/howto/regex.html#regex-howto

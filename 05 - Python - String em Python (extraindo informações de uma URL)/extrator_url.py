import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:  # Anteriormente: <if self.url == "">
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):  # Método Especial __len__
        return len(self.url)

    def __str__(self):  # Método Especial __str__
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url



url = "https://bytebank.com/cambio?quantidade=100&moedaDestino=real&moedaOrigem=dolar"
extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
print("O tamanho da ULR: ", len(extrator_url))
print(extrator_url)

extrator_url2 = ExtratorURL(url)
print(extrator_url == extrator_url2)  # Retona False porque não são objetos iguais  →  extrator_url.__eq__(extrator_url2)
# Para que pudessemos implementar essa comparação da string e não do objeto, implementamos o método especial __eq__ na classe

print(id(extrator_url))  # Estamos mostrando o endereço de memória de um objeto com o método 'id()'
print(id(extrator_url2))


# Desafio do Curso
"""
Modifique o nosso projeto, levando em conta o valor do dólar em real (por exemplo: DOLAR = 5.50), para, sabendo o 
valor do dólar em real (por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (origem, destino e quantidade) e 
imprimir na tela o valor da conversão."""
print("-"*100)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = float(extrator_url.get_valor_parametro("quantidade"))

if moeda_origem == 'real':
    print(quantidade/valor_dolar)
else:
    print(quantidade*valor_dolar)

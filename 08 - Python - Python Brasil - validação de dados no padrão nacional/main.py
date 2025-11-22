"""from cpf_cnpj import Documento
"Gerador de CPFs válidos: https://www.4devs.com.br/gerador_de_cpf"


exemplo_cpf = "29081960180"
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)


# Resumo Regex
# Expressões regulares servem para encontrarmos padrões bem definidos dentro de textos humanos
import re
padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta)
print(resposta.group())

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"  # More details about these operators in '03.Biblioteca re.png'
# padrao = "\w{5,50}@[a-z] {3, 10},com.br"  # Alternativamente, para o padrão brasileiro
texto = "aaabbbccc rodrigo123@gmail.com.br mais texto inutil a ser ignorado"
resposta = re.search(padrao, texto)
print(resposta)

# Definindo padrão para telefones
import re
padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4-5}[0-9]{4}"
texto = "Eu gosto do numero 2126451234"
resposta = re.findall(padrao, texto)
print(resposta)

from TelefonesBr import TelefonesBr
# import re

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4-5})([0-9]{4})"  # () divide em grupos; ? indica que o padrão ñ é obrigatório
# resposta = re.findall(padrao, telefone)
# print(resposta)

# from datetime import datetime, timedelta
# from datas_br import DatasBr

# Principais bibliotecas de Datetime:
#   datetime.datetime  # Retorna uma hora exata
#   datetime.timedelta

# print(datetime.today())
cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())


# Formatando Datas - Strftime
# Existem diversos outros caracteres além dos listados acima, e todos podem ser encontrados nesta documentação.
#   https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
# Além desse link, vou deixar também um artigo bem legal do blog da Alura, que aborda outros métodos além desse.
#   https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python

hoje = datetime.today()
hoje_formatada = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje)
print(hoje_formatada)
print(type(hoje_formatada))  # Perceba que ele transforma o objeto datetime em string.
# Isso é ideal somente quando vamos mostrar algo para o usuário final.

cadastro = DatasBr()
print(cadastro)



# Diferenças entre datas e timedelta
numero1 = 1
numero2 = 2
string = "um"

print(len(string))
# print(len(numero1))  # Int has no Atributte len
print(numero1 + numero2)

# timedelta serve para fazermos operações matemáticas com datas
hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1, hours=20)
print(amanha - hoje)
hoje = DatasBr()
print(hoje.tempo_cadastro())
"""

"""# Introdução APIs e validação de CEP
from acesso_cep import BuscaEndereco

cep = "25800320"
objeto_cep = BuscaEndereco(cep)


# Acessando APIs com Python
# Via CEP: https://viacep.com.br/
# Request HTTPS for Humans: https://requests.readthedocs.io/en/latest/

import requests
r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r.text)

a = objeto_cep.acessa_via_cep()
print(a)
print(type(a))
print(dir(a))
print(a.text)
print(a.json())
print(type(a.text))  # <class 'str'>
print(type(a.json()))  # <class 'dict'>
print(a.json()['cep'])  # vai retornar somente o número do cep
print(a.json()['bairro'])  # vai retornar somente o número do cep


from acesso_cep import BuscaEndereco

cep = "75100630"
objeto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objeto_cep.acessa_via_cep()

print(bairro, cidade, uf)"""


# Mais sobre APIs: https://medium.com/clebertech/como-funciona-uma-requisi%C3%A7%C3%A3o-http-cf76f66fe36e
# HTTP: GET e POST - Conheça as diferenças entre os métodos: https://www.alura.com.br/artigos/diferencas-entre-get-e-post?_gl=1*1raozgk*_ga*MTY5OTE4MjA1OC4xNjkzMjY3NTk2*_ga_59FP0KYKSM*MTY5MzM0MDAwMi4zLjEuMTY5MzM0MjQzNS4wLjAuMA..*_fplc*QW1IUzk0Nk1UMDU5cHhNJTJGVWF2Rjg4ZmhZWDBOM3FmQ0pzdjdGdUJ3dUo3cERnQUtDVEs1Z1cwTHVveGtzU2NJcnFMVm9DUEVlQngyVUtRc0RZNkhGc2V0YVVWQkd0VTlhc3JwdFcxYnJGVVhETGJUUVR2ZGc5RE8zN2RQcnclM0QlM0Q.*_ga_1EPWSW3PCS*MTY5MzM0MDA0NC4zLjEuMTY5MzM0MjQzNS4wLjAuMA..
# Cabeçalhos HTTP: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers

"""
Para entender mais como uma API funciona, é importante que tenhamos em mente o que é uma requisição HTTP 
(Hypertext Transfer Protocol), protocolo baseado em streams de texto. Sempre que acessamos uma página na web ou enviamos
um formulário estamos usando o protocolo de forma transparente.

Agora vamos entender como um requisição HTTP é composta:

request line
headers
headers
headers…

body


Apenas a request line é obrigatória, e perceba que o body vem após uma linha em branco.

De modo geral uma request line se parece com algo assim:

GET http://google.com/ HTTP/1.1
<Método><Espaço><Endereço><Espaço><VersãoHTTP><Envio>


Dentro da request line é importante destacar o método utilizado. Este método também é conhecido como verbo HTTP, que 
indica qual ação deve ser executada no servidor. Os verbos mais utilizados são os seguintes:

GET: Solicita informações de um recurso; POST: Cria um recurso; PUT: Atualiza um recurso; DELETE: Remove um recurso.

O header pode possuir a seguinte aparência:

Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding:gzip, deflate, br
Accept-Language:en-US,en;q=0.9,pt;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
...


Os cabeçalhos têm a função de definir os parâmetros de uma requisição HTTP. Se você quiser entender mais a fundo quais 
são e para que servem os cabeçalhos fica aqui essa Referência. O body possui a seguinte aparência:

parametro=valor&outroparametro=outrovalorCOPIAR CÓDIGO
O body é passado através do HTTP quando enviamos um formulário. Consumir APIs começa com o entendimento do protocolo 
HTTP, então, se necessário, leiam mais de uma vez e tirem suas dúvidas."""

import requests

cep = "75100630"


def retorna_endereco(cep):
    url = 'https://viacep.com.br/ws/{}/json'.format(cep)
    r = requests.get(url)
    dados = r.json()
    bairro = dados.get('bairro')
    cidade = dados.get('localidade')
    uf = dados.get('uf')
    return bairro, cidade, uf


bairro, cidade, uf = retorna_endereco(cep)

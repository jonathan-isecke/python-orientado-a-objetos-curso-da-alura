# (PASSO 1)
from bytebank import Funcionario

"""lucas = Funcionario('Lucas Carvalho', 2000, 1000)  # Instanciando um objeto
print(lucas.idade())

# A Regra de Negócio está falha, pois o parâmetro exigido da classe é a Data de Nascimento completa, e o código só
# funciona se passarmos somente o ano."""

lucas = Funcionario('Lucas Carvalho', '13/02/2000', 1000)  # Instanciando um objeto
# print(lucas.idade())  # Comentei essa linha porque não preciso dela mais a partir do PASSO 10

# (PASSO 2): No arquivo 'projeto-do-bytebank/codigo/bytebank.py'


# (PASSO 3) - Criando o primeiro teste (Teste automatizado unitário)

# O método abaixo está comentada porque a partir do PASSO 10 não precisaremos mais
"""def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste 1 = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
    print(f'Teste 2 = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/05/1999', 1111)
    print(f'Teste 3 = {funcionario_teste2.idade()}')


teste_idade()
"""

"""
Teste Manual
* Lento; Sujeito a falhas (Fator humano); Inconveniente;

Teste Automatizado
* Automatizado; Feedback rápido; Segurança em alteração do código; "Refactoring";

Tipos de testes
* Teste unitário - Pega uma pequena parte de uma aplicação
* Teste de integração - Testa a integração entre unidades
* Teste de ponta (E2E - End to End) - Simula o usuário da aplicação, o ambiente de produção onde é colocado o projeto
"""

# (PASSO 4) Instalação do Pytest
"""
Pytest - Framework especializado em testes
> Oferece uma alternativa mais Pythonica do que o 'unittest'

    * Possui múltiplos plugins / extensões
    * Altamente escalável
    * Utilização simples

NO TERMINAL:
cd '.\09 - Python - Python e TDD - explorando testes unitários\'  # Abrir diretório onde o ambiente virtual está
venv\Scripts\activate  # Iniciar o ambiente virtual
pip install pytest

pip freeze  # Mostra todos as extensões instaladas.
    * É uma boa prática salvar a lista de extensões em um arquivo txt para maio controle

pip freeze > requirements.txt

NO DIRETÓRIO DO PROJETO ATUAL:
Criar um diretório de testes: pasta 'tests'
Dentro desse diretório, vamos criar um arquivo __init__.py que será um módulo de testes.
    > OBS: Esse arquivo init pode permanecer vazio. 

> É assim que fazemos o Python entender que um diretório é um módulo de testes, pela criação da pasta e do arquivo init.

Feito isso, vamos criar um arquivo onde vamos rodar alguns testes. 'test_bytebank.py'

(PASSO 5): No arquivo 'test_bytebank.py' do diretório acima.
"""

# (PASSO 10)
ana = Funcionario('Ana', '12/03/1997', 1000001)
print(ana.calcular_bonus())
# Perceba que ainda não há um teste para o cálculo dos bônus. Então vamos implementá-lo:
# (PASSO 11) No arquivo 'test_bytebank.py'

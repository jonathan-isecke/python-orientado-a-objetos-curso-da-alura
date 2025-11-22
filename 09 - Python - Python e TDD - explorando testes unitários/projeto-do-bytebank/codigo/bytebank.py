from datetime import date


class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    # (PASSO 2)
    # OBS: Para verificar o que foi alterado do original, dê uma olhada no arquivo compactado
    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]  # Pegar o último item da lista de strings
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    # (PASSO 6)
    def sobrenome(self):
        nome_completo = self.nome.strip()  # Para tirar os espaços em branco antes e depois dos nomes
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]  # Para retornar o último nome da lista
    # (PASSO 7) No arquivo 'test_bytebank.py'

    # (PASSO 8)
    """def decrescimo_salario(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']

        if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
            decrescimo = self._salario * 0.1  # decréscimo de 10%
            self._salario = self._salario - decrescimo"""

    # (PASSO 9) - Refatorando o código
    """
    Não é legal que um método execute muitas funções. É interessante termos um método para cada funcionalidade
    """
    def _eh_socio(self):  # Definimos esse método como privado para ser acessado somente dentro da classe.
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)  # Vai retornar True or False

    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1  # decréscimo de 10%
            self._salario = self._salario - decrescimo

    """
        Contexto: A bytebank está com um projeto de conferir algum bônus para seus funcionários. Qual a regra para ganhar 
        este bônus?
            > 10% do salário da pessoa precisa ser igual ou menor que R$1000,00
    """

    # Esse método de calcular bônus já estava implementado pela Dominique (criadora deste arquivo Bytebank)
    """def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor"""

    # (PASSO 10) No arquivo 'main.py'

    # (PASSO 12) Um método com Exception
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor

    # Como construímos um teste que considere exceções com o Pytest?
    # (PASSO 13) No arquivo 'test_bytebank.py'

    def __str__(self):  # É algo intrínseco da linguagem. Não precisa ser testado... mas criamos seu teste no PASSO 18
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'


# (PASSO 16)
"""
Para sabermos se nossos testes vão cobrir todos os métodos contigos neste arquivo (classe Funcionarários), instalar:
    pip install pytest-cov
    
    pip freeze > requirements.txt  # para atualizar a nossa lista de pacotes instalados
    
    pytest --cov  # para verificar a cobertura de todos os testes e métodos no diretório
    
    pytest --cov=codigo tests  # Pasta onde verificar: 'codigo'; pasta onde estão os testes: 'tests'
    
    # OBS: Utilizei o código abaixo porque o de cima não funcionou pra mim :(
    pytest --cov=codigo -k tests  # Está retornando uma cobertura de 98% (até agora)
"""

# (PASSO 17) Garantindo cobertura total
"""
    pytest --cov=codigo -k tests --cov-report term-missing
    >> vai retornar a linha do código que está faltando nos testes
    >> no momento que rodamos esse comando, o método faltante está na linha 80 deste arquivo, portanto, vamos 
    implementá-lo no arquivo 'test_bytebank.py'
"""
# (PASSO 18) No arquivo 'test_bytebank.py'


# (PASSO 19)
"""
Algumas funções já são intrínsecas da própria linguagem. O método __str__ é um desses métodos. Na classe Funcionario,
sabemos que esse método funcionará perfeitamente. Ele não precisa ser testado. Podemos colcoar exceções na lógica 
'coverage' do pytest para indicar que esse método não precisa ser testado; ou seja, exceção. Assim, podemos focar 
somente nos testes que NÓS criamos, e não das lógicas operacionais da própria linguagem Python

    pytest --cov=codigo -k tests --cov-report html  # cria um diretorio 'htmlcov'
    
    >> dentro desse diretório, clicamos botão direito no arquivo 'index.html', depois: Abrir no navegador
    >> no canto superior direito, existe atalhos de teclado. O atalho ']' mostra o próximo arquivo. Uma nova página.
        Nele, é possível ver todos os arquivos que possuem testes cobertos '<number> run' e os não cobertos 
        '<number> missing'
"""

# (PASSO 20) Excluindo código para a cobertura
"""
Para fazermos isso, criaremos um novo arquivoi no diretório 'projeto-do-bytebank': '.coveragerc'

Esse arquivo '.coveragerc' tem a mesma ideia do 'pytest.ini'. Ele executa antes da extensão coverage do pytest; 
tem prioridade.

Dentro dele, definimos o método __str__ da classe Funcionario como exceção para não ser verificado durante os testes.

# OBS: Como estou com problemas no meu diretório, copiei o arquivo '.coveragerc' para a pasta do curso

    pytest --cov=codigo -k tests --cov-report term-missing
    pytest --cov=codigo -k tests --cov-report html  # ideal para visualização, como um report.
"""
# Vamos simplificar os testes que são rodados no terminal para não precisar digitar toda a linha acima novamente.
# (PASSO 21) No arquivo .coveragerc

"""
Agora basta digitarmos 'pytest --cov' no terminal. Não será rodados testes de todos os diretórios. Somente o 
especificado no arquivo '.coveragerc'

    pytest --cov=codigo -k tests --cov-report html
    >> Agora ao invés de criar um diretório chamado 'html', vai criar um diretório chamado coverage_relatorio_html
       conforme especificado no arquivo '.coveragerc'
"""
# Podemos configurar o pytest para retornar todos os testes + todas as coverages
# (PASSO 22) No arquivo 'pytest.ini'


# (PASSO 23)
"""
Feitas as alterações no arquivo 'pytest.ini', podemos simplesmente digitar o seguinte no terminal:

    pytest
"""

# (PASSO 24) Gerando relatórios
"""
Podemos gerar relatórios em diferentes formatos de arquivos, caso seja necessário / requisitado...
    
    pytest --junitxml report.xml  # Relatório dos testes
    >> --junit  →  Ferramenta  de testes do JAVA que estabeleceu esse padrão
    
    pytest --cov-report xml  # Relatório do coverage em XML
"""

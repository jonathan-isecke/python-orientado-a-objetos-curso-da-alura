# (PASSO 5)
"""
Metodologia ágil para o Desenvolvimento de Testes: Given-When-Then
 * Dado (contexto)...  → dado determinado contexto
 * Quando (Ação)...    → vem a ação dele (algo acontece)
 * Então (Desfecho)... →

Outra Metodologia: Arrange-Act-Assert (AAA)
 * Arrange (organizar)   → passos preliminares necessários para montar o contexto inicial do teste;
 * Act (agir)            → ação que leva ao que vamos averiguar no final;
 * Assert (averiguar)    → Nesse caso, averiguarmos que o desfecho trazido pela ação é realmente aquele que esperamos.
"""
from codigo.bytebank import Funcionario
import pytest  # 'pip install pytest' on this directory too  / for Step 13
from pytest import mark  # for Step 14


class TestClass:  # É uma boa prática criar uma classe para testar cada trecho de código
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = '13/03/2000'  # Given-Contexto
        valor_esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When-ação

        assert resultado == valor_esperado  # Then-desfecho  /  assert é um método do pytest

    # O Pytest precisa que o nome do método inicie com 'test_'.
    # O nome do teste precisa ser o mais "verboso" possível. Precisa indicar explicitamente o que será feito.

    """
    Se eu executar esse arquivo atual, o python iniciará os testes e indicará se passou ou não em cada teste. No  
    entanto, também é possível executarmos testes diretamente do TERMINAL. Basta digitar 'pytest' e dar 'Enter'.

    Se o pytest retornar um '.' no final, quer dizer que o teste passou.
    A quantidade de pontos mostrados no terminal é equivalente a quantidade de testes aprovados.

        pytest      →  executa os testes
        pytest -v   →  executa os testes evidenciando os nomes dos métodos. v de verbose

    (PASSO 6) No arquivo 'bytebank.py'
    """

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = ' Lucas Carvalho '  # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome()  # When

        assert resultado == esperado

    """
    (PASSO 7) Test Driven Development (TDD) / Desenvolvimento Guiado por Testes
    
        * No TDD criamos primeiro os testes antes de implementar códigos. Segue a seguinte lógica:
            > Nova Funcionalidade requisitada  →  Teste  →  Código  →  Refatoração
            > Construção de Testes, Implementação de Código e Refatoração
    
    """

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000  # given
        entrada_nome = 'Paulo Bragança'  # nome do diretor da bytebank, por exemplo
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()  # when  /  seguindo o TDD, estamos criando o teste antes da função
        resultado = funcionario_teste.salario

        assert resultado == esperado  # then
    # A lógica do método acima é a seguinte: De acordo com as regras de negócio da empresa, quem recebe 100000, se tiver
    # o nome de algum diretor da empresa, o método será chamado e um decrescimo ocorrerá no salário dessa pessoa.

    # Ao rodarmos o 'pytest -v' no terminal do nosso ambiente virtual, 2 testes terão erro e 1 terá falha. Isso é normal
    # pois ainda não implementamos a função 'decrescimo_salario()' na classe 'Funcionario'. Ela ainda não existe. Mas
    # como essa questão de reduzir 10% do salário num cenário específico foi uma requisição dos diretores da bytebank
    # vamos então criar esse método.
    # (PASSO 8) No arquivo 'bytebank.py'

    # (PASSO 11)
    @mark.calcular_bonus  # for step 14
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario('Test', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then
    # Quando o funcionário não atende aos requisitos do bônus, o chefe não quer que retorne o valor 0, e sim uma Exceção
    # (Passo 12) No arquivo 'bytebank.py'

    # (PASSO 13)
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):  # O que está dentro desse bloco deve ser um método que retornará uma Exception
            entrada = 1000000  # given

            funcionario_teste = Funcionario('Test', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then  / O resultado esperado já é uma exception

    # É comum criarmos 2 ou mais testes para um mesmo método, como fizemos nos PASSOS 11 e 13. Cada teste para uma
    # ocasião espcífica do método; um cenário diferente.


    """
    Contexto: Queremos rodar um teste individualmente dos outros. Apenas um deles.
    
        * A IDE do Pycharm disponibiliza uma função prática para isso: aparece um botão 'play', da cor verde, na linha 
        de cada método de teste. É uma função exclusiva da IDE; dependente dela.
        * Se executarmos 'pytest -v' no terminal de nosso ambiente virtual, todos os testes serão executados.
        
    Problemática: Queremos rodar um teste isolado sem depender da IDE, de forma que funcione em qualquer script Python.
    """
    # (PASSO 14) Organizando testes com Makers
    """
    TERMINAL
        pytest -k idade
    >> estamos filtrando todos os testes e executando somente o/os que contém a palavra 'idade'
    
        pytest -v -k idade
    >> faz a mesma coisa do anterior, mas de forma verbosa
    
    Porém esse jeito não é interessante, uma vez que futuramente, outros novos testes podem ter as mesmas palavras.
    Para contornar esse problema, podemos usar os MARKS para nomear nossos testes. 
    
        from pytest import mark
    
    Para fazer isso, basta digitar: '@mark.nome_desejado'. Isso é um decorator para identificação que ficará sobre o 
    método de teste. Para exemplificar isso, criei a tag: @mark.calcular_bonus.
    
    Colocadas as tags (não têm problema métodos diferentes terem o mesmo nome dede que testem um mesmo método), basta
    rodar no terminal:
        
        pytest -v -m calcular_bonus
        
        >> Dois testes serão executados pq 2 testes tem o mesmo decorator
        >> Perceba q ao rodar isso: 2 passed, 3 deselected, 2 warnings
            > 2 passed  →  2 métodos passaram no teste (os dois que selecionamos)
            > 3 deselected  →  3 foram filtrados; excluídos, pois pedimos somente 2, que são os que atendem o decorator
            > 2 warnings  →  Aviso do pytest: O decorator que vc colocou foi criado? Ou é um erro de digitação?
                >> Isso quer dizer q o próprio pytest já possui alguns marks padrão
                
                Para sabermos quais tipos de marks existem no pytest, basta executar:
                
                    pytest --markers
                    
                Um deles é: @mark.skip  →  quando adicionamos esse decorator, o pytest pula o teste mencionado e executa
                os outros
                    
                @mark.skipif
                
                    import sys

                    @pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
                    def test_funcao():
                        ...
                
                @mark.xfail  →  Indica que o teste precisa falhar em caso de uma condição cumprida.
                
                Para mais detalhes, verificar a documentação: https://docs.pytest.org/en/7.4.x/how-to/mark.html
                
                
                Como tirar esse WARNING?
                    > Podemos criar um arquivo que fica dentro da nossa pasta geral do projeto, no caso, dentro de 
                    'projeto-do-bytebank'. O arquivo é o 'pytest.ini'
                    
                    OBS: O certo seria criar o arquivo no diretório 'projeto-do-bytebank'. No entanto, estou tendo 
                    problemas com minha hierarquia de pastas, devido a nomenclatura com caracteres especiais. Portanto,
                    copiei o arquivo 'pytest.ini' para o diretório: 
                    '09 - Python - Python e TDD - explorando testes unitários'
                    
                    pytest.ini  →  Um arquivo de configuração do pytest que toma precedente pela configuração original
                    do pytest, ou seja, ele dá preferência para este arquivo antes de seguir a própria configuração 
                    padrão.
    """
    # (PASSO 15) No arquivo 'pytest.ini'

    # Notas sobre o arquivo pytest:
    """
    Vamos dar um exemplo de uma nova configuração que sobrepõe a padrão:
    
    Lembra daquela regra que todo teste deve começar com o prefixo test_? Pois bem, por meio de algumas alterações no 
    arquivo pytest.ini podemos mudá-la.
    
    Utilizando as variáveis com os nomes python_functions, python_classes e python_files podemos definir novos padrões de 
    escrita para os nomes de métodos de teste, classes de teste e arquivos de teste, respectivamente.
    
        [pytest]
        python_functions=*_testando
        python_classes=testando_*
        python_files=muitos_testes_*
    
    No exemplo acima definimos um sufixo (_testando) para os nomes de métodos de teste, um prefixo (testando_) para as 
    classes de teste e um prefixo (muitos_testes_*) para os nomes de arquivos de teste.
    
    Existem várias outras configurações que podem ser feitas através do arquivo pytest.ini, confira a lista de presente 
    na documentação.
    """
    # (PASSO 18) - Com este teste de agora, conseguimos 100% de cobertura no teste. Confira PASSO 17
    def test_retorno_str(self):  # Não colocamos mais verboso pq queremos andar mais rápido.
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000  # given
        esperado = "Funcionario(Teste, 12/03/2000, 1000)"

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() # when
        assert resultado == esperado # then

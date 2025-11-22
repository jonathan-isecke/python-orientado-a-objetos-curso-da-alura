"""
print("********************************")
print("Bem vindo no jogo de Advinhação!")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
print("Você digitou ", chute_str)
chute = int(chute_str)

if numero_secreto == chute:
    print("Você acertou")
else:
    print("Você errou.")

print("Fim do jogo")
"""

"""
ERRADO: 

numero1 = 10
numero2 = 10
if(numero1 = numero2):  # O erro está nesta linha aqui.
    print("São números iguais")
    
CORREÇÃO: 
numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")
    
# O problema é que foi usado um = para realizar a comparação. Quando usamos apenas um =, estamos atribuindo um valor 
# à variável.



# OUTRO EXEMPLO:
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)  # Retorna 'NicoSteppat'

# REFATORANDO
nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")  # Retorna 'Nico Steppat'

# ELIF

print("********************************")
print("Bem vindo no jogo de Advinhação!")
print("********************************")

numero_secreto = 42
total_de_tentativas = 5
rodada = 1

while rodada < total_de_tentativas:
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
    else:
        if maior:
            print("Você errou. O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou. O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo")

# REFATORANDO  (String Interpolation)
print("_____"*50)
while rodada < total_de_tentativas:
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # Acabamos de fazer uma String Interpolation
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
    else:
        if maior:
            print("Você errou. O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou. O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1
"""

"""
numero_secreto = 42
total_de_tentativas = 5
rodada = 1

# REFATORANDO  (Loop For)
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # Acabamos de fazer uma String Interpolation
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100...")
        continue  # Continua com a próxima iteração de maneira direta  →  'continua com a próxima rodada do loop for'

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
        break  # 'break' sai do bloco atual abrubtamente quando a condição especificada é atendida
    else:
        if maior:
            print("Você errou. O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou. O seu chute foi menor do que o número secreto.")

print("Fim de jogo")
"""

# Formatação de Strings com Interpolação  (não precisa decorar as informações abaixo!)
#       →  Para mais informações sobre formatação, acessar: https://docs.python.org/3/library/string.html#formatexamples
#       →  Quando for necessário utilizar esse tipo de informação, basta acessar o link acima.

#       Curiosidade: comparando a diferença de formatação do Python2 e Python3  →  https://pyformat.info/

teste = "R$ {}".format(1.59)
print(teste)        # Retorna 'R$ 1.59'

teste = "R$ {:f}".format(1.59)  # ':f' estamos definindo que o valor inserido será do tipo Float.
print(teste)        # Retorna 'R$ 1.590000'

teste = "R$ {:.2f}".format(1.59)  # ':.2f' Tipo float, mas com somente '2' algarismos após o ponto '.'
print(teste)

# Aumentando um pouco a dificuldade:
#   > Quero que o ponto '.' dos números de tipo float fiquem alinhados verticalmente, como se eles fossem a nossa margem
# Exemplo:
#    1.59
#   45.9
# 1234.97

teste = "R$ {:.2f}".format(1234.59)
print(teste)

teste = "R$ {:7.2f}".format(1.59)  # Antes do ponto, terão 7 espaços de distância
print(teste)

teste = "R$ {:07.2f}".format(1.59)  # Aqui estou falando que os espaços vazios serão substituídos por '0'
print(teste)

teste = "R$ {:07d}".format(4)  # 'd' estamos definindo que o valor inserido será do tipo Inteiro.
print(teste)            # Retorna 'R$ 0000004'
# OBS: A formatação de números inteiros pela lógica deveria ser definida por 'i', já que remete ao <type int>, assim
# como 'f' se remete ao <type float>. No entanto, 'i' não existe para formatar. Ao invés disso, usamos o 'd' para se
# referir ao <type int>. 'd' significa 'digit', e note que ao contrário da formatação do <type float>, o 'd' não precisa
# de um '.' (ponto) para separar os algarismos, até porque são números inteiros, e inteiros não têm "vírgula".

teste = "R$ {:07d}".format(46)
print(teste)            # Retorna 'R$ 0000046'

teste = "R$ {:7d}".format(46)
print(teste)            # Retorna 'R$ 0000046'

teste = "R$ {:7d}".format(46)
print(teste)            # Retorna 'R$      46'

# EXEMPLO PRÁTICO DE FORMATAÇÃO:
data = "Data {:2d}/{:2d}/{:4d}".format(9, 4, 2007)
print(data)  # Retorna 'Data  9/ 4/2007'

data = "Data {:02d}/{:02d}/{:04d}".format(9, 4, 2007)
print(data)  # Retorna 'Data 09/04/2007'


# EXTRA:
print("Ola Sr.{1} {0}".format("Batista","João"))  # O '1' e o '0' servem para indicar a ordem de qual informação aparecerá primeiro. Sendo '0' o primeiro e '1' o segundo.


# FORMATAÇÃO: 'f-strings' ou 'formatted strings literals'
nome = 'Matheus'
print(f'Meu nome é {nome}')             # Retorna 'Meu nome é Matheus'
print(f'Meu nome é {nome.lower()}')     # Retorna 'Meu nome é matheus'


print("_____"*50)

"""
# REFATORANDO  (Random)
#       →  Funções bult-ins do Python: https://docs.python.org/3/library/functions.html
#       →  Módulo Random: https://docs.python.org/3/library/random.html#random.random
#                   > O 'random' não está integrado nativamente à linguagem Python. É uma biblioteca que precisa ser
#                   importada pois não está disponível automaticamente.
#       → Curiosidade: Caso onde programadores geraram uma grande brecha no sistema por um erro de programação:
#           > https://www.engadget.com/2010-12-29-hackers-obtain-ps3-private-cryptography-key-due-to-epic-programm.html

import random  # imports devem ser feitas no início do arquivo. Mas como este é um caderno de anotações, está aqui...

# numero_secreto = round(random.random() * 100)  # 'random.random()' gera um número entre '0.0' e '1.0'
numero_secreto = round(random.randrange(0, 100 + 1))
total_de_tentativas = 5
rodada = 1

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # Acabamos de fazer uma String Interpolation
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100...")
        continue  # Continua com a próxima iteração de maneira direta  →  'continua com a próxima rodada do loop for'

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou")
        break  # 'break' sai do bloco atual abrubtamente quando a condição especificada é atendida
    else:
        if maior:
            print("Você errou. O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou. O seu chute foi menor do que o número secreto.")

print("Fim de jogo")
"""

"""
No entanto, computadores têm os seus problemas com aleatoriedade, pois são sistemas determinísticos. Em outras palavras,
nosso Python é previsível e na verdade não sabe criar números verdadeiramente aleatórios. Por isso se chama Pseudo-Random!

Por que funcionou então?
'random' é um função que, dada a mesma entrada, gerará o mesmo número. O truque é oferecer sempre uma entrada diferente 
para ter números diferentes e exatamente isso que está acontecendo por baixo dos panos. Essa entrada também é chamada de
'seed' (semente, em português). Entre as chamadas da função random, sempre é utilizado um novo seed. Por padrão o Python
usa a hora (os milissegundos) como semente, mas nada nos impede de definir o mesmo seed antecipadamente. 
Para isso, existe a função seed!

random.seed(100)  # Se usarmos o mesmo 'seed' mais de uma vez, será gerado o mesmo número
random.randrange(1, 101)

# Repare que a biblioteca random é bem previsível e por isso se chama pseudo-random!
"""


# Adicionando níveis ao jogo e esquema de pontos:

import random


def jogar():
    print("********************************")
    print("Bem vindo no jogo de Advinhação!")
    print("********************************")

    numero_secreto = round(random.randrange(0, 100 + 1))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil    (2) Médio   (3) Difícil")

    nivel = int(input("Digite o nível: "))
    if nivel == 1:
        total_de_tentativas = 20

    elif nivel == 2:
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100...")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou. O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou. O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(
                numero_secreto - chute)  # Pontuação perdida  →  'abs()' retorna o número Absoluto. O número será um inteiro positivo, independente se ele for negativo ou não...
            pontos = pontos - pontos_perdidos  # Pontuação final

    print("Fim de jogo")

"""
SOBRE O ROUND:

O Python 3 usa uma forma de arredondar, que também é chamado de Banker's rounding. Nessa forma, os valores são 
arredondados para o número que for mais próximo, por exemplo: 2.4 seria arredondado para 2, todavia 2.6 já seria 
arredondado para 3. Quando um valor é igualmente próximo de dois números, por exemplo 2.5, que possui 0.5 de diferença
tanto para o número 2 quanto para o número 3, esse é arredondado para o valor par mais próximo, que, nesse caso, seria o
número 2. Vale lembrar que somente os números x.5 recebem o tratamento "especial" do arredondamento para o valor par 
mais próximo, nos demais, o arredondamento ocorre conforme esperado.

Para mais informações: https://docs.python.org/3.5/library/functions.html#round


SOBRE DIVISÃO:

O operador '/' sempre traz um float, mesmo se não for necessário, por isso ele também é chamado de float division:
>>>  3 / 2  # Retorna '1.5'
>>>  2 / 2  # Retorna '1.0'

No entanto, existe um outro operador bem parecido, o //. Tente executar:
>>>  3 // 2  # Retorna '1'
O operador // também é chamado integer division e sempre devolve o valor inteiro (sem arredondar).
        → No Python 2 não existe diferença entre os dois operadores. O Python 2 só tem integer division.
"""

# FINAL:

import random
# OBS: Anotações e informações extras no arquivo origial 002.advinhacao.py


def jogar():
    print("********************************")
    print("Bem vindo no jogo de Advinhação!")
    print("********************************")

    numero_secreto = round(random.randrange(0, 100 + 1))
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil    (2) Médio   (3) Difícil")

    nivel = int(input("Digite o nível: "))
    if nivel == 1:
        total_de_tentativas = 20

    elif nivel == 2:
        total_de_tentativas = 10

    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100...")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if maior:
                print("Você errou. O seu chute foi maior do que o número secreto.")
            elif menor:
                print("Você errou. O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(
                numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")


if __name__ == "main":
    jogar()

"""
Contextualização do código acima ('if __name__ == "__main__":'):
        Quando executamos um arquivo em Python de maneira direta, ou seja, clicar Run neste IDE e ele executar o 
        programa, por baixo dos panos a linguagem Python está criando uma nova variável chamada '__name__', com valor 
        '__main__'. Esse '__main__' quer dizer que o arquivo atual é o principal na prioridade, por assim dizer.
        É o que está sendo executado diretamente pelo usuário, portanto tem a preferência principal. 

        Comparação:
        Aqui podemos falar que seria como a "janela em foco" do Windows. Quando vc clica dentro de um programa, ele está
        em foco. Quando você alterna entre programas, o programa anterior não está mais em foco. Está em segundo plano. 
        Então ele deixou de ser o 'main'. A mesma lógica se aplica ao Python. O 'main' é o programa que está sendo 
        rodado agora...

        Resumo:
        Um arquivo não é 'main' quando é importado e está sendo executado dentro e outro arquivo. Quando fazemos um 
        "import" e utilizamos partes de funções de outros arquivos, esse arquivo importado não é o 'main'.

        Trazendo isso para o nosso código, vamos explicar:
            if __name__ == "__main__": 
                jogar()
        > Se o nome do arquivo for 'main', ou seja, se este arquivo atual for executado diretamente dentro dele mesmo,
        sem ter sido importado por outro programa, ele será o principal. O 'main'. Se ele for o principal, quero que ele
        execute a função 'jogar()'.


Explicação do professor:

    Programa principal vs Programa importado: 
        Quando rodamos diretamente um arquivo no Python, ele internamente cria uma variável e a preenche. E através 
        dessa variável podemos fazer uma consulta, pois se ela estiver preenchida, significa que o arquivo foi executado
        diretamente, mas se a variável não estiver preenchida, então significa que o arquivo só foi importado.

        Essa variável é a __name__, e ela é preenchida com o valor __main__ caso o arquivo seja executado diretamente. 
"""

# O Python é realmente uma linguagem estritamente interpretada?
"""
Para finalizar, falamos que o Python utiliza o conceito de interpretação, ou seja, passamos o código fonte e ele é 
interpretado, mas não é bem assim. Podemos executar o arquivo jogos.py e reparar na pasta que é criada dentro do 
diretório, a pycache. Se formos ver o que tem dentro da sua pasta, vemos que há dois arquivos referentes aos módulos 
importados no jogos.py, ou seja, um arquivo referente à adivinhacao e outro à forca. Mas o que são esses arquivos?

O que o Python faz ao vivo é ler os módulos importados e os compila para bytecode. Esse código foi criado ao mesmo tempo
 em que executamos o arquivo jogos.py. Apesar do Python ter um ambiente de interpretação, ele compila os módulos 
 importados para melhorar o desempenho, a execução do ambiente, apesar de não ter esse processo de compilação explícito.

Do ponto de vista do Python, ele considera que esses módulos não serão modificados, então na próxima execução, para 
melhorar o desempenho, esse código compilado é que será utilizado.

Com isso, terminamos aqui o nosso curso. No próximo implementaremos o jogo da forca, aprendendo mais sobre funções, 
coleções, outras funções built-in, e muito mais! Muito obrigado por assistirem esse curso e nos encontramos no próximo 
treinamento!
"""

# Transferindo código
"""
Em Python, conseguimos executar um arquivo em qualquer sistema operacional, inclusive os códigos aqui feitos são 
disponibilizados para vocês, alunos, e ele poderá ser executado seja qual for o seu sistema operacional, basta ter o 
Python 3 instalado. Já o arquivo executável do C, gerado pelo compilador, não é executável em um sistema operacional 
diferente. É preciso compilar novamente o código fonte no sistema operacional desejado, para ter um executável 
funcional. E muitas vezes o código fonte (não é o nosso caso) utiliza algo específico do sistema operacional, passando 
a depender dele, então nem adiantaria compilá-lo em um SO diferente.

Logo, o Python tem uma portabilidade maior que o C.
"""

#
"""
Para executar um arquivo Python, por exemplo o adivinhacao.py, fazemos:

    python3 adivinhacao.py

Foi isso que fizemos o treinamento inteiro, seja pela linha de comando ou pelo PyCharm. E com o C? Será que existe um 
comando, algo como um cexecuter, para executarmos um arquivo C? Não, não existe.

O ambiente do C exige que primeiramente devemos passar o código fonte (o arquivo .c) para um compilador. O compilador lê
o código fonte e faz uma análise da sintaxe, se esquecemos algum ponto e vírgula, ou de tipar alguma variável, etc. E 
feita essa análise, o compilador cria um outro arquivo, e é esse arquivo que podemos executar. Então primeiro vamos 
compilar o arquivo, vamos utilizar o compilador gcc (novamente, não é necessária a sua instalação, estamos usando-o 
somente para mostrar a diferença entre ambientes que usam o conceito de compilação e ambientes que usam o conceito de 
interpretação):

    gcc adivinhacao.c o adivinhacao

Ou:

    gcc -std=c99 adivinhacao.c -o adivinhacao

Esse comando compila o arquivo adivinhacao.c e se tudo estiver correto, criará o arquivo executável adivinhacao. Agora é
só executar o arquivo gerado. Em UNIX, fazemos:
    
    ./adivinhacao

Essa é a diferença de um ambiente que usa o conceito de compilação, no qual o código fonte, que não é executável, deve 
ser compilado para criar um arquivo executável; e um ambiente que usa o conceito de interpretação, no qual o código 
fonte é executado diretamente.
"""



# Python é interpretado ou compilado?
"""
O senso comum é que o Python é uma linguagem interpretada. Interpretado significa que não há um processo de compilação 
que traduz o código fonte em algum código nativo, que o seu computador entende. A documentação do Python confirma isso, 
no entanto também menciona a presença de um compilador:

"Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the 
presence of the bytecode compiler."

Documentação: https://docs.python.org/3/glossary.html

Temos um compilador, porém de bytecode. Bytecode é um código intermediário, normalmente independente do sistema 
operacional. Então, Python é uma linguagem compilada também? Em 2003, Fredrik Lundh, em seu artigo Compiling Python 
Code, título que perverte o senso comum, começa:

"Python source code is automatically compiled into Python byte code by the CPython interpreter. Compiled code is usually
 tored in PYC (or PYO) files, and is regenerated when the source is updated, or when otherwise necessary."

Novamente traduzindo livremente: "O código fonte é automaticamente compilado para bytecode do Python pelo interpretador
CPython. O código compilado é comumente armazenado nos arquivos no PYC (ou PYO), sendo regerado quando o arquivo fonte é
atualizado ou quando é necessário."

E aí? Python é uma linguagem interpretada ou compilada? As duas coisas? Há discussões acaloradas entre desenvolvedores, 
cada um com sua opinião. Então, uma resposta interessante está no StackOverFlow, aliás, a resposta mais bem avaliada:

"First off, interpreted/compiled is not a property of the language but a property of the implementation (...) Python is 
compiled. Not compiled to machine code ahead of time (i.e. "compiled" by the restricted and wrong, but also common 
definition), "only" compiled to bytecode" Acessar: http://stackoverflow.com/questions/6889747/is-python-interpreted-or-compiled-or-both

Traduzindo: "O fato de uma linguagem ser interpretada ou compilada não é uma questão da linguagem, mas da sua 
implementação. (...) Python é compilada. Não compilada para o código de máquina antes da execução, apenas para o 
bytecode.

Isso significa que alguém pode implementar o Python totalmente compilado, totalmente interpretado ou ambos, a linguagem 
continua a mesma. Ser compilada/interpretada é mais propriedade da implementação do Python do que da linguagem.
"""

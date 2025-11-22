import random

""" print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maca".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]  # List Comprehensions

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto não enforcou e não acertou, então...
    # enquanto não False e não False, então
    # enquanto True e True, então
    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()  # Estamos removendo espaços do início e do final dos inputs do usuário. Mais informações, checar 'outras_anotacoes.py', na parte 'Método Find'.

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:

                if chute == letra:
                    # print("Encontrei a lera {} na posição {}".format(letra, posicao))
                    letras_acertadas[posicao] = letra
                posicao += 1

        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6  # Definimos o nº de tentativas = 6. Enforcou será quando o nº de erros for igual a 6. Isso o tornará True
        print(letras_acertadas)

        acertou = "_" not in letras_acertadas  # Quando não tiver o underscore "_", será True, encerrando assim, o jogo

    if acertou:
        print('Você ganhou!')
    else:
        print('Você perdeu!')

    print("Fim do jogo")


    # REFATORANDO (Do meu jeito...)
def jogar():
    print('_' * 80, '\nBem vindo ao jogo da Forca\n', '_' * 80)

    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()   # Estamos limpando o '\n' que é adicionado ao final das strings
        palavras.append(linha)  # Cada linha é uma palavra
    arquivo.close()

    numero = random.randrange(0, len(palavras))  # Vai escolher uma palavra dentro da lista e retornará o índice dessa palavra.
    palavra_secreta = palavras[numero].upper()
    letras = ["_" for letra in palavra_secreta]

    print(letras)

    tentativas = 7
    erros = 0

    ganhou = False
    perdeu = False

    while not perdeu and not ganhou:
        chute = input('Digite uma letra: ')
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            indice = 0

            for letra in palavra_secreta:
                if chute == letra:
                    letras[indice] = letra
                indice += 1

        else:
            erros += 1
            if tentativas - erros == 0:
                print(f'Poxa, acabaram as tentativas...')
            elif tentativas - erros == 1:
                print(f'Última chance!')
            else:
                print(f"Ops, você errou! Faltam {tentativas - erros} tentativas")

        print(letras)

        perdeu = erros == tentativas
        ganhou = "_" not in letras

    if ganhou:
        print('Parabéns! Você acertou!')
    else:
        print('\nInfelizmente, você perdeu...')

    print('\nFim de jogo! Obrigado por jogar...')


if __name__ == "__main__":
    jogar()
    """

# REFATORANDO (PROFESSOR)


def mensagem_de_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def escolhendo_a_palavra():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def espaco_para_letras(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input('Digite uma letra: ')
    chute = chute.strip().upper()
    return chute


def escreve_letra_correta(chute, letras, palavra_secreta):
    indice = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras[indice] = letra
        indice += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def jogar():

    mensagem_de_abertura()
    palavra_secreta = escolhendo_a_palavra()

    letras = espaco_para_letras(palavra_secreta)
    print(letras)

    tentativas = 7
    erros = 0
    ganhou = False
    perdeu = False

    while not perdeu and not ganhou:
        chute = pede_chute()

        if chute in palavra_secreta:
            escreve_letra_correta(chute, letras, palavra_secreta)

        else:
            erros += 1
            desenha_forca(erros)

            if tentativas - erros == 0:
                print(f'Poxa, acabaram as tentativas...')
            elif tentativas - erros == 1:
                print(f'Última chance!')
            else:
                print(f"Ops, você errou! Faltam {tentativas - erros} tentativas")

        print(letras)

        perdeu = erros == tentativas
        ganhou = "_" not in letras

    if ganhou:
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('\nFim de jogo! Obrigado por jogar...')


if __name__ == "__main__":
    jogar()


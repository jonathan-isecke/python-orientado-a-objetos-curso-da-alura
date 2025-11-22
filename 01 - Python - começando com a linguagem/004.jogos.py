# Importando arquivos dentro de outros:

import advinhacao_copia   # O arquivo original chama 002.advinhacao.py
import forca_copia        # O arquivo original chama 003.forca.py
# OBS: A linguagem Python não aceita arquivos nomeados com números e pontos.

def escolher_jogo():
    print("********************************")
    print("*******Escolha o seu jogo!******")
    print("********************************")

    print("(1) Forca  (2) Advinhação")

    jogo = int(input("Qual jogo? "))

    if jogo == 1:
        print("Jogando forca")
        forca_copia.jogar()

    elif jogo == 2:
        print("Jogando Advinhação")
        advinhacao_copia.jogar()

if __name__ == "__main__":
    escolher_jogo()

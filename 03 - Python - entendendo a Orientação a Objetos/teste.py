# Criando uma Conta Bancária (Método: Paradigma Procedural):


def cria_conta(nome, titular, saldo, limite):
    conta = {"nome": nome, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


conta = cria_conta(159, "Jonathan", 1500, 3000)
deposita(conta, 500)
saca(conta, 1000)
extrato(conta)


"""O acesso direto aos atributos dos objetos, como senha e endereço IP, pode representar um risco à segurança, uma vez 
que não há controle de acesso adequado. A abordagem procedural dificulta a implementação de medidas de segurança 
eficazes. Isso pode tornar o código menos seguro e mais propenso a erros, já que qualquer parte do código pode acessar e
modificar os atributos da câmera diretamente.

Essa abordagem pode levar ao compartilhamento de dados entre as funções, onde a câmera é passada de uma função para 
outra, podendo ser modificada em diferentes pontos do código."""

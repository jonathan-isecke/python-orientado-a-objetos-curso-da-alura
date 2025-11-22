endereco = "Rua das Flores 72, Apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re  # re = Regular Expressions -- RegEx

# CEP Padrão: 5 dígitos + hífen (opcional) + 3 dígitos

# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# o '?' após '[-]' indica que esse elemento '-' pode aparecer 1 ou nenhuma vez na string

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")  # {0,1} indica que o padrão pode aparecer de 0 a 1 vez
busca = padrao.search(endereco)  # search() retorna um objeto 'Match' ou 'None'

if busca:
    cep = busca.group()  # group() retorna a string que foi encontrada atendendo aos padrões especificados
    print(cep)

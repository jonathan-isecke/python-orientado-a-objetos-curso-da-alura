from antigo_cpf_cnpj import CpfCnpj
"Gerador de CPFs válidos: https://www.4devs.com.br/gerador_de_cpf"


exemplo_cpf = "29081960180"
exemplo_cnpj = "35379838000112"
documento = CpfCnpj(exemplo_cnpj, 'cnpj')
print(documento)

from validate_docbr import CPF, CNPJ
"Para mais info, acesse: https://github.com/alvarofpp/validate-docbr/blob/main/validate_docbr/CPF.py"


class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError('CPF inválido!!')

        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError('CNPJ inválido!!')

        else:
            raise ValueError("Documento inválido!!")

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            if validador.validate(cpf):
                self.cpf = cpf
                print('CPF válido')
            else:
                print('Número de dígitos incorreto...')
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()
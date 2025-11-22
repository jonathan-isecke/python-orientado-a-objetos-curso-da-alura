from validate_docbr import CPF, CNPJ
"Para mais info, acesse: https://github.com/alvarofpp/validate-docbr/blob/main/validate_docbr/CPF.py"


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format()

    def valida(self, documento):  # Não precisamos passar a qnt. de dígitos pq já fizemos isso na classe Documento.
        validador = CPF()
        return validador.validate(documento)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador = CNPJ
        return validador.validate(documento)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

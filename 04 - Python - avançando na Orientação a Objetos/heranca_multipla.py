class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:  # Classe MIXIN - Classes pequenas, cujos objetos nem precisam ser instanciados (adicionam recursos)
    def __str__(self):
        return f'Hipster, {self.nome}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum):  # O Python 3 usa um algoritmo chamado de MRO
    pass


class Senior(Alura, Caelum, Hipster):
    pass

"""
jose = Junior()
jose.busca_perguntas_sem_resposta()
# jose.busca_cursos_do_mes()  # Não funciona pois esse funcionário é da Caelum


luan = Pleno()  # Leia abaixo:
# Com base no algoritmo MRO, a execução segue a seguinte ordem: Pleno > Alura > Funcionario > Caelum > Funcionario
# Pleno         > o Python busca primeiro na própria classe <Pleno()>
# Alura         > porque é a primeira classe mãe da esquerda para direita em Pleno(Alura, Caelum)
# Funcionário   > pq é a classe mãe de Alura  (Em caso de removermos o método em comum de duas classes, o Python escolhe uma Good Head - escolhe uma das duas com mesmo nome e desconsidera a outra, pulando para o próximo método na linha da sequência. Nesse caso, o método seguinte é uma Good Head (Uma boa cabeça / Uma escolha melhor))
# Caelum    > pois não há mais classes acima no nível de hierarquia, então Caelum é a próxima classe a ser pesquisada
# Funcionário >
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()
"""

tobias = Senior('Tobias')
print(tobias)
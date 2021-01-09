class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas.')
    
    def mostra_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer')
    
    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')
    
class Alura(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Alurete!')
    
    def busca_perguntas_sem_resposta(self):
        print('Mostrando pergunta não respondidas do fórum')
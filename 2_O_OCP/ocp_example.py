'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle).
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''

from abc import ABC, abstractmethod

class Exame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self): pass

    @abstractmethod
    def verificar_condicoes_exame(self, condicao: bool): pass


class ExameSangue(Exame):
    def aprovar_solicitacao_exame(self):
        if self.verificar_condicoes_exame == False:
            print("Exame de sangue nao aprovado")
        else:
            print("Exame de sangue aprovado!")

    def verificar_condicoes_exame(self, condicao: bool):
        # implemente as condições específicas do exame de sangue
        return condicao


class ExameRaioX(Exame):
    def aprovar_solicitacao_exame(self):
        if self.verificar_condicoes_exame == False:
            print("Exame de raio-x nao aprovado")
        else:
            print("Exame de raio-x aprovado!")

    def verificar_condicoes_exame(self, condicao: bool):
        return condicao

exame_sangue = ExameSangue()
exame_raiox = ExameRaioX()


exame_sangue.verificar_condicoes_exame(condicao=False)
exame_sangue.aprovar_solicitacao_exame()

exame_raiox.verificar_condicoes_exame(condicao=True)
exame_raiox.aprovar_solicitacao_exame()
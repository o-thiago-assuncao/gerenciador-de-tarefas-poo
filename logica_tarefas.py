class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✔️" if self.concluida else "❌"
        return f"{status} {self.descricao}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao):
        if not descricao.strip():
            raise ValueError("A descrição da tarefa não pode ser vazia.")
        self.tarefas.append(Tarefa(descricao))

    def listar_tarefas(self):
        return [str(t) for t in self.tarefas]

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluir()
        else:
            raise IndexError("Tarefa inválida.")

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
        else:
            raise IndexError("Tarefa inválida.")

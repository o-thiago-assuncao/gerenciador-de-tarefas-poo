import tkinter as tk
from tkinter import messagebox
from logica_tarefas import GerenciadorTarefas


class InterfaceTarefas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas 📝")
        self.gerenciador = GerenciadorTarefas()

        self.frame = tk.Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.entry_tarefa = tk.Entry(self.frame, width=40)
        self.entry_tarefa.grid(row=0, column=0, padx=5)

        self.btn_adicionar = tk.Button(self.frame, text="Adicionar", command=self.adicionar)
        self.btn_adicionar.grid(row=0, column=1, padx=5)

        self.lista = tk.Listbox(self.frame, width=50, height=10)
        self.lista.grid(row=1, column=0, columnspan=2, pady=5)

        self.btn_concluir = tk.Button(self.frame, text="Concluir", command=self.concluir)
        self.btn_concluir.grid(row=2, column=0, pady=5)

        self.btn_remover = tk.Button(self.frame, text="Remover", command=self.remover)
        self.btn_remover.grid(row=2, column=1, pady=5)

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarefa in self.gerenciador.listar_tarefas():
            self.lista.insert(tk.END, tarefa)

    def adicionar(self):
        try:
            desc = self.entry_tarefa.get()
            self.gerenciador.adicionar_tarefa(desc)
            self.entry_tarefa.delete(0, tk.END)
            self.atualizar_lista()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def concluir(self):
        try:
            indice = self.lista.curselection()[0]
            self.gerenciador.concluir_tarefa(indice)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")

    def remover(self):
        try:
            indice = self.lista.curselection()[0]
            self.gerenciador.remover_tarefa(indice)
            self.atualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceTarefas(root)
    root.mainloop()

# 📝 Gerenciador de Tarefas — Projeto Final de POO com Python

## 🎯 Descrição do Projeto
Este projeto foi desenvolvido como **trabalho final da disciplina de Programação Orientada a Objetos (POO)**, com o objetivo de aplicar os conceitos de **classes, encapsulamento e separação entre lógica e interface gráfica (GUI)**.

O sistema é um **aplicativo desktop** simples, que permite **gerenciar tarefas (To-Do List)** com uma interface intuitiva criada em **Tkinter**.  
O usuário pode **adicionar, concluir e remover tarefas**, e a lista é atualizada automaticamente na tela.

---

## 🧩 Estrutura do Projeto

projeto_tarefas/
│
├── logica_tarefas.py # Contém as classes de negócio (Tarefa e GerenciadorTarefas)
├── POO.py # Interface gráfica (Tkinter) + inicialização da aplicação
└── README.md # Documentação do projeto

---

## ⚙️ Funcionalidades
✅ Adicionar uma nova tarefa  
✅ Marcar tarefa como concluída  
✅ Remover tarefa da lista  
✅ Interface gráfica amigável  
✅ Separação total entre **lógica de negócio** e **interface (GUI)**

---

## 🧠 Conceitos de POO aplicados
- **Classe `Tarefa`** → representa cada tarefa individual, com estado (`concluída` ou não).  
- **Classe `GerenciadorTarefas`** → controla a lista de tarefas e as operações (CRUD em memória).  
- **Classe `InterfaceTarefas`** → cria a interface gráfica e faz a ponte entre o usuário e a lógica do sistema.  
- **Encapsulamento e Responsabilidade** → cada classe tem sua função bem definida.  

---

## 🖥️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x  
- **Biblioteca GUI:** Tkinter (nativa do Python)  
- **Paradigma:** Programação Orientada a Objetos (POO)

---

## 🚀 Como Executar o Projeto
1. Certifique-se de ter o **Python 3** instalado.  
2. Faça o clone do repositório:
   ```bash
   git clone https://github.com/seuusuario/gerenciador-tarefas.git

# Biblioteca Fácil

## Descrição

Biblioteca Fácil é um mini sistema de biblioteca desenvolvido em Python para a disciplina de Padrões de Projeto.

O sistema permite:

* Cadastrar livros;
* Cadastrar usuários;
* Emprestar livros;
* Devolver livros;
* Controlar o estado dos livros.

---

## Linguagem Utilizada

Python 3

---

## Formato da Aplicação

Aplicação de Linha de Comando (CLI)

---

## Como Executar

1. Certifique-se de ter o Python 3 instalado.
2. Baixe ou clone o projeto.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

```bash
python main.py
```

---

## Padrões de Projeto Utilizados

### Facade (Estrutural)

O padrão Facade foi utilizado na classe `BibliotecaFacade`, responsável por centralizar e simplificar as operações do sistema, como cadastro, empréstimo e devolução de livros.

### State (Comportamental)

O padrão State foi utilizado para controlar os estados dos livros. Um livro pode estar disponível ou emprestado, e seu comportamento muda de acordo com o estado atual.

---

## Estrutura do Projeto

```text
biblioteca/
│
├── estados.py
├── facade.py
├── livro.py
├── main.py
└── usuario.py
```

---

## Autor

João Gabriel Ferreira Ramos Arruda

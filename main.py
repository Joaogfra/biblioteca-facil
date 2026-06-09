from facade import BibliotecaFacade

biblioteca = BibliotecaFacade()

biblioteca.cadastrar_usuario(1, "João Gabriel")

biblioteca.cadastrar_livro(1, "Python para Iniciantes")
biblioteca.cadastrar_livro(2, "Padrões de Projeto")
biblioteca.cadastrar_livro(3, "")

biblioteca.listar_livros()

print("\n--- Empréstimo ---")
biblioteca.emprestar_livro(1)

print("\n--- Tentando emprestar novamente ---")
biblioteca.emprestar_livro(1)

print("\n--- Devolução ---")
biblioteca.devolver_livro(1)

print("\n--- Estado final ---")
biblioteca.listar_livros()
from livro import Livro
from usuario import Usuario

class BibliotecaFacade:

    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, id, titulo):

        if not titulo.strip():
            print("Error: O título não pode estar vazio.")
            return

        self.livros.append(Livro(id, titulo))
        print("Livro cadastrado com sucesso.")

    def cadastrar_usuario(self, id, nome):
        self.usuarios.append(Usuario(id, nome))

    def buscar_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None

    def emprestar_livro(self, id_livro):
        livro = self.buscar_livro(id_livro)

        if livro:
            livro.emprestar()

    def devolver_livro(self, id_livro):
        livro = self.buscar_livro(id_livro)

        if livro:
            livro.devolver()

    def listar_livros(self):
        for livro in self.livros:
            print(
                f"{livro.id} - {livro.titulo} ({livro.status()})"
            )
from abc import ABC, abstractmethod

class EstadoLivro(ABC):

    @abstractmethod
    def emprestar(self, livro):
        pass

    @abstractmethod
    def devolver(self, livro):
        pass


class Disponivel(EstadoLivro):

    def emprestar(self, livro):
        livro.estado = Emprestado()
        print(f"Livro '{livro.titulo}' emprestado.")

    def devolver(self, livro):
        print("Livro já está disponível.")


class Emprestado(EstadoLivro):

    def emprestar(self, livro):
        print("Livro já está emprestado.")

    def devolver(self, livro):
        livro.estado = Disponivel()
        print(f"Livro '{livro.titulo}' devolvido.")
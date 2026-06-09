from estados import Disponivel

class Livro:

    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.estado = Disponivel()

    def emprestar(self):
        self.estado.emprestar(self)

    def devolver(self):
        self.estado.devolver(self)

    def status(self):
        return self.estado.__class__.__name__
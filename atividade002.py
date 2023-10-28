class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

class Autor:
    def __init__(self, nome ):
        self.nome = nome

    def autor_livro (self, livro, autor):
        self.livro = livro
        livro.autor = self.livro

livro1 = Livro("Astronautra")
autor1 = Autor("Guilherme")

autor1.autor_livro(livro1)
print(livro1, nome)




        


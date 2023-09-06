biblioteca = []

def adicionar_livro(titulo):
    biblioteca.append(titulo)

def remover_livro(titulo):
    if titulo in biblioteca:
        biblioteca.remove(titulo)
    else:
        raise ValueError("O livro não está na biblioteca")

def listar_livros():
    return biblioteca


adicionar_livro("The Firefighter book")
adicionar_livro("1990")
adicionar_livro("Fundação")

print("Lista de livros na biblioteca:", listar_livros())

remover_livro("1990")

print("Lista de livros após a remoção de '1990':", listar_livros())

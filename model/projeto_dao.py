lista_projeto = []


def adicionar(nova_projeto):
    novo_id = len(lista_projeto)
    nova_projeto.id = novo_id
    lista_projeto.append(nova_projeto)


def pegarProjeto(id):
    for Projeto in lista_Projeto:
        if Projeto.id == id:
            return Projeto
    return None


def salvar (Projeto):
    for i in range(0, len(lista_Projeto)):
        if Projeto.id == lista_Projeto[i].id:
            lista_Projeto[i] = Projeto


def excluir(id):
    for Projeto in lista_Projeto:
        if Projeto.id == id:
            lista_Projeto.remove(Projeto)
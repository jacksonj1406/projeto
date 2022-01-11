lista_colaborador = []

def adicionar(colaborador):
    
    novo_id = len(lista_colaborador)
    novo_colaborador.id =  novo_id
    
    lista_colaborador.append(novo_colaborador)

    def pegarcolaborador(id):
    
    for colaborador in lista_colaborador:
        if colaborador.id == id: 
            return colaborador 

   return None  

   def editar(colaborador):
    
    for index in range(0, len(lista_colaborador)):
        
        colaborador_atual = lista_colaborador[index]
        if colaborador.id == colaborador_atual.id:

            lista_colaborador[index] = col


def excuir(id_colaborador):
    for index in range(0, len(lista_colaborador)):
        colaborador_atual = lista_colaborador[index]
        if id_colaborador == colaborador_atual.id:
            del lista_colaborador[index]
        
            return  


def listar_todos():
    
    for colaborador in lista_colaborador:
        colaborador.imprime()




def lista_colaborador(id):
    pass
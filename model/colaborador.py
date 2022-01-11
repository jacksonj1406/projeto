class colaborador():
    
    def __init__(self, id, nome, email=0):
        self.id = id
        self.nome = nome
        self.email= email
    
    def imprime(self):
        print(f'{self.id}, {self.nome}, {self.endereco}, {self.telefone}')    
        
        
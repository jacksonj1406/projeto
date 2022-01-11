from PyQt5 import  uic, QtWidgets 

FILE_UI= 'view/cadastro_colaborador.ui'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FUILE_UI, self)
        self.janela_entrada = janela_casdastro

        
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)
    
    def fechar_janela(self):
        self.close()
    
    def salvar(self):
        
        nome = self.nome.text()
        email = self.email.text()
        
        novo_colaborador = colaborador( nome, email)
        funcoes_MainWindow.adicionar(novo_colaborador)
        
        self.janela_cadastro_colaborador.carrega_dados()
    
        self.close()
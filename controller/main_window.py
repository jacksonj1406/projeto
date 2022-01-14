from Qt_core import *
from controller.entrada import  entrada_projeto
from controller.novo import  novo_Projeto
from controller.cad_colaborador import cadastro_colaborador

FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        
        self.entrada = entrada_projeto ()
        self.novo = novo_Projeto()
        self.cad_colaborador = cadastro_colaborador ()

        
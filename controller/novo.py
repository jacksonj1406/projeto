from PyQt5 import  uic, QtWidgets 

FILE_UI = "novo_Projeto .ui"
class novo_Projeto(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
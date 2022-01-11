from PyQt5 import  uic, QtWidgets 

FILE_UI = "entrada_projeto .ui"
class entrada_projeto (QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
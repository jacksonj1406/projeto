# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from Qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

import model.colaborador_dao as funcoes_clientes
import model.projeto_dao as peda_dao
from model.colaborador import Cliente, colaborador
from model.projeto import projeto



def carrega_dados():
    # ADCIONAR CLIENTES
    for i in range(0, 15):
        novo_colaboradoir= colaborador(None, f'colaborador-{i}', 'jackson', 'jack@gmail.com')
       
        funcoes_clientes.adicionar(colaborador)
        peda_dao.adicionar(projeto=(None, 'projeto '+str(i), 50+i, 2*i))

 


app = QApplication(sys.argv)
carrega_dados()

window = MainWindow()
window.show() 
app.setStyle('Fusion')

app.exec()
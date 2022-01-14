from Qt_core import *

from controller.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
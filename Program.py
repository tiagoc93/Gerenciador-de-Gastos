# -*- coding: utf-8 -*- --noconsole
import pandas as pd
from openpyxl import load_workbook, Workbook
from datetime import date
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from projeto3 import Ui_MainWindow

book = load_workbook(filename= 'Controle.xlsx')
aba = book['Sheet1']

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        def armazenador():
            nome = self.nome_imput.text()
            valor = float(self.valor_input.text())
            qtd = int(self.quantidade_input.text())
            data = date.today()
            total = valor * qtd
        
            aba.append([nome, valor, qtd, data, total])
            book.save('Controle.xlsx')
            #df = pd.read_excel('Controle.xlsx')
            #print(df)
        
            
            
            
        self.botao.clicked.connect(armazenador)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
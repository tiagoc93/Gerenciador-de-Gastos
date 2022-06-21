# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto3.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(376, 269)
        MainWindow.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nome_imput = QLineEdit(self.centralwidget)
        self.nome_imput.setObjectName(u"nome_imput")
        self.nome_imput.setGeometry(QRect(110, 50, 113, 20))
        self.nome_imput.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.botao = QPushButton(self.centralwidget)
        self.botao.setObjectName(u"botao")
        self.botao.setGeometry(QRect(130, 220, 75, 23))
        self.nome_despesa = QLabel(self.centralwidget)
        self.nome_despesa.setObjectName(u"nome_despesa")
        self.nome_despesa.setGeometry(QRect(120, 20, 101, 20))
        self.valor_despesa = QLabel(self.centralwidget)
        self.valor_despesa.setObjectName(u"valor_despesa")
        self.valor_despesa.setGeometry(QRect(120, 80, 91, 21))
        self.valor_input = QLineEdit(self.centralwidget)
        self.valor_input.setObjectName(u"valor_input")
        self.valor_input.setGeometry(QRect(110, 110, 113, 20))
        self.valor_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.quantidade_despesa = QLabel(self.centralwidget)
        self.quantidade_despesa.setObjectName(u"quantidade_despesa")
        self.quantidade_despesa.setGeometry(QRect(130, 140, 71, 20))
        self.quantidade_input = QLineEdit(self.centralwidget)
        self.quantidade_input.setObjectName(u"quantidade_input")
        self.quantidade_input.setGeometry(QRect(110, 170, 113, 20))
        self.quantidade_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botao.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.nome_despesa.setText(QCoreApplication.translate("MainWindow", u"Nome da Despesa", None))
        self.valor_despesa.setText(QCoreApplication.translate("MainWindow", u"Valor da Despesa", None))
        self.quantidade_despesa.setText(QCoreApplication.translate("MainWindow", u"Quantidade", None))
    # retranslateUi


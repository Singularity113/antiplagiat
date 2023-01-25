import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
import difflib

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Антиплагиат')
        self.cwd = os.getcwd()
        
        widget = QWidget()
        layout = QGridLayout()

        self.btn_first = QPushButton()
        self.btn_first.setObjectName('btn_first')
        self.btn_first.setText('Выбрать 1-й файл')
        layout.addWidget(self.btn_first, 0, 0)
        self.btn_first.setFixedHeight(40)
        self.btn_first.clicked.connect(self.slot_btn_first)

        self.btn_save1 = QPushButton()
        self.btn_save1.setObjectName('btn_save')
        self.btn_save1.setText('Сохранить 1 файл')
        layout.addWidget(self.btn_save1, 0, 1)
        self.btn_save1.setFixedHeight(40)

        self.first_content = QTextEdit()
        layout.addWidget(self.first_content, 1, 0, 1, 2)

        self.btn_second = QPushButton()
        self.btn_second.setObjectName('btn_second')
        self.btn_second.setText('Выбрать 2-й файл')
        self.btn_second.clicked.connect(self.slot_btn_second)
        layout.addWidget(self.btn_second, 0, 2)
        self.btn_second.setFixedHeight(40)

        self.btn_save2 = QPushButton()
        self.btn_save2.setObjectName('btn_save')
        self.btn_save2.setText('Сохранить 2 файл')
        layout.addWidget(self.btn_save2, 0, 3)
        self.btn_save2.setFixedHeight(40)

        self.second_content = QTextEdit()
        layout.addWidget(self.second_content, 1, 2, 1, 2)

        self.btn = QPushButton('Проверка')
        self.btn.setFixedHeight(40)
        layout.addWidget(self.btn, 2, 0, 1, 0)
        # self.btn.clicked.connect(self.slot_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def slot_btn_first(self):
        self.first_content.clear()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "Выбрать 1-й файл", self.cwd, "Text Files (*.txt)")
        file1 = open(fileName_choose, 'r',encoding='utf-8')
        with file1:
            self.data1 = file1.read()
        self.first_content.setText(self.data1)

    def slot_btn_second(self):
        self.second_content.clear()
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, "Выбрать 2-й файл", self.cwd, "Text Files (*.txt)")
        file2 = open(fileName_choose, 'r',encoding='utf-8')
        with file2:
            self.data2 = file2.read()
        self.second_content.setText(self.data2)
    # def slot_btn(self):
    #     diff=difflib.SequenceMatcher(None,self.data1,self.data2)
    #     print(diff.ratio())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    # sys.__excepthook__ = sys.excepthook
    # def my_exeption_hook(exctype, value, traceback):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText('Введены не верные данные')
    #     msg.setWindowTitle('Ошибка!')
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.exec_()
    # sys.excepthook = my_exeption_hook
    sys.exit(app.exec_())

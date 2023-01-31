import sys
import os
import spacy
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
from spacy.lang.ru import Russian

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
        self.btn_save1.clicked.connect(self.file_save1)
        layout.addWidget(self.btn_save1, 0, 1)
        self.btn_save1.setFixedHeight(40)

        self.first_content = QTextEdit()
        layout.addWidget(self.first_content, 1, 0, 1, 2)
        self.first_content.setFontPointSize(14.0)

        self.btn_second = QPushButton()
        self.btn_second.setObjectName('btn_second')
        self.btn_second.setText('Выбрать 2-й файл')
        self.btn_second.clicked.connect(self.slot_btn_second)
        layout.addWidget(self.btn_second, 0, 2)
        self.btn_second.setFixedHeight(40)

        self.btn_save2 = QPushButton()
        self.btn_save2.setObjectName('btn_save2')
        self.btn_save2.setText('Сохранить 2 файл')
        self.btn_save2.clicked.connect(self.file_save2)
        layout.addWidget(self.btn_save2, 0, 3)
        self.btn_save2.setFixedHeight(40)

        self.second_content = QTextEdit()
        layout.addWidget(self.second_content, 1, 2, 1, 2)
        self.second_content.setFontPointSize(14.0)

        self.btn = QPushButton('Проверка')
        self.btn.setFixedHeight(40)
        layout.addWidget(self.btn, 2, 0, 1, 0)
        self.btn.clicked.connect(self.slot_btn)

        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.fileName_choose1=''
        self.fileName_choose2=''

    def slot_btn_first(self):
        self.first_content.clear()
        self.fileName_choose1, filetype = QFileDialog.getOpenFileName(self, "Выбрать 1-й файл", self.cwd, "Text Files (*.txt)")
        if self.fileName_choose1!='':
            self.file1 = open(self.fileName_choose1, 'r',encoding='utf-8')
            with self.file1:
                self.data1 = self.file1.read()
            self.first_content.setFontPointSize(14.0)
            self.first_content.setText(self.data1)
            self.file1.close()
        else:
            self.error_file()

    def slot_btn_second(self):
        self.second_content.clear()
        self.fileName_choose2, filetype = QFileDialog.getOpenFileName(self, "Выбрать 2-й файл", self.cwd, "Text Files (*.txt)")
        if self.fileName_choose2!='':
            self.file2 = open(self.fileName_choose2, 'r',encoding='utf-8')
            with self.file2:
                self.data2 = self.file2.read()
            self.second_content.setFontPointSize(14.0)
            self.second_content.setText(self.data2)
            self.file2.close()
        else:
            self.error_file()

    def slot_btn(self):
        self.text1 = self.first_content.toPlainText()
        self.text2 = self.second_content.toPlainText()

        # nlp = Russian()
        # doc1 = nlp(self.text1)
        # doc2 = nlp(self.text2)
        # t1=doc1[0]
        # t2=doc1[0]
        # print(t1.similarity(t2)),
    
    def file_save1(self):
        self.text1 = self.first_content.toPlainText()
        if self.fileName_choose1!='':
            self.file1 = open(self.fileName_choose1, 'w',encoding='utf-8')
            self.file1.truncate()
            self.file1.write(self.text1)
            self.file1.close()
        else:
            self.error_save()

    def file_save2(self):
        self.text2 = self.second_content.toPlainText()
        if self.fileName_choose2!='':
            self.file2 = open(self.fileName_choose2, 'w',encoding='utf-8')
            self.file2.truncate()
            self.file2.write(self.text2)
            self.file2.close()
        else:
            self.error_save()
    
    def error_save(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Файл для сохранения не открыт')
        msg.setWindowTitle('Ошибка!')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def error_file(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Файл не выбран')
        msg.setWindowTitle('Ошибка!')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

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
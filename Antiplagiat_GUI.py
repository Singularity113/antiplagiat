import sys # Подключение библиотек 
import os
import spacy
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5.QtWidgets import *
from spacy.lang.ru import Russian

# Создание класса для основного окна
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Антиплагиат') # Название окна
        self.cwd = os.getcwd() # Путь до файла
        
        widget = QWidget()
        layout = QGridLayout() # Создание области для размещения виджетов на форме

        self.btn_first = QPushButton() # Кнопка Выбрать 1-й файл
        self.btn_first.setObjectName('btn_first') # Меняем имя объекта
        self.btn_first.setText('Выбрать 1-й файл') # Надпись в кнопке
        layout.addWidget(self.btn_first, 0, 0) # Кнопка расположена на форме в 0 стр. 0 ст. 
        self.btn_first.setFixedHeight(40) # Задаем высоту кнопки = 40
        self.btn_first.clicked.connect(self.slot_btn_first) # При нажатии на кнопку вызываем функцию

        self.btn_save1 = QPushButton() # Кнопка для сохранения 1-го файла
        self.btn_save1.setObjectName('btn_save') # Меняем имя объекта
        self.btn_save1.setText('Сохранить 1 файл') # Надпись в кнопке
        self.btn_save1.clicked.connect(self.file_save1) # При нажатии вызываем функцию
        layout.addWidget(self.btn_save1, 0, 1) # Кнопка расположена на форме в 0 стр. 1 ст.
        self.btn_save1.setFixedHeight(40) # Задаем высоту кнопки = 40

        self.first_content = QTextEdit() # Поле для текста
        layout.addWidget(self.first_content, 1, 0, 1, 2) # Поле для текста расположено на форме в 1 стр. 0 ст. и занимает 1 стр. и 2 ст
        self.first_content.setFontPointSize(14.0) # Изменяем шрифт содержимого на 14

        self.btn_second = QPushButton() # Кнопка для выбора 2-го файла
        self.btn_second.setObjectName('btn_second') # Изменяем имя объекта
        self.btn_second.setText('Выбрать 2-й файл') # Надпись в кнопке = Выбрать 2-й файл
        self.btn_second.clicked.connect(self.slot_btn_second) # При нажатии на кнопку вызываем функцию()
        layout.addWidget(self.btn_second, 0, 2) # Кнопка расположена на форме в 0 стр. 2 ст
        self.btn_second.setFixedHeight(40) # Задаем высоту кнопки = 40

        self.btn_save2 = QPushButton() # Кнопка для сохранения 2-го файла
        self.btn_save2.setObjectName('btn_save2') # Изменяем имя объекта
        self.btn_save2.setText('Сохранить 2 файл') # Надпись в кнопке = Сохранить 2-й файл
        self.btn_save2.clicked.connect(self.file_save2) # При нажтии вызываем функцию()
        layout.addWidget(self.btn_save2, 0, 3) # Кнопка расположена на форме в 0 стр. 3 ст.
        self.btn_save2.setFixedHeight(40) # Изменяем высоту кнопки = 40

        self.second_content = QTextEdit() # Поле для текста
        layout.addWidget(self.second_content, 1, 2, 1, 2) # Поле для текста расположено на форме в 1 стр. 2 ст. и занимет 1 стр. и 2 ст. 
        self.second_content.setFontPointSize(14.0) # Изменяет размер шрифта на 14

        self.btn = QPushButton('Проверка') # Кнопка Проверка
        self.btn.setFixedHeight(40) # Изменяем высоту кнопки  = 40 
        layout.addWidget(self.btn, 2, 0, 1, 4) # Кнопка расположена на форме во 2 стр. 0 ст. и занимает 1 стр. и 4 ст 
        self.btn.clicked.connect(self.slot_btn) # При нажатии на кнопку вызывает функцию()

        widget.setLayout(layout) # Изменение области для добавления виджетов(кнопок, полей для текста)
        self.setCentralWidget(widget)

        self.fileName_choose1 = '' # Путь до 1-го файла пока пустой
        self.fileName_choose2 = '' # Путь до 2-го файла пока пустой

    def slot_btn_first(self): # Функция для выбора 1-го файла
        self.first_content.clear() # Очищаем содержимое поля для ввода 1-го файла
        self.fileName_choose1, filetype = QFileDialog.getOpenFileName(self, "Выбрать 1-й файл", self.cwd, "Text Files (*.txt)") # Выбираем файл.txt и записываем путь в переменную
        if self.fileName_choose1 != '': # Если путь до файла не пустой выполняем:
            self.file1 = open(self.fileName_choose1, 'r', encoding='utf-8') # Открываем файл для чтения, делаем что бы русский отображался правильно
            with self.file1: 
                self.data1 = self.file1.read() # Записываем содержимое файла в переменную
            self.first_content.setFontPointSize(14.0) # Устанавливаем размер шрифта = 14
            self.first_content.setText(self.data1) # Заполняем поле для текста 
            self.file1.close() # Закрываем файл
        else: # В противном случае выдаем ошибку
            self.error_file()

    def slot_btn_second(self): # Функция для выбора 2-го файла
        self.second_content.clear() # Очищаем содержимое поля для ввода 2-го файла
        self.fileName_choose2, filetype = QFileDialog.getOpenFileName(self, "Выбрать 2-й файл", self.cwd, "Text Files (*.txt)") # Выбираем файл.txt и записываем путь в переменную
        if self.fileName_choose2 != '': # Если путь до файла не пустой выполняем:
            self.file2 = open(self.fileName_choose2, 'r', encoding='utf-8') # Открываем файл для чтения, делаем что бы русский отображался правильно
            with self.file2:
                self.data2 = self.file2.read() # Записываем содержимое файла в переменную
            self.second_content.setFontPointSize(14.0) # Устанавливаем размер шрифта = 14
            self.second_content.setText(self.data2) # Заполняем поле для текста
            self.file2.close() # Закрываем файл
        else:
            self.error_file() # В противном случае выдаем ошибку

    def slot_btn(self): # Функция для проверки
            self.text1 = self.first_content.toPlainText() # Записываем в переменную содержимое поля для текста 1
            self.text2 = self.second_content.toPlainText() # Записываем в переменную содержимое поля для текста 2
            self.w2 = Window2() # Вызываем второе окно для результата
            self.w2.show() # Показываем второе окно для результата
         
    def file_save1(self): # Функция для сохранения файла 1
        self.text1 = self.first_content.toPlainText() # Записываем текст из поля в переменную
        if self.fileName_choose1 != '': # Если путь до файла не пустой выполняем:
            self.file1 = open(self.fileName_choose1, 'w', encoding='utf-8') # Открываем файл для записи 
            self.file1.truncate()
            self.file1.write(self.text1) # Записываем в файл содержимое переменной 1
            self.file1.close() # Закрываем файл
        else: # В противном стучае: 
            self.error_save() # Выдаем ошибку

    def file_save2(self): # Функция для сохранения файла 2
        self.text2 = self.second_content.toPlainText() # Записываем текст из поля в переменную
        if self.fileName_choose2 != '': # Если путь до файла не пустой выполняем:
            self.file2 = open(self.fileName_choose2, 'w',encoding='utf-8') # Открываем файл для записи
            self.file2.truncate()
            self.file2.write(self.text2) # Записываем в файл содержимое переменной 2
            self.file2.close() # Закрываем файл
        else: # В противном стучае: 
            self.error_save() # Выдаем ошибку
    
    def error_save(self): # Функция для ошибки сохранения файла
        msg = QMessageBox() # Используем всплывающее сообщение
        msg.setIcon(QMessageBox.Warning) # Меняем иконку = Предупреждение
        msg.setText('Файл для сохранения не открыт') # Текст в сообщении()
        msg.setWindowTitle('Ошибка!') # Имя окна()
        msg.setStandardButtons(QMessageBox.Ok) # Стандартная кнопка = Ок (без кнопки = Отмена)
        msg.exec_() # Для показа окна

    def error_file(self): # Функция для ошибки при выборе файла
        msg = QMessageBox() # Используем всплывающее сообщение
        msg.setIcon(QMessageBox.Warning) # Меняем иконку = Предупреждение
        msg.setText('Файл не выбран') # Текст в сообщении()
        msg.setWindowTitle('Ошибка!') # Имя окна()
        msg.setStandardButtons(QMessageBox.Ok) # Стандартная кнопка = Ок (без кнопки = Отмена)
        msg.exec_() # Для показа окна
        
class Window2(QWidget): # Класс для вывода окна с результатом 
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Результат проверки на плагиат') # Наименование окна()
        self.setGeometry(100,400,500,300) # Размер окна 500 на 300
        title = QLabel('Результат: ', self) # Текст в окне() 
        self.setFont(QFont('Arial', 14)) # Текст в окне(arial, шрифт = 14)
        self.move(100, 100) # Окно выводится на 100 от левой стороны и на 100 сверху
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow() # Запись в переменную Главного окна
    window.showMaximized() # Показываем окно на весь экран
    # sys.__excepthook__ = sys.excepthook  # Для замены системных ошибок на свои
    # def my_exeption_hook(exctype, value, traceback):
    #     msg = QMessageBox()
    #     msg.setIcon(QMessageBox.Information)
    #     msg.setText('Введены не верные данные')
    #     msg.setWindowTitle('Ошибка!')
    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     msg.exec_()
    # sys.excepthook = my_exeption_hook
    sys.exit(app.exec_())



from os import path
from math import sqrt, radians, log10 as log, sin as Sin, cos as Cos, tan as Tan
from sympy import cot as Cot
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial

def sin(dig: int | float) -> int | float:
    return Sin(radians(dig))

def cos(dig: int | float) -> int | float:
    return Cos(radians(dig))

def tan(dig: int | float) -> int | float:
    return Tan(radians(dig))

def cot(dig: int | float) -> int | float:
    return Cot(radians(dig))

class Calculator(QMainWindow):
    def __new__(cls, *args, **kwargs) -> object:
        return super().__new__(cls)
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = QUiLoader().load('{path}/user_interface.ui'.format(path=path.dirname(__file__)), None)
        self.ui.show()
        self.ui.btn_0.clicked.connect(partial(self.sync, '0'))
        self.ui.btn_1.clicked.connect(partial(self.sync, '1'))
        self.ui.btn_2.clicked.connect(partial(self.sync, '2'))
        self.ui.btn_3.clicked.connect(partial(self.sync, '3'))
        self.ui.btn_4.clicked.connect(partial(self.sync, '4'))
        self.ui.btn_5.clicked.connect(partial(self.sync, '5'))
        self.ui.btn_6.clicked.connect(partial(self.sync, '6'))
        self.ui.btn_7.clicked.connect(partial(self.sync, '7'))
        self.ui.btn_8.clicked.connect(partial(self.sync, '8'))
        self.ui.btn_9.clicked.connect(partial(self.sync, '9'))
        self.ui.parenthesis_o.clicked.connect(partial(self.sync, '('))
        self.ui.parenthesis_c.clicked.connect(partial(self.sync, ')'))
        self.ui.sum_btn.clicked.connect(partial(self.sync, '+'))
        self.ui.sub_btn.clicked.connect(partial(self.sync, '-'))
        self.ui.cross_btn.clicked.connect(partial(self.sync, '*'))
        self.ui.division_btn.clicked.connect(partial(self.sync, '÷'))
        self.ui.pow_btn.clicked.connect(partial(self.sync, '^'))
        self.ui.sin_btn.clicked.connect(partial(self.sync, 'sin('))
        self.ui.cos_btn.clicked.connect(partial(self.sync, 'cos('))
        self.ui.tan_btn.clicked.connect(partial(self.sync, 'tan('))
        self.ui.cot_btn.clicked.connect(partial(self.sync, 'cot('))
        self.ui.log_btn.clicked.connect(partial(self.sync, 'log('))
        self.ui.sqrt_btn.clicked.connect(partial(self.sync, '√('))
        self.ui.backspace.clicked.connect(partial(self.backspace))
        self.ui.percentage_btn.clicked.connect(self.percentage_func)
        self.ui.equal_btn.clicked.connect(self.equal)
        self.ui.ac_btn.clicked.connect(self.ac)
        self.ui.dot_btn.clicked.connect(self.dot_func)
        self.ui.neg_pos_btn.clicked.connect(self.neg_pos)
    
    def backspace(self) -> None:
        text = self.ui.textBox.text()
        if text == 'Error': 
            self.ui.textBox.setText('')
        else:
            if text[len(text) - 2:len(text)] == '√(':
                self.ui.textBox.setText(text[:len(text) - 2])
            elif text[len(text) - 1] == '(':
                self.ui.textBox.setText(text[:len(text) - 4])
            else:
                self.ui.textBox.setText(text[:len(text) - 1])

    def sync(self, num: str) -> None:
        self.ui.textBox.setText(self.ui.textBox.text() + str(num))
    
    def dot_func(self) -> None:
        if '.' not in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text() + '.')
        else: pass

    def neg_pos(self) -> None:
        if '-' in self.ui.textBox.text():
            self.ui.textBox.setText(self.ui.textBox.text()[1:])
        else:
            self.ui.textBox.setText('-' + self.ui.textBox.text())

    def equal(self) -> None:
        try:
            self.equation = self.ui.textBox.text()
            self.equation = self.sync_equation(self.equation)
            self.ui.textBox.setText('= ' + str(round(eval(self.equation), 5)))
        except Exception as e:
            self.ui.textBox.setText('Error')
            print(e)

    def ac(self) -> None:
        self.ui.textBox.setText('')

    def percentage_func(self) -> None:
        self.ui.textBox.setText(str(float(self.ui.textBox.text()) / 100))

    @staticmethod
    def sync_equation(equation: str) -> str:
        synced = equation
        if '√' in synced:
            synced = synced.replace('√', 'sqrt')
        if '÷' in synced:
            synced = synced.replace('÷', '/')
        if '^' in synced:
            synced = synced.replace('^', '**')
        if '= ' in synced:
            synced = synced.replace('= ', '')
        return synced

app = QApplication([])
window = Calculator()
app.exec()

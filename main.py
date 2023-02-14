import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 300)

        grid = QGridLayout()

        self.line_edit = QLineEdit()
        self.line_edit.setReadOnly(True)

        grid.addWidget(self.line_edit, 0, 0, 1, 4)

        self.create_button('7', grid, 1, 0)
        self.create_button('8', grid, 1, 1)
        self.create_button('9', grid, 1, 2)
        self.create_button('/', grid, 1, 3)
        self.create_button('4', grid, 2, 0)
        self.create_button('5', grid, 2, 1)
        self.create_button('6', grid, 2, 2)
        self.create_button('*', grid, 2, 3)
        self.create_button('1', grid, 3, 0)
        self.create_button('2', grid, 3, 1)
        self.create_button('3', grid, 3, 2)
        self.create_button('-', grid, 3, 3)
        self.create_button('0', grid, 4, 0, 1, 2)
        self.create_button('.', grid, 4, 2)
        self.create_button('+', grid, 4, 3)
        self.create_button('C', grid, 5, 0)
        self.create_button('=', grid, 5, 1, 1, 3)

        self.setLayout(grid)

    def create_button(self, text, grid, row, column, rowspan=1, colspan=1):
        button = QPushButton(text)
        button.clicked.connect(lambda: self.on_click(text))

        grid.addWidget(button, row, column, rowspan, colspan)

    def on_click(self, key):
        if key == '=':
            try:
                result = str(eval(self.line_edit.text()))
                self.line_edit.setText(result)
            except:
                self.line_edit.setText('Error')
        elif key == 'C':
            self.line_edit.clear()
        else:
            self.line_edit.setText(self.line_edit.text() + key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())

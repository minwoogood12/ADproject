import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class QPushButtonIcon(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(200)
        self.setFixedWidth(200)
        self.setIconSize(QSize(192, 192))

class QPushButtonReset(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(50)
        font = QFont("Helvetica", 12)
        font.setBold(True)
        self.setFont(font)

class QPushButtonSolution(QPushButton):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedHeight(50)
        font = QFont("Helvetica", 12)
        font.setBold(True)
        self.setFont(font)

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.set_default()
        self.set_style()
        self.init_ui()

    def set_default(self):
        self.selection_list = []
        self.figures = ['사자인척하는 고양이.jpg', '추운 고양이.jpg', '놀란 고양이.jpg', '공부하는 고양이.jpg', '식빵 고양이.jpg', '수줍은 고양이.jpg']

        self.icons = {}
        for index, filename in enumerate(self.figures):
            pixmap = QPixmap(filename)
            pixmap = pixmap.scaled(200, 200, Qt.IgnoreAspectRatio)
            icon = QIcon()
            icon.addPixmap(pixmap)
            self.icons[index] = icon

    def set_style(self):
        with open("style", 'r') as f:
            self.setStyleSheet(f.read())
        pass

    def init_ui(self):
        main_layout = QVBoxLayout()

        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()
        layout_3 = QVBoxLayout()

        self.qbuttons = {}
        for index, icon in self.icons.items():
            button = QPushButtonIcon()
            button.setIcon(icon)
            button.clicked.connect(lambda state, button = button, idx = index :
                                   self.qbutton_clicked(state, idx, button))
            layout_1.addWidget(button)
            self.qbuttons[index] = button

        self.sbuttons ={}
        for index in range(len(self.figures)):
            button = QPushButtonIcon()
            self.sbuttons[index] = button
            button.clicked.connect(lambda state, button = button, idx = index:
                                   self.sbutton_clicked(state, idx, button))
            layout_2.addWidget(button)

        self.button_reset = QPushButtonReset("다시하기")
        self.button_reset.clicked.connect(self.action_reset)

        self.button_solution = QPushButtonSolution("모두 보여주기")
        self.button_solution.clicked.connect(self.action_solution)

        layout_3.addWidget(self.button_reset)
        layout_3.addWidget(self.button_solution)

        main_layout.addLayout(layout_1)
        main_layout.addLayout(layout_2)
        main_layout.addLayout(layout_3)

        main_layout.addLayout(main_layout)

        self.setLayout(main_layout)
        self.setFixedSize(main_layout.sizeHint())
        self.setWindowTitle("AD project 고양이 순서 기억하기")
        self.show()


    def qbutton_clicked(self, state, idx, button):
        self.selection_list.append(idx)
        button.setDisabled(True)

    def sbutton_clicked(self, state, idx, button):
        if len(self.selection_list) > idx:
            self.set_button_selected_index(button, idx)

    def set_button_selected_index(self, button, idx):
        sol_index = self.selection_list[idx]
        icon = self.icons[sol_index]
        button.setIcon(icon)

    def check_all_selected(self):
        return len(self.selection_list) == len(self.figures)

    def action_solution(self):
        if self.check_all_selected():
            for index, button in self.sbuttons.items():
                self.set_button_selected_index(button, index)

    def action_reset(self):
        self.selection_list = []
        for button in self.qbuttons.values():
            button.setDisabled(False)
        for button in self.sbuttons.values():
            button.setIcon(QIcon())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
window.resize(500, 500)
lbl = QLabel("Вікторина")
numberlbl = QLabel("Номер переможця")
starBtn = QVBoxButton()


main_line = QVBoxLayout()
main_line.addWidget(lbl)
window.setLayout(main_line)

def banana():
    a = random.randint(1, 10)
    numberlbl.setText(str(a))
starBtn.clicked.connect(banana)
window.show()
app.exec()

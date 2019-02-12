#import the libraries
import sys
import PyQt5.QtWidgets as widget

#build the initialz
app = widget.QApplication(sys.argv)
app.setStyle('Fusion')

w = widget.QWidget()

layout = widget.QVBoxLayout()
b1 = widget.QPushButton('Encrypt')
b2 = widget.QPushButton('Decrypt')
b3 = widget.QPushButton('Exit')
layout.addWidget(b1)
layout.addWidget(b2)
layout.addWidget(b3)

def encrypt_button():
    alert = widget.QMessageBox()
    alert.setText('You clicked the Encyption!')
    alert.exec_()

def decrypt_button():
    alert = widget.QMessageBox()
    alert.setText('You clicked the Decryption!')
    alert.exec_()

def exit_button():
    alert = widget.QMessageBox()
    alert.setText('You clicked the Exit!')
    alert.exec_()

b1.clicked.connect(encrypt_button)
b1.show()
b2.clicked.connect(decrypt_button)
b2.show()
b3.clicked.connect(exit_button)
b3.show()
w.setLayout(layout)
w.show()

app.exec_()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSteganografiEnkripsi = QtWidgets.QPushButton(self.centralwidget)
        self.btnSteganografiEnkripsi.setGeometry(QtCore.QRect(230, 80, 181, 91))
        self.btnSteganografiEnkripsi.setObjectName("btnSteganografiEnkripsi")
        self.btnExtractDecrypt = QtWidgets.QPushButton(self.centralwidget)
        self.btnExtractDecrypt.setGeometry(QtCore.QRect(230, 200, 181, 91))
        self.btnExtractDecrypt.setObjectName("btnExtractDecrypt")
        self.btnCompare = QtWidgets.QPushButton(self.centralwidget)
        self.btnCompare.setGeometry(QtCore.QRect(230, 320, 181, 91))
        self.btnCompare.setObjectName("btnCompare")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aplikasi Steganografi dan Enkripsi pada Gambar"))
        self.btnSteganografiEnkripsi.setText(_translate("MainWindow", "Enkripsi dan Steganografi"))
        self.btnExtractDecrypt.setText(_translate("MainWindow", "Extract dan Dekripsi"))
        self.btnCompare.setText(_translate("MainWindow", "Perbandingan"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



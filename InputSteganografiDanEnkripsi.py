# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputSteganografiDanEnkripsi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from function.DctEncrypt import processEncryptionAndStegano

class Ui_InputSteganografiDanEnkripsi(object):
    
    def setupUi(self, InputSteganografiDanEnkripsi):
        InputSteganografiDanEnkripsi.setObjectName("InputSteganografiDanEnkripsi")
        InputSteganografiDanEnkripsi.resize(777, 673)
        InputSteganografiDanEnkripsi.setFixedSize(777,673)
        self.centralwidget = QtWidgets.QWidget(InputSteganografiDanEnkripsi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("lblCitraSampul")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("lblCitraPesan")
        self.citraSampulPath = QtWidgets.QLineEdit(self.centralwidget)
        self.citraSampulPath.setGeometry(QtCore.QRect(170, 30, 451, 31))
        self.citraSampulPath.setObjectName("citraSampulPath")
        self.citraPesanPath = QtWidgets.QLineEdit(self.centralwidget)
        self.citraPesanPath.setGeometry(QtCore.QRect(170, 80, 451, 31))
        self.citraPesanPath.setObjectName("citraPesanPath")
        self.btnCitraSampul = QtWidgets.QPushButton(self.centralwidget)
        self.btnCitraSampul.setGeometry(QtCore.QRect(640, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraSampul.setFont(font)
        self.btnCitraSampul.setObjectName("btnCitraSampul")
        self.btnCitraSampul.clicked.connect(lambda: self.openDialog(self.citraSampulPath, dialogName='Citra Sampul'))
        self.btnCitraPesan = QtWidgets.QPushButton(self.centralwidget)
        self.btnCitraPesan.setGeometry(QtCore.QRect(640, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraPesan.setFont(font)
        self.btnCitraPesan.setObjectName("btnCitraPesan")
        self.btnCitraPesan.clicked.connect(lambda: self.openDialog(self.citraPesanPath, dialogName='Citra Pesan'))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 125, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("lblNilaiKunciX0Y0")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("lblNilaiX0")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("lblNilaiY0")
        self.doubleSpinBoxX0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxX0.setGeometry(QtCore.QRect(120, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxX0.setFont(font)
        self.doubleSpinBoxX0.setDecimals(8)
        self.doubleSpinBoxX0.setMaximum(1.0)
        self.doubleSpinBoxX0.setSingleStep(1e-06)
        self.doubleSpinBoxX0.setObjectName("doubleSpinBoxX0")
        self.doubleSpinBoxY0 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxY0.setGeometry(QtCore.QRect(120, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxY0.setFont(font)
        self.doubleSpinBoxY0.setDecimals(8)
        self.doubleSpinBoxY0.setMaximum(1.0)
        self.doubleSpinBoxY0.setSingleStep(1e-06)
        self.doubleSpinBoxY0.setObjectName("doubleSpinBoxY0")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 290, 771, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.btnEnkripsiDanStegano = QtWidgets.QPushButton(self.centralwidget)
        self.btnEnkripsiDanStegano.setGeometry(QtCore.QRect(260, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEnkripsiDanStegano.setFont(font)
        self.btnEnkripsiDanStegano.setObjectName("btnEnkripsiDanStegano")
        self.btnEnkripsiDanStegano.clicked.connect(self.encryptAndStegano)
        self.btnKembali = QtWidgets.QPushButton(self.centralwidget)
        self.btnKembali.setGeometry(QtCore.QRect(650, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        InputSteganografiDanEnkripsi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InputSteganografiDanEnkripsi)
        self.statusbar.setObjectName("statusbar")
        InputSteganografiDanEnkripsi.setStatusBar(self.statusbar)

        self.retranslateUi(InputSteganografiDanEnkripsi)
        QtCore.QMetaObject.connectSlotsByName(InputSteganografiDanEnkripsi)

    def retranslateUi(self, InputSteganografiDanEnkripsi):
        _translate = QtCore.QCoreApplication.translate
        InputSteganografiDanEnkripsi.setWindowTitle(_translate("InputSteganografiDanEnkripsi", "Input Steganografi dan Enkripsi"))
        self.label.setText(_translate("InputSteganografiDanEnkripsi", "Citra Sampul :"))
        self.label_2.setText(_translate("InputSteganografiDanEnkripsi", "Citra Pesan   :"))
        self.btnCitraSampul.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.btnCitraPesan.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.label_3.setText(_translate("InputSteganografiDanEnkripsi", "Input Kunci X0 dan Y0"))
        self.label_4.setText(_translate("InputSteganografiDanEnkripsi", "Nilai X0 :"))
        self.label_5.setText(_translate("InputSteganografiDanEnkripsi", "Nilai Y0 :"))
        self.btnEnkripsiDanStegano.setText(_translate("InputSteganografiDanEnkripsi", "Steganografi dan Enkripsi"))
        self.btnKembali.setText(_translate("InputSteganografiDanEnkripsi", "Kembali"))

    def openDialog(self, lineEdit, dialogName = ""):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(InputSteganografiDanEnkripsi, dialogName, '',
                                                  'Images (*.tiff *.jpeg *.jpg *.bmp)', options=options)
        if fileName:
            lineEdit.setText(fileName)
            print(lineEdit.text())

    def encryptAndStegano(self):
       # CheckError = self.doubleSpinBoxX0.value() = 0
        #if CheckError:
            
            resultFile = processEncryptionAndStegano(self.citraSampulPath.text(), self.citraPesanPath.text(), self.doubleSpinBoxX0.value(), self.doubleSpinBoxY0.value())
            pix = QtGui.QPixmap(resultFile)
            item = QtWidgets.QGraphicsPixmapItem(pix)
            scene = QtWidgets.QGraphicsScene(InputSteganografiDanEnkripsi)
            scene.addItem(item)
            self.graphicsView.setScene(scene)
            self.graphicsView.fitInView(scene.sceneRect(),QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputSteganografiDanEnkripsi = QtWidgets.QMainWindow()
    ui = Ui_InputSteganografiDanEnkripsi()
    ui.setupUi(InputSteganografiDanEnkripsi)
    InputSteganografiDanEnkripsi.show()
    sys.exit(app.exec_())
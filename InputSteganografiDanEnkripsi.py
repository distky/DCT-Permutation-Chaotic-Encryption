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
        InputSteganografiDanEnkripsi.resize(776, 670)
        self.btnCitraSampul = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnCitraSampul.setGeometry(QtCore.QRect(640, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraSampul.setFont(font)
        self.btnCitraSampul.setObjectName("btnCitraSampul")
        self.btnCitraSampul.clicked.connect(lambda: self.openDialog(self.citraSampulPath, dialogName='Citra Sampul'))
        self.doubleSpinBoxY0 = QtWidgets.QDoubleSpinBox(InputSteganografiDanEnkripsi)
        self.doubleSpinBoxY0.setGeometry(QtCore.QRect(120, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxY0.setFont(font)
        self.doubleSpinBoxY0.setDecimals(8)
        self.doubleSpinBoxY0.setMaximum(1.0)
        self.doubleSpinBoxY0.setSingleStep(1e-06)
        self.doubleSpinBoxY0.setObjectName("doubleSpinBoxY0")
        self.citraPesanPath = QtWidgets.QLineEdit(InputSteganografiDanEnkripsi)
        self.citraPesanPath.setGeometry(QtCore.QRect(170, 80, 451, 31))
        self.citraPesanPath.setObjectName("citraPesanPath")
        self.citraSampulPath = QtWidgets.QLineEdit(InputSteganografiDanEnkripsi)
        self.citraSampulPath.setGeometry(QtCore.QRect(170, 30, 451, 31))
        self.citraSampulPath.setObjectName("citraSampulPath")
        self.graphicsView = QtWidgets.QGraphicsView(InputSteganografiDanEnkripsi)
        self.graphicsView.setGeometry(QtCore.QRect(0, 290, 771, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.lblNilaiY0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblNilaiY0.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiY0.setFont(font)
        self.lblNilaiY0.setObjectName("lblNilaiY0")
        self.btnEnkripsiDanStegano = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnEnkripsiDanStegano.setGeometry(QtCore.QRect(260, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEnkripsiDanStegano.setFont(font)
        self.btnEnkripsiDanStegano.setObjectName("btnEnkripsiDanStegano")
        self.btnEnkripsiDanStegano.clicked.connect(self.encryptAndStegano)
        self.btnCitraPesan = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnCitraPesan.setGeometry(QtCore.QRect(640, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraPesan.setFont(font)
        self.btnCitraPesan.setObjectName("btnCitraPesan")
        self.btnCitraPesan.clicked.connect(lambda: self.openDialog(self.citraPesanPath, dialogName='Citra Pesan'))
        self.lblCitraPesan = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesan.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraPesan.setFont(font)
        self.lblCitraPesan.setObjectName("lblCitraPesan")
        self.lblInputKunciX0Y0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblInputKunciX0Y0.setGeometry(QtCore.QRect(20, 125, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblInputKunciX0Y0.setFont(font)
        self.lblInputKunciX0Y0.setObjectName("lblInputKunciX0Y0")
        self.lblCitraSampul = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraSampul.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraSampul.setFont(font)
        self.lblCitraSampul.setObjectName("lblCitraSampul")
        self.btnKembali = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnKembali.setGeometry(QtCore.QRect(650, 610, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        self.doubleSpinBoxX0 = QtWidgets.QDoubleSpinBox(InputSteganografiDanEnkripsi)
        self.doubleSpinBoxX0.setGeometry(QtCore.QRect(120, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxX0.setFont(font)
        self.doubleSpinBoxX0.setDecimals(8)
        self.doubleSpinBoxX0.setMaximum(1.0)
        self.doubleSpinBoxX0.setSingleStep(1e-06)
        self.doubleSpinBoxX0.setObjectName("doubleSpinBoxX0")
        self.lblNilaiX0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblNilaiX0.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiX0.setFont(font)
        self.lblNilaiX0.setObjectName("lblNilaiX0")

        self.retranslateUi(InputSteganografiDanEnkripsi)
        QtCore.QMetaObject.connectSlotsByName(InputSteganografiDanEnkripsi)

    def retranslateUi(self, InputSteganografiDanEnkripsi):
        _translate = QtCore.QCoreApplication.translate
        InputSteganografiDanEnkripsi.setWindowTitle(_translate("InputSteganografiDanEnkripsi", "Input Steganografi dan Enkripsi"))
        self.btnCitraSampul.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.lblNilaiY0.setText(_translate("InputSteganografiDanEnkripsi", "Nilai Y0 :"))
        self.btnEnkripsiDanStegano.setText(_translate("InputSteganografiDanEnkripsi", "Steganografi dan Enkripsi"))
        self.btnCitraPesan.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.lblCitraPesan.setText(_translate("InputSteganografiDanEnkripsi", "Citra Pesan   :"))
        self.lblInputKunciX0Y0.setText(_translate("InputSteganografiDanEnkripsi", "Input Kunci X0 dan Y0"))
        self.lblCitraSampul.setText(_translate("InputSteganografiDanEnkripsi", "Citra Sampul :"))
        self.btnKembali.setText(_translate("InputSteganografiDanEnkripsi", "Kembali"))
        self.lblNilaiX0.setText(_translate("InputSteganografiDanEnkripsi", "Nilai X0 :"))

    def openDialog(self, lineEdit, dialogName = ""):
        InputSteganografiDanEnkripsi = QtWidgets.QDialog()
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(InputSteganografiDanEnkripsi, dialogName, ' ',
                                                  'Images (*.tiff *.jpeg *.jpg *.bmp)', options=options)
        if fileName:
            lineEdit.setText(fileName)
            print(lineEdit.text())

    def encryptAndStegano(self):
       # CheckError = self.doubleSpinBoxX0.value() = 0
        #if CheckError:
            InputSteganografiDanEnkripsi = QtWidgets.QDialog()
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
    InputSteganografiDanEnkripsi = QtWidgets.QDialog()
    ui = Ui_InputSteganografiDanEnkripsi()
    ui.setupUi(InputSteganografiDanEnkripsi)
    InputSteganografiDanEnkripsi.show()
    sys.exit(app.exec_())
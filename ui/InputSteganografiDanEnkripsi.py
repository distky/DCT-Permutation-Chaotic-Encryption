# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputSteganografiDanEnkripsi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputSteganografiDanEnkripsi(object):
    def setupUi(self, InputSteganografiDanEnkripsi):
        InputSteganografiDanEnkripsi.setObjectName("InputSteganografiDanEnkripsi")
        InputSteganografiDanEnkripsi.setFixedSize(1046, 726)
        self.citraPesanPath = QtWidgets.QLineEdit(InputSteganografiDanEnkripsi)
        self.citraPesanPath.setGeometry(QtCore.QRect(170, 80, 711, 31))
        self.citraPesanPath.setEnabled(False)
        self.citraPesanPath.setObjectName("citraPesanPath")
        self.citraPesanView = QtWidgets.QGraphicsView(InputSteganografiDanEnkripsi)
        self.citraPesanView.setGeometry(QtCore.QRect(270, 290, 251, 311))
        self.citraPesanView.setObjectName("citraPesanView")
        self.btnStegano = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnStegano.setGeometry(QtCore.QRect(680, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnStegano.setFont(font)
        self.btnStegano.setObjectName("btnStegano")
        self.lblCitraSampul = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraSampul.setGeometry(QtCore.QRect(20, 20, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraSampul.setFont(font)
        self.lblCitraSampul.setObjectName("lblCitraSampul")
        self.lblInputKunciX0Y0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblInputKunciX0Y0.setGeometry(QtCore.QRect(20, 125, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblInputKunciX0Y0.setFont(font)
        self.lblInputKunciX0Y0.setObjectName("lblInputKunciX0Y0")
        self.lblNilaiX0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblNilaiX0.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiX0.setFont(font)
        self.lblNilaiX0.setObjectName("lblNilaiX0")
        self.btnCitraSampul = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnCitraSampul.setGeometry(QtCore.QRect(900, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraSampul.setFont(font)
        self.btnCitraSampul.setObjectName("btnCitraSampul")
        self.btnCitraPesan = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnCitraPesan.setGeometry(QtCore.QRect(900, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraPesan.setFont(font)
        self.btnCitraPesan.setObjectName("btnCitraPesan")
        self.doubleSpinBoxY0 = QtWidgets.QDoubleSpinBox(InputSteganografiDanEnkripsi)
        self.doubleSpinBoxY0.setGeometry(QtCore.QRect(120, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxY0.setFont(font)
        self.doubleSpinBoxY0.setDecimals(3)
        self.doubleSpinBoxY0.setMaximum(1.0)
        self.doubleSpinBoxY0.setSingleStep(0.001)
        self.doubleSpinBoxY0.setObjectName("doubleSpinBoxY0")
        self.doubleSpinBoxX0 = QtWidgets.QDoubleSpinBox(InputSteganografiDanEnkripsi)
        self.doubleSpinBoxX0.setGeometry(QtCore.QRect(120, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxX0.setFont(font)
        self.doubleSpinBoxX0.setDecimals(3)
        self.doubleSpinBoxX0.setMinimum(0.0)
        self.doubleSpinBoxX0.setMaximum(1.0)
        self.doubleSpinBoxX0.setSingleStep(0.001)
        self.doubleSpinBoxX0.setObjectName("doubleSpinBoxX0")
        self.citraSampulPath = QtWidgets.QLineEdit(InputSteganografiDanEnkripsi)
        self.citraSampulPath.setGeometry(QtCore.QRect(170, 30, 711, 31))
        self.citraSampulPath.setEnabled(False)
        self.citraSampulPath.setObjectName("citraSampulPath")
        self.lblCitraPesan = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesan.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraPesan.setFont(font)
        self.lblCitraPesan.setObjectName("lblCitraPesan")
        self.btnKembali = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnKembali.setGeometry(QtCore.QRect(900, 680, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        self.lblNilaiY0 = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblNilaiY0.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiY0.setFont(font)
        self.lblNilaiY0.setObjectName("lblNilaiY0")
        self.citraEnkripsiView = QtWidgets.QGraphicsView(InputSteganografiDanEnkripsi)
        self.citraEnkripsiView.setGeometry(QtCore.QRect(540, 290, 241, 311))
        self.citraEnkripsiView.setObjectName("citraEnkripsiView")
        self.citraSampulView = QtWidgets.QGraphicsView(InputSteganografiDanEnkripsi)
        self.citraSampulView.setGeometry(QtCore.QRect(10, 290, 241, 311))
        self.citraSampulView.setObjectName("citraSampulView")
        self.lblCitraSampulView = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraSampulView.setGeometry(QtCore.QRect(70, 600, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSampulView.setFont(font)
        self.lblCitraSampulView.setObjectName("lblCitraSampulView")
        self.lblCitraPesanView = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesanView.setGeometry(QtCore.QRect(330, 600, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanView.setFont(font)
        self.lblCitraPesanView.setObjectName("lblCitraPesanView")
        self.lblCitraStego = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraStego.setGeometry(QtCore.QRect(840, 600, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraStego.setFont(font)
        self.lblCitraStego.setObjectName("lblCitraStego")
        self.btnSave = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnSave.setGeometry(QtCore.QRect(740, 680, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.citraSteganoView = QtWidgets.QGraphicsView(InputSteganografiDanEnkripsi)
        self.citraSteganoView.setGeometry(QtCore.QRect(800, 290, 241, 311))
        self.citraSteganoView.setObjectName("citraSteganoView")
        self.lblCitraPesanEnkrip = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesanEnkrip.setGeometry(QtCore.QRect(550, 600, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanEnkrip.setFont(font)
        self.lblCitraPesanEnkrip.setObjectName("lblCitraPesanEnkrip")
        self.lblCitraSampulsize = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraSampulsize.setGeometry(QtCore.QRect(10, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSampulsize.setFont(font)
        self.lblCitraSampulsize.setText("")
        self.lblCitraSampulsize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraSampulsize.setObjectName("lblCitraSampulsize")
        self.lblCitraPesansize = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesansize.setGeometry(QtCore.QRect(260, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesansize.setFont(font)
        self.lblCitraPesansize.setText("")
        self.lblCitraPesansize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraPesansize.setObjectName("lblCitraPesansize")
        self.lblCitraPesanEnkripsisize = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraPesanEnkripsisize.setGeometry(QtCore.QRect(520, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanEnkripsisize.setFont(font)
        self.lblCitraPesanEnkripsisize.setText("")
        self.lblCitraPesanEnkripsisize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraPesanEnkripsisize.setObjectName("lblCitraPesanEnkripsisize")
        self.lblCitraSteganosize = QtWidgets.QLabel(InputSteganografiDanEnkripsi)
        self.lblCitraSteganosize.setGeometry(QtCore.QRect(780, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganosize.setFont(font)
        self.lblCitraSteganosize.setText("")
        self.lblCitraSteganosize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraSteganosize.setObjectName("lblCitraSteganosize")
        self.btnEnkripsi = QtWidgets.QPushButton(InputSteganografiDanEnkripsi)
        self.btnEnkripsi.setGeometry(QtCore.QRect(150, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEnkripsi.setFont(font)
        self.btnEnkripsi.setObjectName("btnEnkripsi")

        self.retranslateUi(InputSteganografiDanEnkripsi)
        QtCore.QMetaObject.connectSlotsByName(InputSteganografiDanEnkripsi)

    def retranslateUi(self, InputSteganografiDanEnkripsi):
        _translate = QtCore.QCoreApplication.translate
        InputSteganografiDanEnkripsi.setWindowTitle(_translate("InputSteganografiDanEnkripsi", "Input Steganografi dan Enkripsi"))
        self.btnStegano.setText(_translate("InputSteganografiDanEnkripsi", "Steganografi "))
        self.lblCitraSampul.setText(_translate("InputSteganografiDanEnkripsi", "Citra Sampul :"))
        self.lblInputKunciX0Y0.setText(_translate("InputSteganografiDanEnkripsi", "Input Kunci X0 dan Y0"))
        self.lblNilaiX0.setText(_translate("InputSteganografiDanEnkripsi", "Nilai X0 :"))
        self.btnCitraSampul.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.btnCitraPesan.setText(_translate("InputSteganografiDanEnkripsi", "Open File"))
        self.lblCitraPesan.setText(_translate("InputSteganografiDanEnkripsi", "Citra Pesan   :"))
        self.btnKembali.setText(_translate("InputSteganografiDanEnkripsi", "Kembali"))
        self.lblNilaiY0.setText(_translate("InputSteganografiDanEnkripsi", "Nilai Y0 :"))
        self.lblCitraSampulView.setText(_translate("InputSteganografiDanEnkripsi", "Citra Sampul"))
        self.lblCitraPesanView.setText(_translate("InputSteganografiDanEnkripsi", "Citra Pesan"))
        self.lblCitraStego.setText(_translate("InputSteganografiDanEnkripsi", "Citra Stegano"))
        self.btnSave.setText(_translate("InputSteganografiDanEnkripsi", "Save Hasil"))
        self.lblCitraPesanEnkrip.setText(_translate("InputSteganografiDanEnkripsi", "Citra Pesan Enkripsi"))
        self.btnEnkripsi.setText(_translate("InputSteganografiDanEnkripsi", "Enkripsi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputSteganografiDanEnkripsi = QtWidgets.QDialog()
    ui = Ui_InputSteganografiDanEnkripsi()
    ui.setupUi(InputSteganografiDanEnkripsi)
    InputSteganografiDanEnkripsi.show()
    sys.exit(app.exec_())
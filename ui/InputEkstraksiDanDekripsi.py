# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputEkstraksiDanDekripsi1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InputEkstraksiDanDekripsi(object):
    def setupUi(self, InputEkstraksiDanDekripsi):
        InputEkstraksiDanDekripsi.setObjectName("InputEkstraksiDanDekripsi")
        InputEkstraksiDanDekripsi.resize(767, 706)
        self.lblNilaiX0 = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblNilaiX0.setGeometry(QtCore.QRect(20, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiX0.setFont(font)
        self.lblNilaiX0.setObjectName("lblNilaiX0")
        self.lblNilaiY0 = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblNilaiY0.setGeometry(QtCore.QRect(20, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNilaiY0.setFont(font)
        self.lblNilaiY0.setObjectName("lblNilaiY0")
        self.lblDcmatrix = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblDcmatrix.setGeometry(QtCore.QRect(10, 80, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblDcmatrix.setFont(font)
        self.lblDcmatrix.setObjectName("lblDcmatrix")
        self.lblInputKunciX0Y0 = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblInputKunciX0Y0.setGeometry(QtCore.QRect(20, 125, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblInputKunciX0Y0.setFont(font)
        self.lblInputKunciX0Y0.setObjectName("lblInputKunciX0Y0")
        self.doubleSpinBoxX0 = QtWidgets.QDoubleSpinBox(InputEkstraksiDanDekripsi)
        self.doubleSpinBoxX0.setGeometry(QtCore.QRect(120, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxX0.setFont(font)
        self.doubleSpinBoxX0.setDecimals(8)
        self.doubleSpinBoxX0.setMaximum(1.0)
        self.doubleSpinBoxX0.setSingleStep(1e-08)
        self.doubleSpinBoxX0.setObjectName("doubleSpinBoxX0")
        self.doubleSpinBoxY0 = QtWidgets.QDoubleSpinBox(InputEkstraksiDanDekripsi)
        self.doubleSpinBoxY0.setGeometry(QtCore.QRect(120, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxY0.setFont(font)
        self.doubleSpinBoxY0.setDecimals(8)
        self.doubleSpinBoxY0.setMaximum(1.0)
        self.doubleSpinBoxY0.setSingleStep(1e-08)
        self.doubleSpinBoxY0.setObjectName("doubleSpinBoxY0")
        self.btnKembali = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnKembali.setGeometry(QtCore.QRect(650, 650, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        self.btnCitraStegano = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnCitraStegano.setGeometry(QtCore.QRect(640, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraStegano.setFont(font)
        self.btnCitraStegano.setObjectName("btnCitraStegano")
        self.citraSteganoPath = QtWidgets.QLineEdit(InputEkstraksiDanDekripsi)
        self.citraSteganoPath.setGeometry(QtCore.QRect(170, 30, 451, 31))
        self.citraSteganoPath.setEnabled(False)
        self.citraSteganoPath.setObjectName("citraSteganoPath")
        self.btnDcMatrix = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnDcMatrix.setGeometry(QtCore.QRect(640, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDcMatrix.setFont(font)
        self.btnDcMatrix.setObjectName("btnDcMatrix")
        self.dcMatrixPath = QtWidgets.QLineEdit(InputEkstraksiDanDekripsi)
        self.dcMatrixPath.setGeometry(QtCore.QRect(170, 80, 451, 31))
        self.dcMatrixPath.setEnabled(False)
        self.dcMatrixPath.setObjectName("dcMatrixPath")
        self.lblCitraStegano = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraStegano.setGeometry(QtCore.QRect(10, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraStegano.setFont(font)
        self.lblCitraStegano.setObjectName("lblCitraStegano")
        self.btnEkstraksiDanDekripsi = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnEkstraksiDanDekripsi.setGeometry(QtCore.QRect(260, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEkstraksiDanDekripsi.setFont(font)
        self.btnEkstraksiDanDekripsi.setObjectName("btnEkstraksiDanDekripsi")
        self.citraSteganoView = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraSteganoView.setGeometry(QtCore.QRect(10, 290, 321, 311))
        self.citraSteganoView.setObjectName("citraSteganoView")
        self.lblCitraSteganoview = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoview.setGeometry(QtCore.QRect(550, 600, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoview.setFont(font)
        self.lblCitraSteganoview.setObjectName("lblCitraSteganoview")
        self.citraHasilView = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraHasilView.setGeometry(QtCore.QRect(440, 290, 321, 311))
        self.citraHasilView.setObjectName("citraHasilView")
        self.lblCitraExtract = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraExtract.setGeometry(QtCore.QRect(50, 600, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraExtract.setFont(font)
        self.lblCitraExtract.setObjectName("lblCitraExtract")

        self.retranslateUi(InputEkstraksiDanDekripsi)
        QtCore.QMetaObject.connectSlotsByName(InputEkstraksiDanDekripsi)

    def retranslateUi(self, InputEkstraksiDanDekripsi):
        _translate = QtCore.QCoreApplication.translate
        InputEkstraksiDanDekripsi.setWindowTitle(_translate("InputEkstraksiDanDekripsi", "Input Ekstraksi dan Dekripsi"))
        self.lblNilaiX0.setText(_translate("InputEkstraksiDanDekripsi", "Nilai X0 :"))
        self.lblNilaiY0.setText(_translate("InputEkstraksiDanDekripsi", "Nilai Y0 :"))
        self.lblDcmatrix.setText(_translate("InputEkstraksiDanDekripsi", "DC Matrix      :"))
        self.lblInputKunciX0Y0.setText(_translate("InputEkstraksiDanDekripsi", "Input Kunci X0 dan Y0"))
        self.btnKembali.setText(_translate("InputEkstraksiDanDekripsi", "Kembali"))
        self.btnCitraStegano.setText(_translate("InputEkstraksiDanDekripsi", "Open File"))
        self.btnDcMatrix.setText(_translate("InputEkstraksiDanDekripsi", "Open File"))
        self.lblCitraStegano.setText(_translate("InputEkstraksiDanDekripsi", "Citra Stegano :"))
        self.btnEkstraksiDanDekripsi.setText(_translate("InputEkstraksiDanDekripsi", "Ekstraksi dan Dekripsi"))
        self.lblCitraSteganoview.setText(_translate("InputEkstraksiDanDekripsi", "Citra Stegano"))
        self.lblCitraExtract.setText(_translate("InputEkstraksiDanDekripsi", "Citra Extraksi dan Dekripsi"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputEkstraksiDanDekripsi = QtWidgets.QDialog()
    ui = Ui_InputEkstraksiDanDekripsi()
    ui.setupUi(InputEkstraksiDanDekripsi)
    InputEkstraksiDanDekripsi.show()
    sys.exit(app.exec_())
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
        InputEkstraksiDanDekripsi.setFixedSize(1044, 726)
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
        self.doubleSpinBoxX0.setDecimals(3)
        self.doubleSpinBoxX0.setMinimum(0.0)
        self.doubleSpinBoxX0.setMaximum(1.0)
        self.doubleSpinBoxX0.setSingleStep(1e-03)
        self.doubleSpinBoxX0.setProperty("value", 0.0)
        self.doubleSpinBoxX0.setObjectName("doubleSpinBoxX0")
        self.doubleSpinBoxY0 = QtWidgets.QDoubleSpinBox(InputEkstraksiDanDekripsi)
        self.doubleSpinBoxY0.setGeometry(QtCore.QRect(120, 200, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doubleSpinBoxY0.setFont(font)
        self.doubleSpinBoxY0.setDecimals(3)
        self.doubleSpinBoxY0.setMaximum(1.0)
        self.doubleSpinBoxY0.setSingleStep(1e-03)
        self.doubleSpinBoxY0.setObjectName("doubleSpinBoxY0")
        self.btnKembali = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnKembali.setGeometry(QtCore.QRect(920, 670, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnKembali.setFont(font)
        self.btnKembali.setObjectName("btnKembali")
        self.btnCitraStegano = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnCitraStegano.setGeometry(QtCore.QRect(890, 30, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnCitraStegano.setFont(font)
        self.btnCitraStegano.setObjectName("btnCitraStegano")
        self.citraSteganoPath = QtWidgets.QLineEdit(InputEkstraksiDanDekripsi)
        self.citraSteganoPath.setGeometry(QtCore.QRect(170, 30, 701, 31))
        self.citraSteganoPath.setEnabled(False)
        self.citraSteganoPath.setObjectName("citraSteganoPath")
        self.btnDcMatrix = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnDcMatrix.setGeometry(QtCore.QRect(890, 80, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnDcMatrix.setFont(font)
        self.btnDcMatrix.setObjectName("btnDcMatrix")
        self.dcMatrixPath = QtWidgets.QLineEdit(InputEkstraksiDanDekripsi)
        self.dcMatrixPath.setGeometry(QtCore.QRect(170, 80, 701, 31))
        self.dcMatrixPath.setEnabled(False)
        self.dcMatrixPath.setObjectName("dcMatrixPath")
        self.lblCitraStegano = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraStegano.setGeometry(QtCore.QRect(10, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblCitraStegano.setFont(font)
        self.lblCitraStegano.setObjectName("lblCitraStegano")
        self.btnEkstraksiDanDekripsi = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnEkstraksiDanDekripsi.setGeometry(QtCore.QRect(170, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEkstraksiDanDekripsi.setFont(font)
        self.btnEkstraksiDanDekripsi.setObjectName("btnEkstraksiDanDekripsi")
        self.citraSteganoView = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraSteganoView.setGeometry(QtCore.QRect(10, 290, 241, 311))
        self.citraSteganoView.setObjectName("citraSteganoView")
        self.lblCitraSteganoview = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoview.setGeometry(QtCore.QRect(60, 600, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoview.setFont(font)
        self.lblCitraSteganoview.setObjectName("lblCitraSteganoview")
        self.citraPesanEkstrakView = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraPesanEkstrakView.setGeometry(QtCore.QRect(280, 290, 241, 311))
        self.citraPesanEkstrakView.setObjectName("citraPesanEkstrakView")
        self.lblCitraPesanEkstraksi = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraPesanEkstraksi.setGeometry(QtCore.QRect(310, 600, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanEkstraksi.setFont(font)
        self.lblCitraPesanEkstraksi.setObjectName("lblCitraPesanEkstraksi")
        self.btnopenx0y0 = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnopenx0y0.setGeometry(QtCore.QRect(330, 160, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnopenx0y0.setFont(font)
        self.btnopenx0y0.setObjectName("btnopenx0y0")
        self.btnSave = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnSave.setGeometry(QtCore.QRect(770, 670, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.citraSteganoEkstraksiView = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraSteganoEkstraksiView.setGeometry(QtCore.QRect(540, 290, 241, 311))
        self.citraSteganoEkstraksiView.setObjectName("citraSteganoEkstraksiView")
        self.btnEkstraksiDanDekripsi_2 = QtWidgets.QPushButton(InputEkstraksiDanDekripsi)
        self.btnEkstraksiDanDekripsi_2.setGeometry(QtCore.QRect(670, 250, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnEkstraksiDanDekripsi_2.setFont(font)
        self.btnEkstraksiDanDekripsi_2.setObjectName("btnEkstraksiDanDekripsi_2")
        self.citraHasilView_3 = QtWidgets.QGraphicsView(InputEkstraksiDanDekripsi)
        self.citraHasilView_3.setGeometry(QtCore.QRect(800, 290, 241, 311))
        self.citraHasilView_3.setObjectName("citraHasilView_3")
        self.lblCitraSteganoEkstraksi = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoEkstraksi.setGeometry(QtCore.QRect(560, 600, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoEkstraksi.setFont(font)
        self.lblCitraSteganoEkstraksi.setObjectName("lblCitraSteganoEkstraksi")
        self.lblCitraPesanDekripsi = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraPesanDekripsi.setGeometry(QtCore.QRect(830, 600, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanDekripsi.setFont(font)
        self.lblCitraPesanDekripsi.setObjectName("lblCitraPesanDekripsi")
        self.lblCitraSteganoSize = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoSize.setGeometry(QtCore.QRect(10, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoSize.setFont(font)
        self.lblCitraSteganoSize.setText("")
        self.lblCitraSteganoSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraSteganoSize.setObjectName("lblCitraSteganoSize")
        self.lblCitraPesanEkstraksiSize = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraPesanEkstraksiSize.setGeometry(QtCore.QRect(280, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraPesanEkstraksiSize.setFont(font)
        self.lblCitraPesanEkstraksiSize.setText("")
        self.lblCitraPesanEkstraksiSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraPesanEkstraksiSize.setObjectName("lblCitraPesanEkstraksiSize")
        self.lblCitraSteganoEkstraksiSize = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoEkstraksiSize.setGeometry(QtCore.QRect(540, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoEkstraksiSize.setFont(font)
        self.lblCitraSteganoEkstraksiSize.setText("")
        self.lblCitraSteganoEkstraksiSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraSteganoEkstraksiSize.setObjectName("lblCitraSteganoEkstraksiSize")
        self.lblCitraSteganoview_5 = QtWidgets.QLabel(InputEkstraksiDanDekripsi)
        self.lblCitraSteganoview_5.setGeometry(QtCore.QRect(800, 630, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblCitraSteganoview_5.setFont(font)
        self.lblCitraSteganoview_5.setText("")
        self.lblCitraSteganoview_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCitraSteganoview_5.setObjectName("lblCitraSteganoview_5")

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
        self.btnEkstraksiDanDekripsi.setText(_translate("InputEkstraksiDanDekripsi", "Ekstraksi "))
        self.lblCitraSteganoview.setText(_translate("InputEkstraksiDanDekripsi", "Citra Stegano"))
        self.lblCitraPesanEkstraksi.setText(_translate("InputEkstraksiDanDekripsi", "Citra Pesan Ekstraksi"))
        self.btnopenx0y0.setText(_translate("InputEkstraksiDanDekripsi", "Open File X0 dan Y0"))
        self.btnSave.setText(_translate("InputEkstraksiDanDekripsi", "Save Hasil"))
        self.btnEkstraksiDanDekripsi_2.setText(_translate("InputEkstraksiDanDekripsi", "Dekripsi"))
        self.lblCitraSteganoEkstraksi.setText(_translate("InputEkstraksiDanDekripsi", "Citra Stegano Ekstraksi"))
        self.lblCitraPesanDekripsi.setText(_translate("InputEkstraksiDanDekripsi", "Citra Pesan Dekripsi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputEkstraksiDanDekripsi = QtWidgets.QDialog()
    ui = Ui_InputEkstraksiDanDekripsi()
    ui.setupUi(InputEkstraksiDanDekripsi)
    InputEkstraksiDanDekripsi.show()
    sys.exit(app.exec_())
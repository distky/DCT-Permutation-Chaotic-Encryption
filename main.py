import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QGridLayout, QLabel, QMainWindow, QMessageBox, QScrollArea, QWidget
from ui import MainWindow as MainWindowUI, InputEkstraksiDanDekripsi as InputEkstraksiDanDekripsiUI, InputSteganografiDanEnkripsi as InputSteganografiDanEnkripsiUI, Perbandingan as PerbandinganUI
from function.MainController import processEncryptionAndStegano, processExtractAndDecrypt, processMSE, processPSNR, processNCC, processSaveResult
from function.CommonFunction import VALIDATION_ERROR, convertImageToPixmap, ACTION_CANCELLED, fullStackTrace, validCriteria

class InputSteganografiDanEnkripsi(QWidget):
    def __init__(self, parent=None):
        super(InputSteganografiDanEnkripsi, self).__init__()
        self.ui_steganoenkripsi = InputSteganografiDanEnkripsiUI.Ui_InputSteganografiDanEnkripsi()
        self.ui_steganoenkripsi.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
        
        self.ui_steganoenkripsi.btnCitraSampul.clicked.connect(lambda: {
            openFileDialog(self, self.ui_steganoenkripsi.citraSampulPath, isImage=True, dialogName='Citra Sampul', graphicView=self.ui_steganoenkripsi.citraSampulView, resetResult=lambda:self.resetResult())
        })
        self.ui_steganoenkripsi.btnCitraPesan.clicked.connect(lambda: {
            openFileDialog(self, self.ui_steganoenkripsi.citraPesanPath, isImage=True, dialogName='Citra Pesan', graphicView=self.ui_steganoenkripsi.citraPesanView, resetResult=lambda:self.resetResult())
        })
        self.ui_steganoenkripsi.btnEnkripsiDanStegano.clicked.connect(self.on_btnEnkripsiDanStegano_click)
        self.ui_steganoenkripsi.btnKembali.clicked.connect(lambda: showWindow(self, parent))
    
    def resetResult(self):
        self.ui_steganoenkripsi.citraSteganoView.setScene(None)

    def reset(self):
        self.ui_steganoenkripsi.citraPesanPath.setText(None)
        self.ui_steganoenkripsi.citraSampulPath.setText(None)
        self.ui_steganoenkripsi.doubleSpinBoxX0.setValue(0)
        self.ui_steganoenkripsi.doubleSpinBoxY0.setValue(0)
        self.ui_steganoenkripsi.citraSampulView.setScene(None)
        self.ui_steganoenkripsi.citraPesanView.setScene(None)
        self.resetResult()
    
    def on_btnEnkripsiDanStegano_click(self):
        try:
            embeddedImage, dcCoefficientMatrix, x0, y0 = processEncryptionAndStegano(self.ui_steganoenkripsi.citraSampulPath.text(), self.ui_steganoenkripsi.citraPesanPath.text(), self.ui_steganoenkripsi.doubleSpinBoxX0.value(), self.ui_steganoenkripsi.doubleSpinBoxY0.value(), showMessageBox)
            addImageToGraphicView(self, convertImageToPixmap(embeddedImage), self.ui_steganoenkripsi.citraSteganoView)
            processSaveResult(embeddedImage, lambda: saveFileDialog(self, 'TIFF (*.tif;*.tiff)'), dcMatrix=dcCoefficientMatrix, x0=x0, y0=y0)
        except Exception as e:
            handleException(e, showMessageBox)

class InputEkstraksiDanDekripsi(QWidget):
    def __init__(self, parent=None):
        super(InputEkstraksiDanDekripsi, self).__init__()
        self.ui_ekstraksidekripsi = InputEkstraksiDanDekripsiUI.Ui_InputEkstraksiDanDekripsi()
        self.ui_ekstraksidekripsi.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
    
        self.ui_ekstraksidekripsi.btnCitraStegano.clicked.connect(lambda: {
            openFileDialog(self, self.ui_ekstraksidekripsi.citraSteganoPath, isImage=True, dialogName='Citra Stegano', imageOptions='TIFF (*.tif;*.tiff)', graphicView=self.ui_ekstraksidekripsi.citraSteganoView, resetResult=lambda:self.resetResult())
        })
        self.ui_ekstraksidekripsi.btnDcMatrix.clicked.connect(lambda: {
            openFileDialog(self, self.ui_ekstraksidekripsi.dcMatrixPath, isImage=False, dialogName='DC Matrix', resetResult=lambda:self.resetResult())
        })
        self.ui_ekstraksidekripsi.btnEkstraksiDanDekripsi.clicked.connect(self.on_btnEkstraksiDanDekripsi_click)
        self.ui_ekstraksidekripsi.btnKembali.clicked.connect(lambda: showWindow(self, parent))
    
    def resetResult(self):
        self.ui_ekstraksidekripsi.citraHasilView.setScene(None)

    def reset(self):
        self.ui_ekstraksidekripsi.citraSteganoPath.setText(None)
        self.ui_ekstraksidekripsi.dcMatrixPath.setText(None)
        self.ui_ekstraksidekripsi.doubleSpinBoxX0.setValue(0)
        self.ui_ekstraksidekripsi.doubleSpinBoxY0.setValue(0)
        self.ui_ekstraksidekripsi.citraSteganoView.setScene(None)
        self.resetResult()

    def on_btnEkstraksiDanDekripsi_click(self):
        self.ui_ekstraksidekripsi.citraHasilView.setScene(None)
        try:
            decryptedImage = processExtractAndDecrypt(self.ui_ekstraksidekripsi.citraSteganoPath.text(), self.ui_ekstraksidekripsi.dcMatrixPath.text())
            addImageToGraphicView(self, convertImageToPixmap(decryptedImage), self.ui_ekstraksidekripsi.citraHasilView)
            processSaveResult(decryptedImage, lambda:saveFileDialog(self, 'BMP (*.bmp);;TIFF (*.tif;*.tiff)'))
        except Exception as e:
            handleException(e, showMessageBox)

class Perbandingan(QWidget):
    def __init__(self, parent=None):
        super(Perbandingan, self).__init__()
        self.ui_perbandingan = PerbandinganUI.Ui_Perbandingan()
        self.ui_perbandingan.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
    
        self.ui_perbandingan.btnCitra1.clicked.connect(lambda: {
            openFileDialog(self, self.ui_perbandingan.citra1Path, graphicView=self.ui_perbandingan.graphicsViewCitra1, isImage=True, dialogName='Citra 1', resetResult=lambda:self.resetResult())
        })
        self.ui_perbandingan.btnCitra2.clicked.connect(lambda: {
            openFileDialog(self, self.ui_perbandingan.citra2Path, graphicView=self.ui_perbandingan.graphicsViewCitra2, isImage=True, dialogName='Citra 2', resetResult=lambda:self.resetResult())
        })
        self.ui_perbandingan.btnHitungMSE.clicked.connect(self.on_btnHitungMSE_click)
        self.ui_perbandingan.btnHitungPSNR.clicked.connect(self.on_btnHitungPSNR_click)
        self.ui_perbandingan.btnHitungNCC.clicked.connect(self.on_btnHitungNCC_click)
        self.ui_perbandingan.btnKembali.clicked.connect(lambda: showWindow(self, parent))
    
    def resetResult(self):
        self.ui_perbandingan.txtMSE.setText(None)
        self.ui_perbandingan.txtPSNR.setText(None)
        self.ui_perbandingan.txtNCC.setText(None)
    
    def reset(self):
        self.ui_perbandingan.citra1Path.setText(None)
        self.ui_perbandingan.citra2Path.setText(None)
        self.ui_perbandingan.graphicsViewCitra1.setScene(None)
        self.ui_perbandingan.graphicsViewCitra2.setScene(None)
        self.resetResult()

    def on_btnHitungMSE_click(self):
        try:
            mse = processMSE(self.ui_perbandingan.citra1Path.text(), self.ui_perbandingan.citra2Path.text())
            self.ui_perbandingan.txtMSE.setText(str(mse))
        except Exception as e:
            handleException(e, showMessageBox, True)
    
    def on_btnHitungPSNR_click(self):
        try:
            psnr = processPSNR(self.ui_perbandingan.citra1Path.text(), self.ui_perbandingan.citra2Path.text())
            self.ui_perbandingan.txtPSNR.setText(str(psnr))
        except Exception as e:
            handleException(e, showMessageBox, True)

    def on_btnHitungNCC_click(self):
        try:
            ncc = processNCC(self.ui_perbandingan.citra1Path.text(), self.ui_perbandingan.citra2Path.text())
            self.ui_perbandingan.txtNCC.setText(str(ncc))
        except Exception as e:
            handleException(e, showMessageBox, True)            

class ScrollMessageBox(QMessageBox):
    def __init__(self, *args, **kwargs):
        QMessageBox.__init__(self, *args, **kwargs)
        scrll = QScrollArea(self)
        scrll.setWidgetResizable(True)
        grd = self.findChild(QGridLayout)
        lbl = QLabel(self.text(), self)
        lbl.setWordWrap(True)
        scrll.setWidget(lbl)
        scrll.setMinimumSize (400,200)
        grd.addWidget(scrll,0,1)
        self.setText(None)
        self.exec_()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui_mainwindow = MainWindowUI.Ui_MainWindow()
        self.ui_mainwindow.setupUi(self)
        self.setWindowIcon(QIcon('main.ico'))
        centerWindow(self)

        self.steganografiEnkripsi = InputSteganografiDanEnkripsi(self)
        self.enkripsiDekripsi = InputEkstraksiDanDekripsi(self)
        self.perbandingan = Perbandingan(self)

        self.ui_mainwindow.btnSteganografiEnkripsi.clicked.connect(lambda: showWindow(self, self.steganografiEnkripsi))
        self.ui_mainwindow.btnExtractDecrypt.clicked.connect(lambda: showWindow(self, self.enkripsiDekripsi))
        self.ui_mainwindow.btnCompare.clicked.connect(lambda: showWindow(self, self.perbandingan))

def openFileDialog(window, lineEdit, graphicView=None, isImage=True, dialogName="Dialog", imageOptions='Images (*tif *.tiff *.jpg *.jpeg *.bmp)', resetResult=None):
    options = QFileDialog.Options()

    fileOptions = imageOptions if isImage else 'Numpy Array (*.npy)'

    fileName, _ = QFileDialog.getOpenFileName(window, dialogName, '', fileOptions, options=options)
    if fileName:
        lineEdit.setText(fileName)
        if graphicView != None:
            pix = convertImageToPixmap(fileName, isPath = True)
            addImageToGraphicView(window, pix, graphicView)
            resetResult()

def saveFileDialog(window, fileOptions):
    options = QFileDialog.Options()
    filename, _ = QFileDialog.getSaveFileName(window, "Enter filename", '', fileOptions, options=options)

    if _ == '':
        raise IOError(ACTION_CANCELLED)
    return filename

def showWindow(window, targetWindow):
    window.hide()
    if(hasattr(window, 'reset')):
        window.reset()
    targetWindow.show()

def addImageToGraphicView(window, pix, graphicView):
    item = QGraphicsPixmapItem(pix)
    scene = QGraphicsScene(window)
    scene.addItem(item)
    graphicView.setScene(scene)
    graphicView.fitInView(scene.sceneRect(),QtCore.Qt.AspectRatioMode.KeepAspectRatio)

def centerWindow(window):
    qtRectangle = window.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    window.move(qtRectangle.topLeft())

def showMessageBox(title, message, type = QMessageBox.Information):
    ScrollMessageBox(type, title, message)

def handleException(e, showMessageBox, isCompare=False):
    s = getattr(e, 'message', str(e))
    if s == VALIDATION_ERROR:
        showMessageBox('Warning', validCriteria(isCompare), QMessageBox.Icon.Warning)
    elif s != ACTION_CANCELLED:
        showMessageBox('Error', fullStackTrace(), QMessageBox.Icon.Critical)

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show() 
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
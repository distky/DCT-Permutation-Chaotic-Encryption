import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QGridLayout, QLabel, QMainWindow, QMessageBox, QScrollArea, QWidget
from ui import MainWindow as MainWindowUI, InputEkstraksiDanDekripsi as InputEkstraksiDanDekripsiUI, InputSteganografiDanEnkripsi as InputSteganografiDanEnkripsiUI, Perbandingan as PerbandinganUI
from function.DctEncrypt import processEncryptionAndStegano, processExtractAndDecrypt
from function.CommonFunction import MSE, PSNR, convertImageToPixmap, ACTION_CANCELLED

class InputSteganografiDanEnkripsi(QWidget):
    def __init__(self, parent=None):
        super(InputSteganografiDanEnkripsi, self).__init__()
        self.ui_steganoenkripsi = InputSteganografiDanEnkripsiUI.Ui_InputSteganografiDanEnkripsi()
        self.ui_steganoenkripsi.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
        
        self.ui_steganoenkripsi.btnCitraSampul.clicked.connect(lambda: openFileDialog(self, self.ui_steganoenkripsi.citraSampulPath, isImage=True, dialogName='Citra Sampul', graphicView=self.ui_steganoenkripsi.citraSampulView))
        self.ui_steganoenkripsi.btnCitraPesan.clicked.connect(lambda: openFileDialog(self, self.ui_steganoenkripsi.citraPesanPath, isImage=True, dialogName='Citra Pesan', graphicView=self.ui_steganoenkripsi.citraPesanView))
        self.ui_steganoenkripsi.btnEnkripsiDanStegano.clicked.connect(self.on_btnEnkripsiDanStegano_click)
        self.ui_steganoenkripsi.btnKembali.clicked.connect(lambda: showWindow(self, parent))
    
    def reset(self):
        self.ui_steganoenkripsi.citraPesanPath.setText(None)
        self.ui_steganoenkripsi.citraSampulPath.setText(None)
        self.ui_steganoenkripsi.doubleSpinBoxX0.setValue(0)
        self.ui_steganoenkripsi.doubleSpinBoxY0.setValue(0)
        self.ui_steganoenkripsi.citraSampulView.setScene(None)
        self.ui_steganoenkripsi.citraPesanView.setScene(None)
        self.ui_steganoenkripsi.citraSteganoView.setScene(None)
    
    def on_btnEnkripsiDanStegano_click(self):
        resultPixmap = processEncryptionAndStegano(self.ui_steganoenkripsi.citraSampulPath.text(), self.ui_steganoenkripsi.citraPesanPath.text(), self.ui_steganoenkripsi.doubleSpinBoxX0.value(), self.ui_steganoenkripsi.doubleSpinBoxY0.value(), lambda: saveFileDialog(self, 'Images (*.tiff)'), showMessageBox)
        addImageToGraphicView(self, resultPixmap, self.ui_steganoenkripsi.citraSteganoView)

class InputEkstraksiDanDekripsi(QWidget):
    def __init__(self, parent=None):
        super(InputEkstraksiDanDekripsi, self).__init__()
        self.ui_ekstraksidekripsi = InputEkstraksiDanDekripsiUI.Ui_InputEkstraksiDanDekripsi()
        self.ui_ekstraksidekripsi.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
    
        self.ui_ekstraksidekripsi.btnCitraStegano.clicked.connect(lambda: openFileDialog(self, self.ui_ekstraksidekripsi.citraSteganoPath, isImage=True, dialogName='Citra Stegano', imageOptions='True Image File (*.tiff)', graphicView=self.ui_ekstraksidekripsi.citraSteganoView)) 
        self.ui_ekstraksidekripsi.btnDcMatrix.clicked.connect(lambda: openFileDialog(self, self.ui_ekstraksidekripsi.dcMatrixPath, isImage=False, dialogName='DC Matrix'))
        self.ui_ekstraksidekripsi.btnEkstraksiDanDekripsi.clicked.connect(self.on_btnEkstraksiDanDekripsi_click)
        self.ui_ekstraksidekripsi.btnKembali.clicked.connect(lambda: showWindow(self, parent))

    def reset(self):
        self.ui_ekstraksidekripsi.citraSteganoPath.setText(None)
        self.ui_ekstraksidekripsi.dcMatrixPath.setText(None)
        self.ui_ekstraksidekripsi.doubleSpinBoxX0.setValue(0)
        self.ui_ekstraksidekripsi.doubleSpinBoxY0.setValue(0)
        self.ui_ekstraksidekripsi.citraSteganoView.setScene(None)
        self.ui_ekstraksidekripsi.citraHasilView.setScene(None)

    def on_btnEkstraksiDanDekripsi_click(self):
        resultPixmap = processExtractAndDecrypt(self.ui_ekstraksidekripsi.citraSteganoPath.text(), self.ui_ekstraksidekripsi.dcMatrixPath.text(), self.ui_ekstraksidekripsi.doubleSpinBoxX0.value(), self.ui_ekstraksidekripsi.doubleSpinBoxY0.value(), lambda: saveFileDialog(self, 'JPEG (*.jpeg)'), showMessageBox)
        addImageToGraphicView(self, resultPixmap, self.ui_ekstraksidekripsi.citraHasilView)

class Perbandingan(QWidget):
    def __init__(self, parent=None):
        super(Perbandingan, self).__init__()
        self.ui_perbandingan = PerbandinganUI.Ui_Perbandingan()
        self.ui_perbandingan.setupUi(self)
        self.setWindowIcon(parent.windowIcon())
        centerWindow(self)
    
        self.ui_perbandingan.btnCitra1.clicked.connect(lambda: openFileDialog(self, self.ui_perbandingan.citra1Path, graphicView=self.ui_perbandingan.graphicsViewCitra1, isImage=True, dialogName='Citra 1'))
        self.ui_perbandingan.btnCitra2.clicked.connect(lambda: openFileDialog(self, self.ui_perbandingan.citra2Path, graphicView=self.ui_perbandingan.graphicsViewCitra2, isImage=True, dialogName='Citra 2'))
        self.ui_perbandingan.btnHitungMSE.clicked.connect(self.on_btnHitungMSE_click)
        self.ui_perbandingan.btnHitungPSNR.clicked.connect(self.on_btnHitungPSNR_click)
        self.ui_perbandingan.btnKembali.clicked.connect(lambda: showWindow(self, parent))
    
    def reset(self):
        self.ui_perbandingan.citra1Path.setText(None)
        self.ui_perbandingan.citra2Path.setText(None)
        self.ui_perbandingan.txtMSE.setText(None)
        self.ui_perbandingan.txtPSNR.setText(None)
        self.ui_perbandingan.graphicsViewCitra1.setScene(None)
        self.ui_perbandingan.graphicsViewCitra2.setScene(None)

    def on_btnHitungMSE_click(self):
        self.ui_perbandingan.txtMSE.setText(str(MSE(self.ui_perbandingan.citra1Path.text(), self.ui_perbandingan.citra2Path.text())))
    
    def on_btnHitungPSNR_click(self):
        self.ui_perbandingan.txtPSNR.setText(str(PSNR(self.ui_perbandingan.citra1Path.text(), self.ui_perbandingan.citra2Path.text())))

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

def openFileDialog(window, lineEdit, graphicView = None, isImage = True, dialogName = "", imageOptions = 'Images (*.tiff *.jpeg *.jpg *.bmp)'):
    options = QFileDialog.Options()

    fileOptions = imageOptions if isImage else 'Numpy Array (*.npy)'

    fileName, _ = QFileDialog.getOpenFileName(window, dialogName, '', fileOptions, options=options)
    if fileName:
        lineEdit.setText(fileName)
        if graphicView != None:
            pix = convertImageToPixmap(fileName, isPath = True)
            addImageToGraphicView(window, pix, graphicView)

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
 
def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show() 
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import imutils
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import sys
from file_input import modify_images
from openfile import App
from panorama_application import Ui_MainWindow
from panorama_stitch import panorama_image

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.open)
        self.ui.pushButton_4.clicked.connect(self.note)
        self.ui.pushButton.clicked.connect(self.panorama)
        self.show()
        
    def open(self):
        self.app = App()
        self.files = self.app.openFileNamesDialog()
        self.images = modify_images(self.files)
    
    def panorama(self):
        self.pano = panorama_image()
        self.no_images = len(self.images)
        if self.no_images == 2:
            self.result = self.pano.images_stitching([self.images[0], self.images[1]])
        else:
            self.result = self.pano.images_stitching([self.images[self.no_images-2], self.images[self.no_images-1]])
            for i in range(self.no_images - 2):
                self.result = self.pano.images_stitching([self.images[self.no_images-i-3],self.result])
        
        rows, cols = np.where(self.result[:, :, 0] != 0)
        min_row, max_row = min(rows), max(rows) + 1
        min_col, max_col = min(cols), max(cols) + 1
        self.result = self.result[min_row:max_row, min_col:max_col, :]
        self.app = App()
        self.file = self.app.saveFileDialog()
        cv2.imwrite(self.file, self.result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def note(self):
        QtWidgets.QMessageBox.information(None, "WARMING", "please renames images files in order from left to right(1.jpg,2.jpg,...,n.jpg)")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
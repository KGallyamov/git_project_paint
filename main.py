from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys
WIDTH = 800
HEIGHT = 600


class Window(QMainWindow):
    def __init__(self):
        super().init()
        top = 400
        left = 400
        width = WIDTH
        height = HEIGHT
        icon = ''  # создание иконки
        self.setWindowTitle('Paint')
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        # здесь задаются изначальные значения
        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()

        mainMenu = self.menuBar()  # этот интерфейс гораздо удобнее
        fileMenu = mainMenu.addMenu('File')
        brushMenu = mainMenu.addMenu('Brush Size')
        brushColor = mainMenu.addMenu('Brush Color')
        saveAction = QAction(QIcon('icons/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')  # горячие клавиши
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save())
        clearAction = QAction(QIcon('icons/clear.png'), 'Clear', self)
        clearAction.setShortcut('Ctrl+C')  # горячие клавиши
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)
        threepxAction = QAction(QIcon('icons/threepx.png'), '3px', self)
        threepxAction.setShortcut('Ctrl+T')  # горячие клавиши
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)
        fivepxAction = QAction(QIcon('icons/fivepx.png'), '5px', self)
        fivepxAction.setShortcut('Ctrl+F')  # горячие клавиши
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)
        sevenpxAction = QAction(QIcon('icons/sevenpx.png'), '7px', self)
        sevenpxAction.setShortcut('Ctrl+S')  # горячие клавиши
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)
        ninepxAction = QAction(QIcon('icons/ninepx.png'), '9px', self)
        ninepxAction.setShortcut('Ctrl+N')  # горячие клавиши
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)
        blackAction = QAction(QIcon('icons/black.png'), 'Black', self)
        blackAction.setShortcut('Ctrl + B')  # горячие клавиши
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)
        redAction = QAction(QIcon('icons/red.png'), 'Red', self)
        redAction.setShortcut('Ctrl + W')  # горячие клавиши
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)
        greenAction = QAction(QIcon('icons/green.png'), 'Green', self)
        greenAction.setShortcut('Ctrl + G')  # горячие клавиши
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)
        yellowAction = QAction(QIcon('icons/yellow.png'), 'Yellow', self)
        yellowAction.setShortcut('Ctrl + H')  # горячие клавиши
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)
        # теперь через клавиатуру можно настроить цвет и толщину пера

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.leftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())  # рисование
            # изначально моей идей было рисование множеством маленьких кружочков, но для этого есть drawLine
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'PNG (*.png);;JPEG(*.jpg)')
        if filePath == '':
            return
        self.image.save(filePath)  # сохранение изображения

    def clear(self):
        self.image.fill(Qt.white)  # очистить экран
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.black

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

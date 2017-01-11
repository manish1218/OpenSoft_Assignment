import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        #Creating Window
        super(Window, self).__init__()
        self.setGeometry(50 , 50 , 640, 320)
        self.setWindowTitle("Basic Text Editor")
        self.setWindowIcon(QtGui.QIcon("text.png"))

        #defining the actions
        #newFile
        actionNew=QtGui.QAction('&New File' , self)
        actionNew.setShortcut('Ctrl+N')
        actionNew.setStatusTip('Create New File')
        actionNew.triggered.connect(self.new_file)

        # openFile
        actionOpen = QtGui.QAction('&Open File', self)
        actionOpen.setShortcut('Ctrl+O')
        actionOpen.setStatusTip('Open a File')
        actionOpen.triggered.connect(self.open_file)

        # saveFile
        actionSave = QtGui.QAction('&Save File', self)
        actionSave.setShortcut('Ctrl+S')
        actionSave.setStatusTip('Save the File')
        actionSave.triggered.connect(self.save_file)

        # exitFile
        actionExit = QtGui.QAction('&Exit File', self)
        actionExit.setShortcut('Ctrl+Q')
        actionExit.setStatusTip('Leave File')
        actionExit.triggered.connect(self.exit_file)

        #creating StatusBar
        self.statusBar()

        #creating MenuBar
        mainMenu=self.menuBar()

        #creating The list title and adding actions into it
        fileMenu=mainMenu.addMenu('&File')
        fileMenu.addAction(actionNew)
        fileMenu.addAction(actionOpen)
        fileMenu.addAction(actionSave)
        fileMenu.addAction(actionExit)

        self.show()

    def home(self):
            # we may also use sizeHint() instead


        boldAction = QtGui.QAction(QtGui.QIcon('bold.png'), 'Bold', self)
        boldAction.triggered.connect(self.bold_text)

        italicAction = QtGui.QAction(QtGui.QIcon('italic.png'), 'Italic', self)
        italicAction.triggered.connect(self.italic_text)

        underlineAction = QtGui.QAction(QtGui.QIcon('underline.png'), 'Underline', self)
        underlineAction.triggered.connect(self.underline_text)

        undoAction = QtGui.QAction(QtGui.QIcon('underline.png'), 'Undo', self)
        undoAction.triggered.connect(self.undo_text)

        self.toolBar = self.addToolBar('Edit Text')
        self.toolBar.addAction(boldAction)
        self.toolBar.addAction(italicAction)
        self.toolBar.addAction(underlineAction)

        self.show()

    def bold_text(self):
        self.textEdit.setFontUnderline(False)

    def italic_text(self):
        pass

    def underline_text(self):
        self.textEdit.setFontUnderline(True)
    def undo_text(self):
        pass


    def new_file(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        print "lola"
        print self.textEdit.currentFont()
        self.home()

    def open_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(name, 'r')
        self.new_file()
        with file:
            text = file.read()
            self.textEdit.setText(text)

    def save_file(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text=self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def exit_file(self):
        choice = QtGui.QMessageBox.question(self, 'Extract', "Unsaved Changes will be Lost! Do you still want to quit?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

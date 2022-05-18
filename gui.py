from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread
from pathlib import Path
import generator
from functools import partial


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1017, 690)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.collectionDescriptionInput = QtWidgets.QTextEdit(
            self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed,
            QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.collectionDescriptionInput.sizePolicy().hasHeightForWidth())
        self.collectionDescriptionInput.setSizePolicy(sizePolicy)
        self.collectionDescriptionInput.setMaximumSize(
            QtCore.QSize(300, 16777215))
        self.collectionDescriptionInput.setTabChangesFocus(True)
        self.collectionDescriptionInput.setObjectName(
            "collectionDescriptionInput")
        self.gridLayout_2.addWidget(
            self.collectionDescriptionInput, 4, 2, 1, 1)
        self.ipfsUriInput = QtWidgets.QTextEdit(self.centralwidget)
        self.ipfsUriInput.setMaximumSize(QtCore.QSize(300, 30))
        self.ipfsUriInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ipfsUriInput.setTabChangesFocus(True)
        self.ipfsUriInput.setObjectName("ipfsUriInput")
        self.gridLayout_2.addWidget(self.ipfsUriInput, 5, 2, 1, 1)
        self.collectionNameInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.collectionNameInput.sizePolicy().hasHeightForWidth())
        self.collectionNameInput.setSizePolicy(sizePolicy)
        self.collectionNameInput.setMaximumSize(QtCore.QSize(300, 30))
        self.collectionNameInput.setTabChangesFocus(True)
        self.collectionNameInput.setObjectName("collectionNameInput")
        self.gridLayout_2.addWidget(self.collectionNameInput, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(
            QtWidgets.QAbstractItemView.InternalMove)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setObjectName("upButton")
        self.verticalLayout_2.addWidget(self.upButton)
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_2.addWidget(self.removeButton)
        self.downButton = QtWidgets.QPushButton(self.centralwidget)
        self.downButton.setObjectName("downButton")
        self.verticalLayout_2.addWidget(self.downButton)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            400, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.layerNameInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.layerNameInput.sizePolicy().hasHeightForWidth())
        self.layerNameInput.setSizePolicy(sizePolicy)
        self.layerNameInput.setMaximumSize(QtCore.QSize(300, 30))
        self.layerNameInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.layerNameInput.setTabChangesFocus(True)
        self.layerNameInput.setObjectName("layerNameInput")
        self.horizontalLayout_4.addWidget(self.layerNameInput)
        self.addLayerButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.addLayerButton.sizePolicy().hasHeightForWidth())
        self.addLayerButton.setSizePolicy(sizePolicy)
        self.addLayerButton.setObjectName("addLayerButton")
        self.horizontalLayout_4.addWidget(self.addLayerButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.metadataUpdateButton = QtWidgets.QPushButton(self.centralwidget)
        self.metadataUpdateButton.setObjectName("metadataUpdateButton")
        self.gridLayout.addWidget(self.metadataUpdateButton, 1, 2, 1, 1)
        self.randomCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.randomCheck.setObjectName("randomCheck")
        self.gridLayout.addWidget(self.randomCheck, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 5, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setContentsMargins(0, 0, -1, -1)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.videoOutputInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.videoOutputInput.sizePolicy().hasHeightForWidth())
        self.videoOutputInput.setSizePolicy(sizePolicy)
        self.videoOutputInput.setMaximumSize(QtCore.QSize(16777215, 30))
        self.videoOutputInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.videoOutputInput.setTabChangesFocus(True)
        self.videoOutputInput.setObjectName("videoOutputInput")
        self.gridLayout_3.addWidget(self.videoOutputInput, 0, 1, 1, 1)
        self.selectFrameOutput = QtWidgets.QPushButton(self.centralwidget)
        self.selectFrameOutput.setObjectName("selectFrameOutput")
        self.gridLayout_3.addWidget(self.selectFrameOutput, 1, 2, 1, 1)
        self.selectVideoOutput = QtWidgets.QPushButton(self.centralwidget)
        self.selectVideoOutput.setObjectName("selectVideoOutput")
        self.gridLayout_3.addWidget(self.selectVideoOutput, 0, 2, 1, 1)
        self.frameOutputInput = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frameOutputInput.sizePolicy().hasHeightForWidth())
        self.frameOutputInput.setSizePolicy(sizePolicy)
        self.frameOutputInput.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frameOutputInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frameOutputInput.setTabChangesFocus(True)
        self.frameOutputInput.setObjectName("frameOutputInput")
        self.gridLayout_3.addWidget(self.frameOutputInput, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 3)
        self.statusText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.statusText.sizePolicy().hasHeightForWidth())
        self.statusText.setSizePolicy(sizePolicy)
        self.statusText.setMaximumSize(QtCore.QSize(16777215, 30))
        self.statusText.setObjectName("statusText")
        self.gridLayout_3.addWidget(self.statusText, 3, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout_3, 6, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.collectionSizeInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.collectionSizeInput.sizePolicy().hasHeightForWidth())
        self.collectionSizeInput.setSizePolicy(sizePolicy)
        self.collectionSizeInput.setMaximumSize(QtCore.QSize(100, 30))
        self.collectionSizeInput.setObjectName("collectionSizeInput")
        self.horizontalLayout_3.addWidget(self.collectionSizeInput)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QtCore.QSize(100, 30))
        self.label_8.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.frameCountInput = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frameCountInput.sizePolicy().hasHeightForWidth())
        self.frameCountInput.setSizePolicy(sizePolicy)
        self.frameCountInput.setMaximumSize(QtCore.QSize(100, 30))
        self.frameCountInput.setClearButtonEnabled(False)
        self.frameCountInput.setObjectName("frameCountInput")
        self.horizontalLayout_3.addWidget(self.frameCountInput)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 2, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setMaximumSize(QtCore.QSize(367, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.generateButton.setFont(font)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout_5.addWidget(self.generateButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 1, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(27)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.layerNameInput, self.addLayerButton)
        MainWindow.setTabOrder(self.addLayerButton, self.randomCheck)
        MainWindow.setTabOrder(self.randomCheck, self.metadataUpdateButton)
        MainWindow.setTabOrder(self.metadataUpdateButton, self.generateButton)
        MainWindow.setTabOrder(self.generateButton, self.collectionSizeInput)
        MainWindow.setTabOrder(self.collectionSizeInput, self.frameCountInput)
        MainWindow.setTabOrder(self.frameCountInput, self.collectionNameInput)
        MainWindow.setTabOrder(self.collectionNameInput,
                               self.collectionDescriptionInput)
        MainWindow.setTabOrder(
            self.collectionDescriptionInput, self.ipfsUriInput)
        MainWindow.setTabOrder(self.ipfsUriInput, self.videoOutputInput)
        MainWindow.setTabOrder(self.videoOutputInput, self.selectVideoOutput)
        MainWindow.setTabOrder(self.selectVideoOutput, self.frameOutputInput)
        MainWindow.setTabOrder(self.frameOutputInput, self.selectFrameOutput)
        MainWindow.setTabOrder(self.selectFrameOutput, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.upButton)
        MainWindow.setTabOrder(self.upButton, self.removeButton)
        MainWindow.setTabOrder(self.removeButton, self.downButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Gordion Video Generator"))
        self.label_4.setText(_translate("MainWindow", "Collection Size"))
        self.label_7.setText(_translate("MainWindow", "IPFS URI"))
        self.label_5.setText(_translate("MainWindow", "Collection Name"))
        self.label.setText(_translate("MainWindow", "Layer Name"))
        self.upButton.setText(_translate("MainWindow", "Up"))
        self.removeButton.setText(_translate("MainWindow", "Remove"))
        self.downButton.setText(_translate("MainWindow", "Down"))
        self.addLayerButton.setText(_translate("MainWindow", "Add Layer"))
        self.metadataUpdateButton.setText(
            _translate("MainWindow", "Update Metadata"))
        self.randomCheck.setText(_translate("MainWindow", "Random Background"))
        self.label_6.setText(_translate(
            "MainWindow", "Collection Description"))
        self.selectFrameOutput.setText(
            _translate("MainWindow", "Select Frame Folder"))
        self.selectVideoOutput.setText(
            _translate("MainWindow", "Select Video Folder"))
        self.label_2.setText(_translate("MainWindow", "Video Output Folder"))
        self.label_3.setText(_translate("MainWindow", "Frame Output Folder"))
        self.statusText.setText(_translate("MainWindow", "Status: None"))
        self.label_8.setText(_translate("MainWindow", "FPS"))
        self.generateButton.setText(_translate("MainWindow", "GENERATE"))
        self.label_9.setText(_translate(
            "MainWindow", "Gordion Video Generator V1"))

        self.frameCountInput.setValidator(QtGui.QIntValidator())
        self.collectionSizeInput.setValidator(QtGui.QIntValidator())

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.setHorizontalHeaderLabels(
            ['Layer Name', 'Layer Directory'])

        self.addLayerButton.clicked.connect(self.addLayer)
        self.upButton.clicked.connect(self.moveUp)
        self.downButton.clicked.connect(self.moveDown)
        self.removeButton.clicked.connect(self.removeRow)
        self.generateButton.clicked.connect(self.generate)
        self.selectFrameOutput.clicked.connect(
            lambda: self.selectFolder(self.frameOutputInput))
        self.selectVideoOutput.clicked.connect(
            lambda: self.selectFolder(self.videoOutputInput))
        self.metadataUpdateButton.clicked.connect(self.updateMetadata)

        MainWindow.setWindowIcon(QtGui.QIcon('encoder.ico'))

    def showErrorBox(self, errorMsg):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText(errorMsg)
        # msg.setInformativeText('Please Select Folder')
        msg.setWindowTitle("Error")
        msg.exec_()

    def moveDown(self):
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        if row < self.tableWidget.rowCount() - 1:
            self.tableWidget.insertRow(row + 2)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(
                    row + 2, i, self.tableWidget.takeItem(row, i))
                self.tableWidget.setCurrentCell(row + 2, column)
            self.tableWidget.removeRow(row)

    def moveUp(self):
        row = self.tableWidget.currentRow()
        column = self.tableWidget.currentColumn()
        if row > 0:
            self.tableWidget.insertRow(row - 1)
            for i in range(self.tableWidget.columnCount()):
                self.tableWidget.setItem(
                    row - 1, i, self.tableWidget.takeItem(row + 1, i))
                self.tableWidget.setCurrentCell(row - 1, column)
            self.tableWidget.removeRow(row + 1)

    def removeRow(self):
        row = self.tableWidget.currentRow()
        self.tableWidget.removeRow(row)

    def addLayer(self):
        layerName = self.layerNameInput.toPlainText()
        if (layerName == ""):
            self.showErrorBox('Please Enter Layer Name')
            return
        file = str(QtWidgets.QFileDialog.getExistingDirectory(
            None, "Select Layer Directory"))
        rowPosition = self.tableWidget.rowCount()
        if(layerName != "" and file != ""):
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(layerName))
            self.tableWidget.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem(file))
        elif (file == ""):
            # self.showErrorBox('Please Select Folder')
            return

    def selectFolder(self, textBox):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(
            None, "Select Layer Directory"))
        textBox.setText(str(Path(file)))

    def updateProgress(self, percent):
        self.progressBar.setProperty("value", percent)

    def updateStatus(self, statusText):
        self.statusText.setText(statusText)

    def updateMetadata(self):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(
            None, "Select Metadata Directory"))

        col_name = self.collectionNameInput.toPlainText()
        col_desc = self.collectionDescriptionInput.toPlainText()
        uri = self.ipfsUriInput.toPlainText()

        # THREADING

        if(str(file) != ''):
            self.thread = QThread()
            self.generator = generator.Generator()
            self.generator.moveToThread(self.thread)
            self.thread.started.connect(
                partial(self.generator.updateMetadata, col_name, col_desc, file, uri))
            self.generator.finished.connect(self.thread.quit)
            self.generator.finished.connect(self.thread.wait)
            self.generator.progress.connect(self.updateProgress)
            self.generator.progressStatus.connect(self.updateStatus)
            self.generator.error.connect(self.showErrorBox)
            self.thread.start()

    isGenerating = False

    def generate(self):
        self.thread = QThread()
        self.generator = generator.Generator()
        if not self.isGenerating:
            self.isGenerating = True
            isRandom = False
            if self.randomCheck.isChecked():
                isRandom = True
            layers = []
            dirs = []
            col_size = 1 if (self.collectionSizeInput.text() == "") else int(
                self.collectionSizeInput.text())
            # print(col_size)
            fps = 30 if (self.frameCountInput.text() == "") else int(
                self.frameCountInput.text())
            # print(fps)
            col_name = self.collectionNameInput.toPlainText()
            col_desc = self.collectionDescriptionInput.toPlainText()
            uri = self.ipfsUriInput.toPlainText()
            frameOutputDir = Path(self.frameOutputInput.toPlainText())
            movieOutputDir = Path(self.videoOutputInput.toPlainText())
            for i in range(self.tableWidget.rowCount()):
                layers.append(str(self.tableWidget.item(i, 0).text()))
                dirs.append(str(self.tableWidget.item(i, 1).text()))
            # print(layers)
            # print(dirs)

            # THREADING

            if(layers != [] and dirs != []):
                self.generator.moveToThread(self.thread)
                self.thread.started.connect(partial(self.generator.main, col_name, col_desc, uri, frameOutputDir,
                                            movieOutputDir, fps, layers=layers, layerDirs=dirs, randomBackground=isRandom, generatedNo=col_size))
                self.generator.finished.connect(self.thread.quit)
                self.generator.finished.connect(self.thread.wait)
                self.generator.progress.connect(self.updateProgress)
                self.generator.progressStatus.connect(self.updateStatus)
                self.generator.error.connect(self.showErrorBox)
                self.thread.start()
                # self.generateButton.setText("STOP")
            else:
                self.showErrorBox("No layer selected!")
                return
        # else:
        #     self.thread.terminate()
        #     self.thread.wait()
        #     self.showErrorBox("Generation Stopped")
        #     self.generateButton.setText("GENERATE")
        #     self.isGenerating = False


if __name__ == "__main__":
    # gen = generator.Generator()
    # gen.main("col_name", "col_desc", "uri", str(Path("D:\Freelance\AnimationGeneration\_FrameOut")), str(Path(
    #     "D:\Freelance\AnimationGeneration\_VideoOut")), 30, ["f", "s"], layerDirs=[str(Path("D:\Freelance\AnimationGeneration\dist\Layers\First")),str(Path("D:\Freelance\AnimationGeneration\dist\Layers\Second"))], generatedNo=1)
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

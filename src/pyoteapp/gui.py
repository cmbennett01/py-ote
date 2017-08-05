# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simple_plot_ver2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1398, 990)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(12)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.readData = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.readData.sizePolicy().hasHeightForWidth())
        self.readData.setSizePolicy(sizePolicy)
        self.readData.setObjectName("readData")
        self.verticalLayout.addWidget(self.readData)
        self.showSecondaryCheckBox = QtWidgets.QCheckBox(self.widget)
        self.showSecondaryCheckBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showSecondaryCheckBox.sizePolicy().hasHeightForWidth())
        self.showSecondaryCheckBox.setSizePolicy(sizePolicy)
        self.showSecondaryCheckBox.setMaximumSize(QtCore.QSize(307, 16777215))
        self.showSecondaryCheckBox.setObjectName("showSecondaryCheckBox")
        self.verticalLayout.addWidget(self.showSecondaryCheckBox)
        self.doBlockIntegration = QtWidgets.QPushButton(self.widget)
        self.doBlockIntegration.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doBlockIntegration.sizePolicy().hasHeightForWidth())
        self.doBlockIntegration.setSizePolicy(sizePolicy)
        self.doBlockIntegration.setObjectName("doBlockIntegration")
        self.verticalLayout.addWidget(self.doBlockIntegration)
        self.setDataLimits = QtWidgets.QPushButton(self.widget)
        self.setDataLimits.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setDataLimits.sizePolicy().hasHeightForWidth())
        self.setDataLimits.setSizePolicy(sizePolicy)
        self.setDataLimits.setToolTipDuration(-1)
        self.setDataLimits.setObjectName("setDataLimits")
        self.verticalLayout.addWidget(self.setDataLimits)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.smoothSecondaryButton = QtWidgets.QPushButton(self.widget)
        self.smoothSecondaryButton.setEnabled(False)
        self.smoothSecondaryButton.setObjectName("smoothSecondaryButton")
        self.horizontalLayout_5.addWidget(self.smoothSecondaryButton)
        self.numSmoothPointsEdit = QtWidgets.QLineEdit(self.widget)
        self.numSmoothPointsEdit.setEnabled(False)
        self.numSmoothPointsEdit.setFrame(True)
        self.numSmoothPointsEdit.setObjectName("numSmoothPointsEdit")
        self.horizontalLayout_5.addWidget(self.numSmoothPointsEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.normalizeButton = QtWidgets.QPushButton(self.widget)
        self.normalizeButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.normalizeButton.sizePolicy().hasHeightForWidth())
        self.normalizeButton.setSizePolicy(sizePolicy)
        self.normalizeButton.setObjectName("normalizeButton")
        self.verticalLayout.addWidget(self.normalizeButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.doNoiseAnalysis = QtWidgets.QPushButton(self.widget)
        self.doNoiseAnalysis.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doNoiseAnalysis.sizePolicy().hasHeightForWidth())
        self.doNoiseAnalysis.setSizePolicy(sizePolicy)
        self.doNoiseAnalysis.setObjectName("doNoiseAnalysis")
        self.verticalLayout.addWidget(self.doNoiseAnalysis)
        self.computeSigmaA = QtWidgets.QPushButton(self.widget)
        self.computeSigmaA.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.computeSigmaA.sizePolicy().hasHeightForWidth())
        self.computeSigmaA.setSizePolicy(sizePolicy)
        self.computeSigmaA.setObjectName("computeSigmaA")
        self.verticalLayout.addWidget(self.computeSigmaA)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.markDzone = QtWidgets.QPushButton(self.widget)
        self.markDzone.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markDzone.sizePolicy().hasHeightForWidth())
        self.markDzone.setSizePolicy(sizePolicy)
        self.markDzone.setObjectName("markDzone")
        self.horizontalLayout_2.addWidget(self.markDzone)
        self.markRzone = QtWidgets.QPushButton(self.widget)
        self.markRzone.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.markRzone.sizePolicy().hasHeightForWidth())
        self.markRzone.setSizePolicy(sizePolicy)
        self.markRzone.setObjectName("markRzone")
        self.horizontalLayout_2.addWidget(self.markRzone)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.minEventLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minEventLabel.sizePolicy().hasHeightForWidth())
        self.minEventLabel.setSizePolicy(sizePolicy)
        self.minEventLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.minEventLabel.setObjectName("minEventLabel")
        self.horizontalLayout_3.addWidget(self.minEventLabel)
        self.minEventEdit = QtWidgets.QLineEdit(self.widget)
        self.minEventEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minEventEdit.sizePolicy().hasHeightForWidth())
        self.minEventEdit.setSizePolicy(sizePolicy)
        self.minEventEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.minEventEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.minEventEdit.setObjectName("minEventEdit")
        self.horizontalLayout_3.addWidget(self.minEventEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.maxEventLabel = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxEventLabel.sizePolicy().hasHeightForWidth())
        self.maxEventLabel.setSizePolicy(sizePolicy)
        self.maxEventLabel.setObjectName("maxEventLabel")
        self.horizontalLayout_4.addWidget(self.maxEventLabel)
        self.maxEventEdit = QtWidgets.QLineEdit(self.widget)
        self.maxEventEdit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxEventEdit.sizePolicy().hasHeightForWidth())
        self.maxEventEdit.setSizePolicy(sizePolicy)
        self.maxEventEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.maxEventEdit.setObjectName("maxEventEdit")
        self.horizontalLayout_4.addWidget(self.maxEventEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DandR = QtWidgets.QRadioButton(self.widget)
        self.DandR.setChecked(True)
        self.DandR.setObjectName("DandR")
        self.horizontalLayout.addWidget(self.DandR)
        self.Donly = QtWidgets.QRadioButton(self.widget)
        self.Donly.setObjectName("Donly")
        self.horizontalLayout.addWidget(self.Donly)
        self.Ronly = QtWidgets.QRadioButton(self.widget)
        self.Ronly.setObjectName("Ronly")
        self.horizontalLayout.addWidget(self.Ronly)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.locateEvent = QtWidgets.QPushButton(self.widget)
        self.locateEvent.setEnabled(False)
        self.locateEvent.setObjectName("locateEvent")
        self.verticalLayout.addWidget(self.locateEvent)
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.verticalLayout.addWidget(self.cancelButton)
        self.calcErrBars = QtWidgets.QPushButton(self.widget)
        self.calcErrBars.setEnabled(False)
        self.calcErrBars.setObjectName("calcErrBars")
        self.verticalLayout.addWidget(self.calcErrBars)
        spacerItem7 = QtWidgets.QSpacerItem(286, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.writeBarPlots = QtWidgets.QPushButton(self.widget)
        self.writeBarPlots.setEnabled(False)
        self.writeBarPlots.setObjectName("writeBarPlots")
        self.verticalLayout.addWidget(self.writeBarPlots)
        self.writePlot = QtWidgets.QPushButton(self.widget)
        self.writePlot.setEnabled(False)
        self.writePlot.setObjectName("writePlot")
        self.verticalLayout.addWidget(self.writePlot)
        self.startOver = QtWidgets.QPushButton(self.widget)
        self.startOver.setEnabled(False)
        self.startOver.setObjectName("startOver")
        self.verticalLayout.addWidget(self.startOver)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.mainPlot = PlotWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPlot.sizePolicy().hasHeightForWidth())
        self.mainPlot.setSizePolicy(sizePolicy)
        self.mainPlot.setMinimumSize(QtCore.QSize(1051, 0))
        self.mainPlot.setObjectName("mainPlot")
        self.horizontalLayout_6.addWidget(self.mainPlot)
        self.horizontalLayout_6.setStretch(1, 1)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(12)
        self.splitter.setObjectName("splitter")
        self.table = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QtCore.QSize(0, 0))
        self.table.setRowCount(11)
        self.table.setColumnCount(4)
        self.table.setObjectName("table")
        self.textOut = QtWidgets.QTextEdit(self.splitter)
        self.textOut.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textOut.setUndoRedoEnabled(False)
        self.textOut.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textOut.setReadOnly(True)
        self.textOut.setObjectName("textOut")
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PY-OTE"))
        self.readData.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Reads Limovie, R-OTE, and Tangra (AOTA format) files.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">Assumed is: object1 is occulted star; object2 (optional) is a reference star to be used for normalizing occulted star.</span></p></body></html>"))
        self.readData.setText(_translate("MainWindow", "Read light curve"))
        self.showSecondaryCheckBox.setText(_translate("MainWindow", "Show secondary star"))
        self.doBlockIntegration.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">First, find  a clearly identifiable integration group.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">Then click on the first and last point of that integration group.</span></p></body></html>"))
        self.doBlockIntegration.setText(_translate("MainWindow", "Do block integration"))
        self.setDataLimits.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">If exactly two data points have been selected, this button will </span><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">trim</span><span style=\" font-size:18pt;\"> off (exclude) data points to the left and right of the selected points.</span></p><p><span style=\" font-size:18pt;\">If no points have been selected, then all data points will be selected as the default.</span></p></body></html>"))
        self.setDataLimits.setText(_translate("MainWindow", "Set data limits (trim left/right)"))
        self.smoothSecondaryButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Smooth the secondary (reference) star light curve using a Savitsky-Golay filter with a default window of 101 points (the edit box to the right allows for this value to be changed) and a degree 3 interpolating polynomial, applied twice.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">The secondary star does not have to be visible for this smoothing to take place.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">Smoothing of the secondary curve is a prerequisite to normalizing the occulted star light curve.</span></p></body></html>"))
        self.smoothSecondaryButton.setText(_translate("MainWindow", "Smooth secondary"))
        self.numSmoothPointsEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Number of points to use in Savitsky-Golay filter.  This should be an odd number in the range of 3 to number of data points in the secondary curve.</span></p></body></html>"))
        self.numSmoothPointsEdit.setText(_translate("MainWindow", "101"))
        self.normalizeButton.setText(_translate("MainWindow", "Normalize around selected point"))
        self.doNoiseAnalysis.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Use the selected baseline points to calculate noise correlation coefficients and sigmaB</span></p><p><span style=\" font-size:18pt;\">If there has already been such a calculation, new results from clicking this button will be averaged with the previously determined coefficients, weighted by the number of points involved.</span></p></body></html>"))
        self.doNoiseAnalysis.setText(_translate("MainWindow", "Analyze baseline noise"))
        self.computeSigmaA.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">The selected points are used to estimate sigmaA (event noise sigma).</span></p><p><br/></p><p><span style=\" font-size:18pt;\">It is optional to do this --- if not done, sigmaA will default to sigmaB (baseline noise sigma)</span></p></body></html>"))
        self.computeSigmaA.setText(_translate("MainWindow", "Analyze event noise"))
        self.markDzone.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Use the two selected points as the min and max D positions to use during the \'event\' search.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">If no points are selected, the D region is removed.</span></p></body></html>"))
        self.markDzone.setText(_translate("MainWindow", "Mark D region"))
        self.markRzone.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Use the two selected points as the min and max R positions to use during the \'event\' search.</span></p><p><br/></p><p><span style=\" font-size:18pt;\">If no points are selected, the R region is removed.</span></p></body></html>"))
        self.markRzone.setText(_translate("MainWindow", "Mark R region"))
        self.minEventLabel.setText(_translate("MainWindow", "min event (rdgs):"))
        self.minEventEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Enter smallest event size (in number of readings) to search for.</span></p></body></html>"))
        self.maxEventLabel.setText(_translate("MainWindow", "max event (rdgs):"))
        self.maxEventEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Enter largest event size (in number of readings) to search for.</span></p></body></html>"))
        self.DandR.setText(_translate("MainWindow", "D:R"))
        self.Donly.setText(_translate("MainWindow", "D"))
        self.Ronly.setText(_translate("MainWindow", "R"))
        self.locateEvent.setText(_translate("MainWindow", "Locate D and R"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel operation"))
        self.calcErrBars.setText(_translate("MainWindow", "Calculate D and R  error bars"))
        self.writeBarPlots.setText(_translate("MainWindow", "Write error bar plot to file"))
        self.writePlot.setText(_translate("MainWindow", "Write main plot to file"))
        self.startOver.setText(_translate("MainWindow", "Start over"))

from pyqtgraph import PlotWidget

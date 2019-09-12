# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Problyzer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from matplotlib.gridspec import GridSpec

from PIL import Image as pil
import skimage as sk
from skimage.morphology.extrema import h_maxima
from skimage.feature import peak_local_max
from skimage.morphology import watershed, disk
from skimage.filters import rank

import pandas as pd, seaborn as sb, \
    time, datetime, matplotlib.pyplot as plt, matplotlib, numpy as np, mahotas as mh
import os, subprocess

from PulseProgressBar import PulseProgressBar as ProgressDialog
from clustermap import ClusterMap

font = {'family': 'Georgia', 'weight': 'bold', 'size': 22}
matplotlib.rc('font', **font)

ViennaRNA_path = os.getcwd() + r"\Vienna_RNA"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2147, 1540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("OB_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Label_status = QtWidgets.QLabel(self.centralwidget)
        self.Label_status.setText("")
        self.Label_status.setObjectName("Label_status")
        self.horizontalLayout_3.addWidget(self.Label_status)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(20, -1, 20, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.Line_Conc = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_Conc.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Line_Conc.sizePolicy().hasHeightForWidth())
        self.Line_Conc.setSizePolicy(sizePolicy)
        self.Line_Conc.setMinimumSize(QtCore.QSize(0, 0))
        self.Line_Conc.setMaximumSize(QtCore.QSize(130, 16777215))
        self.Line_Conc.setObjectName("Line_Conc")
        self.horizontalLayout_4.addWidget(self.Line_Conc)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(50, 0))
        self.label_4.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(30, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.Combo_ChooseProgram = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Combo_ChooseProgram.sizePolicy().hasHeightForWidth())
        self.Combo_ChooseProgram.setSizePolicy(sizePolicy)
        self.Combo_ChooseProgram.setMinimumSize(QtCore.QSize(0, 0))
        self.Combo_ChooseProgram.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.Combo_ChooseProgram.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Combo_ChooseProgram.setFont(font)
        self.Combo_ChooseProgram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Combo_ChooseProgram.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.Combo_ChooseProgram.setObjectName("Combo_ChooseProgram")
        self.Combo_ChooseProgram.addItem("")
        self.Combo_ChooseProgram.addItem("")
        self.Combo_ChooseProgram.addItem("")
        self.Combo_ChooseProgram.addItem("")
        self.horizontalLayout_4.addWidget(self.Combo_ChooseProgram, 0, QtCore.Qt.AlignHCenter)
        self.Button_Run = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Run.setEnabled(False)
        self.Button_Run.setMaximumSize(QtCore.QSize(300, 16777215))
        self.Button_Run.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_Run.setAutoFillBackground(False)
        self.Button_Run.setCheckable(True)
        self.Button_Run.setObjectName("Button_Run")
        self.horizontalLayout_4.addWidget(self.Button_Run)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.Button_ShowImage = QtWidgets.QPushButton(self.centralwidget)
        self.Button_ShowImage.setEnabled(False)
        self.Button_ShowImage.setObjectName("Button_ShowImage")
        self.horizontalLayout_4.addWidget(self.Button_ShowImage)
        self.Combo_ImageType = QtWidgets.QComboBox(self.centralwidget)
        self.Combo_ImageType.setEnabled(False)
        self.Combo_ImageType.setMinimumSize(QtCore.QSize(0, 0))
        self.Combo_ImageType.setObjectName("Combo_ImageType")
        self.Combo_ImageType.addItem("")
        self.Combo_ImageType.addItem("")
        self.horizontalLayout_4.addWidget(self.Combo_ImageType, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 50, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Line_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_filename.setMinimumSize(QtCore.QSize(0, 50))
        self.Line_filename.setObjectName("Line_filename")
        self.horizontalLayout.addWidget(self.Line_filename)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Button_Upload = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Upload.setObjectName("Button_Upload")
        self.horizontalLayout.addWidget(self.Button_Upload)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(True)
        self.scrollArea.setFont(font)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 2099, 1175))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 1, 4, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 1, 5, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 1, 9, 1, 1)
        self.Slider_ShapeStringency = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_ShapeStringency.setEnabled(False)
        self.Slider_ShapeStringency.setMaximum(100)
        self.Slider_ShapeStringency.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_ShapeStringency.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_ShapeStringency.setTickInterval(5)
        self.Slider_ShapeStringency.setObjectName("Slider_ShapeStringency")
        self.gridLayout_2.addWidget(self.Slider_ShapeStringency, 2, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 9, 1, 1)
        self.Slider_Dilate = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_Dilate.setEnabled(False)
        self.Slider_Dilate.setMinimumSize(QtCore.QSize(0, 0))
        self.Slider_Dilate.setMaximumSize(QtCore.QSize(1677, 1677))
        self.Slider_Dilate.setMinimum(1)
        self.Slider_Dilate.setMaximum(7)
        self.Slider_Dilate.setSingleStep(2)
        self.Slider_Dilate.setPageStep(10)
        self.Slider_Dilate.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Dilate.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider_Dilate.setTickInterval(1)
        self.Slider_Dilate.setObjectName("Slider_Dilate")
        self.gridLayout_2.addWidget(self.Slider_Dilate, 0, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setMaximumSize(QtCore.QSize(200, 50))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.Check_ShapeStringency = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_ShapeStringency.setObjectName("Check_ShapeStringency")
        self.gridLayout_2.addWidget(self.Check_ShapeStringency, 2, 3, 1, 1, QtCore.Qt.AlignRight)
        spacerItem4 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 9, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.Check_SpotStringency = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_SpotStringency.setObjectName("Check_SpotStringency")
        self.gridLayout_2.addWidget(self.Check_SpotStringency, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 3, 1, 1)
        self.Slider_SpotStringency = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_SpotStringency.setEnabled(False)
        self.Slider_SpotStringency.setMinimumSize(QtCore.QSize(0, 0))
        self.Slider_SpotStringency.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Slider_SpotStringency.setMinimum(-1000)
        self.Slider_SpotStringency.setMaximum(200)
        self.Slider_SpotStringency.setSingleStep(1)
        self.Slider_SpotStringency.setProperty("value", 200)
        self.Slider_SpotStringency.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_SpotStringency.setInvertedAppearance(False)
        self.Slider_SpotStringency.setInvertedControls(False)
        self.Slider_SpotStringency.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_SpotStringency.setTickInterval(50)
        self.Slider_SpotStringency.setObjectName("Slider_SpotStringency")
        self.gridLayout_2.addWidget(self.Slider_SpotStringency, 2, 2, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_2.addWidget(self.line_4, 1, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_2.addWidget(self.line_9, 1, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_2.addWidget(self.line_10, 1, 1, 1, 1)
        self.Slider_Sigma = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_Sigma.setEnabled(False)
        self.Slider_Sigma.setMinimumSize(QtCore.QSize(0, 0))
        self.Slider_Sigma.setMaximumSize(QtCore.QSize(1677, 50))
        self.Slider_Sigma.setMinimum(0)
        self.Slider_Sigma.setMaximum(100)
        self.Slider_Sigma.setPageStep(10)
        self.Slider_Sigma.setProperty("value", 2)
        self.Slider_Sigma.setSliderPosition(2)
        self.Slider_Sigma.setTracking(True)
        self.Slider_Sigma.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Sigma.setInvertedAppearance(False)
        self.Slider_Sigma.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider_Sigma.setTickInterval(5)
        self.Slider_Sigma.setObjectName("Slider_Sigma")
        self.gridLayout_2.addWidget(self.Slider_Sigma, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)
        self.Slider_Blur = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_Blur.setEnabled(False)
        self.Slider_Blur.setMaximum(100)
        self.Slider_Blur.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_Blur.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_Blur.setTickInterval(5)
        self.Slider_Blur.setObjectName("Slider_Blur")
        self.gridLayout_2.addWidget(self.Slider_Blur, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.ClusterMap = ClusterMap(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ClusterMap.sizePolicy().hasHeightForWidth())
        self.ClusterMap.setSizePolicy(sizePolicy)
        self.ClusterMap.setMinimumSize(QtCore.QSize(0, 0))
        self.ClusterMap.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("SimHei")
        self.ClusterMap.setFont(font)
        self.ClusterMap.setToolTipDuration(-1)
        self.ClusterMap.setWhatsThis("")
        self.ClusterMap.setObjectName("ClusterMap")
        self.verticalLayout_2.addWidget(self.ClusterMap)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14, 0, QtCore.Qt.AlignLeft)
        self.Label_SpotNr = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_SpotNr.setMinimumSize(QtCore.QSize(100, 0))
        self.Label_SpotNr.setText("")
        self.Label_SpotNr.setObjectName("Label_SpotNr")
        self.horizontalLayout_8.addWidget(self.Label_SpotNr, 0, QtCore.Qt.AlignLeft)
        self.Check_SizeThres = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_SizeThres.setText("")
        self.Check_SizeThres.setObjectName("Check_SizeThres")
        self.horizontalLayout_8.addWidget(self.Check_SizeThres)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15)
        self.Slider_SizeThres = QtWidgets.QSlider(self.scrollAreaWidgetContents)
        self.Slider_SizeThres.setEnabled(False)
        self.Slider_SizeThres.setMaximum(255)
        self.Slider_SizeThres.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_SizeThres.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.Slider_SizeThres.setTickInterval(20)
        self.Slider_SizeThres.setObjectName("Slider_SizeThres")
        self.horizontalLayout_8.addWidget(self.Slider_SizeThres)
        self.Button_ImgViewer = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.Button_ImgViewer.setObjectName("Button_ImgViewer")
        self.horizontalLayout_8.addWidget(self.Button_ImgViewer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.Check_NoisyMode = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_NoisyMode.setEnabled(False)
        self.Check_NoisyMode.setMinimumSize(QtCore.QSize(0, 0))
        self.Check_NoisyMode.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.Check_NoisyMode.setObjectName("Check_NoisyMode")
        self.verticalLayout.addWidget(self.Check_NoisyMode, 0, QtCore.Qt.AlignHCenter)
        self.Check_SingleColor = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_SingleColor.setEnabled(False)
        self.Check_SingleColor.setMinimumSize(QtCore.QSize(0, 0))
        self.Check_SingleColor.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Check_SingleColor.setChecked(True)
        self.Check_SingleColor.setObjectName("Check_SingleColor")
        self.verticalLayout.addWidget(self.Check_SingleColor, 0, QtCore.Qt.AlignHCenter)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_18.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(400, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Slider_LowThres = QtWidgets.QSlider(self.frame)
        self.Slider_LowThres.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_LowThres.sizePolicy().hasHeightForWidth())
        self.Slider_LowThres.setSizePolicy(sizePolicy)
        self.Slider_LowThres.setMinimumSize(QtCore.QSize(200, 0))
        self.Slider_LowThres.setMaximumSize(QtCore.QSize(350, 16777215))
        self.Slider_LowThres.setMaximum(127)
        self.Slider_LowThres.setSingleStep(1)
        self.Slider_LowThres.setPageStep(10)
        self.Slider_LowThres.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_LowThres.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_LowThres.setTickInterval(5)
        self.Slider_LowThres.setObjectName("Slider_LowThres")
        self.gridLayout_4.addWidget(self.Slider_LowThres, 0, 1, 1, 1)
        self.Slider_HighThres = QtWidgets.QSlider(self.frame)
        self.Slider_HighThres.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Slider_HighThres.sizePolicy().hasHeightForWidth())
        self.Slider_HighThres.setSizePolicy(sizePolicy)
        self.Slider_HighThres.setMinimumSize(QtCore.QSize(200, 0))
        self.Slider_HighThres.setMaximumSize(QtCore.QSize(350, 16777215))
        self.Slider_HighThres.setMinimum(127)
        self.Slider_HighThres.setMaximum(255)
        self.Slider_HighThres.setProperty("value", 255)
        self.Slider_HighThres.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_HighThres.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Slider_HighThres.setTickInterval(5)
        self.Slider_HighThres.setObjectName("Slider_HighThres")
        self.gridLayout_4.addWidget(self.Slider_HighThres, 1, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        self.label_12.setMaximumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12, 0, QtCore.Qt.AlignHCenter)
        self.Button_DAPI = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button_DAPI.setEnabled(False)
        self.Button_DAPI.setMinimumSize(QtCore.QSize(0, 0))
        self.Button_DAPI.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Button_DAPI.setToolTip("")
        self.Button_DAPI.setToolTipDuration(3)
        self.Button_DAPI.setWhatsThis("")
        self.Button_DAPI.setObjectName("Button_DAPI")
        self.verticalLayout.addWidget(self.Button_DAPI, 0, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Label_DAPI = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_DAPI.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_DAPI.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_DAPI.setText("")
        self.Label_DAPI.setObjectName("Label_DAPI")
        self.verticalLayout.addWidget(self.Label_DAPI, 0, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_7.setMinimumSize(QtCore.QSize(0, 0))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.Label_TissueSNR = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_TissueSNR.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_TissueSNR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_TissueSNR.setText("")
        self.Label_TissueSNR.setObjectName("Label_TissueSNR")
        self.verticalLayout.addWidget(self.Label_TissueSNR, 0, QtCore.Qt.AlignHCenter)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23, 0, QtCore.Qt.AlignHCenter)
        self.Button_SNR = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button_SNR.setEnabled(False)
        self.Button_SNR.setMinimumSize(QtCore.QSize(0, 0))
        self.Button_SNR.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Button_SNR.setObjectName("Button_SNR")
        self.verticalLayout.addWidget(self.Button_SNR, 0, QtCore.Qt.AlignHCenter)
        self.Check_MaximaNoisyMode = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_MaximaNoisyMode.setEnabled(False)
        self.Check_MaximaNoisyMode.setObjectName("Check_MaximaNoisyMode")
        self.verticalLayout.addWidget(self.Check_MaximaNoisyMode, 0, QtCore.Qt.AlignHCenter)
        self.Check_TissueMaxima = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.Check_TissueMaxima.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Check_TissueMaxima.sizePolicy().hasHeightForWidth())
        self.Check_TissueMaxima.setSizePolicy(sizePolicy)
        self.Check_TissueMaxima.setMinimumSize(QtCore.QSize(0, 0))
        self.Check_TissueMaxima.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.Check_TissueMaxima.setChecked(True)
        self.Check_TissueMaxima.setObjectName("Check_TissueMaxima")
        self.verticalLayout.addWidget(self.Check_TissueMaxima, 0, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8, 0, QtCore.Qt.AlignHCenter)
        self.Label_SNR = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_SNR.setMinimumSize(QtCore.QSize(100, 0))
        self.Label_SNR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_SNR.setText("")
        self.Label_SNR.setObjectName("Label_SNR")
        self.verticalLayout.addWidget(self.Label_SNR, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.Label_CellSNR = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Label_CellSNR.setMinimumSize(QtCore.QSize(100, 0))
        self.Label_CellSNR.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_CellSNR.setText("")
        self.Label_CellSNR.setObjectName("Label_CellSNR")
        self.verticalLayout.addWidget(self.Label_CellSNR, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        spacerItem5 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10, 0, QtCore.Qt.AlignHCenter)
        self.Text_Log = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text_Log.sizePolicy().hasHeightForWidth())
        self.Text_Log.setSizePolicy(sizePolicy)
        self.Text_Log.setMinimumSize(QtCore.QSize(0, 0))
        self.Text_Log.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Text_Log.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Text_Log.setReadOnly(True)
        self.Text_Log.setOverwriteMode(False)
        self.Text_Log.setObjectName("Text_Log")
        self.verticalLayout_4.addWidget(self.Text_Log, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_5.addWidget(self.label_22)
        self.Line_SaveName = QtWidgets.QLineEdit(self.centralwidget)
        self.Line_SaveName.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Line_SaveName.setObjectName("Line_SaveName")
        self.horizontalLayout_5.addWidget(self.Line_SaveName)
        self.Button_SaveResults = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SaveResults.setEnabled(False)
        self.Button_SaveResults.setMaximumSize(QtCore.QSize(500, 16777215))
        self.Button_SaveResults.setObjectName("Button_SaveResults")
        self.horizontalLayout_5.addWidget(self.Button_SaveResults, 0, QtCore.Qt.AlignLeft)
        self.Button_SaveMaximas = QtWidgets.QPushButton(self.centralwidget)
        self.Button_SaveMaximas.setEnabled(False)
        self.Button_SaveMaximas.setObjectName("Button_SaveMaximas")
        self.horizontalLayout_5.addWidget(self.Button_SaveMaximas)
        self.Label_Exported = QtWidgets.QLabel(self.centralwidget)
        self.Label_Exported.setMinimumSize(QtCore.QSize(0, 0))
        self.Label_Exported.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Label_Exported.setText("")
        self.Label_Exported.setObjectName("Label_Exported")
        self.horizontalLayout_5.addWidget(self.Label_Exported, 0, QtCore.Qt.AlignLeft)
        spacerItem6 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_5, 7, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Button_Upload.clicked.connect(self.Line_filename.clear)
        self.Check_SpotStringency.clicked['bool'].connect(self.Slider_SpotStringency.setEnabled)
        self.Check_SizeThres.clicked['bool'].connect(self.Slider_SizeThres.setEnabled)
        self.Check_ShapeStringency.clicked['bool'].connect(self.label_21.setEnabled)
        self.mySlotsConnection()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Status:"))
        self.label_3.setText(_translate("MainWindow", "Probe Concentration:"))
        self.Line_Conc.setToolTip(_translate("MainWindow", "Conc. of Seq 1, Conc. of Seq 2 ....Conc. of Seq n"))
        self.label_4.setText(_translate("MainWindow", "μM"))
        self.label.setText(_translate("MainWindow", "Program:"))
        self.Combo_ChooseProgram.setToolTip(_translate("MainWindow",
                                                       "<html><head/><body><p>- <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAcofold</span> works much like RNAfold but uses two RNA sequences as input which are then allowed to form a dimer structure. </p><p>- <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAduplex</span> program is a fast alternative, that works by predicting only intermolecular base pairs. It’s almost as fast as simple sequence alignment, but much more accurate than a BLAST search.</p><p>- Since <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAduplex</span> forms only intermolecular pairs, it neglects the competition between intramolecular folding and hybridization. Thus, it is recommended to use <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAduplex</span> as a pre-ﬁlter and analyse good <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAduplex</span>hits additionally with <span style=\" font-family:\'Menlo,Monaco,Consolas,Courier New,monospace\'; color:#c7254e; background-color:#f9f2f4;\">RNAcofold or RNAup</span></p><p>&lt;Visit: <a href=\"https://www.tbi.univie.ac.at/RNA/tutorial/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.tbi.univie.ac.at/RNA/tutorial/</span></a> for more></p></body></html>"))
        self.Combo_ChooseProgram.setItemText(0, _translate("MainWindow", "RNAcoFold - MFE (no conc.)"))
        self.Combo_ChooseProgram.setItemText(1, _translate("MainWindow", "RNAcoFold - conc. dependent"))
        self.Combo_ChooseProgram.setItemText(2, _translate("MainWindow", "RNAduplex"))
        self.Combo_ChooseProgram.setItemText(3, _translate("MainWindow", "RNAup "))
        self.Button_Run.setText(_translate("MainWindow", "Run"))
        self.Button_ShowImage.setText(_translate("MainWindow", "Display Image"))
        self.Combo_ImageType.setItemText(0, _translate("MainWindow", "Tissue (DAPI/All)"))
        self.Combo_ImageType.setItemText(1, _translate("MainWindow", "Fluorescence (Signal)"))
        self.Button_Upload.setText(_translate("MainWindow", "Upload File"))
        self.label_21.setText(_translate("MainWindow", "Shape Stringency: "))
        self.label_6.setText(_translate("MainWindow", "Dilate: "))
        self.Check_ShapeStringency.setText(_translate("MainWindow", "Use: "))
        self.label_19.setToolTip(_translate("MainWindow",
                                            "<html><head/><body><p align=\"center\">A local maximum M of height h is a local maximum for which there is at least one path joining M with a higher maximum on which the minimal value is f(M) - h (i.e. the values along the path are not decreasing by more than h with respect to the maximum’s value) and no path for which the minimal value is greater.</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "Spot Stringency: "))
        self.Check_SpotStringency.setText(_translate("MainWindow", "Use: "))
        self.label_5.setText(_translate("MainWindow", "Sigma (Gaussian): "))
        self.label_20.setText(_translate("MainWindow", "Blurring Radius: "))
        self.label_14.setText(_translate("MainWindow", "Fluorescence Spots Count: "))
        self.label_15.setToolTip(_translate("MainWindow", "Cut-off size for small spots"))
        self.label_15.setText(_translate("MainWindow", "Spot-size Lower Limit (no. of pixels):"))
        self.Button_ImgViewer.setText(_translate("MainWindow", "..."))
        self.label_13.setText(_translate("MainWindow", "BG Masking"))
        self.Check_NoisyMode.setToolTip(_translate("MainWindow", "Uses image mean intensity as threshold"))
        self.Check_NoisyMode.setText(_translate("MainWindow", "Noise Tolerant (BG)"))
        self.Check_SingleColor.setToolTip(_translate("MainWindow", "Display all spots at single intensity & color"))
        self.Check_SingleColor.setText(_translate("MainWindow", "Show as Single Color"))
        self.label_18.setText(_translate("MainWindow", "Threshold"))
        self.label_17.setText(_translate("MainWindow", "High: "))
        self.label_16.setText(_translate("MainWindow", "Low: "))
        self.label_12.setText(_translate("MainWindow", "Region Selection"))
        self.Button_DAPI.setText(_translate("MainWindow", "Set Colored Region /&\n"
                                                          "Calculate Mean Tissue BG"))
        self.label_11.setText(_translate("MainWindow", "Region\'s Mean Intensity:"))
        self.label_7.setText(_translate("MainWindow", "Region/All SNR Ratio:"))
        self.label_23.setText(_translate("MainWindow", "Maximas"))
        self.Button_SNR.setText(_translate("MainWindow", "Calculate Maximas\' SNR"))
        self.Check_MaximaNoisyMode.setText(_translate("MainWindow", "Noise Tolerant (Maxima)"))
        self.Check_TissueMaxima.setText(_translate("MainWindow", "Show In-bound Maximas Only"))
        self.label_8.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Maximas/All SNR: </p></body></html>"))
        self.label_9.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Maximas/Region SNR:</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Log:"))
        self.label_22.setText(_translate("MainWindow", "Name: "))
        self.Button_SaveResults.setText(_translate("MainWindow", "Save LOG to directory"))
        self.Button_SaveMaximas.setText(_translate("MainWindow", "Save Maximas Coordinates"))

    def mySlotsConnection(self):
        # Both
        self.Button_Upload.clicked.connect(self.ChooseFile)
        # RNA Analyzes
        self.choice = 0
        self.Button_Run.clicked.connect(self.RunAnalysis)
        self.Combo_ChooseProgram.activated.connect(self.Combo_Changed)
        self.command_line = ViennaRNA_path + "\RNAcofold.exe -p < t.seq"
        # Image
        self.Button_ShowImage.clicked.connect(self.DisplayImage)
        self.Button_DAPI.clicked.connect(self.on_click_CalculateDAPI)
        self.Combo_ImageType.activated.connect(self.Combo_ImageChanged)
        self.Slider_LowThres.sliderReleased.connect(self.UpdateImage)
        self.Slider_HighThres.sliderReleased.connect(self.UpdateImage)
        self.Slider_SpotStringency.sliderReleased.connect(self.UpdateImage)
        self.Slider_SizeThres.sliderReleased.connect(self.UpdateImage)
        self.Check_SpotStringency.clicked.connect(self.UpdateImage)
        self.Check_SizeThres.clicked.connect(self.UpdateImage)
        self.Combo_ImageType.activated.connect(self.UpdateImage)
        self.Check_NoisyMode.released.connect(self.UpdateImage)
        self.Check_SingleColor.released.connect(self.UpdateImage)
        self.Slider_Dilate.sliderReleased.connect(self.UpdateImage)
        self.Slider_Sigma.sliderReleased.connect(self.UpdateImage)
        self.Slider_Blur.sliderReleased.connect(self.UpdateImage)
        self.Check_TissueMaxima.released.connect(self.UpdateImage)
        self.Button_SNR.clicked.connect(self.CalculateSNR)
        self.Button_DAPI.clicked.connect(self.on_click_CalculateDAPI)
        self.Button_SaveResults.clicked.connect(self.CSVAddResults)
        self.Button_SaveMaximas.clicked.connect(self.SaveMaximas)
        self.Button_ImgViewer.clicked.connect(self.PopUpViewer)

    def Combo_Changed(self, choice):
        self.choice = choice;
        if choice == 0:
            self.Line_Conc.setEnabled(False);
            self.command_line = ViennaRNA_path + r"\RNAcofold.exe -p < t.seq"
        elif choice == 1:
            self.Line_Conc.setEnabled(True);
            self.command_line = ViennaRNA_path + "\RNAcofold.exe -p -c < t.seq"
        elif choice == 2:
            self.Line_Conc.setEnabled(False);
            self.command_line = ViennaRNA_path + r"\RNAduplex.exe < duplex.seq"
        elif choice == 3:
            self.Line_Conc.setEnabled(False);
            self.command_line = ViennaRNA_path + r"\RNAup.exe -b < duplex.seq"

    def ChooseFile(self):
        fileName, _ = QFileDialog.getOpenFileName(MainWindow, "QFileDialog.getOpenFileName()", "",
                                                  "Tiff Image Files (*.tif);;"
                                                  "Excel Files (*.xls *.xlsx *.xlsm);; "
                                                  "Other Image Files (*.jpg *png);;"
                                                  " All Files (*)",)   # Add options here
        self.fileName = fileName
        if fileName:
            if fileName.endswith('.xls') or fileName.endswith('.xlsx') or fileName.endswith('.xlsm'):
                self.Line_filename.setText('File Uploaded from: ' + str(fileName))
                self.seq_dataset = pd.read_excel(fileName, index_col=0);
                self.Button_Run.setEnabled(True);
                self.Button_ShowImage.setEnabled(False);
                self.Slider_Sigma.setEnabled(False);
                self.Slider_Blur.setEnabled(False)
                self.Slider_Dilate.setEnabled(False);
            elif fileName.endswith('.tif') or fileName.endswith('.png') or fileName.endswith('.jpg'):
                self.Line_filename.setText('File Uploaded from: ' + str(fileName))
                img = pil.open(fileName)
                arr = np.array(img)

                self.img_array_original = mh.stretch(arr);
                img.close(); self.img_array_original.setflags(write=False)
                self.Button_ShowImage.setEnabled(True);
                self.Button_Run.setEnabled(False)
                # Load basic threshold params...
            else:
                self.Label_status.setText('There appears to be something wrong with your input file')

            self.Button_SNR.setEnabled(False);
            self.Check_TissueMaxima.setEnabled(False)
            self.Button_DAPI.setEnabled(False);
        else:
            self.Label_status.setText('File not uploaded')

    def RunAnalysis(self):
        if type(self.seq_dataset) == None:
            self.Label_status.setText('Are you sure you have uploaded a correct sequence file?')
        else:
            self.ProgressBar = ProgressDialog(); self.ProgressBar.show();
            self.ProgressBar.Label_Task.setText('Starting ...')
            if not self.choice == 1:
                self.PlotThread = RNARunThread(self.seq_dataset, self.command_line, self.choice)
            else:
                try:
                    self.PlotThread = RNARunThread(self.seq_dataset, self.command_line, self.choice,
                                                   self.Line_Conc.text())
                except:
                    QMessageBox.question(MainWindow, 'Warning', 'Did you forget something?', QMessageBox.Ok)
                    return
            self.PlotThread.Signal_UpdateStatus.connect(self.UpdateStatus)
            self.PlotThread.Signal_Finished.connect(self.RunFinished)
            self.PlotThread.start()

    def RunFinished(self, clusterplot, t_float):
        self.ClusterMap.setupUi(figure=clusterplot,
                                title='Primary Probe Intermolecular Interaction Energy',
                                xlabel='Sequence ID', ylabel='Sequence ID')
        self.PlotThread.terminate(); self.ProgressBar.close()
        self.Label_status.setText('Run is finished. Time elapsed, %.2f s' % t_float)

    ### Image
    def Combo_ImageChanged(self, choice):
        if choice == 0:
            self.Button_DAPI.setEnabled(True)
            self.Check_SingleColor.setEnabled(True)
            self.Check_NoisyMode.setEnabled(True)
            self.Slider_SpotStringency.setEnabled(False)
            self.Check_SizeThres.setEnabled(False)
            self.Slider_HighThres.setEnabled(True); self.Slider_LowThres.setEnabled(True);
            self.Check_ShapeStringency.setEnabled(False); self.Check_SpotStringency.setEnabled(False)
            self.Check_TissueMaxima.setEnabled(False); self.Check_MaximaNoisyMode.setEnabled(False)

        if choice == 1:
            self.Button_DAPI.setEnabled(False)
            self.Check_SingleColor.setEnabled(False)
            self.Check_NoisyMode.setEnabled(False)
            self.Slider_SpotStringency.setEnabled(True)
            self.Check_SizeThres.setEnabled(True)
            self.Slider_HighThres.setEnabled(False); self.Slider_LowThres.setEnabled(False);
            self.Check_ShapeStringency.setEnabled(True); self.Check_SpotStringency.setEnabled(True)
            self.Button_DAPI.setEnabled(True)
            self.Check_TissueMaxima.setEnabled(True); self.Check_MaximaNoisyMode.setEnabled(True)

    def DisplayImage(self):
        self.im_figure = plt.figure(figsize=(10, 10), constrained_layout=True)
        gs = GridSpec(13, 13, self.im_figure)
        self.im_axes = self.im_figure.add_subplot(gs[:,:]);
        self.thres_axes = self.im_figure.add_subplot(gs[0, :]); self.thres_axes.xaxis.tick_top()

        #Threshold
        self.img_array = self.img_array_original.copy()
        low_thres = self.Slider_LowThres.value(); high_thres = self.Slider_HighThres.value()
        im = self.im_axes.imshow(self.img_array_original); self.im_figure.colorbar(im, ax=self.im_axes)
        sb.kdeplot(self.img_array_original.ravel(), ax=self.thres_axes);  self.thres_axes.set_xlim([0, 254])

        self.ClusterMap.setupUi(figure=self.im_figure, title=None, xlabel=None, ylabel=None)
        self.DAPIworker = DAPIThread(); self.DAPIworker.LoadImage(self.img_array);
        self.DAPIworker.DAPI_UpdateStatus.connect(self.UpdateStatus);
        self.DAPIworker.DAPI_Finished.connect(self.DAPI_Finished)

        if self.Combo_ImageType.currentText() == 'Tissue (DAPI/All)':
            self.Combo_ImageType.setEnabled(True);
            self.Check_SingleColor.setEnabled(True);
            self.Check_NoisyMode.setEnabled(True);
            #self.Check_RandomWalker.setEnabled(True);

        elif self.Combo_ImageType.currentText() == 'Fluorescence (Signal)':
            self.Check_NoisyMode.setEnabled(True);
            self.Button_DAPI.setEnabled(False);
        self.Slider_LowThres.setEnabled(True)
        self.Slider_HighThres.setEnabled(True)
        self.Slider_Sigma.setEnabled(True)
        self.Slider_Blur.setEnabled(True)
        self.Slider_Dilate.setEnabled(True)
        self.Combo_ImageType.setEnabled(True)
        self.DAPI_set_bool = False
        self.ImageViewer = ImageViewWindow(self.img_array)
        self.Button_ImgViewer.clicked.connect(self.PopUpViewer)
        self.Text_Log.append('>Low: %d; High: %d' % (low_thres, high_thres))

        # Initialize for slider values to be compared
        self.blur = blur = self.Slider_Blur.value()
        self.dilate = self.Slider_Dilate.value()
        self.low_thres = self.Slider_LowThres.value();
        self.high_thres = self.Slider_HighThres.value()
        self.sigma = self.Slider_Sigma.value()/10
        #
        self.h_stringency = 10 ** (self.Slider_SpotStringency.value() / 100)
        self.shape_stringency = self.Slider_ShapeStringency

    def UpdateImage(self):
        blur = self.Slider_Blur.value(); sigma = self.Slider_Sigma.value()/10; dilate = self.Slider_Dilate.value()
        low_thres = self.Slider_LowThres.value(); high_thres = self.Slider_HighThres.value()
        self.img_array = self.img_array_original.copy()
        if low_thres != self.low_thres:
            self.img_array *= self.img_array_original > low_thres; self.low_thres = low_thres
        if high_thres != self.high_thres:
            self.img_array *= self.img_array_original < high_thres; self.high_thres = high_thres

        if sigma < 0.125:
            self.gaussian_f = 0
        else:
            self.gaussian_f = mh.gaussian_filter(self.img_array.astype('float'), sigma);
            self.gT_mean = self.gaussian_f.mean(); self.sigma = sigma; self.T_mean = self.img_array.mean()

        if self.dilate != dilate and type(self.gaussian_f) != None:
            self.gaussian_f = mh.dilate(self.gaussian_f, np.ones(dilate, dilate)); self.dilate = dilate

        if self.blur != blur:
            self.img_array = rank.median(self.img_array, disk(blur)); self.blur = blur

        if self.Combo_ImageType.currentText() == 'Tissue (DAPI/All)':
            self.thres_axes.set_axis_on()
            if self.Check_NoisyMode.isChecked():
                self.DAPI_mask = mh.dilate(self.img_array > self.T_mean, np.ones((dilate, dilate)))
            else:   
                self.DAPI_mask = mh.dilate(self.img_array > self.gT_mean, np.ones((dilate, dilate)))

            if self.Check_SingleColor.isChecked():
                self.im_axes.imshow(self.DAPI_mask)
            else:
                self.im_axes.imshow(sk.color.label2rgb(self.DAPI_mask, self.gaussian_f > self.gT_mean, alpha=0.5,
                                                       colors=[(1, 0, 0)], bg_color=None, bg_label=0))
            self.DAPIworker.UpdateMask(self.DAPI_mask)
            self.ClusterMap.setupUi(figure=self.im_figure, title='Image Display')
            self.ImageViewer = ImageViewWindow(self.DAPI_mask*mh.stretch(self.img_array))
            self.Button_SNR.setEnabled(False); self.Check_TissueMaxima.setEnabled(False); self.Button_DAPI.setEnabled(True)
            self.Text_Log.append('>Updated image; Mode:Tissue; sigma=%.1f,dilate=%d; Thres:%d-%d'
                                 % (sigma, dilate, low_thres, high_thres))

        elif self.Combo_ImageType.currentText() == 'Fluorescence (Signal)':
            h_stringency = 10 ** (self.Slider_SpotStringency.value() / 100);
            shape_stringency = self.Slider_ShapeStringency  # 0-1
            if self.DAPI_set_bool:
                self.Button_SNR.setEnabled(True);
                self.Button_DAPI.setEnabled(False)
                self.img_array_fluor = self.img_array_original * self.Tissue_Mask

            self.thres_axes.set_axis_off(); self.Button_ImgViewer.clicked.connect(self.PopUpViewer)
            if self.Check_SpotStringency.isChecked():
                if self.h_stringency != h_stringency:
                    self.all_maximas = sk.measure.label(h_maxima(self.img_array, h_stringency))  # mh.regmax(self.gaussian_f)
                    self.Text_Log.append('Spot stringency used: %.2e' % h_stringency)

            else:
                if self.Check_MaximaNoisyMode.isChecked():
                    self.max_coord = peak_local_max(self.img_array, min_distance=1)
                    self.all_maximas = np.zeros(self.img_array.shape);
                    self.all_maximas[self.max_coord[:, 0], self.max_coord[:, 1]] = 1
                else:
                    self.all_maximas = mh.regmax(self.img_array)

            # Low size limit threshold
            if self.Check_SizeThres.isChecked():
                sizes = mh.labeled.labeled_size(self.img_array)
                self.all_maximas *= mh.labeled.remove_regions_where(self.img_array, sizes < self.Slider_SizeThres.value())

            # Shape limit threshold
            if self.Check_ShapeStringency.isChecked():
                if self.shape_stringency != shape_stringency:
                    shape_index = sk.feature.shape_index(self.img_array)
                    self.all_maximas *= (1-shape_index) < shape_stringency

            if self.Check_TissueMaxima.isChecked():
                _, nr_object = mh.label(self.img_array); self.Label_SpotNr.setText(str(nr_object))
                self.SavingMaximas = SavingMaximas(self.all_maximas, 'Tissue Maximas')
                overlay = sk.color.label2rgb(mh.dilate(self.all_maximas*self.Tissue_Mask, np.ones((dilate, dilate))),
                                self.img_array_original, alpha=0.5, bg_label=0, bg_color=None, colors=[(1, 0, 0)])
                self.ImageViewer = ImageViewWindow(mh.stretch(np.maximum(self.all_maximas*255,self.img_array)))

            else:
                _, nr_object = mh.label(self.all_maximas); self.Label_SpotNr.setText(str(nr_object))
                self.SavingMaximas = SavingMaximas(self.all_maximas, 'All Maximas')
                overlay = sk.color.label2rgb(mh.dilate(self.all_maximas != 0, np.ones((dilate, dilate))),
                                self.img_array_original, alpha=0.5, bg_label=0, bg_color=None, colors=[(1, 0, 0)])
                self.ImageViewer = ImageViewWindow(mh.stretch(np.maximum(self.all_maximas*255,self.img_array_original)))

            self.im_axes.imshow(overlay); self.ClusterMap.setupUi(figure=self.im_figure, title='Image Display')
            self.Button_SaveMaximas.setEnabled(True); self.DAPI_set_bool = False

            # Text log
            self.Text_Log.append('>Updated image; Mode: Fluor; sigma=%.1f,dilate=%d; Thres:%d-%d'
                                 % (sigma, dilate, low_thres, high_thres))

    def PopUpViewer(self, choice):
        self.ImageViewer.show()

    def on_click_CalculateDAPI(self):
        self.ProgressBar = ProgressDialog(); self.ProgressBar.show()
        self.ProgressBar.Label_Task.setText('Starting ...')
        try:
            self.DAPI_mask
        except AttributeError or NameError:
            QMessageBox.question('Warning', 'You should adjust parameters to define a mask first')
            return
        #segment_options = np.argmax([0, self.Check_Segment.isChecked(), self.Check_RandomWalker.isChecked()]);
        self.DAPIworker.start()

    def DAPI_Finished(self, mean_intensity, snr, tissue_mask):
        self.DAPIworker.terminate(); self.ProgressBar.close();
        self.Label_DAPI.setText('%.3f' % mean_intensity); self.Label_TissueSNR.setText('%.3f' % snr);
        self.Label_status.setText('You have set your tissue BG to the current selection!')
        self.Tissue_Mask = tissue_mask; self.TissueBG_SNR = snr; self.im_axes.imshow(tissue_mask);
        self.ClusterMap.setupUi(figure=self.im_figure, title='Mask Display',
                                xlabel='pixels (x)', ylabel='pixels(y)')
        self.Text_Log.append('>New DAPI Tissue Mask; Mean intensity=%.2f; SNR=%.2f' % (mean_intensity, snr))
        self.Button_DAPI.setEnabled(True); self.DAPI_set_bool = True


    def CalculateSNR(self):
        self.ProgressBar = ProgressDialog(); self.ProgressBar.show();
        self.ProgressBar.Label_Task.setText('Wait...')
        if self.Check_TissueMaxima.isChecked():
            self.SNRworker = SNRThread(self.img_array_original, self.all_maximas,
                                       self.all_maximas, self.DAPI_mask, self.MeanofMask)
        else:
            self.SNRworker = SNRThread(self.img_array_original, self.all_maximas,
                                       False, self.DAPI_mask, self.MeanofMask)
        self.SNRworker.Signal_UpdateStatus.connect(self.UpdateStatus)
        self.SNRworker.Signal_Finished.connect(self.CalculateSNR_Finished)
        self.SNRworker.start()

    def CalculateSNR_Finished(self, mean_maxima_intensity, snr, tissue_snr):
        self.Label_SNR.setText('%.2f' % snr)
        self.Text_Log.append('>Maxima/[All BG] SNR; Mean Intensity=%.2f, snr=%.2f\n' % (mean_maxima_intensity, snr))
        if tissue_snr != 0:
            self.Label_CellSNR.setText('%.2f' % tissue_snr)
            self.Text_Log.append('>Maxima/[Tissue BG] SNR; snr=%.2f' % tissue_snr)
            self.maxima_snr = tissue_snr;
            self.mean_maxima_intesnity = mean_maxima_intensity
        self.SNRworker.terminate();
        self.ProgressBar.close();
        self.Button_SaveResults.setEnabled(True)

    def MeanofMask(self, img_array, mask):  # mask should be boolean
        return sumAll(img_array * mask) / sumAll(mask)

    def UpdateStatus(self, text):
        self.ProgressBar.show();
        self.ProgressBar.Label_Task.setText(text)

    def CSVAddResults(self):
        filename = str(datetime.date.today()) + '_ExportedResults.csv'
        data = dict({'Given Index': self.Line_SaveName.currentText(),
                     'Image Name': self.fileName,
                     'Tissues/bg SNR': self.TissueBG_SNR,
                     'Mean Maxima Intensity': self.mean_maxima_intesnity,
                     'Maxima/Tissue SNR': self.maxima_snr});
        rowlist = []; rowlist.append(data);
        df = pd.DataFrame(rowlist); df.set_index(keys='Given Index')
        if os.path.exists(filename):
            df.to_csv(filename, mode='a', header=False)
        else:
            with open(filename, 'w') as f:
                f.write(df.to_csv(header=True))
        self.Label_Exported.setText('Calculated results added to file: ' + str(filename))
        self.Button_SaveResults.setEnabled(False)

    def SaveMaximas(self):
        if str(self.Line_SaveName.text())=='':
            self.Line_SaveName.setText('Default')
        filename = str(datetime.date.today()) + '_' + str(self.Line_SaveName.text()) + '_Maximas.csv'
        choice = QMessageBox.Yes
        if os.path.exists(filename):
            choice = QMessageBox.question(None, 'Warning', 'This file already exist in the directory,\nReplace?',
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes,)
            if choice == QMessageBox.No:
                return
        self.SavingMaximas.SaveMaximas(filename)
        self.Label_Exported.setText('Maximas coordinates added to file: ' + str(filename))
        self.Button_SaveMaximas.setEnabled(False)

class SavingMaximas:
    def __init__(self, mask, text):
        self.mask = mask; self.text = text

    def SaveMaximas(self, filename):
        coord = np.where(self.mask != 0)
        df = pd.DataFrame(columns = ['x','y']); df.columns.names = ['Coordinates']
        df['x'] = coord[0]; df['y'] = coord[1]
        df.to_csv(filename+self.text, header=True)

def sumAll(input):
    return sum(map(sum, input))

class DAPIThread(QThread):
    DAPI_UpdateStatus = pyqtSignal(str, name='DAPI_UpdateStatus')
    DAPI_Finished = pyqtSignal(float, float, object, name='DAPI_Finished')

    def __init__(self, options=None, parent=None):
        QThread.__init__(self, parent)
        #self.options = options

    def run(self):
        self.DAPI_UpdateStatus.emit('Identifying & Counting objects ...')
        #if self.options == 0:       # Defautl: Use regular mask
        Tissue_meanIntensity = self.MeanofMask(self.img_array, self.DAPI_mask)
        Tissue_mask = self.DAPI_mask.copy()
        self.DAPI_UpdateStatus.emit('Calculating Tissue to Non-tissue mean intensities ratios...')
        Tissue_SNR = Tissue_meanIntensity / self.MeanofMask(self.img_array, np.invert(Tissue_mask))
        self.DAPI_Finished.emit(Tissue_meanIntensity, Tissue_SNR, self.DAPI_mask);

    def UpdateMask(self, DAPI_mask):
        self.DAPI_mask = DAPI_mask

    def LoadImage(self, img_array):
        self.img_array = img_array

    def MeanofMask(self, img_array, mask):  # mask should be boolean
        return sumAll(img_array * mask) / sumAll(mask)

def RandomWalker(data, marker_mask):
    data = sk.exposure.rescale_intensity(data.astype('float'), in_range=(0, 255), out_range=(0, 1))
    data = sk.exposure.rescale_intensity(data, in_range=(-0.35, 1 + 0.35), out_range=(-1, 1))

    # The range of the binary image spans over (-1, 1).
    # We choose the hottest and the coldest pixels as markers.
    markers = np.zeros(data.shape, dtype=np.uint)
    markers[data < -0.95] = 1;
    markers[data > 0.95] = 2

    # Run random walker algorithm
    labels = sk.segmentation.random_walk(data, markers, beta=10, mode='bf')

class SNRThread(QThread):
    Signal_UpdateStatus = pyqtSignal(str, name='Signal_UpdateStatus')
    Signal_Finished = pyqtSignal(float, float, float, name='Signal_Finished')

    def __init__(self, img_array, maximas, tissue_maxima, dapi_mask, mean_func, parent=None):
        QThread.__init__(self, parent)
        self.img_array = img_array;
        self.maxima = maximas;
        self.MeanofMask = mean_func
        self.DAPI_mask = dapi_mask;
        self.tissue_maxima = tissue_maxima

    def run(self):
        mean_maxima_intensity = self.MeanofMask(self.img_array, self.maxima)
        bg = np.invert(self.DAPI_mask)
        mean_bg_intensity = sumAll(self.img_array * bg) / sumAll(bg)
        if type(self.tissue_maxima) == np.ndarray:
            mean_tissue_maxima_intensity = self.MeanofMask(self.img_array, self.tissue_maxima)
            snr = mean_tissue_maxima_intensity / mean_bg_intensity
            nonmaxima_DAPI = self.DAPI_mask * np.invert(self.maxima)
            mean_tissue_bg_intensity = sumAll(self.img_array * nonmaxima_DAPI) / sumAll(nonmaxima_DAPI)
            tissue_snr = mean_tissue_maxima_intensity / mean_tissue_bg_intensity
            self.Signal_Finished.emit(mean_maxima_intensity, snr, tissue_snr)
        else:
            snr = mean_maxima_intensity / mean_bg_intensity
            self.Signal_Finished.emit(mean_maxima_intensity, snr, 0)

class RNARunThread(QThread):
    Signal_UpdateStatus = pyqtSignal(str, name='Signal_UpdateStatus')
    Signal_Finished = pyqtSignal(object, float, name='Signal_Finished')

    def __init__(self, sequences, command_line, dropdown_choice, seqs_conc=None, parent=None):
        QThread.__init__(self, parent);
        self.sequences = sequences
        self.command_line = command_line
        self.choice = dropdown_choice
        if seqs_conc != None:
            self.seqs_conc = [float(conc) for conc in seqs_conc.split(',')]

    def run(self):
        start_t = time.time();
        self.seqs = [''.join(i.split(' ')) for i in [ii for ii in self.sequences.iloc[:, 0]]]
        self.Signal_UpdateStatus.emit('Performing calculations...')
        if self.choice == 0:
            energy_df = self.CreateClusterDF(self.seqs, self.coFoldEnergy)
        elif self.choice == 1:
            if len(self.seqs) != len(self.seqs_conc):
                QMessageBox.question(MainWindow, 'Warning', 'Your concentration information is insufficient', QMessageBox.Ok)
                self.terminate()
            energy_df = self.CreateClusterDF(self.seqs, self.coFoldEnergy_conc, self.seqs_conc)
        elif self.choice == 2:
            energy_df = self.CreateClusterDF(self.seqs, self.duplexEnergy)
        elif self.choice == 3:
            energy_df = self.CreateClusterDF(self.seqs, self.duplexEnergy_Up)

        self.Signal_UpdateStatus.emit('Generating Plot...')
        fig = plt.figure(figsize=(19, 19), tight_layout=True);
        ax = fig.add_subplot(1, 1, 1)
        ax.set_title('Primary Probe Intermolecular Interaction Energy', pad=3)
        ax.set_ylabel('Sequence ID', rotation=80);
        ax.set_xlabel('Sequence ID', rotation=20);
        heat_plot = sb.heatmap(energy_df, ax=ax, cbar_kws={'label': 'Energy (kcal/mol)'})
        self.Signal_Finished.emit(fig, time.time() - start_t)

    def coFoldEnergy(self, seq1, seq2):
        with open('t.seq', 'w') as file_seq:
            file_seq.write(seq1 + '&' + seq2)
        with open("test.txt", 'w') as f:
            subprocess.check_call(self.command_line, shell=True, stdout=f, stderr=f, stdin=f)
        with open("test.txt", 'r') as fh:
            fh.seek(4);
            last = fh.readlines()[-1]
            energy = float(last.split('=')[-1].split('\n')[0])
        return energy

    def coFoldEnergy_conc(self, seq1, seq2, conc=[]):
        with open('t.seq', 'w') as file_seq:
            file_seq.write(seq1 + '&' + seq2 + '\n')
            file_seq.write(str(conc[0]) + ' ' + str(conc[1]))
        with open("coFoldc.txt", 'w') as f:
            subprocess.check_call(self.command_line, shell=True, stdout=f, stderr=f, stdin=f)
        with open("coFoldc.txt", 'r') as fh:
            while True:
                line = fh.readline();
                if line.startswith('-'):
                    return float(line.split('\t')[0])

    def duplexEnergy(self, seq1, seq2):
        with open('duplex.seq', 'w') as file_seq:
            file_seq.write(seq1 + '\n' + seq2)
        with open("duplex.txt", 'w') as f:
            subprocess.check_call(self.command_line, shell=True, stdout=f, stderr=f, stdin=f)
        with open('duplex.txt', 'r') as fh:
            energy = float(fh.readline().split(' ')[-1].split('(')[-1].split(')')[0])
        return energy

    def duplexEnergy_Up(self, seq1, seq2):
        with open('duplex.seq', 'w') as file_seq:
            file_seq.write(seq1 + '&' + seq2)
        with open("duplexUp.txt", 'w') as f:
            subprocess.check_call(self.command_line, shell=True, stdout=f, stderr=f, stdin=f)
        with open('duplexUp.txt', 'r') as fh:
            energy = float(fh.readline().split('=')[0].split(':')[-1].split('(')[-1])
        return energy

    def CreateClusterDF(self, seqs, energy_func, concs=None):
        energy_df = pd.DataFrame(columns=range(len(seqs)), index=range(len(seqs)));
        # print('Scale', energy_df.shape)
        for i in range(len(seqs)):
            for ii in range(len(seqs)):
                if not energy_func.__name__ == 'coFoldEnergy_conc':
                    energy_df.iloc[i, ii] = energy_func(seqs[i], seqs[ii])
                else:
                    if i == ii:
                        continue
                    energy_df.iloc[i, ii] = \
                        energy_func(seqs[i], seqs[ii], [concs[i], concs[ii]])
        energy_df.update(energy_df.transpose())
        return energy_df.astype('float')


## Photo Viewer


COLORTABLE=[]; [COLORTABLE.append(QtGui.qRgb(i/4, i, i/2)) for i in range(256)]


class ImageViewWindow(QtWidgets.QWidget):
    def __init__(self, image, parent=None):
        super(ImageViewWindow, self).__init__(parent)
        self.viewer = PhotoViewer(self)
        # 'Load image' button
        self.setGeometry(800, 500, 800, 600)
        self.btnLoad = QtWidgets.QToolButton(self)
        self.btnLoad.setText('Load image')
        self.btnLoad.clicked.connect(self.loadImage)
        # Button to change from drag/pan to getting pixel info
        self.btnPixInfo = QtWidgets.QToolButton(self)
        self.btnPixInfo.setText('Enter pixel info mode')
        self.btnPixInfo.clicked.connect(self.pixInfo)
        self.editPixInfo = QtWidgets.QLineEdit(self)
        self.editPixInfo.setReadOnly(True)
        self.viewer.photoClicked.connect(self.photoClicked)
        # Arrange layout
        VBlayout = QtWidgets.QVBoxLayout(self)
        VBlayout.addWidget(self.viewer)
        HBlayout = QtWidgets.QHBoxLayout()
        HBlayout.setAlignment(QtCore.Qt.AlignLeft)
        HBlayout.addWidget(self.btnLoad)
        HBlayout.addWidget(self.btnPixInfo)
        HBlayout.addWidget(self.editPixInfo)
        VBlayout.addLayout(HBlayout)

        # My code for better viewing
        self.img_noiseless = (mh.gaussian_filter(image,sigma=0.5)>image.mean())*image

    def loadImage(self):
        height, width = self.img_noiseless.shape
        Qimg = QtGui.QImage(self.img_noiseless, width, height, QtGui.QImage.Format_Indexed8)
        Qimg.setColorTable(COLORTABLE)
        self.viewer.setPhoto(QtGui.QPixmap.fromImage(Qimg))

    def pixInfo(self):
        self.viewer.toggleDragMode()

    def photoClicked(self, pos):
        if self.viewer.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.editPixInfo.setText('%d, %d' % (pos.x(), pos.y()))


class PhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._empty = False
        self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self._photo.setPixmap(pixmap)
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif not self._photo.pixmap().isNull():
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            self.photoClicked.emit(QtCore.QPoint(event.pos()))
        super(PhotoViewer, self).mousePressEvent(event)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ScriptTranslator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1043, 1459)
        Form.setMinimumSize(QtCore.QSize(704, 1081))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.Text_Script = QtWidgets.QTextEdit(Form)
        self.Text_Script.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Text_Script.setFont(font)
        self.Text_Script.setObjectName("Text_Script")
        self.verticalLayout_2.addWidget(self.Text_Script)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.Button_Load = QtWidgets.QPushButton(Form)
        self.Button_Load.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Button_Load.setObjectName("Button_Load")
        self.horizontalLayout_9.addWidget(self.Button_Load, 0, QtCore.Qt.AlignHCenter)
        self.Button_Export = QtWidgets.QPushButton(Form)
        self.Button_Export.setMaximumSize(QtCore.QSize(250, 16777215))
        self.Button_Export.setObjectName("Button_Export")
        self.horizontalLayout_9.addWidget(self.Button_Export, 0, QtCore.Qt.AlignHCenter)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Line_FileName = QtWidgets.QLineEdit(self.frame)
        self.Line_FileName.setGeometry(QtCore.QRect(0, 10, 329, 47))
        self.Line_FileName.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Line_FileName.setFont(font)
        self.Line_FileName.setObjectName("Line_FileName")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(330, 10, 37, 57))
        self.label_17.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18, 0, QtCore.Qt.AlignLeft)
        self.Label_Status = QtWidgets.QLabel(Form)
        self.Label_Status.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_Status.setFont(font)
        self.Label_Status.setText("")
        self.Label_Status.setObjectName("Label_Status")
        self.horizontalLayout.addWidget(self.Label_Status)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Check_ScriptEdit = QtWidgets.QCheckBox(Form)
        self.Check_ScriptEdit.setObjectName("Check_ScriptEdit")
        self.horizontalLayout.addWidget(self.Check_ScriptEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.Label_VolumeUsed = QtWidgets.QLabel(Form)
        self.Label_VolumeUsed.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Label_VolumeUsed.setFont(font)
        self.Label_VolumeUsed.setText("")
        self.Label_VolumeUsed.setObjectName("Label_VolumeUsed")
        self.horizontalLayout_2.addWidget(self.Label_VolumeUsed, 0, QtCore.Qt.AlignHCenter)
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_2.addWidget(self.label_22)
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_2.addWidget(self.label_20)
        self.Label_Time = QtWidgets.QLabel(Form)
        self.Label_Time.setMinimumSize(QtCore.QSize(100, 0))
        self.Label_Time.setText("")
        self.Label_Time.setObjectName("Label_Time")
        self.horizontalLayout_2.addWidget(self.Label_Time)
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_2.addWidget(self.label_21)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 5, 5, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(15, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.Combo_Valve = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Combo_Valve.setFont(font)
        self.Combo_Valve.setObjectName("Combo_Valve")
        self.Combo_Valve.addItem("")
        self.Combo_Valve.addItem("")
        self.Combo_Valve.addItem("")
        self.gridLayout.addWidget(self.Combo_Valve, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Combo_Port = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Combo_Port.setFont(font)
        self.Combo_Port.setObjectName("Combo_Port")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.Combo_Port.addItem("")
        self.gridLayout.addWidget(self.Combo_Port, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.Line_Reagent = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Line_Reagent.setFont(font)
        self.Line_Reagent.setObjectName("Line_Reagent")
        self.gridLayout.addWidget(self.Line_Reagent, 3, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Spin_Velocity = QtWidgets.QDoubleSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.Spin_Velocity.setFont(font)
        self.Spin_Velocity.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Spin_Velocity.setDecimals(0)
        self.Spin_Velocity.setMaximum(5000.0)
        self.Spin_Velocity.setSingleStep(10.0)
        self.Spin_Velocity.setProperty("value", 160.0)
        self.Spin_Velocity.setObjectName("Spin_Velocity")
        self.gridLayout_2.addWidget(self.Spin_Velocity, 8, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.Button_TempSet = QtWidgets.QPushButton(Form)
        self.Button_TempSet.setObjectName("Button_TempSet")
        self.gridLayout_2.addWidget(self.Button_TempSet, 5, 2, 1, 1)
        self.Button_SetVolume = QtWidgets.QPushButton(Form)
        self.Button_SetVolume.setObjectName("Button_SetVolume")
        self.gridLayout_2.addWidget(self.Button_SetVolume, 1, 2, 1, 1)
        self.Combo_Temp = QtWidgets.QComboBox(Form)
        self.Combo_Temp.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Combo_Temp.setFont(font)
        self.Combo_Temp.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.Combo_Temp.setEditable(True)
        self.Combo_Temp.setObjectName("Combo_Temp")
        self.Combo_Temp.addItem("")
        self.Combo_Temp.addItem("")
        self.Combo_Temp.addItem("")
        self.Combo_Temp.addItem("")
        self.gridLayout_2.addWidget(self.Combo_Temp, 5, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.Spin_Volume = QtWidgets.QDoubleSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Spin_Volume.setFont(font)
        self.Spin_Volume.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.Spin_Volume.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.Spin_Volume.setAccelerated(False)
        self.Spin_Volume.setProperty("showGroupSeparator", False)
        self.Spin_Volume.setDecimals(1)
        self.Spin_Volume.setMaximum(12.0)
        self.Spin_Volume.setSingleStep(0.1)
        self.Spin_Volume.setObjectName("Spin_Volume")
        self.horizontalLayout_8.addWidget(self.Spin_Volume, 0, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10, 0, QtCore.Qt.AlignLeft)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setMinimumSize(QtCore.QSize(0, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 7, 0, 1, 1)
        self.Button_Init = QtWidgets.QPushButton(Form)
        self.Button_Init.setObjectName("Button_Init")
        self.gridLayout_2.addWidget(self.Button_Init, 9, 2, 1, 1)
        self.Button_Velocity = QtWidgets.QPushButton(Form)
        self.Button_Velocity.setObjectName("Button_Velocity")
        self.gridLayout_2.addWidget(self.Button_Velocity, 8, 2, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.Spin_WaitMins = QtWidgets.QSpinBox(Form)
        self.Spin_WaitMins.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Spin_WaitMins.setFont(font)
        self.Spin_WaitMins.setMaximum(600)
        self.Spin_WaitMins.setProperty("value", 0)
        self.Spin_WaitMins.setObjectName("Spin_WaitMins")
        self.horizontalLayout_10.addWidget(self.Spin_WaitMins, 0, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setMinimumSize(QtCore.QSize(65, 0))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.Spin_WaitSecs = QtWidgets.QSpinBox(Form)
        self.Spin_WaitSecs.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Spin_WaitSecs.setFont(font)
        self.Spin_WaitSecs.setFrame(True)
        self.Spin_WaitSecs.setMaximum(60)
        self.Spin_WaitSecs.setObjectName("Spin_WaitSecs")
        self.horizontalLayout_10.addWidget(self.Spin_WaitSecs, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setMinimumSize(QtCore.QSize(60, 0))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 6, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 3, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 4, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setLineWidth(5)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_11 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 15)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.Spin_LineNum1 = QtWidgets.QSpinBox(Form)
        self.Spin_LineNum1.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Spin_LineNum1.setFont(font)
        self.Spin_LineNum1.setMaximum(0)
        self.Spin_LineNum1.setObjectName("Spin_LineNum1")
        self.gridLayout_3.addWidget(self.Spin_LineNum1, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.Spin_LineNum2 = QtWidgets.QSpinBox(Form)
        self.Spin_LineNum2.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Spin_LineNum2.setFont(font)
        self.Spin_LineNum2.setMaximum(0)
        self.Spin_LineNum2.setObjectName("Spin_LineNum2")
        self.gridLayout_3.addWidget(self.Spin_LineNum2, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.Button_RemoveSteps = QtWidgets.QPushButton(Form)
        self.Button_RemoveSteps.setMinimumSize(QtCore.QSize(200, 0))
        self.Button_RemoveSteps.setObjectName("Button_RemoveSteps")
        self.gridLayout_3.addWidget(self.Button_RemoveSteps, 0, 5, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 6, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        self.Check_ScriptEdit.toggled['bool'].connect(self.Text_Script.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Fluidics Scriptor"))
        self.Button_Load.setText(_translate("Form", "Load script from ..."))
        self.Button_Export.setText(_translate("Form", "Save script as ..."))
        self.Line_FileName.setText(_translate("Form", "MyScript"))
        self.label_17.setText(_translate("Form", ".txt"))
        self.label_18.setText(_translate("Form", "Status:"))
        self.Check_ScriptEdit.setText(_translate("Form", "Enable Manual Editing"))
        self.label_9.setText(_translate("Form", "Syringe volume used:"))
        self.label_22.setText(_translate("Form", "mL"))
        self.label_20.setText(_translate("Form", "Minimum ETC:"))
        self.label_21.setText(_translate("Form", "s"))
        self.label_14.setText(_translate("Form", "Valve/Port"))
        self.label_4.setText(_translate("Form", "Port"))
        self.Combo_Valve.setCurrentText(_translate("Form", "     1"))
        self.Combo_Valve.setItemText(0, _translate("Form", "     1"))
        self.Combo_Valve.setItemText(1, _translate("Form", "     2"))
        self.Combo_Valve.setItemText(2, _translate("Form", "     3"))
        self.label_2.setText(_translate("Form", "Valve"))
        self.label_3.setText(_translate("Form", "Set"))
        self.Combo_Port.setItemText(0, _translate("Form", "      0A"))
        self.Combo_Port.setItemText(1, _translate("Form", "       1"))
        self.Combo_Port.setItemText(2, _translate("Form", "       2"))
        self.Combo_Port.setItemText(3, _translate("Form", "       3"))
        self.Combo_Port.setItemText(4, _translate("Form", "       4"))
        self.Combo_Port.setItemText(5, _translate("Form", "       5"))
        self.Combo_Port.setItemText(6, _translate("Form", "       6"))
        self.Combo_Port.setItemText(7, _translate("Form", "       7"))
        self.Combo_Port.setItemText(8, _translate("Form", "       8"))
        self.Combo_Port.setItemText(9, _translate("Form", "       9"))
        self.label_19.setText(_translate("Form", "Reagent name (optional):"))
        self.label_5.setText(_translate("Form", "Add Steps"))
        self.label_7.setText(_translate("Form", "Temperature:"))
        self.Button_TempSet.setText(_translate("Form", "Set"))
        self.Button_SetVolume.setText(_translate("Form", "Add"))
        self.Combo_Temp.setItemText(0, _translate("Form", "      17"))
        self.Combo_Temp.setItemText(1, _translate("Form", "      37"))
        self.Combo_Temp.setItemText(2, _translate("Form", "      40"))
        self.Combo_Temp.setItemText(3, _translate("Form", "      65"))
        self.label_13.setText(_translate("Form", "Velocity:"))
        self.label_10.setText(_translate("Form", " k"))
        self.label_6.setText(_translate("Form", "Draw Volume:"))
        self.Button_Init.setText(_translate("Form", "Init → Velocity"))
        self.Button_Velocity.setText(_translate("Form", "Set Velocity"))
        self.label_8.setText(_translate("Form", "Wait Time:"))
        self.label_15.setText(_translate("Form", " mins "))
        self.label_16.setText(_translate("Form", " secs "))
        self.label_11.setText(_translate("Form", "Edit"))
        self.label_12.setText(_translate("Form", "to"))
        self.Button_RemoveSteps.setText(_translate("Form", "Remove Steps"))
        self.label_23.setText(_translate("Form", "Steps"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


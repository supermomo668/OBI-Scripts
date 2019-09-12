from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread


class PulseProgressBar(QDialog):
    def __init__(self):
        super(PulseProgressBar,self).__init__()
        loadUi('PulseProgressDialogue.ui',self)
        self.show()

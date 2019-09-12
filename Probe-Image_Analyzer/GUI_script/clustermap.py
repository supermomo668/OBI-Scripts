from PyQt5.QtWidgets  import *
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class ClusterMap(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)         ### Initialize Qwidget

        self.grid_layout = QGridLayout()
        self.grid_layout.setColumnStretch(0, 1)

        self.grid_layout.setRowStretch(0, 1)
        self.grid_layout.setRowStretch(1, 5)

    def setupUi(self, figure=None, title=None, xlabel=None, ylabel = None):
        canvas = FigureCanvas(figure)
        plt.suptitle(title)
        plt.ylabel(ylabel, rotation=85);
        plt.xlabel(xlabel, rotation=10)
        toolbar = NavigationToolbar(canvas, self)

        self.grid_layout.addWidget(toolbar, 0, 0)
        self.grid_layout.addWidget(canvas, 0, 0, 2, 2)

        self.setLayout(self.grid_layout)
        self.show();  self.update();
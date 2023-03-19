import sys
import csv
import pandas as pd
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):

    def open_brake_window(self):
        # Open a brake window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Brake_Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_motor_window(self):
        # Open a motor window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Motor_Window()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        MainWindow.setStyleSheet("")

        #Define the icon of the window
        icon = QtGui.QIcon("icon.jpg")
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(50,10,300,50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Text.setFont(font)
        self.Text.setObjectName("Text")

        #Brake button, open the brake window
        self.Freio_button = QtWidgets.QPushButton(self.centralwidget)
        self.Freio_button.setEnabled(True)
        self.Freio_button.setGeometry(QtCore.QRect(70,80,191,81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.Freio_button.setFont(font)
        self.Freio_button.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(8, 115, 0, 255));\n"
            "color: rgb(255, 255, 255);\n")
        self.Freio_button.setObjectName("Freio_buton")
        self.Freio_button.clicked.connect(self.open_brake_window)

        #Motor button, open the motor window
        self.Motor_button = QtWidgets.QPushButton(self.centralwidget)
        self.Motor_button.setGeometry(QtCore.QRect(70,177,191,81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.Motor_button.setFont(font)
        self.Motor_button.setStyleSheet(
            "background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(8, 115, 0, 255));\n"
            "color: rgb(255, 255, 255);\n")
        self.Motor_button.setObjectName("Motor_button")
        self.Motor_button.clicked.connect(self.open_motor_window)

        #Symbol/image settings
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(270, 100, 58, 51))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("logo.png"))
        self.photo.setObjectName("photo")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Text.setText(_translate("MainWindow", "Escolha a Bancada"))
        self.Freio_button.setText(_translate("MainWindow", "Freio"))
        self.Motor_button.setText(_translate("MainWindow", "Motor"))


class Ui_Brake_Window(object):

    def setupUi(self, Brake_Window):

        Brake_Window.setObjectName("Brake_Window")
        Brake_Window.resize(611, 589)

        b_icon = QtGui.QIcon("b_icon.png")
        Brake_Window.setWindowIcon(b_icon)

        self.centralwidget = QtWidgets.QWidget(Brake_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 591, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.Select_button = QtWidgets.QPushButton(self.layoutWidget, clicked=lambda: self.Open_sheet_Brake())
        self.Select_button.setStyleSheet("border-radius=5px;\n"
                                         "")
        self.Select_button.setObjectName("Select_button")
        self.verticalLayout.addWidget(self.Select_button)

        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.Tem_Pre = QtWidgets.QWidget()
        self.Tem_Pre.setObjectName("Tem_Pre")
        self.graph_Tem_Pre = pg.PlotWidget(self.Tem_Pre)
        self.graph_Tem_Pre.setBackground('w')
        self.graph_Tem_Pre.showGrid(x=True, y=True)
        self.graph_Tem_Pre.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.Tem_Pre, "")

        self.Tem_Vel = QtWidgets.QWidget()
        self.Tem_Vel.setObjectName("Tem_Vel")
        self.graph_Tem_Vel = pg.PlotWidget(self.Tem_Vel)
        self.graph_Tem_Vel.setBackground('w')
        self.graph_Tem_Vel.showGrid(x=True, y=True)
        self.graph_Tem_Vel.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.Tem_Vel, "")

        self.Pre_Vel = QtWidgets.QWidget()
        self.Pre_Vel.setObjectName("Pre_Vel")
        self.graph_Pre_Vel = pg.PlotWidget(self.Pre_Vel)
        self.graph_Pre_Vel.setBackground('w')
        self.graph_Pre_Vel.showGrid(x=True, y=True)
        self.graph_Pre_Vel.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.Pre_Vel, "")

        self.verticalLayout.addWidget(self.tabWidget)
        self.tabWidget.raise_()
        self.Select_button.raise_()
        Brake_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Brake_Window) 
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusbar.setMouseTracking(False)
        self.statusbar.setObjectName("statusbar")
        Brake_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Brake_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Brake_Window)

    def Open_sheet_Brake(self):
        # Open directory to read csv files
        filename = QFileDialog.getOpenFileName(None, ("Open FIle"), "", ("Csv Files (*.csv);;Txt FIles (*.txt)"))[0]

        if filename != '':
            self.alldata = pd.read_csv(filename[0])
            self.rot_tab = self.alldata.set_index('f1')
            self.vel_tab = self.alldata.set_index('f2')
            self.pre_tab = self.alldata.set_index('f4')
            self.temp_tab = self.alldata.set_index('f5')

            self.f1 = self.rot_tab.index.values
            self.f2 = self.vel_tab.index.values
            self.f4 = self.pre_tab.index.values
            self.f5 = self.temp_tab.index.values

    def plot_graph_brake(self):
        self.graph_Tem_Pre.setYRange(self.f5)
        self.graph_Tem_Pre.setXRange(self.f4)

        self.graph_Tem_Vel.setYRange(self.f5)
        self.graph_Tem_Vel.setXRange(self.f2)

        self.graph_Pre_Vel.setYRange(self.f4)
        self.graph_Pre_Vel.setXRange(self.f2)

    def retranslateUi(self, Brake_Window):
        _translate = QtCore.QCoreApplication.translate
        Brake_Window.setWindowTitle(_translate("Brake_Window", "Brake_Window"))
        self.Select_button.setText(_translate("Brake_Window", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tem_Pre),
                                  _translate("Brake_Window", "Temperatura/Pressão"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tem_Vel),
                                  _translate("Brake_Window", "Temperatura/Velocidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pre_Vel),
                                  _translate("Brake_Window", "Pressão/Velocidade"))


class Ui_Motor_Window(object):

    def setupUi(self, Motor_Window):
        Motor_Window.setObjectName("Motor_Window")
        Motor_Window.resize(611, 589)

        #Define the icon of the window
        m_icon = QtGui.QIcon("m_icon.png")
        Motor_Window.setWindowIcon(m_icon)

        self.centralwidget = QtWidgets.QWidget(Motor_Window)
        self.centralwidget.setObjectName("centralwidget")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 591, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #Select button, to open an select your csv file
        self.Select_button = QtWidgets.QPushButton(self.layoutWidget, clicked=lambda: self.Open_sheet_Motor())
        self.Select_button.setStyleSheet("border-radius=5px;\n"
                                         "")
        self.Select_button.setObjectName("Select_button")
        self.verticalLayout.addWidget(self.Select_button)

        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        #graphs to torque and potency
        self.torque = []
        self.potency = []
        self.pot_ = []
        self.pressure = []
        self.temperature = []
        self.temp_ = []

        self.Torque_Potency = QtWidgets.QWidget()
        self.Torque_Potency.setObjectName("Tor_Pot")

        self.graph_Torque_Potency = pg.PlotWidget(self.Torque_Potency)
        self.graph_Torque_Potency.setBackground('w')
        self.graph_Torque_Potency.showGrid(x=True, y=True)
        self.graph_Torque_Potency.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Torque_Potency.setLabel('left', 'Torque')
        self.graph_Torque_Potency.setLabel('bottom', 'Potência')
        self.tabWidget.addTab(self.Torque_Potency, "")

        #graphs to temperature and potency
        self.Temperature_Potency = QtWidgets.QWidget()
        self.Temperature_Potency.setObjectName("Tem_Pot")

        self.graph_Temperature_Potency = pg.PlotWidget(self.Temperature_Potency)
        self.graph_Temperature_Potency.setBackground('w')
        self.graph_Temperature_Potency.showGrid(x=True, y=True)
        self.graph_Temperature_Potency.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Temperature_Potency.setLabel('left', 'Temperatura')
        self.graph_Temperature_Potency.setLabel('bottom', 'Potência')
        self.tabWidget.addTab(self.Temperature_Potency, "")

        #graphs to pressure and temperature
        self.Pressure_Temperature = QtWidgets.QWidget()
        self.Pressure_Temperature.setObjectName("Pre_Temp")

        self.graph_Pressure_Temperature = pg.PlotWidget(self.Pressure_Temperature)
        self.graph_Pressure_Temperature.setBackground('w')
        self.graph_Pressure_Temperature.showGrid(x=True, y=True)
        self.graph_Pressure_Temperature.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Pressure_Temperature.setLabel('left', 'Pressão')
        self.graph_Pressure_Temperature.setLabel('bottom', 'Temperatura')
        self.tabWidget.addTab(self.Pressure_Temperature, "")

        self.plot_graph_Motor()

        self.verticalLayout.addWidget(self.tabWidget)
        self.tabWidget.raise_()
        self.Select_button.raise_()
        Motor_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Motor_Window)
        self.statusbar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusbar.setMouseTracking(True)
        self.statusbar.setObjectName("statusbar")
        Motor_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Motor_Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Motor_Window)

    def Open_sheet_Motor(self):
        # Open directory to read csv files
        file_path, _ = QFileDialog.getOpenFileName(None, 'Open FIle', '', 'Csv Files (*.csv)')

        #Read the csv and append in vectors
        with open(file_path, 'r') as csv_file:
            read = csv.reader(csv_file)
            next(read)

            for row in read:
                self.potency.append(float(row[0]))
                self.pot_.append(float(row[0]))
                self.temperature.append(float(row[1]))
                self.temp_.append(float(row[1]))
                self.torque.append(float(row[2]))
                self.pressure.append(float(row[3]))

            #if file_path != '':
            #self.all_data = pd.read_csv(file_path[0])
            #self.pot_tab = self.all_data.set_index('f1')
            #self.temp_tab = self.all_data.set_index('f2')
            #self.Tor_tab = self.all_data.set_index('f3')
            #self.Pre_tab = self.all_data.set_index('f4')
            #
            #self.f1 = self.pot_tab.index.values
            #self.f2 = self.temp_tab.index.values
            #self.f3 = self.Tor_tab.index.values
            #self.f4 = self.Pre_tab.index.values

    def plot_graph_Motor(self):
        self.graph_Torque_Potency.clear()
        self.graph_Temperature_Potency.clear()
        self.graph_Pressure_Temperature.clear()

        #self.graph_Torque_Potency.setYRange(self.f5)
        #self.graph_Torque_Potency.setXRange(self.f4)
        #self.graph_Temperature_Potency.setYRange(self.f5)
        #self.graph_Temperature_Potency.setXRange(self.f2)
        #self.graph_Pressure_Temperature.setYRange(self.f4)
        #self.graph_Pressure_Temperature.setXRange(self.f2)

    def retranslateUi(self, Motor_Window):
        _translate = QtCore.QCoreApplication.translate
        Motor_Window.setWindowTitle(_translate("Motor_Window", "Motor_Window"))
        self.Select_button.setText(_translate("Motor_Window", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Torque_Potency), _translate("Motor_Window", "Torque/Potência"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Temperature_Potency),
                                  _translate("Motor_Window", "Temperatura/Potência"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pressure_Temperature),
                                  _translate("Motor_Window", "Pressão/Temperatura"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
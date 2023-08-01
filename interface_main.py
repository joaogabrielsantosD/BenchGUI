# Version with filtering function

# Can be used for any post-processing.
import sys
import pandas as pd
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from tkinter import messagebox as msb
from tkinter import filedialog as fd
from tkinter import *
from scipy import signal


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

        '''+ 
            Aqui você pode criar um objeto botão 
        '''
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
        '''+ 
            Aqui você nomeia os objetos criados anteriormente 
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Text.setText(_translate("MainWindow", "Escolha a Bancada"))
        self.Freio_button.setText(_translate("MainWindow", "Freio"))
        self.Motor_button.setText(_translate("MainWindow", "Motor"))


class Ui_Brake_Window(object):

    def setupUi(self, Brake_Window):
        Brake_Window.setObjectName("Brake_Window")
        Brake_Window.resize(611, 589)

        #Define the icon of the window
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

        #Select button, to open an select your csv file
        self.Select_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Select_button.setStyleSheet("border-radius=5px;\n"
                                         "")
        self.Select_button.setObjectName("Select_button")
        self.verticalLayout.addWidget(self.Select_button)
        self.Select_button.clicked.connect(self.csv_file_reader)

        #Tab style
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")   

        '''+ 
            Aqui como criar Widget separados para colocar seus gráficos
            Dentro da tabWidget**
        '''
        #graphs to Temperature and Pressure
        self.Temperature_Pressure = QtWidgets.QWidget(Brake_Window)
        self.Temperature_Pressure.setObjectName("Tem_Pre")
        self.graph_Temperature_Pressure = pg.PlotWidget(self.Temperature_Pressure)
        #change the graph color, default is 'k'(black color)
        self.graph_Temperature_Pressure.setBackground('k')
        self.graph_Temperature_Pressure.setTitle("Temperatura pela Pressão",color='w',size="15pt")
        self.graph_Temperature_Pressure.showGrid(x=True, y=True)
        self.graph_Temperature_Pressure.setLabel('left', "Temperatura(°C)")
        self.graph_Temperature_Pressure.setLabel('bottom', "Pressão(Psi)")
        self.graph_Temperature_Pressure.setGeometry(QtCore.QRect(50,50, 500, 400))
        self.tabWidget.addTab(self.Temperature_Pressure, "")

        #graphs to Temperature and speed
        self.Temperature_Speed = QtWidgets.QWidget(Brake_Window)
        self.Temperature_Speed.setObjectName("Tem_Vel")
        self.graph_Temperature_Speed = pg.PlotWidget(self.Temperature_Speed)
        self.graph_Temperature_Speed.setBackground('k') #w=white and k=black
        self.graph_Temperature_Speed.setTitle("Temperatura pela Velocidade",color='w',size="15pt")
        self.graph_Temperature_Speed.showGrid(x=True, y=True)
        self.graph_Temperature_Speed.setLabel('left', "Temperatura(°C)")
        self.graph_Temperature_Speed.setLabel('bottom', "Velocidade(Km/h)")
        self.graph_Temperature_Speed.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.Temperature_Speed, "")

        #graphs to Pressure and speed
        self.Pressure_Speed = QtWidgets.QWidget(Brake_Window)
        self.Pressure_Speed.setObjectName("Pre_Vel")
        self.graph_Pressure_Speed = pg.PlotWidget(self.Pressure_Speed)
        self.graph_Pressure_Speed.setBackground('k')
        self.graph_Pressure_Speed.setTitle("Pressão pela Velocidade",color='w',size="15pt")
        self.graph_Pressure_Speed.showGrid(x=True, y=True)
        self.graph_Pressure_Speed.setLabel('left', "Pressão(Psi)")
        self.graph_Pressure_Speed.setLabel('bottom', "Velocidade(Km/h)")
        self.graph_Pressure_Speed.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.Pressure_Speed, "")

        #graph to RPM
        self.RPM_t = QtWidgets.QWidget(Brake_Window)
        self.RPM_t.setObjectName("RPM_TIME")
        self.graph_RPM_t = pg.PlotWidget(self.RPM_t)
        self.graph_RPM_t.setBackground('k')
        self.graph_RPM_t.setTitle("Rotação pelo tempo",color='w',size="15pt")
        self.graph_RPM_t.showGrid(x=True,y=True)
        self.graph_RPM_t.setLabel('left', "RPM")
        self.graph_RPM_t.setLabel('bottom', "Tempo(s)")
        self.graph_RPM_t.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.tabWidget.addTab(self.RPM_t, "")

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

    def csv_file_reader(self):
        # Open directory to read csv files
        #filename = QFileDialog.getOpenFileName(None, 'CSV FIle', '', 'Csv Files (*.csv)')
        '''+ 
            Aqui em diante você mudara e criara seus objetos de acordo com o que você deseja ler.
            set_index tem que ter como referencia um "titulo" para a coluna.
            Entao no seu csv deve ter um "titulo" para que tudo naquela coluna possa ser lido e 
            guardado na variavel em que voce criar.s
        '''
        filename = fd.askopenfilename()
        if ".csv" in filename:
            df = pd.read_csv(filename)
            tabela1 = df.set_index('RPM')
            tabela2 = df.set_index('SPEED')
            tabela3 = df.set_index('TIME')
            tabela4 = df.set_index('PRESSURE')
            tabela5 = df.set_index('TEMPERATURE')

            f1 = tabela1.index.values
            f2 = tabela2.index.values
            f3 = tabela3.index.values
            f4 = tabela4.index.values
            f5 = tabela5.index.values

            rpm_in = []
            vel_in = []
            self.time = []
            pres_in = []
            temp_in = []

            for i in range(int(len(f1))):
                rpm_in.append(f1[i])
                vel_in.append(f2[i])
                self.time.append(f3[i])
                pres_in.append(f4[i])
                temp_in.append(f5[i])

            self.update_plots(rpm_in,vel_in,pres_in,temp_in)

        else:
            msb.showerror("ERRO","Arquivo Inválido!")

    def update_plots(self,RPM,VEL, PRES, TEMP):
        b,a = signal.butter(4,0.1,analog=False)
        sig_temp = signal.lfilter(b,a,TEMP)
        sig_pres = signal.lfilter(b,a,PRES)
        sig_vel = signal.lfilter(b,a,VEL)
        sig_rot = signal.lfilter(b, a, RPM)

        self.pen1 = pg.mkPen(color=(0,255,0), width=4)
        self.pen2 = pg.mkPen(color=(255,0,0), width=4)
        self.pen3 = pg.mkPen(color=(0,0,255), width=4)
        self.pen4 = pg.mkPen(color=(255,203,219), width=4)

        self.graph_Temperature_Pressure.setXRange(0,1000)
        self.graph_Temperature_Pressure.setYRange(0,1000)
        self.graph_Temperature_Pressure.plot(PRES, TEMP, name="Original" , pen='w')
        self.graph_Temperature_Pressure.plot(sig_pres, sig_temp, name="Filtrado" , pen=self.pen1)

        self.graph_Temperature_Speed.setXRange(0,1000)
        self.graph_Temperature_Speed.setYRange(0,1000)
        self.graph_Temperature_Speed.plot(VEL, TEMP, name="Original" , pen='w')
        self.graph_Temperature_Speed.plot(sig_vel, sig_temp, name="Filtrado" , pen=self.pen2)

        self.graph_Pressure_Speed.setXRange(0,1000)
        self.graph_Pressure_Speed.setYRange(0,1000)
        self.graph_Pressure_Speed.plot(VEL, PRES, name="Original" , pen='w')
        self.graph_Pressure_Speed.plot(sig_vel, sig_pres, name="Filtrado" , pen=self.pen3)

        self.graph_RPM_t.setXRange(0,5000)
        self.graph_RPM_t.setYRange(0,100)
        self.graph_RPM_t.plot(self.time, RPM, name="Original" , pen='w')
        self.graph_RPM_t.plot(self.time, sig_rot, name="Filtrado" , pen=self.pen4)

    def retranslateUi(self, Brake_Window):
        _translate = QtCore.QCoreApplication.translate
        Brake_Window.setWindowTitle(_translate("Brake_Window", "Brake_Window"))
        self.Select_button.setText(_translate("Brake_Window", "Select"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Temperature_Pressure),
                                  _translate("Brake_Window", "Temperatura/Pressão"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Temperature_Speed),
                                  _translate("Brake_Window", "Temperatura/Velocidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Pressure_Speed),
                                  _translate("Brake_Window", "Pressão/Velocidade"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RPM_t),
                                  _translate("Brake_Window", "Rotação/Tempo"))


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
        self.Select_button = QtWidgets.QPushButton(self.layoutWidget)
        self.Select_button.setStyleSheet("border-radius=5px;\n"
                                         "")
        self.Select_button.setObjectName("Select_button")
        self.verticalLayout.addWidget(self.Select_button)
        self.Select_button.clicked.connect(self.csv_file_reader)

        #Tab style
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        #graphs to torque and potency
        self.Torque_Potency = QtWidgets.QWidget()
        self.Torque_Potency.setObjectName("Tor_Pot")
        self.graph_Torque_Potency = pg.PlotWidget(self.Torque_Potency)
        self.graph_Torque_Potency.setBackground('k')
        self.graph_Torque_Potency.showGrid(x=True, y=True)
        self.graph_Torque_Potency.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Torque_Potency.setLabel('left', 'Torque')
        self.graph_Torque_Potency.setLabel('bottom', 'Potência')
        self.tabWidget.addTab(self.Torque_Potency, "")  

        #graphs to temperature and potency
        self.Temperature_Potency = QtWidgets.QWidget()
        self.Temperature_Potency.setObjectName("Tem_Pot")
        self.graph_Temperature_Potency = pg.PlotWidget(self.Temperature_Potency)
        self.graph_Temperature_Potency.setBackground('k')
        self.graph_Temperature_Potency.showGrid(x=True, y=True)
        self.graph_Temperature_Potency.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Temperature_Potency.setLabel('left', 'Temperatura')
        self.graph_Temperature_Potency.setLabel('bottom', 'Potência')
        self.tabWidget.addTab(self.Temperature_Potency, "")

        #graphs to pressure and temperature
        self.Pressure_Temperature = QtWidgets.QWidget()
        self.Pressure_Temperature.setObjectName("Pre_Temp")
        self.graph_Pressure_Temperature = pg.PlotWidget(self.Pressure_Temperature)
        self.graph_Pressure_Temperature.setBackground('k')
        self.graph_Pressure_Temperature.showGrid(x=True, y=True)
        self.graph_Pressure_Temperature.setGeometry(QtCore.QRect(50, 50, 500, 400))
        self.graph_Pressure_Temperature.setLabel('left', 'Pressão')
        self.graph_Pressure_Temperature.setLabel('bottom', 'Temperatura')
        self.tabWidget.addTab(self.Pressure_Temperature, "")

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

    def csv_file_reader(self):
        filename = fd.askopenfilename()
        if ".csv" in filename:
            df = pd.read_csv(filename)
            tabela1 = df.set_index('TORQUE')
            tabela2 = df.set_index('POTENCY')
            tabela3 = df.set_index('TIME')
            tabela4 = df.set_index('PRESSURE')
            tabela5 = df.set_index('TEMPERATURE')

            f1 = tabela1.index.values
            f2 = tabela2.index.values
            f3 = tabela3.index.values
            f4 = tabela4.index.values
            f5 = tabela5.index.values

            tor_in = []
            pot_in = []
            self.t = []
            pre_in = []
            tem_in = []

            for i in range(int(len(f1))):
                tor_in.append(f1[i])
                pot_in.append(f2[i])
                self.t.append(f3[i])
                pre_in.append(f4[i])
                tem_in.append(f5[i])

            self.update_plots(tor_in,pot_in,pre_in,tem_in)
        else:
            msb.showerror("ERRO","Arquivo Inválido!")

    def update_plots(self,TORQUE,POTENCY,PRES,TEMP):
        self.graph_Torque_Potency.setXRange(0,1000)
        self.graph_Torque_Potency.setYRange(0,1000)
        self.graph_Torque_Potency.plot(POTENCY,TORQUE,pen='w')

        self.graph_Temperature_Potency.setXRange(0,1000)
        self.graph_Temperature_Potency.setYRange(0,1000)
        self.graph_Temperature_Potency.plot(POTENCY,TEMP,pen='w')

        self.graph_Pressure_Temperature.setXRange(0,1000)    
        self.graph_Pressure_Temperature.setYRange(0,1000)
        self.graph_Pressure_Temperature.plot(TEMP,PRES,pen='w')

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

#Functional version without filter

import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from tkinter import messagebox as msb
from tkinter import filedialog as fd
from tkinter import *
import matplotlib.pyplot as plt


class Ui_MainWindow(object):

    #Def's of Brake window
    def open_brake_window(self):
        # Open a brake window
        self.window = Tk()
        self.window.title("Bancada de Freio")
        self.window.geometry('1000x300')
        photo = PhotoImage(file = 'b_icon.png')
        self.window.wm_iconphoto(False, photo)

        lbl = Label(self.window, text="Selecione o arquivo para plot:")
        lbl.grid(column=0, row=4)

        self.txt = Entry(self.window, width=30)
        self.txt.grid(column=1, row=4)
        self.txt.focus()

        btn = Button(self.window, text="Procurar", command=self.file_select)
        btn.grid(column=2, row=4)

        btn2 = Button(self.window, text="Ler CSV", command=self.grafico)
        btn2.grid(column=1, row=5)

        btn_rot = Button(self.window, text="Rotação pelo tempo", command=self.plot_rot)
        btn_rot.grid(column=0,row=8)

        btn_temp_pres = Button(self.window, text="Temperatura por Pressão", command=self.plot_temp_pres)
        btn_temp_pres.grid(column=1,row=8)

        btn_temp_speed = Button(self.window, text="Temperatura por Velocidade", command=self.plot_temp_speed)
        btn_temp_speed.grid(column=2,row=8)

        btn_pres_speed = Button(self.window, text="Pressão por velocidade", command=self.plot_pres_speed)
        btn_pres_speed.grid(column=4,row=8)

        self.window.mainloop()

    def file_select(self):
        filename = fd.askopenfilename()
        if ".csv" in filename:
            self.txt.delete(0, "end")
            self.txt.insert(0, filename)
        else:
            msb.showerror("ERRO", "Arquivo Inválido!")
            self.txt.delete(0, "end")

    def grafico(self):
        if self.txt.get() and ":/" in self.txt.get():
            #print("ok")
            df = pd.read_csv(self.txt.get())
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

            self.rpm_in = []
            self.vel_in = []
            self.time = []
            self.pres_in = []
            self.temp_in = []

            for i in range(int(len(f1))):
                self.rpm_in.append(f1[i])
                self.vel_in.append(f2[i])
                self.time.append(f3[i])
                self.pres_in.append(f4[i])
                self.temp_in.append(f5[i])

        else:
            msb.showerror("ERRO", "O Caminho acima é inválido")

    #Brake plots

    def plot_rot(self):
        if self.txt.get() and ":/" in self.txt.get():
            #b,a = signal.butter(4, 0.15, analog=False)
            #sig_rpm = signal.lfilter(b,a,self.rpm_in)
            plt.plot(self.time, self.rpm_in, color='#3465a4', label='Original')
            #plt.plot(self.time, sig_rpm, color='#3465a4', label='Filtrado')
            plt.grid(True, which='both')
            plt.legend(loc="best")
            plt.xlabel('tempo(s)')
            plt.ylabel('RPM')
            plt.title("Rotação do Motor")
            plt.show()
        else:
            msb.showerror("ERRO", "Leia o arquivo csv primeiro")

    def plot_temp_pres(self):
        if self.txt.get() and ":/" in self.txt.get():
            #b,a = signal.butter(4, 0.15, analog=False)
            #sig_pres = signal.lfilter(b,a,self.pres_in)
            #sig_temp = signal.lfilter(b,a,self.temp_in)
            plt.plot(self.pres_in, self.temp_in, color='#3465a4', label='Original')
            #plt.plot(sig_pres, sig_temp, color='#3465a4', label='Filtrado')
            plt.grid(True, which='both')
            plt.legend(loc="best")
            plt.xlabel('Temperatura (°C))')
            plt.ylabel('Pressão (PSI)')
            plt.title("Temperatura por Pressão")
            plt.show()
        else:
            msb.showerror("ERRO", "Leia o arquivo csv primeiro")

    def plot_temp_speed(self):
        if self.txt.get() and ":/" in self.txt.get():
            #b,a = signal.butter(4, 0.15, analog=False)
            #sig_vel = signal.lfilter(b,a,self.pres_in)
            #sig_temp = signal.lfilter(b,a,self.temp_in)
            plt.plot(self.pres_in, self.temp_in, color='#3465a4', label='Original')
            #plt.plot(sig_vel, sig_temp, color='#3465a4', label='Filtrado')
            plt.grid(True, which='both')
            plt.legend(loc="best")
            plt.xlabel('Temperatura (°C))')
            plt.ylabel('Velocidade (Km/h)')
            plt.title("Temperatura por Velocidade")
            plt.show()
        else:
            msb.showerror("ERRO", "Leia o arquivo csv primeiro")

    def plot_pres_speed(self):
        if self.txt.get() and ":/" in self.txt.get():
            #b,a = signal.butter(4, 0.15, analog=False)
            #sig_vel = signal.lfilter(b,a,self.pres_in)
            #sig_temp = signal.lfilter(b,a,self.temp_in)
            plt.plot(self.vel_in, self.pres_in, color='#3465a4', label='Original')
            #plt.plot(sig_vel, sig_temp, color='#3465a4', label='Filtrado')
            plt.grid(True, which='both')
            plt.legend(loc="best")
            plt.xlabel('Velocidade (Km/h)')
            plt.ylabel('Pressão (PSI)')
            plt.title("Pressão por velocidade")
            plt.show()
        else:
            msb.showerror("ERRO", "Leia o arquivo csv primeiro")



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

class Ui_Motor_Window(object):
    print("ok")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
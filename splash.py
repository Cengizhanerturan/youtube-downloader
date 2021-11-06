# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from youtube import MyWin

counter = 0


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(680, 400)

        ##---------
        ## Title bar kaldırıp arka planı yok etme
        SplashScreen.setWindowFlag(Qt.FramelessWindowHint)
        SplashScreen.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ##---------


        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.281716 rgba(85, 25, 170, 249), stop:0.645522 rgba(101, 24, 160, 245));\n"
"    color: rgb(184, 185, 255);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(0, 90, 660, 31))
        self.label_title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("background-color: none;\n"
"color: rgb(184, 185, 255);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(0, 130, 660, 21))
        self.label_description.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("background-color: none;\n"
"color: rgb(247, 133, 255, 255);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(50, 240, 561, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(184, 185, 241);\n"
"    color: rgb(10, 32, 172);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.483, stop:0 rgba(247, 133, 255, 255), stop:1 rgba(148, 25, 255, 255));\n"
"    border-radius: 10px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(19, 280, 631, 21))
        self.label_loading.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("background-color: none;\n"
"color: rgb(247, 133, 255, 255);\n"
"text-align: center;")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(10, 350, 641, 21))
        self.label_credits.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arabic Typesetting")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("background-color: none;\n"
"color: rgb(247, 133, 255, 255);\n"
"text-align: center;")
        self.label_credits.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(SplashScreen)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTimer ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)

        ## TIMER IN MILISECONDS
        self.timer.start(35)

        ## CHANGE DESCRIPTION
        self.label_description.setText("Gerekli kontroller yapılıyor")
        QtCore.QTimer.singleShot(1500, lambda: self.label_description.setText("İnternet bağlantınız kontrol ediliyor"))
        QtCore.QTimer.singleShot(3700, lambda: self.label_description.setText("Uygulama açılıyor"))


    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_title.setText(_translate("SplashScreen", "Youtube Video | Müzik İndirme Programı"))
        self.label_description.setText(_translate("SplashScreen", "APP DESCRIPTION"))
        self.label_loading.setText(_translate("SplashScreen", "Lütfen bekleyin..."))
        self.label_credits.setText(_translate("SplashScreen", "Designer By: Cengizhan Erturan"))


    def progress(self):
        global counter
        self.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()

            self.main = MyWin()
            self.main.show()

            SplashScreen.close()

        counter += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())

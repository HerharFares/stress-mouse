# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'items/gui/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(531, 493)
        MainWindow.setMinimumSize(QtCore.QSize(530, 470))
        MainWindow.setMaximumSize(QtCore.QSize(1111111, 1111111))
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 261, 161))
        self.groupBox.setObjectName("groupBox")
        self.default_position = QtWidgets.QRadioButton(self.groupBox)
        self.default_position.setGeometry(QtCore.QRect(10, 20, 201, 41))
        self.default_position.setObjectName("default_position")
        self.pick_position = QtWidgets.QRadioButton(self.groupBox)
        self.pick_position.setGeometry(QtCore.QRect(10, 50, 201, 41))
        self.pick_position.setObjectName("pick_position")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(60, 80, 81, 31))
        self.label.setObjectName("label")
        self.x_position = QtWidgets.QLineEdit(self.groupBox)
        self.x_position.setGeometry(QtCore.QRect(140, 80, 81, 24))
        self.x_position.setObjectName("x_position")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.y_position = QtWidgets.QLineEdit(self.groupBox)
        self.y_position.setGeometry(QtCore.QRect(140, 110, 81, 24))
        self.y_position.setObjectName("y_position")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 20, 231, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 81, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 91, 31))
        self.label_6.setObjectName("label_6")
        self.hours = QtWidgets.QLineEdit(self.groupBox_2)
        self.hours.setGeometry(QtCore.QRect(110, 30, 81, 24))
        self.hours.setObjectName("hours")
        self.minutes = QtWidgets.QLineEdit(self.groupBox_2)
        self.minutes.setGeometry(QtCore.QRect(110, 60, 81, 24))
        self.minutes.setObjectName("minutes")
        self.secondes = QtWidgets.QLineEdit(self.groupBox_2)
        self.secondes.setGeometry(QtCore.QRect(110, 90, 81, 24))
        self.secondes.setObjectName("secondes")
        self.mili_secondes = QtWidgets.QLineEdit(self.groupBox_2)
        self.mili_secondes.setGeometry(QtCore.QRect(110, 120, 81, 24))
        self.mili_secondes.setObjectName("mili_secondes")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 200, 261, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.label_8.setObjectName("label_8")
        self.mouse_button = QtWidgets.QComboBox(self.groupBox_3)
        self.mouse_button.setGeometry(QtCore.QRect(130, 30, 111, 25))
        self.mouse_button.setObjectName("mouse_button")
        self.mouse_button.addItem("")
        self.mouse_button.addItem("")
        self.click_type = QtWidgets.QComboBox(self.groupBox_3)
        self.click_type.setGeometry(QtCore.QRect(130, 60, 111, 25))
        self.click_type.setObjectName("click_type")
        self.click_type.addItem("")
        self.click_type.addItem("")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 200, 231, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.repeat = QtWidgets.QRadioButton(self.groupBox_4)
        self.repeat.setGeometry(QtCore.QRect(10, 20, 81, 41))
        self.repeat.setObjectName("repeat")
        self.endless = QtWidgets.QRadioButton(self.groupBox_4)
        self.endless.setGeometry(QtCore.QRect(10, 70, 111, 41))
        self.endless.setObjectName("endless")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(60, 50, 81, 31))
        self.label_9.setObjectName("label_9")
        self.times = QtWidgets.QLineEdit(self.groupBox_4)
        self.times.setGeometry(QtCore.QRect(120, 50, 81, 24))
        self.times.setObjectName("times")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(60, 320, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.start_button.setFont(font)
        self.start_button.setFlat(True)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(320, 310, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.stop_button.setFont(font)
        self.stop_button.setFlat(True)
        self.stop_button.setObjectName("stop_button")
        self.github = QtWidgets.QPushButton(self.centralwidget)
        self.github.setGeometry(QtCore.QRect(170, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        self.github.setFont(font)
        self.github.setStyleSheet("color: rgb(32, 74, 135);")
        self.github.setFlat(True)
        self.github.setObjectName("github")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ##############################################################
        # instructions added by me
        # actions
        ##############################################################
        self.default_position.clicked.connect(self.default_positionClicked)
        self.pick_position.clicked.connect(self.pick_positionClicked)
        self.endless.clicked.connect(self.endlessClicked)
        self.repeat.clicked.connect(self.repeatClicked)
        self.github.clicked.connect(self.githubClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Mouse position"))
        self.default_position.setText(_translate(
            "MainWindow", "Default mouse position"))
        self.pick_position.setText(_translate("MainWindow", "Pick position"))
        self.label.setText(_translate("MainWindow", "X Position"))
        self.label_2.setText(_translate("MainWindow", "Y Position"))
        self.groupBox_2.setTitle(_translate(
            "MainWindow", "Time delay between clicks"))
        self.label_3.setText(_translate("MainWindow", "Hours"))
        self.label_4.setText(_translate("MainWindow", "Minutes"))
        self.label_5.setText(_translate("MainWindow", "Secondes"))
        self.label_6.setText(_translate("MainWindow", "Mili Seconds"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Click options"))
        self.label_7.setText(_translate("MainWindow", "Mouse button"))
        self.label_8.setText(_translate("MainWindow", "Click type"))
        self.mouse_button.setItemText(
            0, _translate("MainWindow", "Left button"))
        self.mouse_button.setItemText(
            1, _translate("MainWindow", "Right button"))
        self.click_type.setItemText(
            0, _translate("MainWindow", "Single click"))
        self.click_type.setItemText(
            1, _translate("MainWindow", "Double click"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Click times"))
        self.repeat.setText(_translate("MainWindow", "Repeat"))
        self.endless.setText(_translate("MainWindow", "Until stoped"))
        self.label_9.setText(_translate("MainWindow", "Times"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.github.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.github.setText(_translate("MainWindow", "Github.com"))

        #############################################################
    # methodes added by me
    ##############################################################

    def default_positionClicked(self):
        """When clicking the position defalt button."""
        self.x_position.setEnabled(False)
        self.y_position.setEnabled(False)
        self.label.setEnabled(False)
        self.label_2.setEnabled(False)

    def pick_positionClicked(self):
        """When clicking the position user defined button."""
        self.x_position.setEnabled(True)
        self.y_position.setEnabled(True)
        self.label.setEnabled(True)
        self.label_2.setEnabled(True)

    def endlessClicked(self):
        """When clicking the number of times as until stoped."""
        self.times.setEnabled(False)
        self.label_9.setEnabled(False)

    def repeatClicked(self):
        """When clicking the number of times as repeat."""
        self.times.setEnabled(True)
        self.label_9.setEnabled(True)

    def githubClicked(self):
        url = "https://github.com/HerharFares/stress-mouse"
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
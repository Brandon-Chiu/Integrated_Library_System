# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from MemberHome import Ui_MainWindow as memberhome
from CreateAccount import Ui_MainWindow as registeraccount
from ResetPassword import Ui_MainWindow as forgetpassword
from AdminHome import Ui_MainWindow as adminhome
import mysql.connector
my_db = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="RunningMan7012",
                                database="ils",
                                autocommit=True)
my_cursor = my_db.cursor()


class Ui_MainWindow(object):
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 612)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.signInBtn = QtWidgets.QPushButton(self.centralwidget)
        self.signInBtn.setGeometry(QtCore.QRect(410, 390, 241, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signInBtn.sizePolicy().hasHeightForWidth())
        self.signInBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.signInBtn.setFont(font)
        self.signInBtn.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid #536DFE;\n"
"color: white;\n"
"background-color: #536DFE;\n"
"text-align: center;\n"
"padding-bottom: 4px;")
        self.signInBtn.setObjectName("signInBtn")
        self.login_email = QtWidgets.QLineEdit(self.centralwidget)
        self.login_email.setGeometry(QtCore.QRect(410, 310, 241, 31))
        self.login_email.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid white;")
        self.login_email.setAlignment(QtCore.Qt.AlignCenter)
        self.login_email.setObjectName("login_email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 230, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.login_heroImage = QtWidgets.QLabel(self.centralwidget)
        self.login_heroImage.setGeometry(QtCore.QRect(0, 0, 1061, 600))
        self.login_heroImage.setStyleSheet("background-image: url(:/Assets/assets/Login.png);")
        self.login_heroImage.setText("")
        self.login_heroImage.setObjectName("login_heroImage")
        self.login_password = QtWidgets.QLineEdit(self.centralwidget)
        self.login_password.setGeometry(QtCore.QRect(410, 350, 241, 31))
        self.login_password.setStyleSheet("border-radius: 5px;\n"
"border: 1px solid white;")
        self.login_password.setAlignment(QtCore.Qt.AlignCenter)
        self.login_password.setObjectName("login_password")
        self.login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.registerAccountBtn = QtWidgets.QPushButton(self.centralwidget)
        self.registerAccountBtn.setGeometry(QtCore.QRect(460, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.registerAccountBtn.setFont(font)
        self.registerAccountBtn.setStyleSheet("background-color: transparent;\n"
"")
        self.registerAccountBtn.setObjectName("registerAccountBtn")
        self.forgetPasswordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.forgetPasswordBtn.setGeometry(QtCore.QRect(460, 460, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.forgetPasswordBtn.setFont(font)
        self.forgetPasswordBtn.setStyleSheet("background-color: transparent;\n"
"")
        self.forgetPasswordBtn.setObjectName("forgetPasswordBtn")
        self.login_heroImage.raise_()
        self.signInBtn.raise_()
        self.login_email.raise_()
        self.label_3.raise_()
        self.login_password.raise_()
        self.registerAccountBtn.raise_()
        self.forgetPasswordBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button assignment
        # Login button
        self.signInBtn.clicked.connect(lambda: self.show_Home_window())

        # Register Button
        self.registerAccountBtn.clicked.connect(lambda: self.show_Registration_window())

        # Forget Password Button
        self.forgetPasswordBtn.clicked.connect(lambda: self.show_ForgetPassword_window())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.signInBtn.setText(_translate("MainWindow", "Sign in"))
        self.login_email.setPlaceholderText(_translate("MainWindow", "Enter email"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Log In</p></body></html>"))
        self.login_password.setPlaceholderText(_translate("MainWindow", "Enter password"))
        self.registerAccountBtn.setText(_translate("MainWindow", "Register Account"))
        self.forgetPasswordBtn.setText(_translate("MainWindow", "Forget Password"))

    # For login
    # Check credentials
    def check_credentials(self):
        user = self.login_email.text()
        password = self.login_password.text()
        my_cursor.execute("SELECT * FROM ils.libraryuser WHERE userID = %s", (user,))
        rows = my_cursor.fetchall()
        result = []
        for i in rows:
            email = i[0]
            userName = i[1]
            pswd = i[2]
            result.append((email, userName, pswd))
        if result == []:
            return False
        if user == result[0][0] and password == result[0][2]:
            return True
        else:
            return False

    # Chekc Admin
    def check_admin(self):
        useremail = self.login_email.text()
        my_cursor.execute("SELECT user.isAdmin 'Admin' FROM Libraryuser user WHERE user.userId = %s;", (useremail,))
        rows = my_cursor.fetchall()
        if rows[0][0] == 1:
            return True
        else:
            return False

    # Error message
    def error_popup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Wrong Userid or Password")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    # Open Member Home tab
    def show_Home_window(self):
        if self.check_credentials():
            if self.check_admin():
                self.window = QtWidgets.QMainWindow()
                details = str(self.login_email.text())
                adminhome(details,self.window,self.MainWindow)
                MainWindow.hide()
            else:
                self.window = QtWidgets.QMainWindow()
                details = str(self.login_email.text())
                memberhome(details,self.window,self.MainWindow)
                MainWindow.hide()
        else:
            self.error_popup()

    # For Account Registration
    def show_Registration_window(self):
        self.window = QtWidgets.QMainWindow()
        registeraccount(self.window)

    # For resetting password
    def show_ForgetPassword_window(self):
        self.window = QtWidgets.QMainWindow()
        forgetpassword(self.window)
import background_image


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    ui.MainWindow.show()
    sys.exit(app.exec_())
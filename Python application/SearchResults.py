# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchResults.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from BookResult import Ui_MainWindow as bookresult



class Ui_MainWindow(object):
    def __init__(self,MainWindow,books,emailid,memberHome):
        self.path = "C:/Users/brand/Documents/BT2102/Project/GRP_10_AS1_Final/Book covers/"
        self.memberHome = memberHome
        self.books = books
        self.emailid = emailid
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.load_results(books)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 612)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 40, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.login_heroImage = QtWidgets.QLabel(self.centralwidget)
        self.login_heroImage.setGeometry(QtCore.QRect(0, 0, 1061, 600))
        self.login_heroImage.setStyleSheet("background-image: url(:/Assets/assets/SearchResult.png);")
        self.login_heroImage.setText("")
        self.login_heroImage.setObjectName("login_heroImage")
        self.borrowTable = QtWidgets.QTableWidget(self.centralwidget)
        self.borrowTable.setGeometry(QtCore.QRect(30, 140, 1001, 341))
        self.borrowTable.setStyleSheet("background-color: white;\n"
"color: black;")
        self.borrowTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.borrowTable.setMidLineWidth(0)
        self.borrowTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.borrowTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.borrowTable.setTabKeyNavigation(True)
        self.borrowTable.setAlternatingRowColors(False)
        self.borrowTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowTable.setShowGrid(True)
        self.borrowTable.setGridStyle(QtCore.Qt.SolidLine)
        self.borrowTable.setObjectName("borrowTable")
        self.borrowTable.setColumnCount(7)
        self.borrowTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.borrowTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(10)
        item.setFont(font)
        self.borrowTable.setHorizontalHeaderItem(6, item)
        self.borrowTable.horizontalHeader().setCascadingSectionResizes(False)
        self.borrowTable.horizontalHeader().setHighlightSections(True)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(330, 110, 391, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.reservation_cancelReservation = QtWidgets.QPushButton(self.centralwidget)
        self.reservation_cancelReservation.setGeometry(QtCore.QRect(820, 510, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reservation_cancelReservation.setFont(font)
        self.reservation_cancelReservation.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"background-color: white;\n"
"color: black;\n"
"font-weight: bold;\n"
"padding-bottom: 2px;\n"
"")
        self.reservation_cancelReservation.setObjectName("reservation_cancelReservation")
        self.login_heroImage.raise_()
        self.label_3.raise_()
        self.borrowTable.raise_()
        self.line_2.raise_()
        self.reservation_cancelReservation.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Table click assignment
        self.borrowTable.cellDoubleClicked.connect(lambda: self.cell_clicked())
        self.reservation_cancelReservation.clicked.connect(lambda: self.backtohome())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Search Result"))
        self.borrowTable.setSortingEnabled(False)
        item = self.borrowTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book"))
        item = self.borrowTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Book ID"))
        item = self.borrowTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Book Title"))
        item = self.borrowTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ISBN"))
        item = self.borrowTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Author"))
        item = self.borrowTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Availability"))
        item = self.borrowTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Expected due date"))
        self.reservation_cancelReservation.setText(_translate("MainWindow", "Back to Search"))

    # Button functions

    def cell_clicked(self):
        indexes = self.borrowTable.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            rowtext = []
            for column in range(self.borrowTable.columnCount()):
                if column == 0:
                    continue
                else:
                    rowtext.append(self.borrowTable.item(row, column).text())
            self.window = QtWidgets.QMainWindow()
            bookresult(self.window,rowtext[0],self.emailid,self.memberHome,False)
            self.MainWindow.close()

    def backtohome(self):
        self.memberHome.load_borrow_books(self.emailid)
        self.memberHome.load_reservations(self.emailid)
        self.memberHome.MainWindow.show()
        self.MainWindow.close()

    # Loading of data
    def load_results(self,result):

        # Loading of data into table
        self.borrowTable.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.borrowTable.insertRow(row_number)
            self.borrowTable.setRowHeight(row_number,200)
            for col_num, data in enumerate(row_data):
                if col_num == 0:
                    if str(data) != "":
                        pixmap = QtGui.QPixmap(self.path + str(data))
                        image_label = QtWidgets.QLabel()
                        image_label.setPixmap(pixmap)
                        self.borrowTable.setCellWidget(row_number,col_num,image_label)
                elif col_num == 4:
                    result = ""
                    for i in range(len(data)):
                        if i == len(data) - 1:
                            result += data[i]
                        elif data[i] == "":
                            continue
                        else:
                            result += (data[i] + ", ")
                    self.borrowTable.setItem(row_number, col_num, QtWidgets.QTableWidgetItem(str(result)))
                else:
                    self.borrowTable.setItem(row_number, col_num, QtWidgets.QTableWidgetItem(str(data)))

        # Table Formatting
        header = self.borrowTable.horizontalHeader()
        header.setDefaultAlignment(QtCore.Qt.AlignCenter)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        self.borrowTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)


import background_image




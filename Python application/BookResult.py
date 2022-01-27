# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookResult.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import mysql.connector
from PyMongo import *

my_db = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="RunningMan7012",
                                database="ils",
                                autocommit=True)

my_cursor = my_db.cursor()

class Ui_MainWindow(object):
    def __init__(self,MainWindow,bookid,emailid,memberHome,from_memberhome):
        self.from_memberhome = from_memberhome
        self.memberHome = memberHome
        self.emailid = emailid
        self.bookid = str(bookid)
        self.listbookid = []
        self.listbookid.append(int(bookid))
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.details = extract_details(self.listbookid)
        words = self.tester(self.details,"_id")
        self.bookResult_bookID.setText("BookID: " + str(words))
        words = self.tester(self.details, "title")
        self.bookResult_bookTitle.setText(str(words))
        words = self.tester(self.details, "isbn")
        self.book_isbn.setText("ISBN : " + str(words))
        words = self.tester(self.details, "shortDescription")
        self.Short.setText(str(words))
        self.Short.setReadOnly(True)
        words = self.tester(self.details, "longDescription")
        self.Long.setText(str(words))
        self.Long.setReadOnly(True)
        words = self.tester(self.details, "status")
        self.bookResult_status.setText("Status: " + str(words))
        words = self.tester(self.details, "authors")
        self.bookResult_authors.setText("Authors: " + self.formatting(words))
        words = self.tester(self.details, "categories")
        self.bookResult_category.setText("Categories: " + self.formatting(words))
        if self.tester(self.details, "thumbnailUrl") != " ":
            image = QtGui.QImage()
            words = self.tester(self.details, "thumbnailUrl")
            image.loadFromData(requests.get(words).content)
            image_label = self.bookResult_bookImage
            image_label.setPixmap(QtGui.QPixmap.fromImage(image))
            image_label.show()

        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 612)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 10, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.bookResult_heroImage = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_heroImage.setGeometry(QtCore.QRect(0, 0, 1061, 600))
        self.bookResult_heroImage.setStyleSheet("background-image: url(:/Assets/assets/BookResults.png);")
        self.bookResult_heroImage.setText("")
        self.bookResult_heroImage.setObjectName("bookResult_heroImage")
        self.bookResult_bookImage = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_bookImage.setGeometry(QtCore.QRect(180, 120, 150, 188))
        self.bookResult_bookImage.setStyleSheet("border: 1px solid #000;")
        self.bookResult_bookImage.setText("")
        self.bookResult_bookImage.setObjectName("bookResult_bookImage")
        self.search_searchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.search_searchBtn.setGeometry(QtCore.QRect(10, 540, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_searchBtn.setFont(font)
        self.search_searchBtn.setStyleSheet("border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color:  #536DFE;\n"
"box-shadow: 5px 10px #888888;\n"
"\n"
"")
        self.search_searchBtn.setObjectName("search_searchBtn")
        self.bookResult_bookTitle = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_bookTitle.setGeometry(QtCore.QRect(350, 100, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookResult_bookTitle.setFont(font)
        self.bookResult_bookTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bookResult_bookTitle.setObjectName("bookResult_bookTitle")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(340, 70, 391, 16))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("background: transparent;\n"
"border-bottom: 2px solid black;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.book_isbn = QtWidgets.QLabel(self.centralwidget)
        self.book_isbn.setGeometry(QtCore.QRect(350, 160, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.book_isbn.setFont(font)
        self.book_isbn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.book_isbn.setObjectName("book_isbn")
        self.bookResult_bookID = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_bookID.setGeometry(QtCore.QRect(350, 190, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookResult_bookID.setFont(font)
        self.bookResult_bookID.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bookResult_bookID.setObjectName("bookResult_bookID")
        self.bookResult_status = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_status.setGeometry(QtCore.QRect(350, 220, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookResult_status.setFont(font)
        self.bookResult_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bookResult_status.setObjectName("bookResult_status")
        self.reserveBookBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reserveBookBtn.setGeometry(QtCore.QRect(730, 540, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.reserveBookBtn.setFont(font)
        self.reserveBookBtn.setStyleSheet("border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color:  #536DFE;\n"
"box-shadow: 5px 10px #888888;\n"
"\n"
"")
        self.reserveBookBtn.setObjectName("reserveBookBtn")
        self.borrowBookBtn = QtWidgets.QPushButton(self.centralwidget)
        self.borrowBookBtn.setGeometry(QtCore.QRect(580, 540, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.borrowBookBtn.setFont(font)
        self.borrowBookBtn.setStyleSheet("border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color:  #536DFE;\n"
"box-shadow: 5px 10px #888888;\n"
"\n"
"")
        self.borrowBookBtn.setObjectName("borrowBookBtn")
        self.bookResult_category = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_category.setGeometry(QtCore.QRect(350, 280, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookResult_category.setFont(font)
        self.bookResult_category.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bookResult_category.setObjectName("bookResult_category")
        self.bookResult_authors = QtWidgets.QLabel(self.centralwidget)
        self.bookResult_authors.setGeometry(QtCore.QRect(350, 250, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookResult_authors.setFont(font)
        self.bookResult_authors.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.bookResult_authors.setObjectName("bookResult_authors")
        self.Short = QtWidgets.QTextEdit(self.centralwidget)
        self.Short.setGeometry(QtCore.QRect(180, 320, 641, 61))
        font = QtGui.QFont()
        font.setFamily("Raleway Medium")
        self.Short.setFont(font)
        self.Short.setObjectName("Short")
        self.Long = QtWidgets.QTextEdit(self.centralwidget)
        self.Long.setGeometry(QtCore.QRect(180, 390, 641, 131))
        font = QtGui.QFont()
        font.setFamily("Raleway Medium")
        self.Long.setFont(font)
        self.Long.setObjectName("Long")
        self.bookResult_heroImage.raise_()
        self.label_3.raise_()
        self.bookResult_bookImage.raise_()
        self.search_searchBtn.raise_()
        self.bookResult_bookTitle.raise_()
        self.line.raise_()
        self.book_isbn.raise_()
        self.bookResult_bookID.raise_()
        self.bookResult_status.raise_()
        self.reserveBookBtn.raise_()
        self.borrowBookBtn.raise_()
        self.bookResult_category.raise_()
        self.bookResult_authors.raise_()
        self.Short.raise_()
        self.Long.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button Assignment
        self.search_searchBtn.clicked.connect(lambda: self.back_to_search_results())
        self.borrowBookBtn.clicked.connect(lambda: self.borrowing_book())
        self.reserveBookBtn.clicked.connect(lambda: self.reserving_book())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Book Result"))
        self.search_searchBtn.setText(_translate("MainWindow", "Back"))
        self.bookResult_bookTitle.setText(_translate("MainWindow", "Book Title"))
        self.book_isbn.setText(_translate("MainWindow", "ISBN"))
        self.bookResult_bookID.setText(_translate("MainWindow", "BookID"))
        self.bookResult_status.setText(_translate("MainWindow", "Status"))
        self.reserveBookBtn.setText(_translate("MainWindow", "Reserve Book"))
        self.borrowBookBtn.setText(_translate("MainWindow", "Borrow Book"))
        self.bookResult_category.setText(_translate("MainWindow", "Categories"))
        self.bookResult_authors.setText(_translate("MainWindow", "Authors"))
        self.Short.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Raleway Medium\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Long.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Raleway Medium\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


    # Button Function
    def back_to_search_results(self):
        if self.from_memberhome == True:
            self.memberHome.load_borrow_books(self.emailid)
            self.memberHome.load_reservations(self.emailid)
            self.MainWindow.close()
        else:
            self.memberHome.simple_search_button()
            self.MainWindow.close()

    def borrowing_book(self):
        if self.test_borrow_cap(self.emailid):
            if self.test_fines(self.emailid):
                if self.test_overdue_books(self.emailid):
                    if self.test_outofCirculation(self.bookid):
                        if self.test_borrowed(self.bookid):
                            if self.test_reserved(self.bookid):
                                my_cursor.execute("INSERT INTO Borrow (userId, bookId, dueDate, extendDueDate, returnDate) "
                                                  "VALUES (%s, %s, DATE_ADD(CURRENT_TIMESTAMP, interval 4 week), 0, null);",(self.emailid,self.bookid))
                                my_db.commit()
                                self.book_borrowed()
                            else:
                                if self.test_reserved_by_me(self.emailid,self.bookid):
                                    my_cursor.execute("INSERT INTO Borrow (userId, bookId, dueDate, extendDueDate, returnDate) "
                                                      "VALUES (%s, %s, DATE_ADD(CURRENT_TIMESTAMP, interval 4 week), 0, null);",
                                                      (self.emailid, self.bookid))
                                    my_db.commit()
                                    my_cursor.execute("DELETE FROM Reserve WHERE userId = %s AND bookId = %s;",
                                                      (self.emailid, self.bookid))
                                    my_db.commit()
                                    self.book_borrowed()
                                else:
                                    self.error_popup_reserved()
                        else:
                            self.error_popup_borrowed()
                    else:
                        self.error_out_of_circulation()
                else:
                    self.error_overdue_books()
            else:
                self.error_popup_fine_found()
        else:
            self.book_cap()

    def reserving_book(self):
        if self.test_reserve_cap(self.emailid):
            if self.test_fines(self.emailid):
                if self.test_overdue_books(self.emailid):
                    if self.test_outofCirculation(self.bookid):
                        if self.test_borrowed_by_me(self.emailid,self.bookid):
                            if self.test_reserved(self.bookid):
                                my_cursor.execute("INSERT INTO Reserve (userId, bookId, reserveDate) "
                                                  "VALUES (%s, %s, CURRENT_TIMESTAMP());",
                                                  (self.emailid, self.bookid))
                                my_db.commit()
                                self.book_reserved()
                            else:
                                self.error_popup_reserved()
                        else:
                            self.error_reserve_borrowed_by_you()
                    else:
                        self.error_out_of_circulation()
                else:
                    self.error_overdue_books()
            else:
                self.error_popup_fine_found()
        else:
            self.reserve_cap()


    # Miscellaneous
    # formatting of lists
    def formatting(self,thing):
        result = ""
        for i in range(len(thing)):
            if i == len(thing) - 1:
                result += thing[i]
            elif thing[i] == "":
                continue
            else:
                result += (thing[i] + ", ")
        return result

    # check for empty image file
    def tester(self,testsubject,condition):
        try:
            testsubject[condition]
        except KeyError:
            return " "
        else:
            return (testsubject[condition][0])

    # testers
    def test_borrow_cap(self,useremail):
        my_cursor.execute("SELECT bookId 'Book ID' FROM Borrow WHERE userId = %s;",(useremail,))
        rows = my_cursor.fetchall()
        if len(rows) >= 4:
            return False
        else:
            return True

    def test_reserve_cap(self,useremail):
        my_cursor.execute("SELECT bookId 'Book ID' FROM Reserve WHERE userId = %s;",(useremail,))
        rows = my_cursor.fetchall()
        if len(rows) >= 4:
            return False
        else:
            return True

    def test_fines(self, useremail):
        # Mysql data load
        my_cursor.execute("SELECT fe.amount 'Amount' FROM fine fe WHERE fe.userId = %s;", (useremail,))
        rows = my_cursor.fetchall()
        if rows != []:
            return False
        else:
            return True

    def test_borrowed(self,book):
        my_cursor.execute("SELECT userId 'User ID' FROM Borrow WHERE bookId = %s;", (book,))
        rows = my_cursor.fetchall()
        if rows != []:
            return False
        else:
            return True

    def test_reserved(self,book):
        my_cursor.execute("SELECT userId 'User ID' FROM Reserve WHERE bookId = %s;", (book,))
        rows = my_cursor.fetchall()
        if rows != []:
            return False
        else:
            return True

    def test_overdue_books(self,useremail):
        # Mysql data load
        my_cursor.execute("SELECT userId 'User ID' FROM Borrow WHERE userId = %s AND dueDate < CURRENT_TIMESTAMP;", (useremail,))
        rows = my_cursor.fetchall()
        if rows != []:
            return False
        else:
            return True

    def test_reserved_by_me(self,useremail,bookidd):
        my_cursor.execute("SELECT bookId 'Book ID' FROM Reserve WHERE userId = %s;", (useremail,))
        rows = my_cursor.fetchall()
        books = []
        for i in rows:
            books.append(str(i[0]))
        if bookidd in books:
            return True
        else:
            return False

    def test_borrowed_by_me(self,useremail,bookidd):
        my_cursor.execute("SELECT bookId 'Book ID' FROM Borrow WHERE userId = %s;", (useremail,))
        rows = my_cursor.fetchall()
        books = []
        for i in rows:
            books.append(str(i[0]))
        if bookidd in books:
            return False
        else:
            return True

    def test_outofCirculation(self,bookidd):
        my_cursor.execute("SELECT bookId 'Book ID', outOfCirculation 'availability' FROM book WHERE bookId = %s;", (bookidd,))
        rows = my_cursor.fetchall()
        if rows[0][1] == 1:
            return False
        else:
            return True

    # error out of circulation
    def error_out_of_circulation(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("Book is out of circulation by admin")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    # error fine
    def error_popup_fine_found(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Fine found")
        msg.setText("You still have unpaid fines")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # error borrow
    def error_popup_borrowed(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book unavailable")
        msg.setText("Book is borrowed")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # error reserve
    def error_popup_reserved(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book unavailable")
        msg.setText("Book is reserved")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # error overdue books
    def error_overdue_books(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book unavailable")
        msg.setText("You have Overdue books")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # Reserve book borrowed by me
    def error_reserve_borrowed_by_you(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("Book is borrowed by you")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # Book borrowed!
    def book_borrowed(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("Book has been successfully borrowed!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # Book reserved!
    def book_reserved(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("Book has been successfully reserved!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.exec_()

    # Borrow limit
    def book_cap(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("You have reached your borrow limit")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()

    # Reserve limit
    def reserve_cap(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Book")
        msg.setText("You have reached your reserve limit")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.exec_()


    # update search results
    def update_search_results(self):
        texts = simple_search(self.search_term)
        allbookids = []
        for i in texts:
            allbookids.append(i[0])
        allauthors = extract_authors(allbookids)
        for i in range(len(texts)):
            texts[i].append(allauthors[i][1])
        words = []
        images = []
        for i in texts:
            words.append(i[:3] + [i[4]])
            images.append(i[3])
        my_cursor.execute(
            'SELECT bk.bookId "Book ID", IF(EXISTS(SELECT * FROM Borrow bw WHERE bw.bookID = bk.bookID), "No", "Yes") AS "Availability"FROM Book bk;')
        availability = my_cursor.fetchall()
        for i in words:
            for t in availability:
                if i[0] == t[0]:
                    i.append(t[1])
                    break
        result = []
        for i in range(len(words)):
            result.append([images[i], ] + words[i])
        return result


import background_image





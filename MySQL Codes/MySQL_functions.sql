### SHOW BOOKS THAT MEMBER BORROW ###
# Variables in Python = enteredUserId
SELECT bk.bookId "Book ID", bk.title "Title", bk.authors "Authors", bk.isbn "ISBN", bw.dueDate "Due Date"
FROM Book bk RIGHT JOIN Borrow bw USING (bookID)
WHERE bw.userId = enteredUserId;


### SHOW BOOKS THAT MEMBER RESERVED ###
# Variables in Python = enteredUserId
SELECT bk.bookId "Book ID", bk.title "Title", bk.authors "Authors", bk.isbn "ISBN", IF(EXISTS (SELECT * FROM borrow bw WHERE bk.bookId = bw.bookId), "No", "Yes") AS "Availability"
FROM Book bk RIGHT JOIN Reserve re USING (bookID)
WHERE re.userId = enteredUserId;


### ADMIN VIEW OF ALL UNPAID FINES ###
SELECT fe.userId "User Id", lr.userName "User Name", fe.amount "Amount"
FROM Fine fe LEFT JOIN Libraryuser lr USING (userID);


### ADMIN VIEW OF ALL BORROWED BOOKS ###
SELECT lr.userID "Email", lr.userName "Username", bk.bookId "Book ID", bk.title "Title", bk.authors "Authors", bk.isbn "ISBN", bw.dueDate "Due Date", IF(bw.extendDueDate = 1, "Yes", "No") AS "Extended Due Date"
FROM Borrow bw LEFT JOIN Book bk USING (bookID)
LEFT JOIN LibraryUser lr USING (userID);


### ADMIN VIEW OF ALL RESERVED BOOKS ###
SELECT lr.userID "Email", lr.userName "Username", bk.bookId "Book ID", bk.title "Title", bk.authors "Authors", bk.isbn "ISBN", re.reserveDate "Reserve Date"
FROM Reserve re LEFT JOIN Book bk USING (bookID)
LEFT JOIN LibraryUser lr USING (userID);


### SEARCH RESULTS (MySQL) ###
# To be combined with MongoDB search results
SELECT bk.bookId "Book ID", IF(EXISTS(SELECT * FROM Borrow bw WHERE bw.bookID = bk.bookID)
OR bk.outOfCirculation = 1, "No", "Yes") AS "Availability" FROM Book bk;

# To extract due date
SELECT bookId "Book Id", dueDate "Due Date"
FROM Borrow;


### SHOW FINE AMOUNT FOR MEMBER ###
# Variables in Python = enteredUserId
SELECT amount "Amount"
FROM Fine
WHERE userId = enteredUserId;


### SHOW DUE DATE FOR BOOK ###
# Variables in python: enteredBookId;
SELECT dueDate " Due Date"
FROM Borrow
WHERE bookId = enteredBookId;


### CHANGE/RESET PASSWORD FOR USER ###
# Variables in Python = enteredUserId, enteredPassword
# Step 1 = CHECK IF USERID EXIST
# Instructions for Python = If empty, return error. Else, run UPDATE LIBRARYUSER TABLE.
SELECT userId "User ID"
FROM LibraryUser
WHERE userID = enteredUserId;

# Step 2 = UPDATE LIBRARYUSER TABLE
UPDATE LibraryUser
SET password = enteredPassword
WHERE userId = enteredUserId;


### BORROW BOOK ###
# Variables in Python = enteredUserId, enteredBookId
# Step 1 = CHECK IF BOOK IS BORROWED
# Instructions for Python = If not empty, return error. Else, run CHECK IF BOOK IS RESERVED.
SELECT userId "User ID"
FROM Borrow
WHERE bookId = enteredBookId;

# Step 2 = CHECK IF USER HAS FINE
# Instructions for Python = If user has fine, return error. Else, continue.

# Step 3 = CHECK IF USER HAS OVERDUE BOOK
SELECT userId "User ID"
FROM Borrow
WHERE userId = enteredUserId AND dueDate < CURRENT_TIMESTAMP;

# Step 4 = CHECK IF USER ALREADY BORROWED 4 BOOKS
# Instructions for Python = If there are 4 books, return error. Else, continue.
SELECT bookId "Book ID"
FROM Borrow
WHERE userId = enteredUserId;

# Step 5 = CHECK IF BOOK IS RESERVED
# Instructions for Python = If empty, run BORROW BOOK. Else, check in Python if userId is current user. If yes, run INSERT INTO BORROW TABLE. Else, return error.
SELECT userId "User ID"
FROM Reserve
WHERE bookId = enteredBookId;

# Step 6 = INSERT INTO BORROW TABLE
INSERT INTO Borrow (userId, bookId, dueDate, extendDueDate, returnDate)
VALUES (enteredUserId, enteredBookId, DATE_ADD(CURRENT_TIMESTAMP, interval 4 week), 0, null);


### CREATE ACCOUNT ###
# Variables in Python = enteredUserId, enteredUserName, enteredPassword, enteredIsAdmin
# Step 1 = CHECK IF USERID ALREADY EXIST
# Instructions for Python = If not empty, return error. Else, run INSERT INTO LIBRARYUSER TABLE.
SELECT userId "User ID"
FROM LibraryUser
WHERE userId = enteredUserId;

# Step 2 = INSERT INTO LIBRARYUSER TABLE
INSERT INTO LibraryUser (userID, userName, password, isAdmin)
VALUES (enteredUserId, enteredUserName, enteredPassword, enteredIsAdmin);


### EXTEND DUE DATE ###
# Variables in Python = enteredUserId, enteredBookId
# Step 1 = CHECK IF DUE DATE HAS BEEN EXTENDED
# Instructions for Python = If 1, return error. Else (0), run UPDATE IN BORROW TABLE.
SELECT extendDueDate "Extend Due Date"
FROM Borrow
WHERE userId = enteredUserId AND bookId = enteredBookId;

# Step 2 = CHECK IF USER HAS FINE
# Instructions for Python = If user has fine, return error. Else, continue.

# Step 3 = CHECK IF USER HAS OVERDUE BOOK
SELECT userId "User ID"
FROM Borrow
WHERE userId = enteredUserId AND dueDate < CURRENT_TIMESTAMP;

# Step 4 = CHECK IF BOOK RESERVED ALREADY.
# Instructions for Python = If not empty, return error. Else, run UPDATE IN BORROW TABLE.
SELECT userId "User ID"
FROM Reserve
WHERE bookId = enteredBookId;

# Step 5 = UPDATE IN BORROW TABLE
UPDATE Borrow
SET extendDueDate = 1, dueDate = DATE_ADD(dueDate, interval 4 week)
WHERE userId = enteredUserId AND bookId = enteredBookId;


### RESERVE BOOK ###
# Variables in Python = enteredUserId, enteredBookId
# Step 1 = CHECK IF BOOK RESERVED ALREADY.
# Instructions for Python = If not empty, return error. Else, run CHECK IF USER ALREADY RESERVED 4 BOOKS.
SELECT userId "User ID"
FROM Reserve
WHERE bookId = enteredBookId;

# Step 2 = CHECK IF USER HAS FINE
# Instructions for Python = If user has fine, return error. Else, continue.

# Step 3 = CHECK IF USER HAS OVERDUE BOOK
SELECT userId "User ID"
FROM Borrow
WHERE userId = enteredUserId AND dueDate < CURRENT_TIMESTAMP;

# Step 4 = CHECK IF USER ALREADY RESERVED 4 BOOKS
# Instructions for Python = If there are 4 books, return error. Else, continue.
SELECT bookId "Book ID"
FROM Reserve
WHERE userId = enteredUserId;

# Step 5 = INSERT INTO RESERVE TABLE
INSERT INTO Reserve (userId, bookId, reserveDate) 
VALUES (enteredUserId, enteredBookId, CURRENT_TIMESTAMP);


### MEMBER MAKES PAYMENT ###
# Variables in Python = enteredPaidAmount, enteredUserId, enteredFineUserId, enteredBookId
# Step 1 = CHECK IF USER HAS FINE
# Instructions for Python = If 0, return error. Else, continue.

# Step 2 = INSERT INTO PAYMENT TABLE
# Instructions for Python = enteredPaidAmount should be exactly the same as in Step 1 and 3. 
INSERT INTO Payment (paidAmount, date, userId, fineUserId)
VALUES (enteredPaidAmount, CURRENT_TIMESTAMP(), enteredUserId, enteredFineUserId);

# Step 3 = DELETE FINE FROM FINE TABLE
# Instruction for Python: enteredPaidAmount should be exactly the same as in Step 1 and 2. 
DELETE FROM Fine
WHERE userId = enteredUserId;


### MEMBER BORROWS RESERVED BOOK ###
# Variables in Python = enteredUserId, enteredBookId
# Step 1 = CHECK IF USER HAS FINE
# Instructions for Python = If user has fine, return error. Else, continue.

# Step 2 = CHECK IF BOOK RESERVED BY USER
# Instructions for Python = If not empty, return error. Else, continue.
SELECT userId "User ID"
FROM Reserve
WHERE userId = enteredUserId AND bookId = enteredBookId;

# Step 3 = USER BORROWS BOOK
# Instructions for Python = Run code for borrow book.

# Step 4 = REMOVE FROM RESERVE
## Remove reservation of book from user
DELETE FROM Reserve
WHERE userId = enteredUserId AND bookId = enteredBookId;


### MEMBER RETURNS BOOK ###
# Variable in python: enteredUserId, enteredBookId
# Step 1: CHECK IF BOOK IS OVERDUE
## Instruction for python: If book is overdue, proceed to calculate and update Fine table before removing row from borrow table; Else, remove row from borrow table straight
SELECT IF(CURRENT_TIMESTAMP - dueDate > 0, "Yes", "No") "OverDue"
FROM Borrow
WHERE userId = enteredUserId and bookId = enteredBookId;

# Step 2: CALCULATE EXTRA FINE AMOUNT
SELECT DATEDIFF(CURRENT_TIMESTAMP, dueDate) * 1 "Fine Amount"
FROM Borrow
WHERE userId = enteredUserId and bookId = enteredBookId;

# Step 3: UPDATE FINE AMOUNT (calculatedAmount obtained from previous SQL query)
UPDATE Fine
SET amount = amount + calculatedAmount
WHERE userId = enteredUserId;

# Step 4: REMOVE FROM BORROW
DELETE FROM Borrow
where userId = enteredUserId and bookId = enteredUserId;


### DELETE RESERVATIONS IF USER HAS OVERDUE BOOK ###
# Variables in python: enteredUserId, enteredBookId;
# Step 1: Check if user has overdue book on initialisation. If not empty, run CANCEL ALL RESERVATION code. Else, break.
SELECT IF(CURRENT_TIMESTAMP - dueDate > 0, "Yes", "No") "OverDue"
FROM Borrow
WHERE userId = enteredUserId;

# Step 2: Cancel all reservation ONLY IF user has overdue book
DELETE FROM Reserve
WHERE userId = enteredUserId;
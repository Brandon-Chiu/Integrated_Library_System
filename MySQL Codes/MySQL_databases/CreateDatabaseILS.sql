/*
--------------------------------------------
DATA MANAGEMENT AND VISUALISATION (BT2102)
GROUP 10 BT2102 ASSIGNMENT 1
CREATION OF SQL TABLES AND FOREIGN KEYS
LAST EDITED: 27/03/2021
--------------------------------------------
*/

/* ------------- GUIDE ON RUNNING THIS SQL CODE ----------------------
1. DROP DATABASE
2. CREATE DATABASE
3. Refresh the schemas on the left side
4. If creating table contains error as "No Database Selected",
Click the RECONNECT TO DBMS icon,
(the most right icon of just below the Tools and Scripting buttons)
5. Create all the tables below
6. Alter table by adding foreign key
7. Open the other 6 POPULATE SQL FILES and run sequentially shown below :-
    1. CreateDatabaseILS
    2. POPULATE_LibraryUser
    3. POPULATE_Book
	4. POPULATE_Fine
    5. POPULATE_Payment
    6. POPULATE_Borrow
    7. POPULATE_Reserve
*/

DROP DATABASE IF EXISTS `ILS`;

CREATE DATABASE ILS;

-- Can use if need to drop the specific table for debugging purposes

DROP TABLE IF EXISTS `LibraryUser`;
DROP TABLE IF EXISTS `Fine`;
DROP TABLE IF EXISTS `Book`;
DROP TABLE IF EXISTS `Payment`;
DROP TABLE IF EXISTS `BookDetails`;
DROP TABLE IF EXISTS `Borrow`;

/*
If creating table contains error as "No Database Selected",
Click the RECONNECT TO DBMS icon,
(the most right icon of just below the Tools and Scripting buttons)
*/
CREATE TABLE LibraryUser (
userId varchar(255) NOT NULL,
userName varchar(255) NOT NULL,
password varchar(255) NOT NULL,
isAdmin bool NOT NULL, PRIMARY KEY(userId));


CREATE TABLE Book(
bookId int(11) NOT NULL,
isbn varchar(50) NULL,
title varchar(255) NOT NULL,
authors varchar(255) NULL,
categories varchar(50) NULL,
outOfCirculation bool NOT NULL,
PRIMARY KEY(bookId));
    
CREATE TABLE Reserve(
userId varchar(255) NOT NULL,
bookId int(11) NOT NULL,
reserveDate datetime NOT NULL,
PRIMARY KEY(bookId));

CREATE TABLE Payment(
transactionId int(11) NOT NULL AUTO_INCREMENT,
paidAmount decimal(15,2) NOT NULL,
`date` datetime NOT NULL,
userId varchar(255) NOT NULL,
fineUserId varchar(255) NULL,
PRIMARY KEY(transactionId));

ALTER TABLE Payment AUTO_INCREMENT = 100000;

CREATE TABLE Fine(
userId varchar(255) NOT NULL,
amount decimal(15,2) NOT NULL,
PRIMARY KEY(userId));

CREATE TABLE Borrow(
userId varchar(255) NOT NULL,
bookId int(11) NOT NULL,
dueDate datetime NOT NULL,
extendDueDate bool NOT NULL,
returnDate datetime NULL,
PRIMARY KEY(bookId));

-- Here are all the foreign key to be added into each table
ALTER TABLE Fine ADD FOREIGN KEY(userId) references LibraryUser(userId);
ALTER TABLE Payment ADD FOREIGN KEY(userId) references LibraryUser(userId);
ALTER TABLE Payment ADD FOREIGN KEY(fineUserId) references Fine(userId);
ALTER TABLE Borrow ADD FOREIGN KEY(userId) references LibraryUser(userId);
ALTER TABLE Borrow ADD FOREIGN KEY(bookId) references Book(bookId);
ALTER TABLE Reserve ADD FOREIGN KEY(bookId) references Book(bookId);
ALTER TABLE Reserve ADD FOREIGN KEY (userId) references LibraryUser(userId);


-- ONLY FOR CREATING ER DIAGRAM IN THE MYSQL
/*GUIDE ON CREATING THE DATABASE MODEL (ER Diagram by MySQL)
1. Go to Home (top left of the MySQL workbench)
2. Head to models icon (Looks like an ERD icon with relationship)
3. Click the plus icon.
4. Once you're inside, under database tab, click "Reverse Engineer"
4. Select Your Local Instance
5. Click next
6. Select the schema/database you want to create the model 
(which basically is ILS database)
7. click next until you reach the end. Then click finish
8. You should be able to view the ER Diagram

Note: You should create the SQL Database using the code below
before creating the model or else cannot create it at all LOL
*/

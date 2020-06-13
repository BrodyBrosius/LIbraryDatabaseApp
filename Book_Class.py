from Author_Class import *
import random
import pandas as pd

class Book(Author):
    def __init__(self, authorFirstName,authorLastName,authorID,bookTitle,numOfPages):
        self.authorFirstName = authorFirstName
        self.authorLastName = authorLastName
        self.authorID = authorID
        self.bookTitle = bookTitle
        self.bookID = random.randint(10000,99999)
        self.numOfPages = numOfPages
        self.currentStatus = "CHECKED IN"
        self.authorFullName = authorFirstName + " " + authorLastName

    
    def getAuthorFirstName(self):
        return self.authorFirstName
    
    def getAuthorLastName(self):
        return self.authorLastName

    def getAuthorID(self):
        return self.authorID

    def getBookTitle(self):
        return self.bookTitle
    
    def getBookID(self):
        return self.bookID

    def getNumOfPages(self):
        return self.numOfPages
    
    def getCurrentStatus(self):
        return self.currentStatus
    
    def setCurrentStatus(self,currentStatus):
        self.currentStatus = currentStatus
    
    def getAuthorFullName(self):
        return self.authorFullName
        
    
    

   

    @staticmethod
    def editBookStatus(self):
        editBookConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = editBookConn.cursor()
        inputBookID = input("What is the ID of the book whose status you'd like to change?")
        inputStatusChange = raw_input("What is the status you would like to change? Acceptable inputs are: Lost, Damaged, Checked-out, Checked-in.")

        editBookConn.execute("UPDATE BOOK \
                                SET CurrentStatus = ? \
                                WHERE BookID = ?",
                                (str(inputStatusChange),inputBookID))
        editBookConn.commit()

    @staticmethod
    def removeBookFromDatabase(self):
        delBookConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = delBookConn.cursor()
        inputBookID = input("What is the ID of the book whose status you'd like to remove?")
        delBookConn.execute("DELETE FROM BOOK \
                                WHERE BookID = ?",
                                (int(inputBookID),))
        delBookConn.commit()
        


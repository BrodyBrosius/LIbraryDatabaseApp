from Author_Class import *

class Book(Author):
    def __init__(self, authorFirstName,authorLastName,authorID,bookTitle,bookID,numOfPages,currentStatus):
        self.authorFirstName = authorFirstName
        self.authorLastName = authorLastName
        self.authorID = authorID
        self.bookTitle = bookTitle
        self.bookID = bookID
        self.numOfPages = numOfPages
        self.currentStatus = currentStatus

    
    def getAuthor(self):
        return self.Author

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
        
    @staticmethod
    def addBookToDatabase():
        print("Please provide the AuthorID for the author of the book.")
        bookInputAuthorID = raw_input("\n Author ID:")

        newBookConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        newBookConn.execute("INSERT INTO BOOK (BookID,AuthorID,Title,NumOfPages,CurrentStatus)   \
                            VALUES (?,?,?,?,?)", (givenBookID, givenBookAuthorID, givenBookTitle,givenBookPages,givenBookStatus))
        newBookConn.commit()



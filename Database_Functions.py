import sqlite3
from sqlite3 import Error
import os
from Author_Class import *


class DatabaseFunctions():

    @staticmethod
    def create_connection(db_file):
        """ create a database connection to the SQLite database
        specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        print("CONSOLE LOG: Connected to database successfully.")
        return conn

    @staticmethod
    def create_table(conn,create_table_sql):
        global e
        e = Error
        """create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:d
        print(e)
    @staticmethod
    def addAuthorToDatabase(firstName,lastName):
        current_working_directory = os.getcwd()
        current_working_directory_and_Users_DB_file = os.path.join(current_working_directory,'Users.db')
        current_working_directory_and_Library_DB_file = os.path.join(current_working_directory, 'Library.db')
        newAuthConn = DatabaseFunctions.create_connection(current_working_directory_and_Library_DB_file)
        cur = newAuthConn.cursor()
        print("Checking if Author is presently inside database...")
        cur.execute("SELECT * FROM AUTHOR \
                        WHERE FirstName = ?  \
                        AND LastName = ?",
                        (str(firstName),str(lastName)))
        result = cur.fetchone()
        if(result == None):
            print("Success! No conflicts detected.")
            newAuthor = Author(firstName,lastName)
            fullName = newAuthor.getFullName()
            cur.execute("INSERT INTO AUTHOR (AuthorID,FirstName,LastName)   \
                     VALUES (?,?,?)", (newAuthor.getAuthorID(), str(firstName), str(lastName)))
            newAuthConn.commit()
        else:
            print("Error! Couldnt verify author database. They may already exist in the database.")

    @staticmethod
    def addBookToDatabase(self,bookID,authorID,title,numOfPages,currentStatus,authorFullName):
            newBookConn = DatabaseFunctions.create_connection(r"/home/masonc/Documents/library database app/Library.db")
            newBookConn.execute("INSERT INTO BOOK (BookID,AuthorID,Title,NumOfPages,CurrentStatus,AuthorFullName)   \
                                VALUES (?,?,?,?,?,?)", (int(bookID), int(authorID), str(title),
                                int(numOfPages),str(currentStatus),str(authorFullName)))
            newBookConn.commit()

    @staticmethod
    def displayBookTable(self):
        bookConn = DatabaseFunctions.create_connection(r"/home/masonc/Documents/library database app/Library.db")
        print pd.read_sql_query("SELECT * FROM BOOK",bookConn)
    
    @staticmethod
    def editAuthorInDatabase(AuthorID):
        inputtedID = AuthorID
        int(inputtedID)
        newAuthConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = newAuthConn.cursor()
        print("Selecting author...")
        cur.execute("SELECT * FROM AUTHOR \
                        WHERE AuthorID = ?",  \
                        (inputtedID,))
        result = cur.fetchone()
        if(result == None):
            print("Error! Could not find Author")
        else:
            print("Success! Author found!")
            print(result)
            newInput = raw_input("Is this the author entry you wanted to edit? y/n")
            if(newInput == 'y'):
                newInputTwo = raw_input("You can change the author's first or last name, which would you like to change? Input 'first' or 'last'.")
                if(newInputTwo == 'first'):
                    firstNameChange = raw_input("Please input the new first name!")
                    newAuthConn.execute("UPDATE AUTHOR \
                                SET FirstName = ? \
                                WHERE AuthorID = ?",
                                (str(firstNameChange),inputtedID))
                    newAuthConn.commit()
                elif(newInputTwo == 'last'):
                    lastNameChange = raw_input("Please input the new last name!")
                    newAuthConn.execute("UPDATE AUTHOR \
                                SET LastName = ? \
                                WHERE AuthorID = ?",
                                (str(lastNameChange),inputtedID))
                    newAuthConn.commit()
                else:
                    print("Error!")
            elif(newInput == 'n'):
                print("Exiting to main menu...")
            else:
                print("Invalid input, exiting to main menu. Remember to input exactly 'y' or 'n'. The input is case sensitive.")

    @staticmethod
    def createNewUsersDatabase(current_working_directory_and_Users_DB_file):
            userConn = DatabaseFunctions.create_connection(current_working_directory_and_Users_DB_file)
            sql_create_users_table = """ CREATE TABLE IF NOT EXISTS USERS (
                                        UserID      INT PRIMARY KEY,
                                        UserName    TEXT,
                                        Pass        TEXT
                                    );"""
            DatabaseFunctions.create_table(userConn,sql_create_users_table)
            userConn.commit()
            print("CONSOLE LOG: New users database and accompanying table completed.")
    @staticmethod
    def createNewLibraryDatabase(current_working_directory_and_Library_DB_file):
            libConn = DatabaseFunctions.create_connection(current_working_directory_and_Library_DB_file)
            sql_create_authors_table = """ CREATE TABLE IF NOT EXISTS AUTHOR (
                                            AuthorID    INT PRIMARY KEY,
                                            FirstName   VARCHAR,
                                            LastName    VARCHAR
                                        );"""
            sql_create_books_table = """CREATE TABLE IF NOT EXISTS BOOK (
                                            BookID          INT PRIMARY KEY,
                                            AuthorID        INT REFERENCES AUTHOR(AuthorID),
                                            Title           VARCHAR,
                                            NumOfPages      INT,
                                            CurrentStatus   VARCHAR,
                                            AuthorFullName  VARCHAR
                                        );"""
            DatabaseFunctions.create_table(libConn, sql_create_authors_table)
            DatabaseFunctions.create_table(libConn, sql_create_books_table)
            libConn.commit()

            print("CONSOLE LOG: New Library database and accompanying tables completed.")













    


    
    

    
    @staticmethod
    def removeAuthorFromDatabase(AuthorID):
        print("FEATURE COMING SOON") #Need more rsrch on deletion methods in SQL
    
    @staticmethod
    def displayAuthorTable(self):
        authConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        print pd.read_sql_query("SELECT * FROM AUTHOR",authConn)





    @staticmethod
    def checkIfAuthorIDAlreadyExists(self,authorID):
        givenAuthorID = authorID
        authConn = DatabaseFunctions.create_connection(r"/home/masonc/Documents/library database app/Library.db")
        cur = authConn.cursor()
        cur.execute("SELECT * FROM AUTHOR \
                    WHERE AuthorID = ?",
                    (givenAuthorID,))
        result = cur.fetchone()
        if(result == None):
            return False
        else:
            return True
      

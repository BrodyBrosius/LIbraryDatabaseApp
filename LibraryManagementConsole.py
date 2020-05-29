#Command line driven, library tracking database, CRUD
from Author_Class import *
from Book_Class import *
from Database_Functions import *
from User_Class import *
from sqlalchemy import *
import pandas as pd
import os.path
import sys

class libraryManagementConsole():
    def __init__(self,currentlyActiveUser):
        

        print("Hello! Welcome to Library Management 1.0! You can use this console to manage your library of books!")
        
        if(os.path.exists("/home/masonc/Documents/library database app/Users.db") and os.path.exists("/home/masonc/Documents/library database app/Library.db")):
            self.createNewAccountOrLogin()

        elif(not os.path.exists("/home/masonc/Documents/library database app/Users.db") and os.path.exists("/home/masonc/Documents/library database app/Library.db")):
            createNewDbResponse = raw_input("There appears to be a Library Database already present but no Users database. Create one now?")
            if(createNewDbResponse == 'y'):
                self.createNewUsersDatabase()

        
        elif(os.path.exists("/home/masonc/Documents/library database app/Users.db") and (not os.path.exists("/home/masonc/Documents/library database app/Library.db"))):
            createNewDbResponse = raw_input("There appears to be a Users database but no Library. Create one now?")
            if(createNewDbResponse == 'y'):
                self.createNewLibraryDatabase()

        else:
            self.createNewUsersDatabaseAndLibraryDatabase()

    def getCurrentlyActiveUser(self):
        return self.currentlyActiveUser
      

    def createNewAccountOrLogin(self):
        exitLoop = False
        isReturningUser = False
        while (exitLoop == False):
            answerOne = raw_input("Are you a new or returning user? Please input 'New' or 'Returning'")
            if(answerOne == 'New'):
                print("\n" + "Fantastic! Please create a new user name and password!")
                newUserName = raw_input("Username: ")
                newPassWord = raw_input("Password: ")
                isReturningUser = False
                currentNewUser = User(newUserName, newPassWord, isReturningUser)
                self.currentlyActiveUser = currentNewUser
                print(newUserName + " logged in successfully!")
                exitLoop = True
            elif(answerOne == 'Returning'):
                print("Please login!")
                oldUser = raw_input("Username: ")
                oldPassWord = raw_input("Password: ")
                self.loginUser(oldUser,oldPassWord)
                exitLoop = True
            else:
                print("\n" + "Please try again. Reminder: Input exactly either 'New' or 'Returning'.")
                exitLoop = False
            self.mainMenu()
    
    def createNewUsersDatabaseAndLibraryDatabase(self):
        createNewDbResponse = raw_input("This appears to be a new installation as no users or library databases were found. Create them now?")
        if(createNewDbResponse == 'y'):
            self.createNewUsersDatabase()            
            self.createNewLibraryDatabase()    
    
    def createNewUsersDatabase(self):
        userConn = create_connection(r"/home/masonc/Documents/library database app/Users.db")
        sql_create_users_table = """ CREATE TABLE IF NOT EXISTS USERS (
                                        UserID      INT PRIMARY KEY,
                                        UserName    TEXT,
                                        Pass        TEXT
                                    );"""
        create_table(userConn,sql_create_users_table)
        print("CONSOLE LOG: New users database and accompanying table completed.")
    
    def createNewLibraryDatabase(self):
        libConn = create_connection(r"/home/masonc/Documents/library database app/Library.db")
        sql_create_authors_table = """ CREATE TABLE IF NOT EXISTS AUTHOR (
                                        AuthorID    INT PRIMARY KEY,
                                        FirstName   VARCHAR,
                                        LastName    VARCHAR,
                                        FullName    VARCHAR
                                    );"""
        sql_create_books_table = """CREATE TABLE IF NOT EXISTS BOOK (
                                        BookID          INT PRIMARY KEY,
                                        AuthorID        INT REFERENCES AUTHOR(AuthorID),
                                        Title           VARCHAR,
                                        NumOfPages      INT,
                                        CurrentStatus   VARCHAR
                                    );"""
        create_table(libConn, sql_create_authors_table)
        create_table(libConn, sql_create_books_table)
        print("CONSOLE LOG: New Library database and accompanying tables completed.")

    def loginUser(self,userName,passWord):
            thisUserName = userName
            thisUserPassword = passWord
            loginConn = create_connection(r"/home/masonc/Documents/library database app/Users.db")
            cur = loginConn.cursor()
            cur.execute("SELECT * FROM USERS \
                        WHERE UserName = ?  \
                        AND Pass = ?", 
                        (str(thisUserName),str(thisUserPassword)))
            result = cur.fetchone()
            if(result == None):
                print("Error! User not found in database. Please create a new account or contact your systems administrator.")
            else:
                isReturning = True
                returningUser = User(thisUserName,thisUserPassword,isReturning)
                self.currentlyActiveUser = returningUser
                print("Welcome " + self.currentlyActiveUser.getUserName() + "!")

    def logoutUser(self):
        if(self.getCurrentlyActiveUser != None):
            print("Logging out " + self.getCurrentlyActiveUser().getUserName() + "...")
            self.getCurrentlyActiveUser = None
            self.createNewAccountOrLogin()
        else:
            print("Error! No user currently logged in, please login or see a systems administrator for assistance")
            self.createNewAccountOrLogin()

    
    def mainMenu(self):
        userInput = 0
        exitLoop = False
        print("===============LIBRARY MANAGEMENT CONSOLE VERSION 1.0===============")
        print("Add, display, edit or remove Books from the database - 1")
        print("Add, display, edit or remove Users from the database - 2")
        print("Add, display, edit or remove Authors from the database - 3")
        print("Logout - 4")
        print("Shutdown - 5")
        print("Advanced Options (Requires Admin Login) - 6") #Delete databases
            
        int(userInput)
        while(exitLoop == False):
            userInput = input("Please select one of the corresponding options using the number keys on your keyboard:")
            if(userInput == 1):
                print("FEATURE COMING 1")
            elif(userInput == 2):
                print("FEATURE COMING 2")
            elif(userInput == 0):
                print("FEATURE COMING 0")
            elif(userInput ==3):
                print("FEATURE COMING 3")
                print("Add Author to Database - 1")
                print("Edit Author Currently in Database - 2")
                print("Remove Author from Database - 3")
                authInput = input("Please select from the above options, or input 'e' to return to main menu")
                if(authInput == 1):
                    print("Calling add method...")
                    firstNameInput = raw_input("What is the author's first name?")
                    lastNameInput = raw_input("What is the author's last name?")
                    createdAuthor = Author(firstNameInput,lastNameInput)
                    createdAuthor.addAuthorToDatabase()
                elif(authInput == 2):
                    print("Calling edit method...")
                    Author.displayAuthorTable(self)
                elif(authInput == 'e'):
                    self.mainMenu()
            elif(userInput == 4):
                self.logoutUser()
            elif(userInput == 5):
                print("Shutting down...")
                sys.exit()
            elif(userInput == 6):
                print("FEATURE COMING SOON")
            else:
                print("Error, unacceptable input type. Please try again.")







            

            
            


        
a = libraryManagementConsole(currentlyActiveUser=None)

        








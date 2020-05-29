from Database_Functions import *
import random

class User():
    def __init__(self, userName, passWord,isReturning):
        self.userName = str(userName)
        self.passWord = str(passWord)
        if(isReturning == False):
            self.addUserToDatabase()
        
    
    def getUserName(self):
        return self.userName

    def getPassWord(self):
        return self.passWord

    def getUserID(self):
        return self.userID
    

    def addUserToDatabase(self):
        thisUserID = random.randint(5,1000)
        int(thisUserID)
        newUserConn = create_connection(r"/home/masonc/Documents/library database app/Users.db")
        newUserConn.execute("INSERT INTO USERS (UserID,UserName,Pass)   \
                     VALUES (?,?,?)", (thisUserID, str(self.getUserName()), str(self.getPassWord())))
        newUserConn.commit()
        cur = newUserConn.cursor()
        print("Checking if user is added to database...")
        cur.execute("SELECT * FROM USERS \
                        WHERE UserID = ?  \
                        AND UserName = ? \
                        AND Pass = ?",
                        (thisUserID, str(self.getUserName()),str(self.getPassWord())))
        result = cur.fetchone()
        if(result == None):
            print("Error! User not added to database.")
        else:
            print("Added new user to database successfully!")

'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
import json
from Tkinter import *
from ttk import *


#create a window to allow the user to login to a given group a
class NewUserWindow(Toplevel):
    #windowHeight = None
   # windowWidth = None
#     newNameString = None
#     newPassString = None
#     newConfirmString = None
#     existNameString = None
#     existPassString = None
    
    
    def __init__(self, parent):
        Toplevel.__init__(self, parent, filename)
        self.parent = parent
        self.read_userData(filename)
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.userNameString = StringVar()
        self.userPassString = StringVar()
        self.userConfirmString = StringVar()
        self.googleLoginString = StringVar()
        self.googlePassString = StringVar()
        #define widgets
        self.instructionMessage = Message(self, text="Enter your desired user name, password, and the email and password for the google account you want to link to this account.", width = 500, background='lightgray')
        self.userNamePrompt = Label(self, text="User name:", background='lightgray')
        self.userNameEntry = Entry(self, textvariable = self.userNameString, width=30)
        self.userPassPrompt = Label(self, text="User password:", background='lightgray')
        self.userPassEntry = Entry(self, textvariable = self.userPassString, width=30, show="*")
        self.userConfirmPrompt = Label(self, text="Confirm Password:", background='lightgray')
        self.userConfirmEntry = Entry(self, textvariable = self.userConfirmString, width=30, show="*")
        self.googleLoginPrompt = Label(self, text="Google Account Name:", background='lightgray')
        self.googleLoginEntry = Entry(self, textvariable = self.googleLoginString, width=30)
        self.googlePassPrompt = Label(self, text="Google Password:", background='lightgray')
        self.googlePassEntry = Entry(self, textvariable = self.googlePassString, width=30, show="*")
        
        self.confirmButton = Button(self, text="Confirm", command=lambda: self.callBack("Button","Confirm"))
        self.cancelButton = Button(self, text="Skip", command=lambda: self.callBack("Button","Cancel"))
        
        #design window
        self.title("Register New Account")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background='lightgray')
        
        #place widgets
        self.instructionMessage.grid(row=0, column=0, columnspan=4, pady=5)
        self.userNamePrompt.grid(row=1, column=0, padx=5, sticky=W+E)
        self.userNameEntry.grid(row=1, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        
        self.userPassPrompt.grid(row=2, column=0, padx=5, sticky=W+E)
        self.userPassEntry.grid(row=2, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        
        self.userConfirmPrompt.grid(row=3, column=0, padx=5, sticky=W+E)
        self.userConfirmEntry.grid(row=3, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        
        self.googleLoginPrompt.grid(row=4, column=0, padx=5, sticky=W+E)
        self.googleLoginEntry.grid(row=4, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        
        self.googlePassPrompt.grid(row=5, column=0, padx=5, sticky=W+E)
        self.googlePassEntry.grid(row=5, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        
        self.confirmButton.grid(row=6, column=2, padx=0, pady=5, sticky=E+S)
        self.cancelButton.grid(row=6, column=3, padx=10, pady=5, sticky=E+W+S)
        
    def read_userData(self, filename):
        json_data=open(filename)
        userData=json.load(json_data)
        self.userData=userData    
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Confirm":
                print("Confirm clicked")
                #attempt to create new account
                
            elif callerName == "Cancel":
                print("Cancel clicked")
                #hide the window, clear self.nameEntryString, show map window

    def createAccount(self):
        #make sure all entries have been filled
        allEntriesFilled = self.checkFields()
        #make sure name is available
        nameAvailable = self.userNameAvailable()
        #make sure passwords match
        matchingPasswords = self.passwordsMatch()
        #make sure google information is valid
        validGoogleAccount = self.validGoogleInformation()
        #make sure user does not already have an account
        googleAccountNotInUse = self.emailNotInUse()
        #create new account
        if allEntriesFilled and nameAvailable and matchingPasswords and validGoogleAccount and googleAccountNotInUse:
            self.makeAccount()
        else:
            print ("Account creation failed.")
        

    def checkFields(self):
        #return false if any entry is empty
        if self.userNameString.get == "":
            return False
        if self.userPassString.get == "":
            return False
        if self.userConfirmString.get == "":
            return False
        if self.googleLoginString.get == "":
            return False
        if self.googleLoginString.get == "":
            return False
        return True
    
    def userNameAvailable(self):
        #return false if user name is taken
        return True
    
    def passwordsMatch(self):
        #return false if passwords do not match
        desiredPass = self.userPassString.get()
        confirmPass = self.userConfirmString.get()
        
        if desiredPass == confirmPass:
            return True
        return False
    
    def validGoogleInformation(self):
        #attempt to log in to google with the given information; if it doesnt work return false, else return true
        calendarService = gdata.calendar.client.CalendarClient()
        calendarService.email = self.userName.get()
        calendarService.password = self.userPass.get()
        calendarService.source = 'CalReader' # not really sure what this is
        try:
            calendarService.ProgrammaticLogin() #add an if statement or something to catch a bad authentication error;
        except gdata.service.BadAuthentication:
            return False
        return True
    
    def emailNotInUse(self):
        #compare the google login information with all stored login information; if account is in use, return false, else return true
        return True
    
    def makeAccount(self):
        #add new account to user database
        return
        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = NewUserWindow(root, "UserDatabase.json")
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
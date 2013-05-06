'''
Created on Apr 18, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
from Tkinter import *
from ttk import *
import GroupLoginWindow
import CalendarWindow
import InvitationWindow
import NewUserWindow
import MapWindow
import webbrowser
import json

#convert MessageWindow into a class (do later)
class Window(object):
    """ Main Window For Program. Additional windows created from this one"""
    isRunning = True
    def __init__(self, parent): 
        self.root = parent
        self.root.title("Main Window")
        self.frame = Frame(parent)
        self.frame.pack()
        self.openWindow()
        self.hide()
        
    def listener(self, arg1, arg2=None):
        self.show()

    def hide(self):
        self.root.withdraw()
    
    def openWindow(self):
        """ Add new window classes here"""
        logWindow = LoginWindow(self.root)
    
    def show(self):
        self.root.update()
        self.root.deiconify()
        
class LoginWindow(Toplevel):
    haveLogged = False
    windowHeight = None
    windowWidth = None

    def __init__(self, parent):
        Toplevel.__init__(self)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        #define widgets for window
        self.quitButton = Button(self, text="Cancel", command=lambda: self.callBack("Button", "Quit"))
        self.submitButton = Button(self, text="Submit", command=lambda: self.callBack("Button", "Submit"))
        #testMessage = Message(self)
        self.userName = StringVar()
        self.userPass = StringVar()
        self.userEmail = StringVar()
        self.userEmailPass = StringVar()
        self.userNamePrompt = Label(self, text="User Name:", background="lightgray")
        self.userPassPrompt = Label(self, text="Password:", background="lightgray")
        self.userNameEntry = Entry(self, textvariable=self.userName)
        self.userPassEntry = Entry(self, textvariable=self.userPass, show="*")
        self.read_userData('UserDatabase.json')
        
        #set up window theme
        self.title("Login to GroupMeet")
        self.style = Style()
        self.style.theme_use("clam")
        self.configure(background="lightgray")
        # self.pack(fill=BOTH, expand = 1)
        
        #place widgets
        self.userNamePrompt.grid(row=0, column=0, padx=5, pady=10, sticky=E+W)
        self.userNameEntry.grid(row=0, column=1, padx=5, pady=10, sticky=E+W)
        self.userPassPrompt.grid(row=0, column=2,padx=5,pady=10,sticky=E+W)
        self.userPassEntry.grid(row=0,column=3, padx=5, pady=10, sticky=E+W)
        self.submitButton.grid(row=1,column=2, columnspan=2, padx=5, pady= 5, sticky=W)
        self.quitButton.grid(row=1,column=3, padx=5, pady=5, sticky=E)
        
    def onClose(self):
        self.destroy()
    
    def callBack(self, callerType, callerName):
        #handle each widget's callback
        
        #Buttons
        if callerType == "Button":
            if callerName == "Submit":
                print("Submit button pressed")
                if self.userExists(self.userName.get()):
                    self.client = self.Login()
                else:
                    print("The username does not exist. Would you like to create a new account?")
                    #pop a newUser window
                    newUser = NewUserWindow.NewUserWindow(self.parent, 'UserDatabase.json')
                    self.withdraw()
                    
            elif callerName == "Quit":
                print("Exiting")
                self.parent.isRunning = False
                self.quit()
        #Entries - does nothing, but shows how to use elif
        if callerType == "Entry":
            if callerName == "UserName":
                self.userName = self.userNameEntry.textvariable.get()
     
                
    def Login(self):
        if self.accountLoginCheck(self.userName, self.userPass):
            try:
                calendarService = gdata.calendar.client.CalendarClient()
                email = self.userEmail
                password = self.userEmailPass
                source = 'CalReader' # not really sure what this is
                calendarService.ClientLogin(email, password, source) #add an if statement or something to catch a bad authentication error;
                self.groupClient = gdata.calendar.client.CalendarClient()
                self.groupClient.ClientLogin('project3team07@gmail.com', 'teamseven', 'GroupMeet')
                self.haveLogged = True
                groupLogin = GroupLoginWindow.GroupLoginWindow(self.parent, self.userName.get(), calendarService, self.groupClient)
                self.hide()
                return calendarService
            except gdata.service.BadAuthentication:
                print("Bad user name or password.")
        else:
            print("incorrect username or password. Please try again.")
            
            
    def userExists(self, userName):
        #compare the input user name with the existing ones in the data server
        print("%s", userName)
        for Users in self.userData['Users']:
            if Users['username']==userName:
                return True
        return False
        
    def read_userData(self, filename):
        json_data=open(filename)
        userData=json.load(json_data)
        #userData=json.dumps(userData, ensure_ascii=False)
        print(userData)
        self.userData=userData
        
    def write_userData(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(json.dumps(self.userData, sort_keys=True, indent=2))
            
    def addUser(self, userName, userPassword, emailAccount, emailPassword):
        self.userData['Users'].append({"username":userName, "userpassword":userPassword,
                                       "googleid":emailAccount, "googlepass":emailPassword,
                                       "grouplist":[]})
        self.write_userData('UserDatabase.json')
    
    def accountLoginCheck(self, userName, password):
        #print("%s", userName.get())
        #print("%s", password.get())
        for Users in self.userData['Users']:
            userNameData=str(Users['username'])
            userPassData=str(Users['userpassword'])
            #print("%s", userNameData)
            #print("%s", userPassData)  
            if userNameData==userName.get() and userPassData==password.get():
                self.userEmail=str(Users['googleid'])
                self.userEmailPass=str(Users['googlepass'])
                return True
        return False
    
    def hide(self):
        self.withdraw()     
       
def main():
    
    root = Tk()
    root.geometry("600x200+300+300")
    app = Window(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

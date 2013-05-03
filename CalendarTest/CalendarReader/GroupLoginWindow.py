'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *
import json

#create a window to allow the user to login to a given group a
class GroupLoginWindow(Toplevel):
    #groupdata = None
    
    def __init__(self, parent, calendarClient):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.read_groupData('GroupDatabase.json')
        self.read_userData('UserDatabase.json')
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.newNameString = StringVar()
        self.newPassString = StringVar()
        self.newConfirmString = StringVar()
        self.existNameString = StringVar()
        self.existPassString = StringVar()
        #define widgets
        #widgets for "NEW" group side
        self.newHeader = Label(self, text="Register A New Group", underline=0)
        self.newName = Entry(self, textvariable=self.newNameString)
        self.newPass = Entry(self, textvariable=self.newPassString, show ='*')
        self.newConfirm = Entry(self, textvariable=self.newConfirmString, show ='*')
        self.newNamePrompt = Label(self, text="Group Name:")
        self.newPassPrompt = Label(self, text="Password:")
        self.newConfirmPrompt = Label(self, text="Confirm Password:")
        self.registerButton = Button(self, text="Register Group", command=lambda: self.callBack("Button","Register"))
        
        #widgets for "EXISTING" group side
        self.existHeader = Label(self, text="Access An Existing Group", underline=0)
        self.existName = Entry(self, textvariable=self.existNameString)
        self.existPass= Entry(self, textvariable=self.existPassString, show="*")
        self.existNamePrompt = Label(self, text="Group Name:")
        self.existPassPrompt = Label(self, text="Password:")
        self.loginButton = Button(self, text="Login", command=lambda: self.callBack("Button","Login"))
        
        #widget to quit
        self.quitButton = Button(self, text="Quit", command=lambda: self.callBack("Button","Quit"))
        
        #design window
        self.title("Group Login")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background="lightgray")
        
        #handle New side
        self.newHeader.grid(row=0, column=0, columnspan=2, pady=5)
        self.newNamePrompt.grid(row=1, column=0, pady=5, sticky=E)
        self.newName.grid(row=1,column=1, padx=10, sticky=W)
        self.newPassPrompt.grid(row=2,column=0, pady=5, sticky=E)
        self.newPass.grid(row=2,column=1, padx=10, sticky=E)
        self.newConfirmPrompt.grid(row=3,column=0, pady=5, sticky=E)
        self.newConfirm.grid(row=3,column=1, padx=10)
        self.registerButton.grid(row=4,column=1, padx=10, pady=5, sticky= E+S)
        
        #handle Existing side
        self.existHeader.grid(row=0, column=3, columnspan=2, pady=5)
        self.existNamePrompt.grid(row=1,column=3, pady=5, sticky=E)
        self.existName.grid(row=1,column=4, padx=10)
        self.existPassPrompt.grid(row=2,column=3, pady=5, sticky=E)
        self.existPass.grid(row=2,column=4, padx=10)
        self.loginButton.grid(row=4,column=4, padx=10, pady=5, sticky=E+S)
        
    def read_groupData(self, filename):
        json_data=open(filename)
        groupData=json.load(json_data)
        self.groupData=groupData
    
    def write_groupData(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self.groupData, outfile)        
            
    def read_userData(self, filename):
        json_data=open(filename)
        userData=json.load(json_data)
        self.userData=userData
            
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            
            if callerName == "Register":
                print("Register clicked")
                print(self.newNameString.get())
                if self.groupExists(self.newNameString.get()) == True:
                    print ("Group name is already taken. Enter a different name.")
                else:
                    print ("Group name is available!")
                    if self.confirmPassword(self.newPassString.get(), self.newConfirmString.get()):
                        print("Adding new group!")
                        self.addGroup(self.newNameString.get(), self.newPassString.get(), "William");
                    else :
                        print("Passwords don't match.")
                        
            elif callerName == "Login":
                print("Login clicked")
                print(self.existNameString.get())
                if self.groupExists(self.existNameString.get()) == True:
                    print ("Group exists. Attempting to login.")
                    
                    self.groupLogin(self.existNameString.get(), self.existPassString.get())
                else:
                    print ("Group does not exist. Please enter the name of a valid group!")
            elif callerName == "Quit":
                print("Exiting")
       
    def confirmPassword (self, password, confirmPassword):
        if password==confirmPassword:
            return True;
        return False;
       
    def groupExists(self, groupName):
       #Compare group with name GroupName to other groups in data server; if group exists, return true, else return false
       for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                return True
       return False 
    
    
    def addGroup(self, groupName, password, memberName):
        self.groupData['Groups'].append({"groupName":groupName, "dateCreated":"5/2/2013",
                                          "calendarId":"Empty for now", "password":password, 
                                          "members":[{"name":memberName}]})
        self.write_groupData('GroupDatabase.json')
        return
    
    def userInGroup(self, groupName, userName):
        for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                for Members in Groups['members']:
                    if Members['name'] == userName:
                        return True
        return False
    
    def groupLogin(self, groupName, groupPass):
        #find the appropriate group and pass 
        return False
#     def addUserToGroup(self):
        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = GroupLoginWindow(root, gdata.calendar.service.CalendarService())
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
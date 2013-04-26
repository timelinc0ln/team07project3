'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *


#create a window to allow the user to login to a given group a
class GroupLoginWindow(Frame):
    #windowHeight = None
   # windowWidth = None
#     newNameString = None
#     newPassString = None
#     newConfirmString = None
#     existNameString = None
#     existPassString = None
    
    
    def __init__(self, parent, calendarClient):
        Frame.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.newNameString = None
        self.newPassString = None
        self.newConfirmString = None
        self.existNameString = None
        self.existPassString = None
        #define widgets
        #widgets for "NEW" group side
        self.newHeader = Label(self, text="Register A New Group", underline=0)
        self.newName = Entry(self, textvariable=self.newNameString)
        self.newPass = Entry(self, textvariable=self.newPassString)
        self.newConfirm = Entry(self, textvariable=self.newConfirmString)
        self.newNamePrompt = Label(self, text="Group Name:")
        self.newPassPrompt = Label(self, text="Password:")
        self.newConfirmPrompt = Label(self, text="Confirm Password:")
        self.registerButton = Button(self, text="Register Group", command=lambda: self.callBack("Button","Register"))
        
        #widgets for "EXISTING" group side
        self.existHeader = Label(self, text="Access An Existing Group", underline=1)
        self.existName = Entry(self, textvariable=self.existNameString)
        self.existPass= Entry(self, textvariable=self.existPassString)
        self.existNamePrompt = Label(self, text="Group Name:")
        self.existPassPrompt = Label(self, text="Password:")
        self.loginButton = Button(self, text="Login", command=lambda: self.callBack("Button","Login"))
        
        #widget to quit
        self.quitButton = Button(self, text="Quit", command=lambda: self.callBack("Button","Quit"))
        
        #design window
        self.parent.title("Group Login")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        
        #handle New side
        self.newHeader.grid(row=0, column=0, columnspan=2, pady=5)
        self.newNamePrompt.grid(row=1, column=0, pady=5, sticky=E)
        self.newName.grid(row=1,column=1, padx=10, sticky=W)
        self.newPassPrompt.grid(row=2,column=0, pady=5, sticky=E)
        self.newPass.grid(row=2,column=1, padx=10, sticky=E)
        self.newConfirmPrompt.grid(row=3,column=0, pady=5, sticky=E)
        self.newConfirm.grid(row=3,column=1, padx=10)
        self.registerButton.grid(row=4,column=1, padx=10, sticky= E+S)
        
        #handle Existing side
        self.existHeader.grid(row=0, column=3, columnspan=2, pady=5)
        self.existNamePrompt.grid(row=1,column=3, pady=5, sticky=E)
        self.existName.grid(row=1,column=4, padx=10)
        self.existPassPrompt.grid(row=2,column=3, pady=5, sticky=E)
        self.existPass.grid(row=2,column=4, padx=10)
        self.loginButton.grid(row=4,column=4, padx=10, sticky=E+S)
        
        #self.existHeader.place(x=self.windowWidth* 1.75, y = self.windowHeight * .1)
        #self.existNamePrompt.place(x=self.windowWidth* 2, y = self.windowHeight* .25)
    
        #self.existName.place(x=self.existNamePrompt.winfo_x() + self.existNamePrompt.winfo_reqwidth(), y = self.windowHeight* .25)
        
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Register":
                print("Register clicked")
            elif callerName == "Login":
                print("Login clicked")
            elif callerName == "Quit":
                print("Exiting")
       
    
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = GroupLoginWindow(root, gdata.calendar.service.CalendarService())
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
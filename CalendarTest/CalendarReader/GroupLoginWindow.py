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
    
    def __init__(self, parent, calendarClient):
        Frame.__init__(self, parent)
        self.parent = parent
        self.calendarClient = calendarClient
        self.initUI()
        
    def initUI(self):
        #define widgets
        #widgets for "NEW" group side
        self.newHeader = Label(self, text="Register A New Group", underline=1)
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
        
        
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Register":
                print("Register clicked")
            elif callerName == "Login":
                print("Login clicked")
            elif callerName == "Quit":
                print("Exiting")
       
    
        
        
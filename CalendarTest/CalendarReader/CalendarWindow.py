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

class CalendarWindow(Toplevel):
    def __init__(self, parent, client):
            Toplevel.__init__(self)
            self.parent = parent
            self.client = client
            self.initUI()  
          
    def openGroupLogin(self, parent, client):
        groupWindow = GroupLoginWindow.GroupLoginWindow(parent, self.userName.get(), client, client)
                 
    def initUI(self):
        self.geometry("700x700+100+100")
        self.title("Calendar Window")
        loginButton = Button(self, text = 'Login', command=lambda: self.callBack("Button", "Login")).pack(side = BOTTOM)
        self.newHeader = Label(self, text = "Instructions:")
        self.newHeader.grid(row=0, column=0, columnspan=2, pady=5)
               
               
    def callBack(self, callerType, callerName):
        if callerType == "Button":
            if callerName == "Login":
                print("Login button pressed")
                self.openGroupLogin(self.parent, self.client)
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
        self.newGroupHeader = Label(self, text="Register A New Group", underline=1)
        self.newGroupName = Entry(self, textvariable=self.newGroupNameString)
        self.newGroupPass = Entry(self, textvariable=self.newGroupPassString)
        self.newGroupConfirm = Entry(self, textvariable=self.newGroupConfirmString)
        self.nGNPrompt = Label(self, text="Group Name:")
        self.nGPPrompt = Label(self, text="Password:")
        self.nGCPrompt = Label(self, text="Confirm Password:")
        
        
        #widgets for "EXISTING" group side
        self.existGroupName = Entry(self, textvariable=self.existGroupNameString)
        self.existGroupPass= Entry(self, textvariable=self.existGroupPass)
    
        
        
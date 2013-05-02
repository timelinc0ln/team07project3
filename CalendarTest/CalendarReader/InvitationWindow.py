'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
from Tkinter import *
from ttk import *


#create a window to allow the user to login to a given group a
class InvitationWindow(Toplevel):
    #windowHeight = None
   # windowWidth = None
#     newNameString = None
#     newPassString = None
#     newConfirmString = None
#     existNameString = None
#     existPassString = None
    
    
    def __init__(self, parent, calendarClient):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.emailEntryString = StringVar()
        #define widgets
        self.instructionMessage = Label(self, text="Enter the email addresses of the invitees below, separated by commas", background='lightgray')
        self.emailEntryPrompt = Label(self, text="Event name:", background='lightgray')
        self.emailEntry = Entry(self, textvariable = self.emailEntryString, width=30)
        self.confirmButton = Button(self, text="Confirm", command=lambda: self.callBack("Button","Confirm"))
        self.skipButton = Button(self, text="Skip", command=lambda: self.callBack("Button","Skip"))
        
        #design window
        self.title("Invite Friends")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background='lightgray')
        
        #place widgets
        self.instructionMessage.grid(row=0, column=0, columnspan=4, pady=5)
        self.emailEntryPrompt.grid(row=1, column=0, padx=5, sticky=E)
        self.emailEntry.grid(row=1, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        self.confirmButton.grid(row=2, column=2, padx=0, pady=5, sticky=E+S)
        self.skipButton.grid(row=2, column=3, padx=10, pady=5, sticky=E+W+S)
        
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Confirm":
                print("Confirm clicked")
                #email every email address in the list
                self.sendInvites()
            elif callerName == "Skip":
                print("Skip clicked")
                #hide the window, clear self.nameEntryString, show map window

    def sendInvites(self):
        #store email addresses found in emailEntryString
        rawEmailInfo = self.emailEntryString.get()
        emailAddresses = rawEmailInfo.split(",", )
        print (emailAddresses)
        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = InvitationWindow(root, gdata.calendar.client.CalendarClient())
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
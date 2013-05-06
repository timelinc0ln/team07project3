'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
from Tkinter import *
from ttk import *
import ConfirmEventWindow


#create a window to allow the user to login to a given group a
class EventNamingWindow(Toplevel): 
    def __init__(self, parent, calendarID, calendarClient, location, eventStart, eventEnd):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.location = location
        self.calendarID = calendarID
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.nameEntryString = StringVar()
        #define widgets
        self.instructionMessage = Label(self, text="Enter a name for your event (i.e. \"Conference Call\")", background='lightgray')
        self.nameEntryPrompt = Label(self, text="Event name:", background='lightgray')
        self.nameEntry = Entry(self, textvariable = self.nameEntryString, width=30)
        self.nextButton = Button(self, text="Next", command=lambda: self.callBack("Button","Next"))
        self.backButton = Button(self, text="Back", command=lambda: self.callBack("Button","Back"))
        
        #design window
        self.title("Name Event")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background='lightgray')
        
        #place widgets
        self.instructionMessage.grid(row=0, column=0, columnspan=4, pady=5)
        self.nameEntryPrompt.grid(row=1, column=0, padx=5, sticky=E)
        self.nameEntry.grid(row=1, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        self.nextButton.grid(row=2, column=2, padx=0, pady=5, sticky=E+S)
        self.backButton.grid(row=2, column=3, padx=10, pady=5, sticky=E+W+S)
        
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Next":
                print("Next clicked")
                self.EventName = self.nameEntryString.get()
                #hide the window, open a confirmation window, pass main program the event name
                confirm = ConfirmEventWindow.ConfirmEventWindow(self.parent, self.calendarClient, self.calendarID, self.EventName, self.eventStart, self.eventEnd, self.location)
                self.withdraw()
            elif callerName == "Back":
                print("Back clicked")
                #hide the window, clear self.nameEntryString, show map window

        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = EventNamingWindow(root, gdata.calendar.client.CalendarClient())
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
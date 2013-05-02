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
class ConfirmEventWindow(Toplevel):
    
    def __init__(self, parent, calendarClient, eventName, eventDate, eventPlace):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.eventName = eventName
        self.eventDate = eventDate
        self.eventPlace = eventPlace
        self.initUI()
        
    def initUI(self):
        #define widgets

        #Labels
        self.instructionsLabel = Label(self, text="Is this the event you want to add to the calendar?")
        self.nameLabelPrompt = Label(self, text="Name:", background="lightgray")
        self.dateLabelPrompt = Label(self, text="Date:", background="lightgray")
        self.placeLabelPrompt = Label(self, text="Location:", background="lightgray")
        self.nameLabel = Label(self, text=self.eventName, background="lightgray")
        self.dateLabel = Label(self, text=self.eventDate, background="lightgray")
        self.placeLabel = Label(self, text=self.eventPlace, background="lightgray")
        #Buttons
        self.modifyNameButton = Button(self, text="Change Name", command=lambda: self.callBack("Button","Name"))
        self.modifyDateButton = Button(self, text="Change Date", command=lambda: self.callBack("Button","Date"))
        self.modifyPlaceButton = Button(self, text="Change Location", command=lambda: self.callBack("Button","Place"))
        self.addEventButton = Button(self, text="Add Event", command=lambda: self.callBack("Button","Add"))
        self.cancelButton = Button(self, text="Cancel", command=lambda: self.callBack("Button","Cancel"))
        
        #design window
        self.title("Name Event")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background='lightgray')
        
        #place widgets
        self.instructionsLabel.grid(row=0, column=0, columnspan=4, pady=5)
        
        self.nameLabelPrompt.grid(row=1,column=0,padx=10, sticky=E+W)
        self.nameLabel.grid(row=1, column=1, padx=5, sticky=E+W)
        self.modifyNameButton.grid(row=1,column=2, columnspan=2, padx=10, pady=5, sticky=E+W)
        
        self.dateLabelPrompt.grid(row=2,column=0,padx=10, sticky=E+W)
        self.dateLabel.grid(row=2, column=1, padx=5, sticky=E+W)
        self.modifyDateButton.grid(row=2,column=2, columnspan=2, padx=10, pady=5, sticky=E+W)
        
        self.placeLabelPrompt.grid(row=3,column=0,padx=10, sticky=E+W)
        self.placeLabel.grid(row=3, column=1, padx=5, sticky=E+W)
        self.modifyPlaceButton.grid(row=3,column=2, columnspan=2, padx=10, pady=5, sticky=E+W)
        
        self.addEventButton.grid(row=4, column=2, padx=10, pady=5, sticky=E+W)
        self.cancelButton.grid(row=4, column=3, padx=10, pady=5, sticky=E+W)
#         
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Name":
                print("Name clicked")
                #hide the window, show the EventNamingWindow
                self.withdraw()
            elif callerName == "Date":
                print("Date clicked")
                #hide the window, show the CalendarWindow
                self.withdraw()
            elif callerName == "Place":
                print("Place clicked")
                #hide the window, show the LocationWindow
                self.withdraw()
            elif callerName == "Add":
                print("Add clicked")
                #hide the window, show mainMenu Window
                self.withdraw()
            elif callerName == "Cancel":
                print("Cancel clicked")
                #hide the window, show mainMenu Window
                self.withdraw()

        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    eventName = "Basketball"
    eventDate = "March 3rd "
    eventPlace = "Space"
    app = ConfirmEventWindow(root, gdata.calendar.client.CalendarClient(), eventName, eventDate, eventPlace)
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
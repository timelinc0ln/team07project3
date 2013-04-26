'''
Created on Apr 26, 2013

@author: Cullen
'''

import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *


#create a window to allow the user to decide which of his calendars will be added to the group calendar
class CalendarSelectionWindow(Frame):
    
    def __init__(self, parent, calendarClient):
        Frame.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.newNameString = StringVar()
        self.newPassString = StringVar()
        self.newConfirmString = StringVar()
        self.existNameString = StringVar()
        self.existPassString = StringVar()
        self.calendarSelectionExplanation = StringVar()
        #define widgets
        #listboxes
        self.userCalendars = Listbox(self)
        self.selectedCalendars = Listbox(self)
        #buttons
        self.selectCalendarButton = Button(self, text=">>", command=lambda: self.callBack("Button","Select"))
        self.deselectCalendarButton = Button(self, text="<<", command=lambda: self.callBack("Button", "Deselect"))
        self.nextButton = Button(self, text="Next", command=lambda: self.callBack("Button", "Next"))
        #labels
        self.calendarSelectionMessage = Label(self, textvariable=self.calendarSelectionExplanation)
        self.userCalendarHeader = Label(self, text= "User Calendars")
        self.selectedCalendarHeader = Label(self, text= "Selected Calendars")
        
        #widgets for "NEW" group side
#         self.newHeader = Label(self, text="Register A New Group", underline=0)
#         self.newName = Entry(self, textvariable=self.newNameString)
#         self.newPass = Entry(self, textvariable=self.newPassString)
#         self.newConfirm = Entry(self, textvariable=self.newConfirmString)
#         self.newNamePrompt = Label(self, text="Group Name:")
#         self.newPassPrompt = Label(self, text="Password:")
#         self.newConfirmPrompt = Label(self, text="Confirm Password:")
#         self.registerButton = Button(self, text="Register Group", command=lambda: self.callBack("Button","Register"))
#         
#         #widgets for "EXISTING" group side
#         self.existHeader = Label(self, text="Access An Existing Group", underline=1)
#         self.existName = Entry(self, textvariable=self.existNameString)
#         self.existPass= Entry(self, textvariable=self.existPassString, show="*")
#         self.existNamePrompt = Label(self, text="Group Name:")
#         self.existPassPrompt = Label(self, text="Password:")
#         self.loginButton = Button(self, text="Login", command=lambda: self.callBack("Button","Login"))
#         
#         #widget to quit
#         self.quitButton = Button(self, text="Quit", command=lambda: self.callBack("Button","Quit"))
#         
        #design window
        self.parent.title("Select Calendars to Sync")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        
        self.calendarSelectionMessage.grid(row=0, column=0, columnspan=8)
        self.calendarSelectionExplanation.set("Select which of your calendars you want to have added to the group calendar below.")
        self.userCalendarHeader.grid(row=1,column=1, sticky=S)
        self.selectedCalendarHeader.grid(row=1, column=3, sticky=S)
        self.userCalendars.grid(row=2,column=1, rowspan=4, sticky=E)
        self.selectedCalendars.grid(row=2, column=3, rowspan=4, sticky=W)
        self.selectCalendarButton.grid(row=3, column=2)
        self.deselectCalendarButton.grid(row=4, column=2)
        self.nextButton.grid(row=5, column=4)
        
        #fill the userCalendar box
        self.seedCalendarList()
#         #handle New side
#         self.newHeader.grid(row=0, column=0, columnspan=2, pady=5)
#         self.newNamePrompt.grid(row=1, column=0, pady=5, sticky=E)
#         self.newName.grid(row=1,column=1, padx=10, sticky=W)
#         self.newPassPrompt.grid(row=2,column=0, pady=5, sticky=E)
#         self.newPass.grid(row=2,column=1, padx=10, sticky=E)
#         self.newConfirmPrompt.grid(row=3,column=0, pady=5, sticky=E)
#         self.newConfirm.grid(row=3,column=1, padx=10)
#         self.registerButton.grid(row=4,column=1, padx=10, sticky= E+S)
#         
#         #handle Existing side
#         self.existHeader.grid(row=0, column=3, columnspan=2, pady=5)
#         self.existNamePrompt.grid(row=1,column=3, pady=5, sticky=E)
#         self.existName.grid(row=1,column=4, padx=10)
#         self.existPassPrompt.grid(row=2,column=3, pady=5, sticky=E)
#         self.existPass.grid(row=2,column=4, padx=10)
#         self.loginButton.grid(row=4,column=4, padx=10, sticky=E+S)
        
        #self.existHeader.place(x=self.windowWidth* 1.75, y = self.windowHeight * .1)
        #self.existNamePrompt.place(x=self.windowWidth* 2, y = self.windowHeight* .25)
    
        #self.existName.place(x=self.existNamePrompt.winfo_x() + self.existNamePrompt.winfo_reqwidth(), y = self.windowHeight* .25)
        
    
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
                    
            elif callerName == "Login":
                print("Login clicked")
                print(self.existNameString.get())
                if self.groupExists(self.existNameString.get()) == True:
                    print ("Group exists. Attempting to login.")
                else:
                    print ("Group does not exist. Please enter the name of a valid group!")
            elif callerName == "Quit":
                print("Exiting")
            elif callerName == "Select":
                print ("Calendar Select Button pressed")
                self.selectCalendar()
            elif callerName == "Deselect":
                print ("Calendar Deselect Button pressed")
                self.deselectCalendar()
            elif callerName == "Next":
                print ("Next Button pressed")
                self.updateGroupCalendar()
       
    def seedCalendarList(self):
        #insert calendar names into userCalendars
        calendar_feed = self.calendarClient.GetCalendarListFeed()
        for calendar_list_entry in calendar_feed.entry:
            self.userCalendars.insert(END, calendar_list_entry.title.text)
        return
       
    def selectCalendar(self):
        #move selected calendar in userCalendars to selectedCalendars, if an entry is selected
        if len(self.userCalendars.curselection()) != 0:
            selectedIndex = self.userCalendars.curselection()[0]
            self.selectedCalendars.insert(END, self.userCalendars.get(selectedIndex))
            self.userCalendars.delete(selectedIndex)
        else:
            print ("No calendar selected")
        return
      
    def deselectCalendar(self):
        #move selected calendar in selectedCalendars to userCalendars, if an entry is selected
        if len(self.selectedCalendars.curselection()) != 0:
            selectedIndex = self.selectedCalendars.curselection()[0]
            self.userCalendars.insert(END, self.selectedCalendars.get(selectedIndex))
            self.selectedCalendars.delete(selectedIndex)
        else:
            print ("No calendar selected")
        return
    
    def updateGroupCalendar(self):
        #add all events from calendars listed in selectedCalendars to the Group Calendar
        #NOT WORKING YET
        self.quit()
        return
    
           
    def groupExists(self, GroupName):
       #Compare group with name GroupName to other groups in data server; if group exists, return true, else return false
        return False
        
def main():
    
    root = Tk()
    root.geometry("600x300+300+300")
    #print(root.geometry.)
    myClient = gdata.calendar.service.CalendarService()
    myClient.ClientLogin("project3team07@gmail.com", "teamseven")
    app = CalendarSelectionWindow(root, myClient)
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
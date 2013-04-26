'''
Created on Apr 26, 2013

@author: Cullen
'''

import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *


#create a window to allow the user to decide which of his/her calendars will be added to the group calendar
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
        
        #design window
        self.parent.title("Select Calendars to Sync")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        
        self.calendarSelectionMessage.grid(row=0, column=0, columnspan=8)
        self.calendarSelectionExplanation.set("Select which of your calendars you want to add to the group calendar below.")
        self.userCalendarHeader.grid(row=1,column=1, sticky=S)
        self.selectedCalendarHeader.grid(row=1, column=3, sticky=S)
        self.userCalendars.grid(row=2,column=1, rowspan=4, sticky=E)
        self.selectedCalendars.grid(row=2, column=3, rowspan=4, sticky=W)
        self.selectCalendarButton.grid(row=3, column=2)
        self.deselectCalendarButton.grid(row=4, column=2)
        self.nextButton.grid(row=5, column=4)
        
        #fill the userCalendar box
        self.seedCalendarList()
        
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Select":
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

        
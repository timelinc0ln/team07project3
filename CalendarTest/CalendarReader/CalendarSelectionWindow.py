'''
Created on Apr 26, 2013

@author: Cullen
'''

import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.data
import gdata.calendar.client
import CalAccessMethods
import atom
from atom import *
from Tkinter import *
from ttk import *


#create a window to allow the user to decide which of his/her calendars will be added to the group calendar
class CalendarSelectionWindow(Frame):
    
    def __init__(self, parent, calendarClient, groupClient):
        Frame.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.groupClient = groupClient
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
        calendar_feed = self.calendarClient.GetOwnCalendarsFeed()
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
        
        #find calendars listed in selectedCalendars
        calendar_feed = self.calendarClient.GetOwnCalendarsFeed()
        calendarsToAccess = []
        chosenCalendars = self.selectedCalendars.get(0, END)
        
        #print(calendar_feed)
        for calendar_list_entry in calendar_feed.entry:
            #print(calendar_list_entry)
            if calendar_list_entry.title.text in chosenCalendars:
                calendarsToAccess.append(calendar_list_entry)
        
        #print (len(calendarsToAccess))
        if len(calendarsToAccess) != 0:
            #print (calendarsToAccess[0])
            #print(self.calendarClient.GetCalendarEventFeed(calendar=calendarsToAccess[0]))
            eventsFound = []
            for cal in calendarsToAccess:
                print(cal.title.text)
                #get actual calendar id from calendar uri
                calID = CalAccessMethods.getCalendarID(cal.id.text)
                calEventFeedUri = self.calendarClient.GetCalendarEventFeedUri(calID)
                print (calEventFeedUri)
                calEventFeed = self.calendarClient.GetCalendarEventFeed(uri=calEventFeedUri)

                for calEvent in calEventFeed.entry:
                     print (calEvent.title.text)
#                     eventsFound.append(calEvent)
#                     print (len(eventsFound))
                print("")
            
            
            
#             #find group calendar
#             #group calendar id should be accessed as part of a group; for now, use the following variable
#             calendarID=  "pog27t596e2vu8sigfvqnvk59s@group.calendar.google.com"
#             groupCalendar = gdata.calendar.data.CalendarEntry()
#             groupCalendar.id = atom.data.Id(text=calendarID)
#             print(groupCalendar)
            
            #get each event in calendarsToAccess and add a duplicate event to groupCalendar
#             for cal in calendarsToAccess:
#                 eventsFound = []
#                 eventToAdd = gdata.calendar.data.CalendarEventEntry()
                
#                 print (currentCalendar)
#                 events = self.calendarClient.GetCalendarEventFeed(currentCalendar)
        
        
           
        
        #self.quit()
        else:
            print("No calendars have been selected. Select a calendar to add before moving on.")
        return
        
def main():
    
    root = Tk()
    root.geometry("600x300+300+300")
    #print(root.geometry.)
    myClient = gdata.calendar.client.CalendarClient()
#     myClient.ClientLogin("projthee@gmail.com", "proj3pass", source = "Bla")
    myClient.ClientLogin("project3team07@gmail.com", "teamseven", source = "Bla")
    groupClient =  gdata.calendar.service.CalendarService()
    groupClient.ClientLogin("project3team07@gmail.com", "teamseven")
    
    app = CalendarSelectionWindow(root, myClient, groupClient)
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
import CalAccessMethods
from Tkinter import *
from ttk import *
import EventNamingWindow
import CalendarWindow
import MapWindow
import json


#create a window to allow the user to login to a given group a
class ConfirmEventWindow(Toplevel):
    
    def __init__(self, parent, calendarClient, calendarID, eventName, eventStart, eventEnd, eventPlace):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.calendarID = calendarID
        self.eventName = eventName
        self.eventStart = eventStart
        self.eventEnd = eventEnd
        self.eventPlace = eventPlace
        self.readableEventStart = self.parseDate(self.eventStart)
        self.readableEventEnd = self.parseDate(self.eventEnd)
#         print(self.readableEventDate)
        self.initUI()
        
    def initUI(self):
        #define widgets
        
        #Labels
        self.instructionsLabel = Label(self, text="Is this the event you want to add to the calendar?", background="lightgray")
        self.nameLabelPrompt = Label(self, text="Name:", background="lightgray")
        self.startLabelPrompt = Label(self, text="Starting time:", background="lightgray")
        self.endLabelPrompt = Label(self, text="Ending time:", background="lightgray")
        self.placeLabelPrompt = Label(self, text="Location:", background="lightgray")
        self.nameLabel = Label(self, text=self.eventName, background="lightgray")
        self.startLabel = Label(self, text=self.readableEventStart, background="lightgray")
        self.endLabel = Label(self, text=self.readableEventEnd, background="lightgray")
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
        
        self.startLabelPrompt.grid(row=2,column=0,padx=10,pady=5, sticky=E+W)
        self.startLabel.grid(row=2, column=1, padx=5, sticky=E+W)
        self.modifyDateButton.grid(row=2,column=2, rowspan=2,columnspan=2, padx=10, pady=5, sticky=N+S+E+W)
        
        self.endLabelPrompt.grid(row=3,column=0,padx=10, pady=5, sticky=E+W)
        self.endLabel.grid(row=3, column=1, padx=5, sticky=E+W)
        
        self.placeLabelPrompt.grid(row=4,column=0,padx=10, sticky=E+W)
        self.placeLabel.grid(row=4, column=1, padx=5, sticky=E+W)
        self.modifyPlaceButton.grid(row=4,column=2, columnspan=2, padx=10, pady=5, sticky=E+W)
        
        self.addEventButton.grid(row=5, column=2, padx=10, pady=5, sticky=E+W)
        self.cancelButton.grid(row=5, column=3, padx=10, pady=5, sticky=E+W)
#         
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Name":
                print("Name clicked")
                #hide the window, show the EventNamingWindow
                name = EventNamingWindow.EventNamingWindow(self.parent, self.calendarID, 
                    self.calendarClient, self.eventPlace, self.eventStart, self.eventEnd)
                self.withdraw()
            elif callerName == "Date":
                print("Date clicked")
                #hide the window, show the CalendarWindow
                calWin = CalendarWindow.CalendarWindow(self.parent, self.calendarClient, 
                    self.calendarID)
                self.withdraw()
            elif callerName == "Place":
                print("Place clicked")
                #hide the window, show the LocationWindow
                mapwin = MapWindow.MapWindow(self.parent, self.calendarClient, self.calendarID, 
                    self.eventStart, self.eventEnd) #sketchy
                self.withdraw()
            elif callerName == "Add":
                print("Add clicked")
                #add event, hide the window, show mainMenu Window
                self.makeEvent()
                self.withdraw()
            elif callerName == "Cancel":
                print("Cancel clicked")
                #hide the window, show mainMenu Window
                calWin = CalendarWindow.CalendarWindow(self.parent, self.calendarClient, 
                    self.calendarID)
                self.withdraw()



    def parseDate(self, rawDate):
        date = ""
        year = rawDate[:4:]
        month = self.parseMonth(rawDate[5:7:])
        day = rawDate[8:10:]
        time = rawDate[11:19:]
        timezone = rawDate[19::]
        
        date = month + " " + day + ", " + year + " at " + time + " (" + timezone + ")"
        return date
        
    def parseMonth(self, rawMonth):
        if rawMonth == "01":
            return "January"
        elif rawMonth == "02":
            return "February"
        elif rawMonth == "03":
            return "March"
        elif rawMonth == "04":
            return "April"
        elif rawMonth == "05":
            return "May"
        elif rawMonth == "06":
            return "June"
        elif rawMonth == "07":
            return "July"
        elif rawMonth == "08":
            return "August"
        elif rawMonth == "09":
            return "September"
        elif rawMonth == "10":
            return "October"
        elif rawMonth == "11":
            return "November"
        elif rawMonth == "12":
            return "December"

    def makeEvent(self):
        #create new event
        newEvent = CalAccessMethods.createNewEvent(self.eventName, self.eventStart, self.eventEnd, self.eventPlace)
        print(newEvent)
        print(newEvent.title.text)
        print(newEvent.when[0])
        print(newEvent.where[0])
        #find calendar with id self.CalendarID
        calendarFeed = self.calendarClient.GetOwnCalendarsFeed()
        for calendar in calendarFeed.entry:
            calID = CalAccessMethods.getCalendarID(calendar.id.text)
            if calID == self.calendarID:
                self.calendarEventFeedUri = self.calendarClient.GetCalendarEventFeedUri(self.calendarID)
                self.calendarClient.InsertEvent(new_event=newEvent, insert_uri=self.calendarEventFeedUri)
        return

    def membersOfGroup (self, groupName):
        emailAddresses=[]
        self.read_groupData('GroupDatabase.json')
        self.read_userData('UserDatabase.json')
        for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                for Users in self.userData['Users']:
                    emailAddresses.push(Users['googleid'])
                return emailAddresses
            
    def read_groupData(self, filename):
        json_data=open(filename)
        groupData=json.load(json_data)
        self.groupData=groupData
            
    def read_userData(self, filename):
        json_data=open(filename)
        userData=json.load(json_data)
        self.userData=userData
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    calendarID = "n3e76680gcabna20da1gaktg34%40group.calendar.google.com"
    client = gdata.calendar.client.CalendarClient()
    client.ClientLogin("project3team07", "teamseven", "CalReader")
    eventName = "Basketball"
    eventStart = "2013-08-09T10:57:00+02:00"
    eventEnd = "2013-08-09T11:57:00+02:00"
    eventPlace = "Space"
    app = ConfirmEventWindow(root, client, calendarID, eventName, eventStart, eventEnd, eventPlace)
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
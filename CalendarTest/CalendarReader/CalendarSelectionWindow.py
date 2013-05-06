'''
Created on Apr 26, 2013

@author: Cullen
'''

import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.data
import gdata.calendar.client
import CalAccessMethods
import CalendarWindow
import atom
from atom import *
from Tkinter import *
from ttk import *
import json
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders
import os

#create a window to allow the user to decide which of his/her calendars will be added to the group calendar
class CalendarSelectionWindow(Toplevel):
    
    def __init__(self, parent, calendarClient, groupClient, groupName):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.groupClient = groupClient
        self.groupName = groupName
        self.groupCalendarID = self.getGroupCalendarID(self.groupName)
        print(self.groupCalendarID)
        self.initUI()
        self.attachment = "C:\Users\casey\Downloads\GroupMeet.png"
        self.subject = "GroupMeet Invitation"
        self.message = """Howdy!
        This is an automatic notification provided by the GroupMeet service informing you that you have been invited to an event
        by the following group:

        GroupName: %s
        
        Please log in to the GroupMeet Service in order to view this event.

        Thanks!

        -GroupMeet Development Team""" % (self.groupName)
        
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
        #self.pack(fill=BOTH, expand = 1)
        
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

    def getGroupCalendarID(self, groupName):
        #get the ID of the group calendar
        calendar_feed = self.groupClient.GetOwnCalendarsFeed()
        for calendar_list_entry in calendar_feed.entry:
            if calendar_list_entry.title.text == groupName:
                return CalAccessMethods.getCalendarID(calendar_list_entry.id.text)  
    
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
                #update the group calendar with events from the selected calendar
                self.updateGroupCalendar()
                #subscribe the user to the group calendar
                #self.subscribeUser()
                #hide the window
                calWin = CalendarWindow.CalendarWindow(self.parent, self.groupClient, self.groupCalendarID)
                self.withdraw()
       
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
        #NOT WORKING YET; modify to take in a calendar id and a username
        
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
            eventsToAdd = []
            for cal in calendarsToAccess:
                print(cal.title.text)
                #get actual calendar id from calendar uri
                calID = CalAccessMethods.getCalendarID(cal.id.text)
                calEventFeedUri = self.calendarClient.GetCalendarEventFeedUri(calID)
                print (calEventFeedUri)
                calEventFeed = self.calendarClient.GetCalendarEventFeed(uri=calEventFeedUri)

                for calEvent in calEventFeed.entry:
                     #print (calEvent.title.text)
                     #print (calEvent.when)
                     eventsFound.append(calEvent)
                     #print (len(eventsFound))
                     
#                      CalAccessMethods.modifyEvent(calEvent, "John")
                     newEvent = gdata.calendar.data.CalendarEventEntry()
                     newEvent = CalAccessMethods.modifyEvent(calEvent, "User") #hard coded
                     #if it blows up here we haven't made events correctly yet
                     print(newEvent)
                     print("We made an event!")
                     eventsToAdd.append(newEvent)
#                      eventsToAdd.append(CalAccessMethods.modifyEvent(calEvent, "John"))
                print("")
            
                #make and store 
            
            #find group calendar
            #group calendar id should be accessed as part of a group; for now, use the following variable
            #calendarID=  "n3e76680gcabna20da1gaktg34%40group.calendar.google.com"
            calendarID = self.groupCalendarID
            self.groupCalendar = None
            
            server_calendar_feed = self.groupClient.GetOwnCalendarsFeed()
            for server_calendar in server_calendar_feed.entry:
                server_calendar_id = CalAccessMethods.getCalendarID(server_calendar.id.text)
                if server_calendar_id == calendarID:
                    self.groupCalendar = server_calendar
                    
            print(self.groupCalendar)

            for event in eventsToAdd:
                groupCalendarEventFeedUri = self.groupClient.GetCalendarEventFeedUri(calendarID)
                groupCalendarEventFeed = self.groupClient.GetCalendarEventFeed(uri=groupCalendarEventFeedUri)
                
                print("Attempting to add event to calendar")
                self.groupClient.InsertEvent(new_event=event,insert_uri=groupCalendarEventFeedUri)
                

        #self.quit()
        else:
            print("No calendars have been selected. Select a calendar to add before moving on.")
        return

        def mail(self, to, subject, text, attach):
        gmail_user = "project3team07@gmail.com"
        gmail_pwd = "teamseven"
        msg = MIMEMultipart()

        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()

    def sendInvites(self):
        rawEmailInfo = self.emailEntryString.get()
        emailAddresses = rawEmailInfo.split(",", )
        #print (emailAddresses)

        for item in emailAddresses:
            self.mail(item, self.subject, self.message, self.attachment) 
    def subscribeUser(self):
        self.sendInvites()
        #subscribe the user to the given calendar
        #get calendar from group calendar ID
        
#         print("group calendar id")
#         print(self.groupCalendarID)
#         groupCalendar = gdata.calendar.data.CalendarEntry()
#              
#         calendarFeed = self.groupClient.GetOwnCalendarsFeed()
#         for calendar in calendarFeed.entry:
#             calendarID = CalAccessMethods.getCalendarID(calendar.id.text)
#             print("calendar id")
#             print(calendarID)
#             if  self.groupCalendarID == calendarID:
#                 print("Attempting to subscribe to calendar")
#                 self.calendarClient.InsertCalendarSubscription(calendar)
#                 print("Calendar subscription successfull!")        
        #subscribe user to calendar
        
#           print 'Subscribing to the calendar with ID: %s' % id
#           calendar = gdata.calendar.data.CalendarEntry()
#           calendar.id = atom.data.Id(text=id)
#           returned_calendar = self.cal_client.InsertCalendarSubscription(calendar)
#           return returned_calendar
        return  
      
def main():
    
    root = Tk()
    root.geometry("600x300+300+300")
    #print(root.geometry.)
    myClient = gdata.calendar.client.CalendarClient()
    myClient.ClientLogin("projthee@gmail.com", "proj3pass", source = "Bla")
#    myClient.ClientLogin("project3team07@gmail.com", "teamseven", source = "Bla")
    groupClient =  gdata.calendar.client.CalendarClient()
    groupClient.ClientLogin("project3team07@gmail.com", "teamseven", source = "Calendar Access")
    
    app = CalendarSelectionWindow(root, myClient, groupClient, 'projthee@gmail.com')
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
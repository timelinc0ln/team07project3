import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
import exceptions
import string
from Tkinter import *
from ttk import *
from string import *
import GroupLoginWindow
import InvitationWindow
import NewUserWindow
import MapWindow
import webbrowser
import json
import os
import MapWindow

class CalendarWindow(Toplevel):
    def __init__(self, parent, client, calendarID, groupName):
            Toplevel.__init__(self)
            self.parent = parent
            self.groupClient = client
            self.calendarID = calendarID
            self.groupName = groupName
            self.initUI()  
          
#     def openGroupLogin(self, parent, client):
#         groupWindow = GroupLoginWindow.GroupLoginWindow(parent, self.userName.get(), client, client)
                 
    def initUI(self):
        #create widgets
        self.makeWidgets()
        
#         self.geometry("700x700+100+100")
        self.title("Calendar Window")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background="lightgray")
        
        #place widgets
        self.placeWidgets()
        
        #get embed code for calendar
        self.produceHTMLFile()
        #open calendar in browser
        
               
    def makeWidgets(self):
        #define stringvariables and widgets for the window
        #strings
        self.startDateString = StringVar()
        self.endDateString = StringVar()
        #labels
        self.calendarExplanationLabel = Label(self, text="On the linked calendar you can see when each member of the group is busy and when they are not.", background="lightgray")
        self.instructionsLabel = Label(self, text="Please enter the starting and ending dates for a new event in the following format: YYYY-MM-DDTHH:MM:SS.", background="lightgray")
        self.startDatePrompt = Label(self, text="Start date:", background="lightgray")
        self.endDatePrompt = Label(self, text="End date:", background="lightgray")
        #entries
        self.startDateEntry = Entry(self, textvariable=self.startDateString)
        self.endDateEntry = Entry(self, textvariable=self.endDateString)
        #buttons
        self.nextButton = Button(self, text="Next", command=lambda: self.callBack("Button", "Next"))
        self.quitButton = Button(self, text="Quit", command=lambda: self.callBack("Button", "Quit")) 
        
    def placeWidgets(self):
        self.calendarExplanationLabel.grid(row=0,column=0, columnspan=4, padx=10, pady=5, sticky=N+E+W)
        self.instructionsLabel.grid(row=1,column=0, columnspan=4, padx=10,pady=5,sticky=E+W) 
        self.startDatePrompt.grid(row=2,column=0, padx=10,pady=5, sticky=E+W)
        self.startDateEntry.grid(row=2,column=1, padx=10, pady=5, columnspan=3, sticky=E+W)          
        self.endDatePrompt.grid(row=3,column=0, padx=10, pady=5, sticky=E+W)
        self.endDateEntry.grid(row=3,column=1, padx=10, pady=5, columnspan=3, sticky=E+W) 
        self.nextButton.grid(row=4, column=2, padx=10, pady=10, sticky=E+W)
        self.quitButton.grid(row=4, column=3, padx=10, pady=10, sticky=E+W)
    
    def callBack(self, callerType, callerName):
        if callerType == "Button":
            if callerName == "Next":
                print("Next button pressed")
                #store the entered date values
                validStart = self.dateValid(self.startDateString.get())
                validEnd = self.dateValid(self.endDateString.get())
                
                if validStart and validEnd:
                    self.storeTimes()
                    self.openMapWindow()
            elif callerName == "Quit":
                print("Quit button pressed")
                #kill all windows, shut down program  
                self.withdraw()  
    
    def openMapWindow(self):
        mapWin = MapWindow.MapWindow(self.parent, self.groupClient, self.calendarID, self.eventStart, self.eventEnd, self.groupName)

    ValueError = exceptions.ValueError
    
    def validDateFormat(self, year, month, day, divider, hour, minute, second, rawDate):
        #compile date string again and make sure it matches the raw date
        date = Template("$yr-$mon-$d$div$hr:$min:$sec")
        newDate = date.substitute(yr=year, mon=month, d=day, div=divider, hr=hour, min=minute, sec=second)
        if rawDate != newDate:
            return False
        return True
    
    def dateValid(self, rawDate):
        #break date into segments
        year = rawDate[:4:]
        month = rawDate[5:7:]
        day = rawDate[8:10:]
        timeDivider = rawDate[10:11:]
        hour = rawDate[11:13:]
        min = rawDate[14:16:]
        sec = rawDate[17:19:]
        #check that the format is correct
        valFormat = self.validDateFormat(year, month, day, timeDivider, hour, min, sec, rawDate)
        #check for validity of each segment
        valYear = self.validYear(year)
        valMonth = self.validMonth(month)
        valDay = self.validDay(month,day)
        valDivider = self.validDivider(timeDivider)
        valHour = self.validHour(hour)
        valMin = self.validMinute(min)
        valSec = self.validSecond(sec)
        
        if valFormat and valYear and valMonth and valDay and valDivider and valHour and valMin and valSec:
            return True
        return False
     
    def validYear(self, rawYear):
        try:
            year = string.atoi(rawYear)
            return True
        except ValueError:
            return False
        
    def validMonth(self, rawMonth):
        try:
            month = string.atoi(rawMonth)
            if month > 12 or month < 0:
                return False
            return True
        except ValueError:
            return False
    
    def validDay(self, rawMonth, rawDay):
        try:
            month = string.atoi(rawMonth)
            day = string.atoi(rawDay)
        
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day > 31:
                    return False
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day > 30:
                    return False
            elif month == 2:
                if day > 28:    #ignore leap year
                    return False
            elif day < 1:
                return False
            return True
        except ValueError:
            return False
    
    def validDivider(self, divider):
        if divider != "T":
            return False
        return True
    
    def validHour(self, rawHour):
        try:
            hour = string.atoi(rawHour)
            if hour > 23 or hour < 0:
                return False
            return True
        except ValueError:
            return False
    
    def validMinute(self, rawMinute):
        try:
            minute = string.atoi(rawMinute)
            if minute>59 or minute < 0:
                return False
            return True
        except ValueError:
            return False
        
    def validSecond(self, rawSecond):
        try:
            second = string.atoi(rawSecond)
            if second>59 or second< 0:
                return False
            return True
        except ValueError:
            return False

    
    def storeTimes(self):
        self.eventStart=self.startDateString.get()
        self.eventEnd=self.endDateString.get()

    #create an HTML file with the user's calendar
    def produceHTMLFile(self):
        message = """<iframe src="https://www.google.com/calendar/embed?mode=WEEK&amp;height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;src=""" 
        message += self.calendarID 
        message += """&ctz=America/Chicago" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>"""
        #check to see if file exists, if so delete it
        try:
            os.remove('calendar.html')
        except OSError:
            pass
        fh = open("calendar.html", "w")
        fh.write(message)
        fh.close()
        webbrowser.open('calendar.html')
                
                
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    calendarID = "n3e76680gcabna20da1gaktg34%40group.calendar.google.com"
    client = gdata.calendar.client.CalendarClient()
    client.ClientLogin("project3team07", "teamseven", "CalReader")
    app = CalendarWindow(root, client, calendarID)
    root.mainloop()
    
if __name__ == '__main__':
    main()
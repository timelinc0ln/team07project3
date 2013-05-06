'''
Created on May 2, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.data
import gdata.calendar.client
import atom
import datetime
from atom import *
from Tkinter import *
from ttk import *

#gets calendar id from a calendar feed entry
def getCalendarID(rawCalendarString):
    return rawCalendarString[55::]

def createCalendar(title='New Calendar', description='No Description',
      time_zone='America/Chicago', hidden=False, location='College Station',
      color='#2952A3'):
    
    calendar = gdata.calendar.data.CalendarEntry()
    calendar.title = atom.data.Title(text=title)
    calendar.summary = atom.data.Summary(text=description)
    calendar.where.append(gdata.calendar.data.CalendarWhere(value=location))
    calendar.color = gdata.calendar.data.ColorProperty(value=color)
    calendar.timezone = gdata.calendar.data.TimeZoneProperty(value=time_zone)

    if hidden:
      calendar.hidden = gdata.calendar.data.HiddenProperty(value='true')
    else:
      calendar.hidden = gdata.calendar.data.HiddenProperty(value='false')

    return calendar


def _InsertSubscription(id=''):
    if id != '':
        calendar = gdata.calendar.data.CalendarEntry()
        calendar.id = atom.data.Id(text=id)
        return calendar

def createNewEvent(eventName, eventStartTime, eventEndTime, eventLocation):
    #given a name, rudimentary event time information, and a location, make an event
    newEvent = gdata.calendar.data.CalendarEventEntry()
    #set title
    newEvent.title=atom.data.Title(text=eventName)
    #set time
    newEvent.when.append(gdata.data.When(start=eventStartTime,end=eventEndTime))
    #set location
    newEvent.where.append(gdata.data.Where(value=eventLocation))
    
    return newEvent

def modifyEvent(rawEvent, userName):
    '''
    Create a new calendar event identical to rawEvent, except with title "Username Unavailable"
    '''
    newEvent = gdata.calendar.data.CalendarEventEntry()
    eventTitle = userName + " Unavailable"
    newEvent.title = atom.data.Title(text=eventTitle)
    #copy a recurring event
    if rawEvent.recurrence is not None:
        print (rawEvent.recurrence.text)
        newEvent.recurrence = gdata.data.Recurrence(text=rawEvent.recurrence.text)
    else:
        if len(rawEvent.when) != 0:
            print ("we have a time")
            print("starting time")
            start_time = rawEvent.when[0].start
            print(start_time)
            print("ending time")
            end_time = rawEvent.when[0].end
            print(end_time)
            print("adding time")
            newEvent.when.append(gdata.data.When(start=start_time, end=end_time))
    return newEvent
  
def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S")
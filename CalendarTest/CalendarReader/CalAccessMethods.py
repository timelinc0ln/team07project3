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
    
    """Creates a new calendar using the specified data."""
    print 'Creating new calendar with title "%s"' % title
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


def _InsertSubscription(id='python.gcal.test%40gmail.com'):
    """Subscribes to the calendar with the specified ID."""
    print 'Subscribing to the calendar with ID: %s' % id
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
#     event.content = atom.data.Content(text=content)
#     event.where.append(gdata.data.Where(value=where))
# 
#     if recurrence_data is not None:
#       # Set a recurring event
#       event.recurrence = gdata.data.Recurrence(text=recurrence_data)
#     else:
#       if start_time is None:
#         # Use current time for the start_time and have the event last 1 hour
#         start_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
#         end_time = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',
#             time.gmtime(time.time() + 3600))
#       event.when.append(gdata.data.When(start=start_time,
#           end=end_time))
#     "
#     newEvent.when = rawEvent.when

    print(newEvent.title)
    for time in newEvent.when:
        print("Event time")
        print(time.start)
        print(time.end)
        print("")
        

#     print(newEvent.when)
    print("")
    
    print(rawEvent.title)
    for time in rawEvent.when:
        print("Event time")
        print(time.start)
        print(time.end)
        print("")
#     print(rawEvent.when)
    return newEvent
  
def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S")
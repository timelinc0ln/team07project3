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

def modifyEvent(rawEvent, userName):
    '''
    Create a new calendar event identical to rawEvent, except with title "Username Unavailable"
    '''
    newEvent = gdata.calendar.data.CalendarEntry()
    
    newEvent.title = userName + " Unavailable"
    newEvent.quick_add = rawEvent.quick_add
    newEvent.send_event_notifications = rawEvent.send_event_notifications
    newEvent.sync_event = rawEvent.sync_event
    
    
    '''
    anyone_can_add_self = anyone_can_add_self
    extended_property = [CalendarExtendedProperty]
    sequence = SequenceNumberProperty
    guests_can_invite_others = GuestsCanInviteOthersProperty
    guests_can_modify = GuestsCanModifyProperty
    guests_can_see_guests = GuestsCanSeeGuestsProperty
    georss_where = gdata.geo.data.GeoRssWhere
    private_copy = rawEvent.private_copy
    suppress_reply_notifications = SuppressReplyNotificationsProperty
    uid = IcalUIDProperty
    where = [gdata.data.Where]
    when = [When]
    who = [gdata.data.Who]
    transparency = gdata.data.Transparency
    comments = gdata.data.Comments
    event_status = gdata.data.EventStatus
    visibility = gdata.data.Visibility
    recurrence = gdata.data.Recurrence
    recurrence_exception = [gdata.data.RecurrenceException]
    original_event = gdata.data.OriginalEvent
    reminder = [gdata.data.Reminder]
    '''
    
    print(newEvent)
    print("")
    print(rawEvent)
  
  
def getTime():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%S")
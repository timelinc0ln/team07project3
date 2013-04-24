import gdata.calendar.service
import gdata.service
import atom.service
import gdata.calendar
import atom
import getopt
import sys
import string
import time
import cgi

parameters = cgi.FieldStorage()

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.email = 'project3team07@domain.com'
calendar_service.password = 'teamseven'
calendar_service.source = 'Google-Calendar_Python_Sample-1.0'
calendar_service.ProgrammaticLogin()
authsub_token = parameters['token']

def GetAuthSubUrl():
  next = 'http://www.coolcalendarsite.com/welcome.pyc'
  scope = 'https://www.google.com/calendar/feeds/'
  secure = False
  session = True
  calendar_service = gdata.calendar.service.CalendarService()
  return calendar_service.GenerateAuthSubURL(next, scope, secure, session);

authSubUrl = GetAuthSubUrl();
print '<a href="%s">Login to your Google account</a>' % authSubUrl

calendar_service = gdata.calendar.service.CalendarService()
calendar_service.SetAuthSubToken(authsub_token)
calendar_service.UpgradeToSessionToken()
feed = calendar_service.GetCalendarListFeed()
for i, a_calendar in enumerate(feed.entry):
  print '\t%s. %s' % (i, a_calendar.title.text,)

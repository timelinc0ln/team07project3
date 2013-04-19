'''
Created on Apr 18, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service

client = gdata.docs.service.DocsService()
client.ClientLogin('project3team07@gmail.com', 'teamseven')

documents_feed = client.GetDocumentListFeed()

client2 = gdata.calendar.service.CalendarService()
client2.ClientLogin('project3team07@gmail.com', 'teamseven', None, None, None, None, None, None)



calendar_feed = client2.GetAllCalendarsFeed()
calendar_feed


for document_entry in documents_feed.entry:
    print(document_entry.title.text)
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
#client2.ClientLogin(username, password, account_type, service, auth_service_url, source, captcha_token, captcha_response)
client2.ClientLogin('project3team07@gmail.com', 'teamseven', "HOSTED_OR_GOOGLE", "cl", None, None, None, None)

print(client2.account_type)

calendar_feed = client2.GetOwnCalendarsFeed()

#comments and stuff
#comments
#comments


for document_entry in documents_feed.entry:
    print(document_entry.title.text)
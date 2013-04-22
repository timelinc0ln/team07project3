'''
Created on Apr 18, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
from Tkinter import Tk, BOTH, Entry
from ttk import Frame, Button, Style 

class CalendarFrame(Frame):
    username = ""
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Calendar Entry")
        self.style = Style()
        self.style.theme_use("alt")
        self.pack(fill = BOTH, expand = 1)
        
        quitButton = Button(self, text = "Quit", command = self.quit)
        quitButton.place(x = 425, y = 475)
   # def googleLogin(self):
        entry = Entry(self)
        entry.place(x = 200, y = 70)
        username = entry.get()
    def getUsername(self):
        return self.username
    
client = gdata.docs.service.DocsService()
client.ClientLogin('project3team07@gmail.com', 'teamseven')

# documents_feed = client.GetDocumentListFeed()
# 
# client2 = gdata.calendar.service.CalendarService()
# #client2.ClientLogin(username, password, account_type, service, auth_service_url, source, captcha_token, captcha_response)
# client2.ClientLogin('project3team07@gmail.com', 'teamseven', "HOSTED_OR_GOOGLE", "cl", None, None, None, None)
# 
# print(client2.account_type)
# 
# calendar_feed = client2.GetCalendarListFeed()
# for calendar_list_entry in calendar_feed.entry:
    
#     if calendar_list_entry.title.text == "Test Calendar":
#         # print(calendar_list_entry.title.text)
#         calendar_event_feed = client2.GetCalendarEventFeed(calendar_list_entry.GetCalendarListEntryUri())
#         for calendar_event_list_entry in calendar_event_feed.entry:
#             print(calendar_event_list_entry.title.text)
#         print("I found it")

# for document_entry in documents_feed.entry:
#     print(document_entry.title.text)
    
def main():
    root = Tk()
    root.geometry ("500x500+300+300")
    app = CalendarFrame(root)
    root.mainloop()
    print(app.getUsername())
    
if __name__ == '__main__':
        main()
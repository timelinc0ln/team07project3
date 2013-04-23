'''
Created on Apr 18, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *


client = gdata.docs.service.DocsService()
client.ClientLogin('project3team07@gmail.com', 'teamseven')

documents_feed = client.GetDocumentListFeed()

client2 = gdata.calendar.service.CalendarService()
#client2.ClientLogin(username, password, account_type, service, auth_service_url, source, captcha_token, captcha_response)
client2.ClientLogin('project3team07@gmail.com', 'teamseven', "HOSTED_OR_GOOGLE", "cl", None, None, None, None)

print(client2.account_type)

calendar_feed = client2.GetCalendarListFeed()
for calendar_list_entry in calendar_feed.entry:
    
    if calendar_list_entry.title.text == "Test Calendar":
       print(calendar_list_entry.title.text)
       #calendar_event_feed = calendar_list_entry.GetCalendarEventFeed()
        #for calendar_event_list_entry in calendar_event_feed.entry:
            #print(calendar_event_list_entry.title.text)
       print("I found it")

#comments and stuff


calendar_feed = client2.GetAllCalendarsFeed()
#print(calendar_feed)
#calendar_feed = 
#client2.CalendarClient.InsertEvent()


#<<<<<<< HEAD

#=======
#=======
class LoginWindow(Frame):
    quitButton = None
    submitButton = None
    testMessage = None
    userNameEntry = None
    userPassEntry = None
    userName = None
    userPass = None
    haveSubmitted = None
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        #define widgets for window
        quitButton = Button(self, text="Cancel", command=lambda: self.callBack("Button", "Quit"))
        submitButton = Button(self, text="Submit", command=lambda: self.callBack("Button", "Submit"))
        #testMessage = Message(self)
        self.userName = StringVar()
        self.userPass = StringVar()
        self.userNamePrompt = Label(self, text="User Name:")
        self.userPassPrompt = Label(self, text="Password:")
        self.userNameEntry = Entry(self, textvariable=self.userName)
        self.userPassEntry = Entry(self, textvariable=self.userPass)
        
        #set up window theme
        self.parent.title("Login to GroupMeet")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        
        #place widgets
        self.userNamePrompt.place(x=0, y=25)
        self.userNameEntry.place(x=80, y=25)
        self.userPassPrompt.place(x=260, y=25)
        self.userPassEntry.place(x=335, y=25)
        submitButton.place(x=80, y=80)
        quitButton.place(x=180, y=80)
    
    def callBack(self, callerType, callerName):
        #handle each widget's callback
        
        #Buttons
        if callerType == "Button":
            if callerName == "Submit":
                print("Submit button pressed")
                print(self.userName.get())
                print(self.userPass.get())
                self.haveSubmitted = True
            elif callerName == "Quit":
                print("Exiting")
                self.quit()
        #Entries
        if callerType == "Entry":
            if callerName == "UserName":
                self.userName = self.userNameEntry.textvariable.get()
                
    
    
                
#>>>>>>> Reading in a user name
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("window title")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand = 1)
        
        quitButton = Button(self,text="Quit", command=self.quit)
        quitButton.place(x=50, y=50)
        v = None
        
        m = Message(self, textvariable = v)
        m.place(x = 25, y = 25)
        
        myEntry = Entry(self, textvariable = v)
        myEntry.place (x = 150, y = 50)
        
        p = None
        
        printButton = Button(self,text="Print")
        printButton.place(x = 400, y = 50)
        
        

for document_entry in documents_feed.entry:
    print(document_entry.title.text)
    
    
    
def main():
    
    root = Tk()
    root.geometry("600x200+300+300")
    #app = Example(root)
    app = LoginWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()

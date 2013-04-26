'''
Created on Apr 18, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
from Tkinter import *
from ttk import *



# client = gdata.docs.service.DocsService()
# client.ClientLogin('project3team07@gmail.com', 'teamseven')
# 
# documents_feed = client.GetDocumentListFeed()
# 
# client2 = gdata.calendar.service.CalendarService()
# # client2.ClientLogin(username, password, account_type, service, auth_service_url, source, captcha_token, captcha_response)
# client2.ClientLogin('project3team07@gmail.com', 'teamseven', "HOSTED_OR_GOOGLE", "cl", None, None, None, None)
# 
# print(client2.account_type)
# 
# calendar_feed = client2.GetCalendarListFeed()
# for calendar_list_entry in calendar_feed.entry:
#     
#     if calendar_list_entry.title.text == "Test Calendar":
#        print(calendar_list_entry.title.text)
#        #calendar_event_feed = calendar_list_entry.GetCalendarEventFeed()
#         #for calendar_event_list_entry in calendar_event_feed.entry:
#             #print(calendar_event_list_entry.title.text)
#        print("I found it")
# 
# 
# 
# 
# calendar_feed = client2.GetAllCalendarsFeed()

#convert MessageWindow into a class (do later)

class Window(object):
    """ Main Window For Program. Additional windows created from this one"""
    isRunning = True
    def __init__(self, parent): 
        self.root = parent
        self.root.title("Main Window")
        self.frame = Frame(parent)
        self.frame.pack()
        self.checkWindows()
        self.hide()
        
    def listener(self, arg1, arg2=None):
        self.show()

    def hide(self):
        self.root.withdraw()
        
    def checkWindows(self):
        while self.isRunning == True:
            self.openWindow()
    
    def openWindow(self):
        """ Add new window classes here"""
        logWindow = LoginWindow()
        calWindow = CalendarWindow()   
    
    def show(self):
        self.root.update()
        self.root.deiconify()
        
class LoginWindow(Toplevel):
#     quitButton = None
#     submitButton = None
#     testMessage = None
#     userNameEntry = None
#     userPassEntry = None
#     userName = None
#     userPass = None
    haveLogged = False
    windowHeight = None
    windowWidth = None
    
<<<<<<< HEAD
    def __init__(self):
        Toplevel.__init__(self)
=======
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_width()
        print(self.windowWidth)
>>>>>>> Group Login Window has been designed
        self.initUI()
    
    def initUI(self):
        # setup window size
        self.geometry("600x200+300+300")
        #define widgets for window
        self.quitButton = Button(self, text="Cancel", command=lambda: self.callBack("Button", "Quit"))
        submitButton = Button(self, text="Submit", command=lambda: self.callBack("Button", "Submit"))
        #testMessage = Message(self)
        self.userName = StringVar()
        self.userPass = StringVar()
        self.userNamePrompt = Label(self, text="User Name:")
        self.userPassPrompt = Label(self, text="Password:")
        self.userNameEntry = Entry(self, textvariable=self.userName)
        self.userPassEntry = Entry(self, textvariable=self.userPass, show="*")
        
        #set up window theme
        self.title("Login to GroupMeet")
        self.style = Style()
        self.style.theme_use("clam")
        # self.pack(fill=BOTH, expand = 1)
        
        #place widgets
        self.userNamePrompt.place(x=0, y=25)
        self.userNameEntry.place(x=80, y=25)
        self.userPassPrompt.place(x=260, y=25)
        self.userPassEntry.place(x=335, y=25)
        submitButton.place(x=80, y=80)
        self.quitButton.place(x=180, y=80)
        
    def onClose(self):
        self.destroy()
    
    def callBack(self, callerType, callerName):
        #handle each widget's callback
        
        #Buttons
        if callerType == "Button":
            if callerName == "Submit":
                print("Submit button pressed")
                self.Login()
                #if self.haveLogged == True:
                    #getting this to work may take some doing
                    #self.messageWindow()
                    #self.quit()
            elif callerName == "Quit":
                print("Exiting")
                self.parent.isRunning = False
                self.quit()
        #Entries - does nothing, but shows how to use elif
        if callerType == "Entry":
            if callerName == "UserName":
                self.userName = self.userNameEntry.textvariable.get()
     
                
    def Login(self):
        calendarService = gdata.calendar.service.CalendarService()
        calendarService.email = self.userName.get()
        calendarService.password = self.userPass.get()
        calendarService.source = 'CalReader' # not really sure what this is
        try:
            calendarService.ProgrammaticLogin() #add an if statement or something to catch a bad authentication error;
            print(self.userName.get())
            print(self.userPass.get())
            self.haveLogged = True
            self.hide()
        except gdata.service.BadAuthentication:
            print("Bad user name or password.")
            
    def hide(self):
        self.withdraw()     
        
    def messageWindow(self):
        if self.haveLogged == True:
            calendarFrame = Toplevel()
            message = "The calendar will go here"
            Label(calendarFrame, text = message).pack()
            calendarFrame.geometry("700x700+100+100")
            #quitButton = Button(calendarFrame, text="OK", command=lambda: self.callBack("Button", "Quit"))
            quitButton = Button(calendarFrame, text = 'OK', command = calendarFrame.destroy).pack(side = BOTTOM)  
            
class CalendarWindow(Toplevel):
    def __init__(self):
        if LoginWindow.haveLogged == True:
            Toplevel.__init__(self)
            self.initUI()
    
    def initUI(self):
        self.geometry("700x700+100+100")
        self.title("Calendar Window")
        quitButton = Button(self, text = 'OK', command = self.destroy).pack(side = BOTTOM)
               
                
#>>>>>>> Reading in a user name
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("window title")
        self.style = Style()
        self.style.theme_use("step")
        self.pack(fill=BOTH, expand = 1)
        
        quitButton = Button(self,text="Quit", command=self.quit)
        quitButton.place(x=350, y=675)
        v = None
        
        m = Message(self, textvariable = v)
        m.place(x = 25, y = 25)
        
        myEntry = Entry(self, textvariable = v)
        myEntry.place (x = 150, y = 50)
        
        p = None
        
        printButton = Button(self,text="Print")
        printButton.place(x = 400, y = 50)

        

# for document_entry in documents_feed.entry:
#     print(document_entry.title.text)
    
    
    
def main():
    
    root = Tk()
    root.geometry("600x200+300+300")
    # app = Example(root)
    app = Window(root)
#     app = Window.MainWindow(root)
    print(root.winfo_reqwidth())
    #app = Example(root)
    app = LoginWindow(root)
    print(app.parent.winfo_width())
    root.mainloop()
    
if __name__ == '__main__':
    main()

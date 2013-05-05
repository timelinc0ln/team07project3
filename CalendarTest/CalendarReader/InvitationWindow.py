'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
import smtplib
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import Encoders
from Tkinter import *
from ttk import *
import os


#create a window to allow the user to login to a given group a
class InvitationWindow(Toplevel):   # also need to pass in Group username/password
    groupUsername = "Test" # pass these in later
    groupPassword = "12345"
    attachment = "C:\Users\casey\Downloads\GroupMeet.png"
    subject = "GroupMeet Invitation"
    message = """Howdy!

            This is an automatic notificaiton that you have been invited to a group on the GroupMeet service.

            Here is the information regarding your new GroupMeet group account:

            Group Username: %s
            Group Password: %s

            Please save this information for your use. You will need to make a GroupMeet account to access the features of this group.

            Thanks!

            -GroupMeet Development Team""" % (groupUsername, groupPassword) 

    def __init__(self, parent, calendarClient): 
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.calendarClient = calendarClient
        self.initUI()
        
    def initUI(self):
        #define strings for use in widgets
        self.emailEntryString = StringVar()
        #define widgets
        self.instructionMessage = Label(self, text="Enter the email addresses of the invitees below, separated by commas", background='lightgray')
        self.emailEntryPrompt = Label(self, text="Event name:", background='lightgray')
        self.emailEntry = Entry(self, textvariable = self.emailEntryString, width=30)
        self.confirmButton = Button(self, text="Confirm", command=lambda: self.callBack("Button","Confirm"))
        self.skipButton = Button(self, text="Skip", command=lambda: self.callBack("Button","Skip"))
        
        #design window
        self.title("Invite Friends")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background='lightgray')
        
        #place widgets
        self.instructionMessage.grid(row=0, column=0, columnspan=4, pady=5)
        self.emailEntryPrompt.grid(row=1, column=0, padx=5, sticky=E)
        self.emailEntry.grid(row=1, column=1, columnspan=2,padx=10, pady=5, sticky=W+S)
        self.confirmButton.grid(row=2, column=2, padx=0, pady=5, sticky=E+S)
        self.skipButton.grid(row=2, column=3, padx=10, pady=5, sticky=E+W+S)
        
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            if callerName == "Confirm":
                print("Confirm clicked")
                #email every email address in the list
                self.sendInvites()
            elif callerName == "Skip":
                print("Skip clicked")
                #hide the window, clear self.nameEntryString, show map window

    def mail(self, to, subject, text, attach):
        gmail_user = "project3team07@gmail.com"
        gmail_pwd = "teamseven"
        msg = MIMEMultipart()

        msg['From'] = gmail_user
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
               'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()

    def sendInvites(self):
        rawEmailInfo = self.emailEntryString.get()
        emailAddresses = rawEmailInfo.split(",", )
        #print (emailAddresses)

        for item in emailAddresses:
            self.mail(item, self.subject, self.message, self.attachment)
        # SERVER = "smtp-relay.tamu.edu"
        # FROM = "project3team07@gmail.com"
        # TO = ["patrickcasey2014@gmail.com"]
        # SUBJECT = "Here is a test message"
        # TEXT = "Here is a conformation email."
        # message = """\
        # From: %s
        # To: %s
        # Subject: %s

        # %s
        # """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        # try:
        #     server = smtplib.SMTP(SERVER)
        #     server.sendmail(FROM,TO, message)
        #     print("Successfully sent email")
        # except:
        #     print("Error: unable to send email")
    
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    app = InvitationWindow(root, gdata.calendar.client.CalendarClient())
    root.mainloop()

if __name__ == '__main__':
    main()

        
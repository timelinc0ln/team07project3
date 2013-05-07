'''
Created on Apr 25, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.client
import gdata.calendar.data
import datetime
import CalAccessMethods
import InvitationWindow
import CalendarWindow
import CalReader
import CalendarSelectionWindow
from Tkinter import *
from ttk import *
import json
# User logs in to group they are not a part of
# new group is registered- added to user's list of groups
#create a window to allow the user to login to a given group a
class GroupLoginWindow(Toplevel):    
    def __init__(self, parent, userName, calendarClient, groupClient):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.windowWidth = parent.winfo_reqwidth()+parent.winfo_x()
        self.windowHeight = parent.winfo_reqheight()
        self.userName = userName
        self.calendarClient = calendarClient
        self.groupClient = groupClient
        self.read_groupData('GroupDatabase.json')
        self.read_userData('UserDatabase.json')
        self.initUI()
        
    def initUI(self):
        self.defineWidgets()
        
        #design window
        self.title("Group Login")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background="lightgray")
        
        self.placeWidgets()
        
    def defineWidgets(self):
        #define strings for use in widgets
        self.newNameString = StringVar()
        self.newPassString = StringVar()
        self.newConfirmString = StringVar()
        self.existNameString = StringVar()
        self.existPassString = StringVar()
        self.errorLabelString = StringVar()
        #define widgets
        #widgets for "NEW" group side
        self.newHeader = Label(self, text="Register A New Group", underline=0, background = "lightgray")
        self.newName = Entry(self, textvariable=self.newNameString)
        self.newPass = Entry(self, textvariable=self.newPassString, show ='*')
        self.newConfirm = Entry(self, textvariable=self.newConfirmString, show ='*')
        self.newNamePrompt = Label(self, text="Group Name:", background = "lightgray")
        self.newPassPrompt = Label(self, text="Password:", background = "lightgray")
        self.newConfirmPrompt = Label(self, text="Confirm Password:", background = "lightgray")
        self.registerButton = Button(self, text="Register Group", command=lambda: self.callBack("Button","Register"))
        
        #widgets for "EXISTING" group side
        self.existHeader = Label(self, text="Access An Existing Group", underline=0, background = "lightgray")
        self.existName = Entry(self, textvariable=self.existNameString)
        self.existPass= Entry(self, textvariable=self.existPassString, show="*")
        self.existNamePrompt = Label(self, text="Group Name:", background = "lightgray")
        self.existPassPrompt = Label(self, text="Password:", background = "lightgray")
        self.loginButton = Button(self, text="Login", command=lambda: self.callBack("Button","Login"))
        
        
    def placeWidgets(self):
        #handle New side
        self.newHeader.grid(row=0, column=0, columnspan=2, pady=5)
        self.newNamePrompt.grid(row=1, column=0, padx=5, pady=5, sticky=E+W)
        self.newName.grid(row=1,column=1, padx=10, sticky=W)
        self.newPassPrompt.grid(row=2,column=0, padx=5, pady=5, sticky=E+W)
        self.newPass.grid(row=2,column=1, padx=10, sticky=E)
        self.newConfirmPrompt.grid(row=3,column=0, padx=5, pady=5, sticky=E+W)
        self.newConfirm.grid(row=3,column=1, padx=10)
        self.registerButton.grid(row=4,column=1, padx=10, pady=5, sticky= E+W+S)
        
        #handle Existing side
        self.existHeader.grid(row=0, column=3, columnspan=2, pady=5)
        self.existNamePrompt.grid(row=1,column=3, pady=5, sticky=E+W)
        self.existName.grid(row=1,column=4, padx=10)
        self.existPassPrompt.grid(row=2,column=3, pady=5, sticky=E+W)
        self.existPass.grid(row=2,column=4, padx=10)
        self.loginButton.grid(row=4,column=4, padx=10, pady=5, sticky=E+W+S)

    
    def read_groupData(self, filename):
        json_data=open(filename)
        groupData=json.load(json_data)
        self.groupData=groupData
    
    def write_groupData(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(json.dumps(self.groupData, sort_keys=True, indent=2))
            
    def read_userData(self, filename):
        json_data=open(filename)
        userData=json.load(json_data)
        self.userData=userData

    def write_userData(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(json.dumps(self.userData, sort_keys = True, indent = 2))   
        
    def allFieldsCompleted(self, callerName):
        if callerName == "Register":
            if self.newNameString.get() == "":
                return False
            if self.newPassString.get() == "":
                return False
            if self.newConfirmString.get() == "":
                return False
            return True
            
        elif callerName == "Login":
            if self.existNameString.get() == "":
                return False
            if self.existPassString.get() == "":
                return False
            return True
    
    def callBack(self, callerType, callerName):
        #Buttons
        if callerType == "Button":
            
            if callerName == "Register":
                
                print("Register clicked")
                if self.allFieldsCompleted(callerName):
                    
                    groupName = self.newNameString.get()
                    groupPass = self.newPassString.get()
                    confirmPass = self.newConfirmString.get()
                    
                    if self.groupExists(groupName) == True:
                        print ("Group name is already taken. Enter a different name.")
                    else:
                        print ("Group name is available!")
                        if self.confirmPassword(groupPass, confirmPass):
                            if groupPass != "" and confirmPass != "":
                                print("Adding new group!")
                                self.addGroup(groupName, groupPass, self.userName);
                                #minimize and go to CalendarSelectionWindow
                        else :
                            print("Passwords don't match.")
                else:
                    print ("Invalid registration; please fill all entry fields.")
            #break this down and make it more legible
            elif callerName == "Login":
                print("Login clicked")
                if self.allFieldsCompleted(callerName):   
                    groupName = self.existNameString.get()
                    groupPass = self.existPassString.get()
                    if self.groupExists(groupName) == True:
                        print ("Group exists. Attempting to login.")
                        if self.groupLogin(groupName, groupPass) == True:
                            print("Login Successful!")
                            #determine whether or not the user is part of the group
                            if self.userInGroup(groupName, self.userName) == True:
                                #pass group information to CalendarWindow
                                print("Existing user")
                                calWindow = CalendarWindow.CalendarWindow(self.parent, self.calendarClient, self.getGroupCalendarID(groupName), groupName)
                                #calWindow = CalendarSelectionWindow.CalendarSelectionWindow(self.parent, self.calendarClient, self.groupClient)
                                self.withdraw()
                            else:
                                #pass group information to CalendarSelectionWindow
                                print("New user")
                                self.updateUserJson(groupName, self.userName)
                                self.updateGroupJson(groupName, self.userName)
                                calWindow = CalendarSelectionWindow.CalendarSelectionWindow(self.parent, self.calendarClient, self.groupClient, groupName)
                                self.withdraw()
                        else:
                            print("Incorrect Password. Login Failed.")
                    else:
                        print ("Group does not exist. Please enter the name of a valid group!")
                else:
                    print ("Invalid login; please fill all entry fields.")                        
       
    def confirmPassword (self, password, confirmPassword):
        #compare password and confirmPassword; if they match, return True, else return false
        if password==confirmPassword:
            return True;
        return False;
       
    def groupExists(self, groupName):
        #Compare group with name GroupName to other groups in data server; if group exists, return true, else return false
        for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                return True
        return False 
    
    def addGroupCalendar(self,groupName):
        #create a new calendar on the server account for the group
        calendarDescription = "Calendar for group " + groupName + "."
        groupCalendar = CalAccessMethods.createCalendar(title=groupName, description=calendarDescription)
        self.groupClient.InsertCalendar(new_calendar=groupCalendar, visibility="public")
    
    def getGroupCalendarID(self,groupName):
        #get the ID of the group calendar
        calendar_feed = self.groupClient.GetOwnCalendarsFeed()
        for calendar_list_entry in calendar_feed.entry:
            if calendar_list_entry.title.text == groupName:
                return CalAccessMethods.getCalendarID(calendar_list_entry.id.text)
    
    def addGroup(self, groupName, password, memberName):
        #create the calendar the group will be using
        self.addGroupCalendar(groupName)
        #get the ID of the calendar
        groupCalendarID = self.getGroupCalendarID(groupName)
        #get current time
        currTime = CalAccessMethods.getTime()
        #add group to database
        self.groupData['Groups'].append({"groupName":groupName, "dateCreated":currTime,
                                          "calendarId":groupCalendarID, "password":password, 
                                          "members":[{"name":memberName}]})
        self.write_groupData('GroupDatabase.json')
        #add group name to user's list of groups
        self.updateUserJson(groupName, memberName)

        #prompt user to add collaborators 
        addInvites = InvitationWindow.InvitationWindow(self.parent, self.calendarClient, self.groupClient, groupName, password) 
        self.withdraw() 
        
        return
    
    def updateUserJson(self, groupName, memberName):
        for Users in self.userData['Users']:
            if Users['username']==memberName:
                Users["grouplist"].append({"groupname":groupName})
        self.write_userData('UserDatabase.json')

    def updateGroupJson(self, groupName, memberName):
        for Group in self.groupData['Groups']:
            if Group['groupName']==groupName:
                Group["members"].append({"name":memberName})
        self.write_groupData('GroupDatabase.json')
        
    def userInGroup(self, groupName, userName):
        #determine whether userName is in group groupName
        for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                for Members in Groups['members']:
                    if Members['name'] == userName:
                        return True
        return False
    
    # def showCalWindow(self):
    #     groupName = self.existNameString.get()
    #     self.CalendarID = self.getGroupCalendarID(groupName)
    #     calWindow = CalendarWindow.CalendarWindow(self.parent, self.client, self.CalendarID)
        
    
    def groupLogin(self, groupName, groupPass):
        #find the appropriate group
        for Groups in self.groupData['Groups']:
            if Groups['groupName']==groupName:
                #check to see if groupPass and the stored password match
                if self.confirmPassword(groupPass, Groups['password']) == True:
                    return True
                else:
                    return False
        return False
        
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    #print(root.geometry.)
    userName = "Spartacus"
    calendarClient =  gdata.calendar.client.CalendarClient()
    calendarClient.ClientLogin("projthee@gmail.com", "proj3pass", source = "User Login")
    groupClient =  gdata.calendar.client.CalendarClient()
    groupClient.ClientLogin("project3team07@gmail.com", "teamseven", source = "Calendar Access")
    app = GroupLoginWindow(root, userName, calendarClient, groupClient)
    root.mainloop()
    
if __name__ == '__main__':
    main()

        
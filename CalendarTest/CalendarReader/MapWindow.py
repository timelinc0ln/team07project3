import webbrowser
from Tkinter import *
from ttk import *
import CalReader

class MapWindow(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        #define widgets
        self.defineWidgets()
        #setup window
        self.title("Calendar Window")
        self.style = Style()
        self.style.theme_use("default")
        self.configure(background="lightgray")
        #place widgets
        self.placeWidgets()
               
    def defineWidgets(self):
        #create widgets
        #start with StringVars
        self.locationString = StringVar()
        #labels
        self.instructionLabel = Label(self, text="Enter the location where you would like to meet.", background="lightgray")
        self.locationPrompt = Label(self, text="Location:", background="lightgray")
        #entry
        self.locationEntry = Entry(self, textvariable=self.locationString)
        #buttons
        self.mapButton = Button(self, text="Find On Map", command=lambda: self.callBack("Button", "Map"))
        self.backButton = Button(self, text="Back", command=lambda: self.callBack("Button", "Back"))
        self.nextButton = Button(self, text="Next", command=lambda: self.callBack("Button", "Next"))
    
    def placeWidgets(self):
        self.instructionLabel.grid(row=0,column=0, columnspan=3, padx=5, pady=5, sticky=N)
        self.locationPrompt.grid(row=1,column=0, padx=5, pady=5, sticky=E+W)
        self.locationEntry.grid(row=1,column=1, padx=5, pady=5, sticky=E+W)
        self.mapButton.grid(row=1,column=2, padx=5, pady=5, sticky=E+W)
        self.nextButton.grid(row=2, column=1, padx=5, pady=5, sticky=E+S)
        self.backButton.grid(row=2, column=2, padx=5, pady=5, sticky=E+W+S)
        
    def onClose(self):
        self.destroy()
    
    def callBack(self, callerType, callerName):
        #handle each widget's callback
        if callerType == "Button":
            if callerName == "Map":
                print("Map button pressed")
                webbrowser.open('maps.html')
            elif callerName == "Next":
                print("Next button pressed")
                #pass the entered location and the passed times to the naming window
            elif callerName == "Back":
                print("Back button pressed")
                #close window, go back to calendar window
                
    def storeLocation(self):
        self.location = self.locationString.get()
                         
def main():
    
    root = Tk()
    root.geometry("600x155+300+300")
    app = MapWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
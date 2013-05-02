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
        # setup window size
        self.geometry("400x200+300+300")
        #define widgets for window
        self.quitButton = Button(self, text="Cancel", command=lambda: self.callBack("Button", "Quit"))
        self.submitButton = Button(self, text="Submit", command=lambda: self.callBack("Button", "Display Map"))
               
    def onClose(self):
        self.destroy()
    
    def callBack(self, callerType, callerName):
        #handle each widget's callback
        if callerType == "Button":
            if callerName == "Display Map":
                print("Display button pressed")
                webbrowser.open('maps.html')
            elif callerName == "Quit":
                print("Exiting")
                self.quit()            
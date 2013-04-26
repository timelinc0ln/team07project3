'''
Created on Apr 25, 2013

@author: casey
'''

from Tkinter import *
from ttk import *
import CalReader

class MainWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
    	logWindow = CalReader.LoginWindow(self)
    	logWindow.show()
    
    
def main():
    
    root = Tk()
    root.geometry("600x200+300+300")
    # app = Example(root)
    # app = LoginWindow(root)
    app = MainWindow(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()


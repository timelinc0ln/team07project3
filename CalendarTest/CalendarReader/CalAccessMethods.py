'''
Created on May 2, 2013

@author: Cullen
'''
import gdata.docs.service
import gdata.calendar.service
import gdata.calendar.data
import gdata.calendar.client
import atom
from atom import *
from Tkinter import *
from ttk import *

def getCalendarID(rawCalendarString):
    return rawCalendarString[55::]
#By Justin Hagerty
#Ip locator

import urllib.request
from tkinter import *
import json


window = Tk()
window.geometry('425x110')
window.title("IP Locator by Justin Hagerty")
class display:
    button = dict()
    textBox = dict()
    Label = dict()
    
def sendIP():
    try:
        IPaddress = display.textBox['IP'].get("1.0", END)
        output = []
        output = json.loads(urllib.request.urlopen("http://ip-api.com/json/" + IPaddress).read())
        display.Label['output'].config(text=("Location: " + output["city"] + ", " + output["country"]))
    except:
        display.Label['output'].config(text=("Entry Error (Incorrect IP format)"))
        

def createDisplay():
    display.button['send'] = Button(window, text="Get Location", command=sendIP)
    display.button['send'].grid(row=3, column=1, rowspan=2, padx=10, pady=10, sticky="w")

    display.textBox['IP'] = Text(window, height=1, width=50)
    display.textBox['IP'].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    
    display.Label['info'] = Label(window, text="Insert IP address and click \"Get Location\"")
    display.Label['info'].grid(row=2, column=1, padx=10, pady=0, sticky="w")

    display.Label['output'] = Label(window, text=" ")
    display.Label['output'].grid(row=2,column=2, padx=10)

createDisplay()
window.mainloop()

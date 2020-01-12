from tkinter import *
import sys
from function import *

sys.path.append("/")

class App(Frame):
    def o2m(self):
        sys.stdout = self
        try:
            del(sys.modules[""])
        except:
            pass
        o2m()
        sys.stdout = sys.__stdout__
    def single(self):
        sys.stdout = self
        try:
            del(sys.modules[""])
        except:
            pass
        singleFile()
        sys.stdout = sys.__stdout__

    def build_widgets(self):
        self.text1 = Text(self,bg='Black',bd=0,fg='Snow',height=20,width=65,padx=15,pady=15)
        self.text1.pack(anchor=CENTER,side=RIGHT,padx=60,pady=0)
        self.text2 = Text(self,bg='LightBlue',bd=0,fg='Black',height=7,width=50,padx=15,pady=15,wrap=WORD)
        self.text2.tag_configure("center", justify='center')
        self.text2.insert('1.0',"INSTRUCTIONS\n\n")
        self.text2.insert(INSERT, "**Multiple File Comparision : Compute similarity among multiple documents\n\n")
        self.text2.insert(INSERT, "**Single File Comparision: Compute similarity between two documents  ")
        self.text2.tag_add("center", "1.0", "end")
        self.text2.pack(anchor=CENTER,side=TOP,padx=0,pady=60)
        self.button = Button(self, text="Multiple File Comparision",bd=0,bg='Tan',fg='black',padx=9,pady=15,activebackground='SeaGreen')
        self.button["command"] = self.o2m
        self.button2 = Button(self, text="Single File Comparision",bd=0,bg='Tan',fg='black',padx=15,pady=15,activebackground='SeaGreen')
        self.button2["command"] = self.single
        self.button.pack(anchor=CENTER,side=TOP,padx=0,pady=10)
        self.button2.pack(anchor=CENTER,side=TOP,padx=0,pady=10)
        self.text2.config(state=DISABLED)

    def write(self, txt):
        self.text1.insert(INSERT, txt)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(background='LightBlue')
        self.pack(fill="both", expand="yes")
        self.build_widgets()



root = Tk()
root.wm_title("Plagiarism Detector")
root.configure(background='Lavender')
root.iconbitmap('icon.ico')
window_height = 600
window_width = 1266

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def close_window ():
    root.destroy()


frame = Frame(root)
frame.pack(side=BOTTOM,fill="both", expand="no")
button3 = Button (frame, text = "Exit",command = close_window,bd=0,bg='IndianRed',fg='black',padx=5,pady=5,activebackground='SeaGreen',font=14)
button3.pack(side=BOTTOM,fill="both", expand="no")


root.overrideredirect(True) # removes title bar
root.state("zoomed") #fullscreen

labelframe = LabelFrame(root, text="",bg='teal',bd=3,padx=10,pady=10)
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text="NLP Based Plagiarism Detection Software",bg='teal',bd=0, font=24,padx=10,pady=10)
left.pack(fill="both", expand="yes")




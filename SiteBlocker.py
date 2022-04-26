from tkinter import *
import webbrowser
from plyer import notification
win=Tk()
win.resizable(False,False)
win.title("Site Blocker")
# Set the size of the window
win.geometry("620x340")

def check(link):
	print(link)
	webbrowser.open(link, new=2)

def howToUse():
	webbrowser.open('https://github.com/sachira-madhushan/Site-Blocker/', new=2)

#About me url
def me():
	webbrowser.open('https://github.com/sachira-madhushan/', new=2)


def block(link):
	try:
		f = open("C:/Windows/System32/drivers/etc/hosts","a")
		f.write("\n127.0.0.1	"+link)
		f.close()
		notification.notify(title = "Done",message="Successfully Blocked This Site",timeout=2)
	except:
		notification.notify(title = "Error While Run",message="Plz Run This Software As Adminstrator.",timeout=2)

def unBlock(link):
	try:
		with open("C:/Windows/System32/drivers/etc/hosts", "r") as f:
			lines = f.readlines()
		f.close()

		with open("C:/Windows/System32/drivers/etc/hosts", "w") as f:
			for line in lines:
				if line.strip("\n") != "127.0.0.1\t"+link:
					f.write(line)
		notification.notify(title = "Done",message="Successfully Unblocked Site.",timeout=2)
	except:
		notification.notify(title = "Error While Run",message="Plz Run This Software As Adminstrator.",timeout=2)


Label(win,text="Site Blocker").grid(row = 0, column = 0,columnspan = 3, padx = 5, pady = 5)
Label(win,text="Enter Your Site Link Here :").grid(row = 1, column = 0)
site =Entry(win,width=25 )
site.insert(0,"www.facebook.com")
c2 = Button(win, text ="Block This Site",width=25,pady=10, command =lambda: block(site.get()))
c3 = Button(win, text ="Check This Site",width=25,pady=10,command =lambda: check(site.get()))
c6 = Button(win, text ="Unblock This Site",width=51,pady=10,command =lambda: unBlock(site.get()))
L=Label(win,text="D  e  v  e  l  o  p  e  d  B y  S  a  c  h  i  r  a  M  a  d  h  u  s  h  a  n ",bg="aqua")
site.grid(row = 1, column =1, sticky = W,columnspan=3)
c4 = Button(win, text ="About Me",width=25,pady=10, command =me)
c5 = Button(win, text ="How To Use",width=25,pady=10,command =howToUse)
L.grid(row = 4, column = 0, sticky = W, pady = 2,columnspan=3)
c2.grid(row = 2, column = 0, sticky = W)
c3.grid(row = 2, column = 1, sticky = W)
c6.grid(row = 3, column = 0, sticky = W ,columnspan=3)
c4.grid(row = 5, column = 0, sticky = W)
c5.grid(row = 5, column = 1, sticky = W)


win.mainloop()
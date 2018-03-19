import wget
from urllib import request
from tkinter import *
import webbrowser


def ref(click):
    webbrowser.open_new(r'https://github.com/Abhinav1004')


def PDF_Download():
    global tutorial
    tutorial=tutorial_name.get()
    try:
      PDF_url = 'https://www.tutorialspoint.com/' + tutorial + '/' + tutorial + '_tutorial.pdf'
      print(PDF_url)
      wget.download(PDF_url)
    except:
        raise Exception('No such Tutorial Found')

#creating the window
win =Tk()
win.geometry ="400x400"
win.wm_title('TutorialPoint Downloader')
win.config(background = '#708090', height = 600, width = 450)

#creating the frame 
f= Frame(win,height=500, width=150)
f.grid(row=0, column=0,padx=50, pady=50)

#taking the tutorials to download 
tutorial_name = Entry(f, width=70)
tutorial_name.grid(row=0, column=0)
Get_PDF = Button(f, text =' Download',command = PDF_Download)
Get_PDF.grid(row =0, column =1)

#affixing the background image
Photo = PhotoImage(file ='tutorial.png')
Photo0 = PhotoImage(file = 'b.png')

#creating the labels
lbl0 = Label(f,image=Photo0)
lbl = Label(f, image = Photo)
lbl.grid(row =5, column =0,padx=10,pady=10)
lbl0.grid(row=4,column=0)
lbl1 = Label(f, text="Created by :  Abhinav1004", fg='blue', cursor ="hand2")
lbl1.grid(row =6, column =0,padx=10,pady=10)
lbl1.bind("<Button-1>",  ref)

win.mainloop()
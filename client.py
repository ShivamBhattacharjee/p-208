#-----------Bolierplate Code Start -----
from msilib.schema import ListBox
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
Window=None

def mainWindow():
    global Window
    Window=Tk()
    Window.title("messenger")
    Window.geometry("500x500")

    name=Label(Window,text="enter your name",font=("monospace",15))
    name.place(x=30,y=10)

    name_entry=Entry(Window,width=12,font=("monospace",15),bg="white",fg="black")
    name_entry.place(x=190,y=10)
    name_entry.focus()

    connect_server=Button(Window,text="connect to chat server",font=("monospace",10),bd=2)
    connect_server.place(x=340,y=10)

    seperator=ttk.Separator(Window,orient="horizontal")
    seperator.place(x=0,y=50,relwidth=1,relheight=0.4)

    active_users=Label(Window,text="active users",font=("monospace",15))
    active_users.place(x=30,y=70)

    active_entry=Listbox(Window,width=43,height=5,font=("monospace",15))
    active_entry.place(x=10,y=100)

    active_connect=Button(Window,text="connect",font=("monospace",10),bd=2)
    active_connect.place(x=240,y=230)

    
    active_disconnect=Button(Window,text="disconnect",font=("monospace",10),bd=2)
    active_disconnect.place(x=310,y=230)

    active_refresh=Button(Window,text="refresh",font=("monospace",10),bd=2)
    active_refresh.place(x=400,y=230)

    chat_window=Label(Window,text="chat window",font=("monospace",15))
    chat_window.place(x=30,y=280)

    chat_entry=Listbox(Window,width=43,height=5,font=("monospace",15))
    chat_entry.place(x=10,y=310)

    attach_button=Button(Window,text="Attach & send",font=("monospace",10),bd=2)
    attach_button.place(x=10,y=450)

    attach_entry=Entry(Window,width=30,font=("monospace",15),bg="white",fg="black")
    attach_entry.place(x=110,y=450)

    attach_send=Button(Window,text="send",font=("monospace",10),bd=2)
    attach_send.place(x=450,y=450)

    Window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    mainWindow()


setup()


#-----------Bolierplate Code Start -----
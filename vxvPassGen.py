# developed by Zach - Vidi x Vici
# last updated 1 August 2025
# BEFORE USE
# MUST INSTALL TKINTER, AND PYPERCLIP
# -*- coding: utf-8 -*-
import tkinter as tk 
import array as arr 
import random 
import pyperclip as pc 
from tkinter import *
import os

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window

        self.pack(fill=BOTH, expand=1)

        # create buttons

        exitButton = Button(self, text='Exit',command=self.clickExitButton)

        newFile = Button(self, text='  Save  ', command=self.createFile)

        passwordButton = Button(self, text='Generate Pass', command=self.createArrandPassVar)

        passwordCopyButton = Button(self, text='Copy Password', command=self.copyPassword)

        usernameCopyButton = Button(self, text='Copy Username', command=self.copyUsername)

        emailCopyButton = Button(self, text='    Copy Email    ', command=self.copyEmail)

        openFileButton = Button(self, text='Open', command=self.openLoginButton)

        clearButton = Button(self, text='         Clear        ', command=self.clearField)

        # create text entry boxes under global var

        global emailEntry
        emailEntry = tk.Entry()
        emailEntry.configure(bg='#09111D')

        global nameEntry
        nameEntry = tk.Entry()
        nameEntry.configure(bg='#09111D')

        global passwordEntry
        passwordEntry = tk.Entry()
        passwordEntry.configure(bg='#09111D')

        global extraInfoEntry
        extraInfoEntry = tk.Text(width=26, height=10)
        extraInfoEntry.configure(bg='#09111D')

        global titleEntry
        titleEntry = tk.Entry()
        titleEntry.configure(fg="#ffffff")
        titleEntry.bind("<Button-1>", lambda e: titleEntry.delete(0, tk.END))
        
        titleEntry.insert(0, "Search...")
        titleEntry.configure(bg='#09111D')

        # Number of Characters Entry:
        global CharEntry
        CharEntry = tk.Entry()
        CharEntry.configure(fg="#ffffff",bg='#09111D')
        CharEntry.place(x=300, y=179)


        # create labels and place in application window

        titlelabel = tk.Label(text='Title:')
        titlelabel.place(x=0, y=0)
        titleEntry.place(x=0, y=23)
        titlelabel.configure(fg="#ffffff",bg='#09111D')

        emaillabel = tk.Label(text='Email:')
        emaillabel.place(x=0, y=51)
        emailEntry.place(x=0, y=72)
        emailEntry.configure(fg="#ffffff")
        emaillabel.configure(fg="#ffffff",bg='#09111D')

        usernamelabel = tk.Label(text='Username:')
        usernamelabel.place(x=0, y=103)
        nameEntry.place(x=0, y=128)
        nameEntry.configure(fg="#ffffff")
        usernamelabel.configure(fg="#ffffff",bg='#09111D')

        passwordlabel = tk.Label(text='Password:')
        passwordlabel.place(x=0, y=157)
        passwordLengthlabel = tk.Label(text='Password Length:')
        passwordLengthlabel.place(x=320, y=157)
        passwordEntry.place(x=0, y=179)
        passwordEntry.configure(fg="#ffffff")
        passwordlabel.configure(fg="#ffffff",bg='#09111D')
        passwordLengthlabel.configure(fg="#ffffff",bg='#09111D')

        extraInfolabel = tk.Label(text='Extra Info:')
        extraInfolabel.place(x=0, y=213)
        extraInfoEntry.place(x=0, y=235)
        extraInfoEntry.configure(fg="#ffffff")
        extraInfolabel.configure(fg="#ffffff",bg='#09111D')

        # place buttons created earlier to run functions

        exitButton.place(x=335, y=370)
        exitButton.configure(highlightbackground='#09111D')

        newFile.place(x=255, y=370)
        newFile.configure(highlightbackground='#09111D')

        passwordButton.place(x=450, y=179)
        passwordButton.configure(highlightbackground="#FFFFFF")

        passwordCopyButton.place(x=190, y=176)
        passwordCopyButton.configure(highlightbackground='#09111D')

        usernameCopyButton.place(x=190, y=126)
        usernameCopyButton.configure(highlightbackground='#09111D')

        emailCopyButton.place(x=190, y=69)
        emailCopyButton.configure(highlightbackground='#09111D')

        openFileButton.place(x=190, y=22)
        openFileButton.configure(highlightbackground='#09111D')

        clearButton.place(x=450, y=370)
        clearButton.configure(highlightbackground='#09111D')

    # clears all fields

    def clearField(self):
        global titleEntry
        global emailEntry
        global nameEntry
        global passwordEntry
        global extraInfoEntry
        titleEntry.delete(0, tk.END)
        emailEntry.delete(0, tk.END)
        nameEntry.delete(0, tk.END)
        passwordEntry.delete(0, tk.END)
        extraInfoEntry.delete('1.0','20.0')



    # opens existing login

    def openLoginButton(self):
        global title
        global titleEntry
        title = titleEntry.get()

        global emailEntry
        global nameEntry
        global passwordEntry
        global extraInfoEntry
        titleEntry.configure(fg='#ffffff')
        titleEntry.delete(0, tk.END)
        emailEntry.delete(0, tk.END)
        nameEntry.delete(0, tk.END)
        passwordEntry.delete(0, tk.END)
        extraInfoEntry.delete('1.0','20.0')

        f = open("data/" + title, "r")
        title = f.readline()
        email = f.readline()
        username = f.readline()
        Password = f.readline()
        f.close()
        e = open("data/" + title.rstrip('\n') + "extra", "r")
        extraInfo = e.read()

        titleEntry.insert(0, title.rstrip('\n'))
        emailEntry.insert(0, email.rstrip('\n'))
        nameEntry.insert(0, username.rstrip('\n'))
        passwordEntry.insert(0, Password.rstrip('\n'))
        extraInfoEntry.insert('1.0', extraInfo)

    # function for exit button

    def clickExitButton(self):
        exit()

    # creates new .txt file

    def createFile(self):
        global email
        global username
        global Password
        global extraInfo
        global emailEntry
        global nameEntry
        global extraInfoEntry
        global title
        global titleEntry
        title = ''
        username = ''
        Password = ''
        extraInfo = ''
        email = ''
        title = titleEntry.get()
        username = nameEntry.get()
        email = emailEntry.get()
        Password = passwordEntry.get()
        extraInfo = extraInfoEntry.get('1.0', '20.0')
        # creating a new directory
        isExist = os.path.exists("data")
        if not isExist:
        # Create a new directory because it does not exist
            os.makedirs("data")

         # Changing current path to the directory
        os.chdir("data")

        # creating a new file for writing operation
        f = open(title, "w")
        f.write(title + "\n")
        f.write(email + "\n")
        f.write(username + "\n")
        f.write(Password + "\n")
        
        f.close()
        e = open(title + "extra", "w")
        e.write(extraInfo)
        e.close()
        os.chdir("..")


    # copies username to clipboard

    def copyUsername(self):
        global username
        username = nameEntry.get()
        pc.copy(username)

    # copies email to clipboard

    def copyEmail(self):
        global email
        email = emailEntry.get()
        pc.copy(email)

    # copies password to clipboard

    def copyPassword(self):
        global Password
        Password = passwordEntry.get()
        pc.copy(Password)

    # deletes current password and randomly generates new password

    def createArrandPassVar(self):
        global passwordEntry
        global Password
        passwordEntry.delete(0, tk.END)
        Password = ''
        arrX = ['A','B','C','D',
            'E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z','a','b','c','d','e','f',
            'g','h','i','j','k','l','m','n','o','p','q','r','s','t',
            'u','v','w','x','y','z','0','1','2','3','4','5','6','7',
            '8','9','!','$','#','&',']','[','}','{','%','@',')','(',]

        global CharEntry
        PassLength = int(CharEntry.get())
        arrP = [0] * PassLength
        i = 0
        while i < PassLength:
            arrP[i] = arrX[random.randint(0, 73)]
            i += 1
        Password = ''.join(arrP)
        pc.copy(Password)
        passwordEntry.insert(0, Password)

root = Tk()
app = Window(root)
root.wm_title('VxV GenPass')
root.geometry('400x400')
app.configure(bg='#09111D')
root.mainloop()

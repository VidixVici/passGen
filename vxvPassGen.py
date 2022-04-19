# developed by Zach - Vidi x Vici
# last updated 19 April 2022
# For any optimizations or advise on improvement go to VidixVici.github.io
# and fill out the form to contact me
#
# BEFORE USE
# 
# How to install On Windows
# C:\Users\USER NAME\AppData\Local\Programs\Python\Python310
# install get-pip.py file here
# do this by cd'ing to correct folder path and using
# python get-pip.py
# install other imports
# python -m pip install tk
# python -m pip install pyperclip
# create desktop shortcut
# change target field to line below
# drag to windows task bar
#
# ALSO! SCROLL THROUGH CODE AND UPDATE PASSWORD KEY AND FOLDER DIRECTORIES
# LINES THAT NEED TO BE UPDATED BELOW
#
# 270, 282, 
# 303, 304, 306, 325, 344, 345, 347, 366, 385, 386, 388, 407, 426, 427, 429, 448
#
#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkinter as tk 
import array as arr 
import random 
import pyperclip as pc 
from tkinter import *
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
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
        titleEntry.configure(bg='#09111D')

        # create labels and place in application window

        titlelabel = tk.Label(text='Title:')
        titlelabel.place(x=0, y=0)
        titleEntry.place(x=0, y=23)
        titlelabel.configure(bg='#09111D')

        emaillabel = tk.Label(text='Email:')
        emaillabel.place(x=0, y=51)
        emailEntry.place(x=0, y=72)
        emaillabel.configure(bg='#09111D')

        usernamelabel = tk.Label(text='Username:')
        usernamelabel.place(x=0, y=103)
        nameEntry.place(x=0, y=128)
        usernamelabel.configure(bg='#09111D')

        passwordlabel = tk.Label(text='Password:')
        passwordlabel.place(x=0, y=157)
        passwordEntry.place(x=0, y=179)
        passwordlabel.configure(bg='#09111D')

        extraInfolabel = tk.Label(text='Extra Info:')
        extraInfolabel.place(x=0, y=213)
        extraInfoEntry.place(x=0, y=235)
        extraInfolabel.configure(bg='#09111D')

        # place buttons created earlier to run functions

        exitButton.place(x=335, y=370)
        exitButton.configure(highlightbackground='#09111D')

        newFile.place(x=255, y=370)
        newFile.configure(highlightbackground='#09111D')

        passwordButton.place(x=130, y=370)
        passwordButton.configure(highlightbackground='#09111D')

        passwordCopyButton.place(x=190, y=176)
        passwordCopyButton.configure(highlightbackground='#09111D')

        usernameCopyButton.place(x=190, y=126)
        usernameCopyButton.configure(highlightbackground='#09111D')

        emailCopyButton.place(x=190, y=69)
        emailCopyButton.configure(highlightbackground='#09111D')

        openFileButton.place(x=190, y=22)
        openFileButton.configure(highlightbackground='#09111D')

        clearButton.place(x=0, y=370)
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
        titleEntry.delete(0, tk.END)
        emailEntry.delete(0, tk.END)
        nameEntry.delete(0, tk.END)
        passwordEntry.delete(0, tk.END)
        extraInfoEntry.delete('1.0','20.0')

        titleEntry.insert(0, title)

        self.decryptEmail()
        email = encryptedEmail
        emailEntry.insert(0, email)

        self.decryptUsername()
        username = encryptedUser
        nameEntry.insert(0, username)

        self.decryptPass()
        Password = encryptedPass
        passwordEntry.insert(0, Password)

        self.decryptExtra()
        extraInfo = encryptedExtra
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
        self.rsaBackIn()
        self.encryptPass()
        self.encryptEmail()
        self.encryptUsername()
        self.encryptExtra()

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

        arrP = ['1','2','3','4','5','6','7','8','9','10','11','12',]

        i = 0
        while i < 12:
            arrP[i] = arrX[random.randint(0, 73)]
            i += 1
        Password = ''.join(arrP)
        pc.copy(Password)
        passwordEntry.insert(0, Password)
    
    def genRsa(self):
        secret_code = "insertYours"
        key = RSA.generate(2048)
        encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,
                                    protection="scryptAndAES128-CBC")

        file_out = open("rsa_key.bin", "wb")
        file_out.write(encrypted_key)
        file_out.close()

        #print(key.publickey().export_key())

    def rsaBackIn(self):
        secret_code = "insertYours"
        encoded_key = open("rsa_key.bin", "rb").read()
        key = RSA.import_key(encoded_key, passphrase=secret_code)

        #print(key.publickey().export_key())

    def genPubPriv(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        file_out = open("receiver.pem", "wb")
        file_out.write(public_key)
        file_out.close()

    def encryptUsername(self):
        global username
        global title
        if not os.path.exists('filepath' + title + '/'):
            os.makedirs('filepath' + title + '/')
        data = username.encode("utf-8")
        file_out = open('filepath' + title + '/' + title + 'user' + 'encrypted_data.bin', 'wb')

        recipient_key = RSA.import_key(open("receiver.pem").read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()

    def decryptUsername(self):
        global title
        global encryptedUser
        string1 = ''
        file_in = open('filepath' + title + '/' + title + 'user' + 'encrypted_data.bin', "rb")

        private_key = RSA.import_key(open("private.pem").read())

        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        encryptedUser = (data.decode("utf-8"))

    def encryptEmail(self):
        global email
        global title
        if not os.path.exists('filepath' + title + '/'):
            os.makedirs('filepath' + title + '/')
        data = email.encode("utf-8")
        file_out = open('filepath' + title + '/' + title + 'email' + 'encrypted_data.bin', 'wb')

        recipient_key = RSA.import_key(open("receiver.pem").read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()

    def decryptEmail(self):
        global title
        global encryptedEmail
        string1 = ''
        file_in = open('filepath' + title + '/' + title + 'email' + 'encrypted_data.bin', "rb")

        private_key = RSA.import_key(open("private.pem").read())

        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        encryptedEmail = (data.decode("utf-8"))

    def encryptPass(self):
        global Password
        global title
        if not os.path.exists('filepath' + title + '/'):
            os.makedirs('filepath' + title + '/')
        data = Password.encode("utf-8")
        file_out = open('filepath' + title + '/' + title + 'pass' + 'encrypted_data.bin', 'wb')

        recipient_key = RSA.import_key(open("receiver.pem").read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()

    def decryptPass(self):
        global title
        global encryptedPass
        string1 = ''
        file_in = open('filepath' + title + '/' + title + 'pass' + 'encrypted_data.bin', "rb")

        private_key = RSA.import_key(open("private.pem").read())

        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        encryptedPass = (data.decode("utf-8"))

    def encryptExtra(self):
        global extraInfo
        global title
        if not os.path.exists('filepath' + title + '/'):
            os.makedirs('filepath' + title + '/')
        data = extraInfo.encode("utf-8")
        file_out = open('filepath' + title + '/' + title + 'extra' + 'encrypted_data.bin', 'wb')

        recipient_key = RSA.import_key(open("receiver.pem").read())
        session_key = get_random_bytes(16)

        # Encrypt the session key with the public RSA key
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # Encrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
        file_out.close()

    def decryptExtra(self):
        global extraInfo
        global encryptedExtra
        string1 = ''
        file_in = open('filepath' + title + '/' + title + 'extra' + 'encrypted_data.bin', "rb")

        private_key = RSA.import_key(open("private.pem").read())

        enc_session_key, nonce, tag, ciphertext = \
        [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypt the session key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypt the data with the AES session key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        encryptedExtra = (data.decode("utf-8"))

root = Tk()
app = Window(root)
root.wm_title('VxV GenPass')
root.geometry('400x400')
app.configure(bg='#09111D')
root.mainloop()

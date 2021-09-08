import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from cryptography import fernet
from cryptography.fernet import Fernet
import random



def decrypt(window):
    global keyname,file,file_save,check
    window.destroy()
    window2=Tk()
    window2.geometry("600x650+450+50")
    window2.resizable(0, 0)
    window2.config(bg="green")
    window2.title("Decryptor")
    window2.iconbitmap(r'images/lock icon2.ico')
    window2.update_idletasks()
    image2=Image.open('images/back.jpg')
    image2= image2.resize((600,650), Image.ANTIALIAS)
    photo2=ImageTk.PhotoImage(image2)
    lab3=Label(image=photo2)
    lab3.pack()
    keyname=StringVar()
    file=StringVar()
    file_save=StringVar()
    
    check=0
    def key():
        global b,check
        try:
            check=1
            file_ko = open(keyname.get(), "rb")
            the_key = file_ko.read()
            b = Fernet(the_key)  # using fernet class instance
            file_ko.close()
            messagebox.showinfo("Decryption Page","Key read successfully!")
            
        except BaseException as e:
            messagebox.showerror("Decryption", e)

    def decrypt_data():
        global check,dec_message
        if check==1:
            try:
                check=2
                my_fileE = open(file.get(), "rb")
                content = my_fileE.read()
                my_fileE.close()
                dec_message = b.decrypt(content) 
                messagebox.showinfo("Decryption page","Successfully decrypted the message.")
            except BaseException as e:
                messagebox.showerror("Decryption",e)
        else:
            messagebox.showerror("Decryption page","Provide the key first!")


    def save_decrypted_data():
        if check==2:
            try:
                my_fileD = open(file_save.get(), "wb")
                my_fileD.write((dec_message))
                my_fileD.close()
                messagebox.showinfo("Decryption page","Successfully saved the decrpyted data.")
                window2.destroy()
                main_window()
            except BaseException as e:
                messagebox.showerror("Decryption page",e)
        else:
            messagebox.showerror("Decryption Page","First decrypt the data then only you can save it!")

    
    label1=Label(window2,text="Key file with extension",bg="#150501",width=30,fg="white",relief="groove",font=('arial',13),borderwidth=1).place(x=40,y=100)
    
    entry1=Entry(window2,textvar=keyname).place(x=360,y=100,width=200,height=25)
    dec_button1=Button(window2,text="OK",width=5,bd=3,bg="black",fg="white",command=lambda: key(),font=('arial',13)).place(x=430,y=150)


    label2=Label(window2,text="File to be decrypted",bg="#150501",width=30,fg="white",relief="groove",font=('arial',13),borderwidth=1).place(x=40,y=300)
    
    entry2=Entry(window2,textvar=file).place(x=360,y=300,width=200,height=25)
    dec_button2=Button(window2,text="OK",width=5,bd=3,bg="black",fg="white",command=lambda: decrypt_data(),font=('arial',13)).place(x=430,y=350)


    label3=Label(window2,text="File name to save decrypted data",bg="#150501",width=30,fg="white",relief="groove",font=('arial',13),borderwidth=1).place(x=40,y=500)
    
    entry3=Entry(window2,textvar=file_save).place(x=360,y=500,width=200,height=25)
    dec_button3=Button(window2,text="OK",width=5,bd=3,bg="black",fg="white",command=lambda: save_decrypted_data(),font=('arial',13)).place(x=430,y=550)

    window2.mainloop()





 

def encrypt(window):
    global enc_message,filename,my_file,b
    enc_message=""
    window.destroy()
    window1=Tk()
    window1.geometry("600x500+450+100")
    window1.resizable(0, 0)
    window1.config(bg="green")
    window1.title("Encryptor")
    window1.iconbitmap(r'images/lock icon2.ico')
    window1.update_idletasks()
    image1=Image.open('images/back.jpg')
    image1= image1.resize((600,500), Image.ANTIALIAS)
    photo1=ImageTk.PhotoImage(image1)
    lab2=Label(image=photo1)
    lab2.pack()
    filename=StringVar()
    my_file=StringVar()
    key = 2 * Fernet.generate_key() * random.randint(1, 5) * 2
    file_k = open("key.key", "wb")
    file_k.write(key)
    file_k.close()
    a = Fernet(key)  # using fernet class instance
    
    
    b=0
    def submit_filename():
        global b,enc_message
        try:
            file_n = str(filename.get())
            my_filecontents = open(file_n, "rb")
            contents = my_filecontents.read()
            enc_message = a.encrypt(contents)
            b=1
            messagebox.showinfo("Encryption page","Data encrypted successfully.")
            
        except BaseException as e:
            messagebox.showerror("Encrytion page", e)

    def save_encrypted_data():
        if b==1:
            my_file1 = open(str(my_file.get()), "wb")
            my_file1.write((enc_message))
            my_file1.close()
            messagebox.showinfo("Encryption page","Encrypted data successfully stored in "+str(my_file.get())+" file.")
            window1.destroy()
            main_window()
        else:
            messagebox.showerror("Encryption page","First encrypt the data")


    label1=Label(window1,text="Enter file name to be encrypted",bg="#150501",width=35,fg="white",relief="groove",font=('arial',13)).place(x=30,y=100)
    
    entry1=Entry(window1,textvar=filename).place(x=360,y=100,width=200,height=25)
    enc_button1=Button(window1,text="OK",width=5,bd=3,bg="black",fg="white",command=lambda: submit_filename(),font=('arial',13,'bold')).place(x=430,y=150)


    label2=Label(window1,text="Enter file name to save encrypted data",bg="#150501",width=35,fg="white",relief="groove",font=('arial',11)).place(x=30,y=300)
    
    entry2=Entry(window1,textvar=my_file).place(x=360,y=300,width=200,height=25)
    enc_button2=Button(window1,text="OK",width=5,bd=3,bg="black",fg="white",command=lambda: save_encrypted_data(),font=('arial',13,'bold')).place(x=430,y=350)

    messagebox.showinfo("Encryption Page","Encryption Key Generated Successfully.")
    window1.mainloop()

def main_window():
    window=Tk()
    window.geometry("600x500+450+100")
    window.resizable(0, 0)
    window.config(bg="green")
    window.title("Cryptonia")
    window.iconbitmap(r'images/lock icon2.ico')
    image=Image.open('images/home.jpeg')
    resized_image= image.resize((600,500), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(resized_image)
    lab1=Label(image=photo)
    lab1.pack(fill=BOTH,expand=True)

    button1=Button(window,text="Encryption",width=25,bd=3,bg="black",fg="white",font=('arial',16,'bold'),command = lambda: encrypt(window)).place(x=120,y=150)
    button2=Button(window,text="Decryption",width=25,bd=3,bg="black",fg="white",font=('arial',16,'bold'),command = lambda: decrypt(window)).place(x=120,y=250)

    window.mainloop()
main_window()
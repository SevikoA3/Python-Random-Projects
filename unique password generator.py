import tkinter
import random

window = tkinter.Tk()
window.minsize(720, 400)
window.title('Password Generator')

label = tkinter.Label(window, text="Your new password is:", font="14")
label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
text = tkinter.StringVar()
text.set("Click 'Generate' to start generating.")
label1 = tkinter.Entry(window, textvariable=text, font="none 20 bold", bd=0, width=31, justify="center", state="readonly")
label1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

def changePass() :
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=[]\;:+_'
    newPass = ''
    for i in range (12) :
        newPass += chars[random.randint(0,70)]
    text.set(newPass)


button1 = tkinter.Button(window, text="Generate", command=changePass, font="14")
button1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

window.mainloop()
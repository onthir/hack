import subprocess
from tkinter import *
import time

root = Tk()
root.title("Password Sniffer")
root.geometry("1920x1080+0+0")


def main_function():
     name_list = str(subprocess.check_output("netsh wlan show interfaces"))
     lb = Label(root, text=(name_list[40:]), font=('arial 15 bold'), fg="green").pack()
     print(name_list)


btn = Button(root, text="My Network Details", width=30, height= 3, command=main_function).pack()

def generate_password():
     lab = Label(root, text="Generating......(It takes around 1-5 minutes)", font=('arial 13 bold'), fg="red").pack()
     
     lab2 = Label(root, text="Password: Error@404", font=('arial 13 bold'), fg="steelblue").pack()


btn2 = Button(root, text="Try Sniffing", width=30, height= 3, command=generate_password).pack()


root.mainloop()





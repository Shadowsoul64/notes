# 2022-11-03 3:38 pm
# This is like the 10th time im starting this because I could never get Git right
# This project will be used to create a simple text/ journal app
# As well as test out and get a better understanding of GitHub and version control!
# Without further adieu, lets begin!
from tkinter import *
from tkinter import ttk

def main():

    # In the frst part of my code I am making a gui window.

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="Hello World!").grid(column=200, row=200)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=6, row=2)
    root.mainloop()











main()
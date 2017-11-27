from tkinter import *

def gedrukt():
    text ['text'] = schrijven.get()

root = Tk() # Creëer het hoofdscherm

text = Label(master=root, text='Hey, hoe is het', font=('Verdana', 14), background='red', width=50, height=5) #text maken
text.pack()

knop = Button(master=root, text='Druk voor geluk', command=gedrukt)
knop.pack(pady=10, padx=10)

schrijven = Entry(master=root)
schrijven.pack(padx=10, pady=10)

root.mainloop()
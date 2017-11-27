from tkinter import *
import requests
import xmltodict

#Opmaak van de GUI
font_text = ('Verdana', 60, 'bold')
yellow = '#fed633'
blue = '#333399'

#Tkinter GUI's
root = Tk()
root2 = Tk()
root2.withdraw()
root.configure(width=1400, height=500, background=yellow)
root.title('NS Hoofdpagina')

def zoekbalk():
    root.configure(width=1400, height=700, background=yellow)

def stoppen():
    root.destroy()
    root2.destroy()

def vertrekschema():
    # Tkinter GUI Vertrekschema venster
    root2.deiconify()
    root2.configure(height=690, width=500, background='white')
    root2.title('NS Vertrekschema')

#Invoer balkje
station = StringVar()
invoerStation = Entry(root, textvariable=station, font=('Verdana', 15))
invoerStation.place(x=555, y=560)

#Inhoud vertrekschema
Label(root2, text='Vertrektijd', font=('Verdana', 12, 'bold'), foreground='black', background='white').place(x=5, y=10)
Label(root2, text='Bestemming', font=('Verdana', 12, 'bold'), foreground='black', background='white').place(x=120, y=10)
Label(root2, text='Spoor', font=('Verdana', 12, 'bold'), foreground='black', background='white').place(x=300, y=10)
Label(root2, text='Soort', font=('Verdana', 12, 'bold'), foreground='black', background='white').place(x=370, y=10)

def openvertrekschema(station, root2):
    vertrekschema()
    # Verbinden met API
    username = 'stef.bos@student.hu.nl'
    password = 'xKc4QO9SwPMO4zTv-S8A5QEHChUz_aJv8eR0EQm7GWOK1UG0LVGVMw'
    url = 'https://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(url, auth=(username, password))
    vertrekXML = xmltodict.parse(response.text)
    var_y = 30
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        Label(root2, text=vertrek['VertrekTijd'][11:16], font=('Verdana', 12), anchor='w', foreground='black', background='white').place(x=5, y=var_y)
        Label(root2, text=vertrek['EindBestemming'], font=('Verdana', 12), anchor='w', foreground='black', background='white').place(x=120, y=var_y)
        Label(root2, text=vertrek['VertrekSpoor']['#text'], font=('Verdana', 12), anchor='w', foreground='black', background='white').place(x=300, y=var_y)
        Label(root2, text=vertrek['TreinSoort'], font=('Verdana', 12), anchor='w', foreground='black', background='white').place(x=370, y=var_y)
        var_y += 20


#Inhoud van het vesnter
Label(root, text='Hallo reiziger, welkom bij NS', font=('Verdana', 55, 'bold'), foreground=blue, background=yellow).place(x=170, y=100)
Label(root, text='Wilt u de vertrektijden bekijken?', font=('Verdana', 30, 'bold'), foreground=blue, background=yellow).place(x=400, y=300)
Label(root, text='Voer het station in:', font=('Verdana', 15), foreground='black', background=yellow).place(x=590, y=530)

#Knoppen
knopJa = Button(master=root, text='Ja', foreground='black', font=('Verdana', 15, 'bold'), command=lambda: zoekbalk())
knopNee = Button(master=root, text='Nee', foreground='black', font=('Verdana', 15, 'bold'), command=lambda: stoppen())
knopZoeken = Button(master=root, text='zoeken', foreground='black', font=('Verdana', 12), command=lambda: openvertrekschema(station.get(), root2))
knopJa.place(x=600, y=370)
knopNee.place(x=700, y=370)
knopZoeken.place(x=630, y=590)

root.mainloop()
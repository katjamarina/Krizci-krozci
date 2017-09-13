import tkinter as tk
import random

class KrizciKrozci:
    def __init__(self, master):
        self.okvir = tk.Frame(master)
        self.okvir.pack(fill='both',expand=True)
        self.label = tk.Label(self.okvir, text='KRIŽCI KROŽCI', font = ("Verdana", "15"), height=3, bg='white', fg='red', borderwidth = 1, relief="solid")
        self.label.pack(fill="both", expand=True)
        self.polje = tk.Canvas(self.okvir, width = 330, height = 330)
        self.polje.pack(fill="both", expand=True)
        self.okvir2 = tk.Frame(self.okvir)
        self.okvir2.pack(fill="both", expand=True)
        self.zacni = tk.Button(self.okvir2, text='Klikni za začetek igre!',font = ("Verdana", 12), height=2, command=self.zacetek,bg='white', fg='black')
        self.zacni.pack(fill="both", expand=True)
        self.plosca()

    def zacetek(self):
        self.polje.delete(tk.ALL)
        self.label['text'] = ('KRIŽCI KROŽCI')
        self.polje.bind("<ButtonPress-1>", self.igraj)
        self.plosca()
        self.polja=[[0,0,0],[0,0,0],[0,0,0]]
        self.i = 0
        self.j = False


    def konec(self):
        self.polje.unbind("<ButtonPress-1>")
        self.j=True

    def plosca(self):
        self.polje.create_rectangle(0, 0, 330, 330, outline="black") #celotno polje
        self.polje.create_rectangle(110, 330, 220, 0, outline="black") #navp pravokotnik
        self.polje.create_rectangle(0, 110, 330, 220, outline="black") #vod pravokotnik

    def igraj(self, koord):
        for m in range(0, 330, 110):
            for n in range(0, 330, 110):
                if koord.x in range(m, m+110) and koord.y in range(n, n+110):
                    if self.polje.find_enclosed(m , n, m+110, n+110) == ():
                        if self.i % 2 == 0:  #da se igralca menjavata
                            W= (2*m+110)/2
                            Z= (2*n+110)/2
                            W1= int(m/110)
                            Z1= int(n/110)
                            self.polje.create_oval( W+25, Z+25, W-25, Z-25, width=4, outline="black") #narise krozec
                            self.polja[Z1][W1] += 1
                            self.i += 1
                            self.label['text'] = 'Na vrsti je 2. igralec'
                        else:
                            W= (2*m+110)/2
                            Z= (2*n+110)/2
                            W1= int(m/110)
                            Z1= int(n/110)
                            self.polje.create_line( W+25, Z+25, W-25, Z-25, width=4, fill="red") #naredi del križca
                            self.polje.create_line( W-25, Z+25, W+25, Z-25, width=4, fill="red") #še drug del križca#še drug del križca
                            self.polja[Z1][W1] += 9
                            self.i += 1
                            self.label['text'] = 'Na vrsti je 1. igralec'
        self.preveri()

    def preveri(self):
        #preverimo navpicno
        for i in range(0,3):
            if sum(self.polja[i]) == 27: #navpicno so tri polja X (9+9+9)
                self.label['text']=('!!!2. IGRALEC JE ZMAGAL!!!')
                self.konec()
            if sum(self.polja[i]) == 3:
                self.label['text']=('!!!1. IGRALEC JE ZMAGAL!!!')
                self.konec()
        #preverimo vodoravno
        #matrika spodaj transponira self.polja , da lahko uporabimo seštevek
        self.trans_polja=[[vrstica[i] for vrstica in self.polja] for i in range(3)]
        for i in range(0,3):
            if sum(self.trans_polja[i]) == 27:
                self.label['text']=('!!!2. IGRALEC JE ZMAGAL!!!')
                self.konec()
            if sum(self.trans_polja[i]) == 3:
                self.label['text']=('!!!1. IGRALEC JE ZMAGAL!!!')
                self.konec()
        #preverimo še diagonalno
        if self.polja[1][1] == 9:
            if self.polja[0][0] == self.polja[1][1] and self.polja[2][2] == self.polja[1][1] :
                self.label['text'] = ('!!!2. IGRALEC JE ZMAGAL!!!')
                self.konec()
            if self.polja[0][2] == self.polja[1][1] and self.polja[2][0] == self.polja[1][1] :
                self.label['text'] = ('!!!2. IGRALEC JE ZMAGAL!!!')
                self.konec()
        if self.polja[1][1] == 1:
            if self.polja[0][0] == self.polja[1][1] and self.polja[2][2] == self.polja[1][1] :
                self.label['text'] = ('!!!1. IGRALEC JE ZMAGAL!!!')
                self.konec()
            if self.polja[0][2] == self.polja[1][1] and self.polja[2][0] == self.polja[1][1] :
                self.label['text'] = ('!!!1. IGRALEC JE ZMAGAL!!!')
                self.konec()
        #preveri če je izenačeno
        if self.j == False:
            a=0
            for i in range(0,3):
                a+= sum(self.polja[i])
            if a == 41:
                self.label['text']=("Izenačena sta. \n Poskusita še enkrat!")
                self.konec()

root = tk.Tk()
krizcikrozci = KrizciKrozci(root)
root.title('Križci Krožci')
root.mainloop()


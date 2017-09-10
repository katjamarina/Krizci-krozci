import tkinter as tk
import random

class KrizciKrozci:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.pack(fill='both',expand=True)
        self.label = tk.Label(self.frame, text='KRIŽCI KROŽCI', font = ("Verdana", "15"), height=3, bg='white', fg='red', borderwidth = 1, relief="solid")
        self.label.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(self.frame, width = 300, height = 300)
        self.canvas.pack(fill="both", expand=True)
        self.frame2 = tk.Frame(self.frame)
        self.frame2.pack(fill="both", expand=True)
        self.zacni = tk.Button(self.frame2, text='Klikni za začetek igre!',font = ("Verdana", 12), height=2, command=self.zacetek,bg='white', fg='black')
        self.zacni.pack(fill="both", expand=True)
        self.plosca()

        '''menu = Menu(master)
        master.config(menu=menu)
        datoteka = Menu(menu)
        menu.add_cascade(label='Datoteka', menu=datoteka)
        datoteka.add_command(label='Shrani igro', command=self.shrani_igro)
        datoteka.add_command(label="Izhod", command=master.destroy)'''

    def zacetek(self):
        self.canvas.delete(tk.ALL)
        self.label['text'] = ('KRIŽCI KROŽCI')
        self.canvas.bind("<ButtonPress-1>", self.igraj)
        self.plosca()
        self.polja=[[0,0,0],[0,0,0],[0,0,0]]
        self.i = 0
        self.j = False


    def konec(self):
        self.canvas.unbind("<ButtonPress-1>")
        self.j=True

    def plosca(self):
        self.canvas.create_rectangle(0, 0, 300, 300, outline="black")
        self.canvas.create_rectangle(100, 300, 200, 0, outline="black")
        self.canvas.create_rectangle(0, 100, 300, 200, outline="black")

    def igraj(self, koord):
        for k in range(0, 300, 100):
            for j in range(0, 300, 100):
                if koord.x in range(k, k+100) and koord.y in range(j, j+100):
                    if self.canvas.find_enclosed(k , j, k+100, j+100)== ():
                        if self.i % 2 == 0:
                            W= (2*k+100)/2
                            Z= (2*j+100)/2
                            W1= int(k/100)
                            Z1= int(j/100)
                            self.canvas.create_oval( W+25, Z+25, W-25, Z-25, width=4, outline="black")
                            self.polja[Z1][W1] += 1
                            self.i += 1
                            self.label['text'] = 'Na vrsti je 2. igralec'
                        else:
                            W= (2*k+100)/2
                            Z= (2*j+100)/2
                            W1= int(k/100)
                            Z1= int(j/100)
                            self.canvas.create_line( W+20, Z+20, W-20, Z-20, width=4, fill="red") #naredi del križca
                            self.canvas.create_line( W-20, Z+20, W+20, Z-20, width=4, fill="red") #še drug del križca#še drug del križca
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


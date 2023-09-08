def main(): pass
if __name__ == '__main__': main()
from tkinter import *
from tkinter import messagebox
import tkinter.ttk,pickle_dick_2,random
from tkinter.font import Font, nametofont
from tkinter import filedialog
from mytext import *

w = Tk()
ws = w.winfo_screenwidth()
hs = w.winfo_screenheight()
default_font = nametofont("TkDefaultFont")
default_font.configure(size=13,weight="bold",family="helvetica")
w.title("benim SOZLUK")
##w.geometry('%dx%d+30+30' % (ws//1.5, hs//1.3))

sozluk=pickle_dick_2.oku()
ilk=len(sozluk)
key=list(sozluk.keys())
key.sort()
sorulanlar, saklananlar,yannislar = pickle_dick_2.sorulmuslari_oku()
sorulanlar+=saklananlar[:]
en_yakin=IntVar()
en_yakin.set(-1)

pencere_acikmi={"tercih":0,"kel_kart":0,"ekle_yeni":0,"sil":0,"degis_yeni":0,"liste_kutusu":0}

sol=Frame(w,bg=w.cget("bg"))

combo = tkinter.ttk.Combobox(sol, height=20,width=18,font=("ariel",24))
combo['values']= key
combo.current(0)

def bos(root,x=1,sekil=""):   # § ֎⁛ ⁜ ⁂ ⁘ ⅏ ◊ ⸞ ⸟
    col=["black","dim" "grey","dark grey","silver","light","grey","gainsboro","white","smoke","white"]
    for i in range(x):
        bos_satir=Label(root,text=sekil*5,bg=root.cget("bg"),fg=col[i%11]).pack()

def dosya_sec():
    global sozluk,key
    filename =  filedialog.askopenfilename(initialdir = ".",title = "Sec dosya",filetypes = (("PKL dosyalar","*.soz"),("all files","*.*")))
    if filename!="":
        sozluk=pickle_dick_2.oku(filename)
        key=list(sozluk.keys())
        key.sort()
        combo['values']= key
        combo.current(0)
        kay.configure(text=("kayit adedi "+str(len(sozluk))))
        print (filename)
    else : print("dosya sechmedin")

def dosyaya():
    global ilk
    if messagebox.askyesno("KAYIT->İLK:{}\nSON:{}".format(ilk,len(sozluk)),"DOSYAYA KAYDEDİİM Mİ") :
        pickle_dick_2.yaz(sozluk)
        ilk=len(sozluk)

def yaz_ve_cik():
    print("yazip chikiyom")
    pickle_dick_2.yaz(sozluk)
    w.destroy()

def dosya_yedek():
    if messagebox.askyesno("DOSYA YEDEKLE","bahh eski yedegin ustune yaziyom!",icon="warning") :
        pickle_dick_2.dosya_yedekle()

def deger_ver():
    if combo.get() in sozluk:
        lbl.configure(text=str(sozluk[combo.get()]).upper())
    elif combo.get()=="":
        combo.current(0)
    elif en_yakin.get() !=-1:
        combo.current(en_yakin.get())
        lbl.configure(text=str(sozluk[combo.get()]).upper())
        en_yakin.set(-1)
    elif len(sozluk)==0:
        lbl.configure(text="Sifir Yok !")
    else:
        lbl.configure(text="Yanlish Sechim !")
        combo.current(0)
        print("yanlish sectin")
    en_yakin.set(-1)

def acikmi(x):
    if pencere_acikmi[x]:
        print("Zaten AchIK")
        return 1
    else:
        pencere_acikmi[x]=1

def degis_yeni():

    if acikmi("degis_yeni"): return

    if (len(sozluk)==0) or (combo.get() not in sozluk): return

    a = tkinter.Toplevel(w)
    a.title("Degishtirme Ekrani")
    a.geometry('450x350')

    lb =  Label(a, text ="<< "+(combo.get()).upper()+" >>"+"\n ichin yeni bir anlam gir")
    lb.pack(pady=20)

    tx1 = Entry(a,relief=RAISED, justify=CENTER, width=25,
                selectborderwidth=3, bd=5,bg="azure",fg="red",font=("ariel",22))

    txt = Entry(a,relief=RAISED, justify=CENTER, width=25,
                selectborderwidth=3, bd=5,bg="azure",fg="red",font=("ariel",22))
    tx1.pack()
    txt.pack()

    txt.focus()

    tx1.insert(END,combo.get())
    tx1.select_to(END)

    txt.insert(END,sozluk[combo.get()])
    txt.select_to(END)

    def yeni_anlam_gir():
        if txt.get()=="":
            print("bishi girmedin")
        else:
            sozluk.update({combo.get():txt.get()})
            print("kayit degishtirildi")
            lb.config(text=combo.get()+" guncellendi")
            txt.delete(0,END)

    bos(a)

    def cik_degis():
        pencere_acikmi["degis_yeni"]=0
        a.destroy()

    btn = Button(a, text="OK",width=14, command=yeni_anlam_gir).pack()

    btn = Button(a,text="chIK",bg="red",fg="white", command=cik_degis).pack(side="right")

    a.protocol('WM_DELETE_WINDOW', cik_degis)

    def callback(event):
        yeni_anlam_gir()

    a.bind("<Return>", callback)

def sil():
    global key

    if combo.get() in sozluk:
        if messagebox.askyesno("\nsiliyom-> {}".format(combo.get()),icon="warning") :

            nerdeyim=combo.current()
            lbl.configure(text="kayit silindi :"+sozluk.pop(combo.get()))
            key=list(sozluk.keys())
            key.sort()
            combo['values']= key
            if nerdeyim>0 :
                combo.current(nerdeyim-1)
            else:
                combo.current(0)
            kay.configure(text=("kayit adedi "+str(len(sozluk))))
    else:
        lbl.configure(text="Yanlish Sechim !")
        print("yanlish sectin")
#---------------------------------------------------------------------------
def ekle_yeni():
    if acikmi("ekle_yeni"):return
    global key
##    a = tkinter.Toplevel(w)
##    a.title("Yeni Kelime Girish Ekrani")

    a=Frame(w)
    a.grid(column=0, row=1,sticky="n")

    w.unbind("<Return>")

    lbn=Label(a,fg="red")
    lbn.grid(column=2,row=0)

    txt = Entry(a,relief=RIDGE, width=22, bd=3,bg="cornsilk",fg="red",font=("ariel",22))
    txt1 = Entry(a,relief=RIDGE, width=22, bd=3,bg="cornsilk",fg="blue",font=("ariel",22))

    Label(a, text = "Kelime : ").grid(column=0,row=1)
    txt.grid(column=2,row=1,columnspan=1)

    Label(a, text = "Anlami : ").grid(column=0,row=2)
    txt1.grid(column=2,row=2,columnspan=1)

    txt.focus()

    def koy(event): txt.insert(END,event)

    OptionMenu(a, StringVar(),*["á","é","í","ó","ú","ñ","Ñ","u","u","¿","¡"],command=koy).grid(row=1,column=3)

    def gir():
        if txt.get() in sozluk:
            mes="Bu kayit var->\n"+sozluk[txt.get()]

            txt.delete(0, END)
        elif txt.get()=="" or txt1.get()=="":
            mes="Veri eksik"
        else:
            sozluk.update({txt.get():txt1.get()})
            mes=str(len(sozluk))+". kayit eklendi,dosyaya yazmayi unutma"
            kay.configure(text=("kayit adedi "+str(len(sozluk))))
            key=list(sozluk.keys())
            key.sort()
            combo['values']= key
            txt.delete(0, END)
        lbn.configure(text = mes)

        txt1.delete(0, END)
        txt.focus()
        a.after(1500,lambda:lbn.configure(text = ""))

    def cik_ekle_yeni():
        w.unbind("<Return>")
        w.bind("<Return>", callb)
        pencere_acikmi["ekle_yeni"]=0
        a.destroy()

    def callbac(event):
        gir()

    w.bind("<Return>", callbac)

    Button(a, text="OK",width=14, command=gir).grid(column=2,row=3)

    Button(a,text="Kapat", command=cik_ekle_yeni).grid(column=3,row=3)

    boss(a)
#---------------------------------------------------------------------------
def kel_kart():
    if acikmi("kel_kart"): return
    t = tkinter.Toplevel(w)
    t.title("Kelime Karti")
    t.geometry('550x250')

    w.iconify()

    t.focus_set()
    kelime=StringVar()
    kelime.set("kelime > tik > anlam")
    say=0
    i=0
    rng = random.Random()
    a=list(range(len(key)))
    rng.shuffle(a)

    progressbar=tkinter.ttk.Progressbar(t,maximum=len(a),orient="horizontal",length=200,mode="determinate")
    progressbar.pack(side="bottom")

    def rasgele():
        nonlocal say,i
        say+=1
        print(say,"\t",i,"\t",a[i])
        if say%2:
            kelime.set(">> "+key[a[i]]+" <<")
            btn9["bg"]="white"
        else:
            kelime.set(sozluk[key[a[i]]])
            btn9["bg"]="yellow"
            i+=1
            progressbar["value"]=i
            if i==len(a):
                i=0

    def callback(event):
        rasgele()

    t.bind("<Return>", callback)

    def cik_kel_kart():
        pencere_acikmi["kel_kart"]=0
        t.destroy()
        w.deiconify()

    t.protocol('WM_DELETE_WINDOW', cik_kel_kart)

    btn9 = Button(t, relief=RIDGE,textvariable=kelime, height=3,width=22,wraplength=450,
           bd=16,bg="white",fg="blue",font=("ariel bold",28), command=rasgele)
    btn9.pack(pady=50)
#---------------------------------------------------------------------------
def tercih():

    if acikmi("tercih"): return
    if len(sozluk)<4 : return

    global sorulanlar,yannislar

    t = tkinter.Toplevel(w)
    t.title("Soru Ekrani")

    w.iconify()

##    t.geometry('600x530')
##    t.focus_set()

    def cark_cevir():
        ras=[]
        rng = random.Random()
        for i in range(4):
            while True:
                a=rng.randrange(0,len(key))
                if a not in ras:
                    break
            ras.append(a)
        return ras

    def siklari_kar():
        rng = random.Random()
        karma=list(range(4))
        rng.shuffle(karma)
        return karma

    bos(t)

    sor=[]
    soru=StringVar()
    cevap=StringVar()
    mesaj=StringVar()
    v = StringVar()
    dogru_tik=0
    yannis_tik=0

    lbt = Label(t,relief=RIDGE, width=25,height=2,bd=3,bg="alice blue",fg="red",textvariable=soru,font=("ariel",20))
    lbt.pack(side="top")

    lbc = Label(t, fg="blue",textvariable=mesaj )
    lbc.pack()

    r1 = Radiobutton(t,text="",bg="gainsboro", value="a",variable=v,indicatoron=0)
    r1.pack(padx=40,pady=10,anchor="w")
    r2 = Radiobutton(t,text="",bg="silver",    value="b",variable=v,indicatoron=0)
    r2.pack(padx=40,anchor="w")
    r3 = Radiobutton(t,text="",bg="gainsboro", value="c",variable=v,indicatoron=0)
    r3.pack(padx=40,pady=10,anchor="w")
    r4 = Radiobutton(t,text="",bg="silver",    value="d",variable=v,indicatoron=0)
    r4.pack(padx=40,anchor="w")

    progressbar=tkinter.ttk.Progressbar(t,maximum=len(key),orient="horizontal",length=300,mode="determinate")
    progressbar.pack(side="bottom")

    def yeni_kelime():
        global sorulanlar,yannislar
        print("YENİ KELİME")

        while True:
            sor=cark_cevir()
            if key[sor[0]] not in sorulanlar:
                break
            if len(sorulanlar)==len(key):
                print("bitti sayachlari resetliyom")
                mesaj.set("bitti sayachlari resetliyom")
                sorulanlar.clear()
                sorulanlar=saklananlar[:]
                progressbar["value"]=len(sorulanlar)

                return

        sorulanlar.append(key[sor[0]])
        sorulanlar.sort()
        si=siklari_kar()
        soru.set(key[sor[0]])
        cevap.set(sozluk[key[sor[0]]])
        v.set("")

        a=sozluk[key[sor[si[0]]]]
        b=sozluk[key[sor[si[1]]]]
        c=sozluk[key[sor[si[2]]]]
        d=sozluk[key[sor[si[3]]]]

        r1.config(text="a) "+ a, value=a)
        r2.config(text="b) "+ b, value=b)
        r3.config(text="c) "+ c, value=c)
        r4.config(text="d) "+ d, value=d)
        etkin()
        progressbar["value"]=len(sorulanlar)
        mesaj.set("Bir Sechim Yap "+str(len(sorulanlar)))

        print("\nsorulan:",len(sorulanlar),"\nsaklanan:",len(saklananlar),"\nyannis:",len(yannislar))

    def rad_clicked():
        nonlocal dogru_tik
        nonlocal yannis_tik
        print(v.get())
        if v.get()=="":
            print("sechmedin")
            mesaj.set("Sechmedin")

        else:
            print("sechtin",v.get(),soru.get(),cevap.get())
            if cevap.get()==v.get():
                dogru_tik+=1
                print("DOgRU")
                lbc.config(fg="blue")
                mesaj.set("DOgRU "+str(dogru_tik))
                etkisiz()

            else:
                t.bell()
                print("YALINIsh")
                lbc.config(fg="red")
                mesaj.set("YALINIsh "+str(yannis_tik))
                yannis_tik+=1
                if soru.get() not in yannislar: yannislar.append(soru.get())

    btn8 = Button(t, text="Kontrol et",width=40,height=2, command=rad_clicked,bg="alice blue")
    btn8.pack(anchor="c",pady=10)

    def etkisiz():
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)
        btn8.config(state=DISABLED)

    def etkin():
        r1.config(state=NORMAL)
        r2.config(state=NORMAL)
        r3.config(state=NORMAL)
        r4.config(state=NORMAL)
        btn8.config(state=NORMAL)

    def yaz_cik():
        pickle_dick_2.sorulmuslari_yaz(sorulanlar,saklananlar,yannislar)
        print("\nsorulan:",len(sorulanlar),"\nsaklanan:",len(saklananlar),"\nyannis:",len(yannislar))
        pencere_acikmi["tercih"]=0
        t.destroy()
        w.deiconify()

    t.protocol('WM_DELETE_WINDOW', yaz_cik)

    def sorulanlar_resetle():
        global sorulanlar
        sorulanlar.clear()
        sorulanlar=saklananlar[:]
        progressbar["value"]=len(sorulanlar)
        yeni_kelime()

    def sakla():
        if soru.get() not in saklananlar:
            saklananlar.append(soru.get())
            saklananlar.sort()
            print("saklanan:",len(saklananlar))

    btn9 = Button(t, text="Yeni Kelime",width=40,height=1,bg="gold", command=yeni_kelime)
    btn9.pack(pady=10,padx=10)

    btn10 = Button(t,text="chikish",bg="red",fg="white",command=yaz_cik)
    btn10.pack(side=RIGHT,pady=10,padx=10)

    btn10 = Button(t,text="reset",bg="black",fg="white",command=sorulanlar_resetle)
    btn10.pack(side=LEFT,pady=10,padx=10)

    btn10 = Button(t,text="sakla",bg="grey",fg="white",command=sakla)
    btn10.pack(side=LEFT,pady=10,padx=10)

    yeni_kelime()

    def saklanan_reset():
        if messagebox.askyesno("emin misun?"):
            saklananlar.clear()

    menubar = Menu(t)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label = "yannislar" , command=lambda:yannislar.clear())
    filemenu.add_command(label="saklananlar",command=saklanan_reset)
    menubar.add_cascade(label="Reset", menu=filemenu)
    t.config(menu=menubar)
#---------------------------------------------------------------------------
def liste_kutusu():

    t = tkinter.Toplevel(w)
    t.title("LİSTE")
    t.geometry('550x500')

    f1=LabelFrame(t,text="kELLİmE",relief=RIDGE,bd=10,bg="ghost white")
    f1.pack(fill=BOTH,expand=1,side=TOP)

    f2=LabelFrame(t,text="AnLaMi",relief=RIDGE,bd=10,bg="snow")
    f2.pack(fill=X,expand=1,side=LEFT)

    f3=Frame(t,relief=RIDGE)
    f3.pack(fill=X,expand=1,side=LEFT)

    lb1=Label(f1,text="listelerr",wraplength=450,font=("ariel",20))
    lb1.pack()

    scrollbar = Scrollbar(f2)
    scrollbar.pack( side = RIGHT, fill = Y )

    listem=StringVar()

    lb=Listbox(f2,listvariable=listem,bg="snow", height=14,yscrollcommand = scrollbar.set)
    lb.pack()

    scrollbar.config( command = lb.yview )

    def yannislari_getir() : listem.set(yannislar)

    def saklananlari_getir() : listem.set(saklananlar)

    def tumunu_getir() :     listem.set(key)

    Button(f3, text="Tam Liste", command= tumunu_getir).pack()
    bos(f3)
    Button(f3, text="yannislar", command= yannislari_getir).pack()
    bos(f3)
    Button(f3, text="saklananlar",command= saklananlari_getir).pack()

    def goster(event):
        keyy=lb.get(ANCHOR)
        if keyy !="" and keyy in sozluk:
            lb1.config(text=sozluk[keyy])
            print(sozluk[keyy])
        else: print("kayit yok")

    lb.bind("<<ListboxSelect>>",goster)

    tumunu_getir()
#---------------------------------------------------------------------------
def callb(event):
        deger_ver()

def hh(event):
    aktif_satir = combo.get()
    print("ComboBox KeyReleased :")
    for indeks, key_ in enumerate(key):
        if key_.startswith(aktif_satir):
            print(indeks, key_)
            en_yakin.set(indeks)
            return

w.bind("<Return>", callb)

combo.bind("<KeyRelease>", hh)


def call_to_text():

    print(mytext(w).a)


#******************************************
menubar = Menu(w)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = "YEDEKLE" , command=dosya_yedek)
filemenu.add_command(label="YuKLE",command=dosya_sec)
filemenu.add_command(label="KAYDET",command=dosyaya)
menubar.add_cascade(label="DOSYALAR", menu=filemenu)

exmenu= Menu(menubar, tearoff=0)
exmenu.add_command(label="to CVS ",command=lambda:pickle_dick_2.export_to_cvs_file(sozluk))
exmenu.add_command(label="to TXT ",command=lambda:pickle_dick_2.export_to_text_file(sozluk))
exmenu.add_command(label="to JSON ",command=lambda:pickle_dick_2.export_to_json_file(sozluk))

menubar.add_cascade(label="EXPORT", menu=exmenu)

w.config(menu=menubar)
#--------------------------------
g=10

sol.grid(column=0, row=0,sticky="n", padx=20, pady=20)

sag=Frame(w,bg=w.cget("bg"))
sag.grid(column=1, row=0,rowspan=2,ipadx=10,ipady=10, padx=20, pady=20)

def boss(master): Label(master,bg=w.cget("bg")).grid()

#--------------frame left---------

lbl=Label(sol,relief=RIDGE, width=32,height=4,bd=5,bg="azure",fg="blue",text="Kelime Anlami",wraplength=470,font=("ariel",20))
lbl.grid()
boss(sol)
combo.grid()
boss(sol)
im = tkinter.PhotoImage(file="forward.png")
Button(sol, image=im,bg="lavender",command=deger_ver).grid()
boss(sol)

#---------------frame right------

#"error","gray75","gray50","gray25","gray12","hourglass","info","questhead","question","warning"
boss(sag)
Button(sag, text="shiklar",bg="lime",width=g,command=tercih).grid(pady=2)

Button(sag, text="Kelime Karti",bg="lime",width=g,command=kel_kart).grid(pady=2)
boss(sag)
Button(sag, text="Ekle",bg="alice blue",width=g,command=ekle_yeni).grid(pady=2)

Button(sag, text="Sil",bg="alice blue",width=g,command=sil).grid(pady=2)

Button(sag, text="Degishtir",bg="alice blue",width=g,command=degis_yeni).grid(pady=2)
boss(sag)
##Button(sag, text="Kaydet",bg="dark turquoise",width=g,command=dosyaya).grid(pady=2)

##Button(sag, text="Yedekle",bg="dark turquoise",width=g,command=dosya_yedek).grid(pady=2)

##Button(sag, text="Yukle",bg="dark turquoise",width=g,command=dosya_sec).grid(pady=2)
boss(sag)
Button(sag, text="ListBoks",width=g,command=liste_kutusu).grid(pady=2)

Button(sag,text="Karalama",width=g,command=call_to_text).grid(pady=2)
boss(sag)

Button(sag,text="test buton",width=g,command=lambda:print(karala)).grid(pady=2)
boss(sag)


Button(sag,text="YAZ chIK",relief=RIDGE,bd=3,bg="red",fg="white",font=("ariel bold",10),command=yaz_ve_cik).grid(pady=2)

##im = tkinter.PhotoImage(file="d:\\8.png")
##btn2 = Button(w,relief=RIDGE,image=im,text="YAZ_chIK",compound="top",bg="black",fg="white",font=("ariel bold",10),command=yaz_ve_cik)
##btn2.grid(column=2, row=0,sticky="e")

kay=Label(w,text="Kayit Adedi : {} ".format(len(sozluk)),bd=1, relief=SUNKEN,bg="silver",fg="white",anchor="e")
kay.grid(columnspan=2,sticky="ew")

print("kayit adedi",len(sozluk))

def cikis():
    if messagebox.askyesno("KAYIT-> İLK:{} SON:{}".format(ilk,len(sozluk))," KAYDEDİİM Mİ") :
        pickle_dick_2.yaz(sozluk)
    w.destroy()

w.protocol('WM_DELETE_WINDOW', cikis)

w.mainloop()


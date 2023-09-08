import tkinter as tk

class mytext:
    def __init__(self,root):

        self.window = True
        self.t=tk.Toplevel(root)

        self.a=self.t.winfo_id()

        self.b=self.t.winfo_exists()

        self.c=self.t.winfo_ismapped()

        self.d=self.t.winfo_name()

        self.sayfa=tk.Text(self.t)
        self.sil_btn=tk.Button(self.t,text="sil",command=self.temizle)
        self.cik_btn=tk.Button(self.t,text="çık",command=self.cikis)
        self.t.title("karalama defteri")

        self.sayfa.pack()
        self.sil_btn.pack(side=tk.LEFT)
        self.cik_btn.pack()

        self.dosyadan_al()  #buna bi bak

        self.sayfa.focus_set()

        self.t.protocol('WM_DELETE_WINDOW', self.cikis)

    def temizle(self):
        self.sayfa.delete("1.0",tk.END)

    def dosyaya_kaydet(self):
        print("text dosyası kayıt ediliyor")
        with open("esp2eng_k.txt","w") as f:
            f.write(self.sayfa.get("1.0","end-1c"))

    def dosyadan_al(self):
        print("text dosyasından kayıt alınıyor")
        try:
            with open("esp2eng_k.txt","r") as f:
                a=f.read()
                self.sayfa.insert(tk.END,a)
        except:
            print("dosya henüz yok çıkışta yeni oluşcak")

    def cikis(self):
        self.dosyaya_kaydet()
        self.t.destroy()




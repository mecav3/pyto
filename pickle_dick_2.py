import pickle


def oku(dosyam='eng_eng.soz'):
    # read python dict from the file and return a dict
    try:
        dosya = open(dosyam, 'rb')
        aktif_dict = pickle.load(dosya)
        dosya.close()
        print("\nDosyadan veriler alindi\n",len(aktif_dict))
        return aktif_dict
    except:
        print("\nDOSYA YOK,yeni olushturim mi sen kendin Yuklermisin\n")
        if str(input("yes/no ?")).lower()[0]=="y":
            dosya = open('eng_eng.soz', 'wb')
            pickle.dump({"ilk":"kayit"},dosya)
            dosya.close()
            print("yeni dosya oldu")
        print("çiktim")
        return {"ilk":"kayit"}

def veri_gir(aktif_dict):
    a=str(input("un vocabilario:"))
    b=str(input("English meaning:"))
    if a=="" or b=="":
        print("\nVeri Girishi İptal\n")
        return
    if a in aktif_dict:
        print("\nBu kayit var çikiyom\n")
        return
    aktif_dict.update({a:b})
    print("\nVeri eklendi\n",aktif_dict)

def degistir(aktif_dict):
    a=str(input("un vocabilario:"))
    b=str(input("English meaning:"))
    if a=="" or b=="":
        print("\nGüncelleme İptal\n")
        return
    if a not in aktif_dict:
        print("\nBu kayit yok güncelleyemessin VERİ_GİR'i çalishtir\n")
        return
    aktif_dict.update({a:b})
    print("\nGüncellendi\n",aktif_dict)

def yaz(aktif_dict):
    dosya = open('eng_eng.soz', 'wb')
    pickle.dump(aktif_dict, dosya)
    dosya.close()
    print("\n",len(aktif_dict),"kayit dosyaya yazildi\n")

def sil(aktif_dict):
    for (i,j) in aktif_dict.items(): print(i,"=",j,"\n")
    s=str(input("\nhangisini silmeli ?\n"))
    if s not in aktif_dict:
        print("\nbu kelime yok\n")
        return
    print("\n.........silindi",aktif_dict.pop(s))
    print("\nkalanlar\n")
    for (i,j) in aktif_dict.items(): print(i,"=",j,"\n")

def dosya_yedekle():
    import datetime

    months = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    x = datetime.datetime.now()
    yedek_dosya_adi="eng_eng_{}_{}_{}.soz".format(x.day,months[x.month],str(x.year)[:2])

    try:
        f = open('eng_eng.soz', 'rb')
        g = open(yedek_dosya_adi, "wb")
        i=0
        while True:
            buf = f.read(1014)
            if len(buf) == 0:
                break
            i+=1
            g.write(buf)
        print(i,"kilobayt YEDEKLENDİ")
        f.close()
        g.close()
    except:
        print("DOSYA YOK yedekleme iptal")

def sorulmuslari_oku():
    # read sorulanlar from the file and return
    try:
        dosya = open('eng_eng_.sox', 'rb')
        sorulmus = pickle.load(dosya)
        saklanan = pickle.load(dosya)
        yannislar= pickle.load(dosya)
        dosya.close()
        print("\nDosyadan sorulmushlar:",len(sorulmus),"\nSaklanan:",len(saklanan),"\nyannis:",len(yannislar))
        return sorulmus,saklanan,yannislar
    except:
        print("\nsorulmushlar dosyasi YOK,yeni olushturimmi\n")
        if str(input("yes/no ?"))[0]=="y":
            dosya = open('eng_eng_.sox', 'wb')
            pickle.dump([],dosya)
            pickle.dump([],dosya)
            pickle.dump([],dosya)
            dosya.close()
            print("yeni dosya oldu")
        print("çiktim")
        return [], [], []

def sorulmuslari_yaz(sorulan_listesi,saklanan_listesi,yannislar_listesi):
    # write sorulanlar to file
        dosya = open('eng_eng_.sox', 'wb')
        pickle.dump(sorulan_listesi,dosya)
        pickle.dump(saklanan_listesi,dosya)
        pickle.dump(yannislar_listesi,dosya)

        dosya.close()
        print("\nsorulmushlar dosyaya yazdim\n")

def export_to_text_file(dictin):
    a=[]
    with open('c:\\users\\hhm\\desktop\\lotr.txt','w',encoding="utf-8") as f:
        for i,j in dictin.items():
            a.append([i,j])
        a.sort()
        for i,j in a:
            f.writelines(i+"="+j+"\n")
        print("DOSYA yazildi :: eng_eng.TXT")

def export_to_cvs_file(dictin):
    import csv
    a=[]
    with open( "eng_eng.csv", "w", newline='' ) as f:
        writer = csv.writer(f,delimiter=',')
        for i,j in dictin.items():
            a.append([i,j])
        a.sort()
        writer.writerows(a)
        print("DOSYA yazildi :: eng_eng.CSV")

def export_to_json_file(dictin):
    import json
##    z=json.dumps(dictin, indent=2, sort_keys=True, separators=(", ", ": "))

    with open('eng2_json.txt', 'w') as json_file:
        json.dump(dictin, json_file,indent=2,sort_keys=True,separators=(", ", ": "))
    print("DOSYA yazildi :: eng2_JSON.txt")


if __name__ == '__main__':

    soz=oku()

    veri_gir(soz)

    sil(soz)

    yaz(soz)

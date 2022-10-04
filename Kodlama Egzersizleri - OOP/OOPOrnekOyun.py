import time,sys,random

def hatalı_eksik():
    print("!Eksik ya da Hatalı Tuşlama!")

def nokta_ekle():
    print(".")
    time.sleep(.3)
    print("..")
    time.sleep(.3)
    print("...")
    time.sleep(.3)

class Oyuncu():
    def __init__(self,isim,can=10,power=100,puan=0):
        self.isim = isim
        self.can = can
        self.power = power
        self.puan = puan

    def bilgileri_goster(self):
        print("""
        
        İsim: {}
        Can: {}
        Power: {}
        Puan: {}
        """.format(self.isim,self.can,self.power,self.puan))

    def saldir(self, dusman):
        sonuc = self.saldir_savun_sayi()
        if(sonuc==1):
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı Başarılı")
            self.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()

        else:
            print("Saldırı Başladı...")
            nokta_ekle()
            print("Saldırı Başarısız")
            self.power -= 8
            self.can -= 1
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()

    def savun(self,dusman):
        sonuc = self.saldir_savun_sayi()
        if (sonuc == 1):
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma Başarılı")
            dusman.power -= 8
            self.puan += 10
            dusman.can -= 1
            self.bilgileri_goster()
            dusman.bilgileri_goster()
        else:
            print("Savunma Başladı...")
            nokta_ekle()
            print("Savunma Başarısız")
            dusman.power -= 8
            self.can -= 1
            dusman.puan += 10
            self.bilgileri_goster()
            dusman.bilgileri_goster()

    def saldir_savun_sayi(self):
        return random.randint(1,2)

    def exit(self):
        print("Oyun Kapatılıyor...")
        nokta_ekle()
        sys.exit()

oyuncu1 = Oyuncu("Ahmet")
oyuncu2 = Oyuncu("Mehmet")

print("Oyun Başlatılıyor...")
nokta_ekle()

while True:
    hamle = input("""
    1-Saldır
    2-Savun
    3-Çık
    Hamle Seçimi:
    """)

    if(hamle=="1"):
        oyuncu1.saldir(oyuncu2)
    elif(hamle=="2"):
        oyuncu1.savun(oyuncu2)
    elif(hamle=="3"):
        oyuncu1.exit()
    else:
        hatalı_eksik()

    if(oyuncu1.puan==100 or oyuncu2.can==0 or oyuncu2.power<=0):
        print("Oyunun Kazananı:", oyuncu1.isim)
        break
    if(oyuncu2.puan==100 or oyuncu1.can==0 or oyuncu1.power<=0):
        print("Oyunun Kazananı:", oyuncu2.isim)
        break

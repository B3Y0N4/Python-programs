pi = 3.14

def kare_cevre(kare_kenar):
    cevre = kare_kenar*4
    print("Karenin Çevresi:", cevre)
def kare_alan(kare_kenar):
    alan = kare_kenar*kare_kenar
    print("Karenin Alanı:", alan)

def dikdortgen_cevre(uzun_kenar,kisa_kenar):
    cevre = (uzun_kenar*2)+(kisa_kenar*2)
    print("Dikdörtgenin Çevrei:", cevre)
def dikdortgen_alan(uzun_kenar,kisa_kenar):
    alan = uzun_kenar*kisa_kenar
    print("Dikdörtgenin Alanı:", alan)

def ucgen_cevre(taban, ilk_kenar, ikinci_kenar):
    cevre = taban+ilk_kenar+ikinci_kenar
    print("Üçgenin Çevresi:", cevre)
def ucgen_alan(taban,yukseklik):
    alan = (taban*yukseklik)/2
    print("Üçgenin Alanı:", alan)

def daire_cevre(yari_cap):
    cevre = 2*pi*yari_cap
    print("Dairenin Çevresi:", cevre)
def daire_alan(yari_cap):
    alan = pi*(yari_cap**2)
    print("Dairenin Alanı:", alan)


def hesaplama_turleri():
    print("""Hesaplama Şekilleri
                        1-Çevre
                        2-Alan""")

def eksik_tuslama():
    print("******Eksik ya da Hatalı Tuşlama!******")


while True:
    print("""Şekil Cevre-Alan Hesaplama Programına Hoşgeldiniz
            Hesaplama Yapılabilen Şekiller
            Kare
            Dikdörtgen
            Üçgen
            Daire
            Programdan çıkmak için 'q' tuşlaması yapın!""")
    sekil = input("Lütfen Bir Şekil Seçin:")

    if(sekil=="q"):
        print("Program kapatılıyor...")
        break
    elif(sekil == "kare" or sekil== "Kare"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = input("Lütfen Hesaplama Türünü Seçin:")
            if(hesaplama_turu == "1"):
                kare_kenar = int(input("Karenin Bir Kenarını Girin:"))
                kare_cevre(kare_kenar)
                break
            elif(hesaplama_turu == "2"):
                kare_kenar = int(input("Karenin Bir Kenarını Girin:"))
                kare_alan(kare_kenar)
                break
            else:
                eksik_tuslama()
    elif(sekil == "dikdörtgen" or sekil == "Dikdörtgen"):
        while True:

            hesaplama_turleri()
            hesaplama_turu = input("Lütfen Hesaplama Türünü Seçin:")
            if(hesaplama_turu=="1"):
                uzun_kenar = int(input("Uzun Kenarı Girin:"))
                kisa_kenar = int(input("Kısa Kenarı Girin:"))
                dikdortgen_cevre(uzun_kenar,kisa_kenar)
                break
            elif(hesaplama_turu=="2"):
                uzun_kenar = int(input("Uzun Kenarı Girin:"))
                kisa_kenar = int(input("Kısa Kenarı Girin:"))
                dikdortgen_alan(uzun_kenar, kisa_kenar)
                break
            else:
                eksik_tuslama()


    elif(sekil=="üçgen" or sekil=="Üçgen"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = input("Lütfen Hesaplama Türünü Seçin:")
            if(hesaplama_turu=="1"):
                taban = int(input("Tabanı Girin:"))
                ucgen_ilk_kenar = int(input("Üçgenin İlk Kenarını Girin:"))
                ucgen_ikinci_kenar = int(input("Üçgenin İkinci Kenarını Girin:"))
                ucgen_cevre(taban,ucgen_ilk_kenar,ucgen_ikinci_kenar)
                break
            elif(hesaplama_turu=="2"):
                taban = int(input("Tabanı Girin:"))
                yukseklik = int(input("Yüksekliği Girin:"))
                ucgen_alan(taban,yukseklik)
                break
            else:
                eksik_tuslama()

    elif(sekil=="daire" or sekil=="Daire"):
        while True:
            hesaplama_turleri()
            hesaplama_turu = input("Lütfen Hesaplama Türünü Seçin:")
            if(hesaplama_turu=="1"):
                yari_cap = int(input("Yarıçapı Girin:"))
                daire_cevre(yari_cap)
                break
            elif(hesaplama_turu=="2"):
                yari_cap = int(input("Yarıçapı Giriniz:"))
                daire_alan(yari_cap)
                break
            else:
                eksik_tuslama()
    else:
        eksik_tuslama()


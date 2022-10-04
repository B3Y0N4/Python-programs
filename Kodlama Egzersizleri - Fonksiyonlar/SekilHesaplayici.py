pi = 3.14

def sekil_cesitleri():
    print("""Hesaplama Yapılabilen Şekiller\n
            Kare
            Dikdörtgen
            Üçgen
            Daire
            Çıkmak için 'q' tuşlaması yapın.""")
    global sekil
    sekil = input("Lütfen Bir Şekil Seçiniz: ")



def hesap_turu():
    print("""Hesaplama Çeşitleri\n
    1-Çevre
    2-Alan""")


def kare_cevre(kenar):
    cevre = kenar*4
    print("Karenin Çevresi:", cevre)
def kare_alan(kenar):
    alan = kenar*kenar
    print("Karenin Alanı:", alan)

def dikdortgen_cevre(uzun_kenar,kisa_kenar):
    cevre = (uzun_kenar*2)+(kisa_kenar*2)
    print("Dikdörtgenin Çevresi:", cevre)

def dikdortgen_alan(uzun_kenar, kisa_kenar):
    alan = uzun_kenar*kisa_kenar
    print("Dikdörtgenin Alanı:", alan)

def ucgen_cevre(taban,ilk_kenar,ikinci_kenar):
    cevre = taban+ilk_kenar+ikinci_kenar
    print("Üçgenin Çevresi:", cevre)

def ucgen_alan(taban, yukseklik):
    alan = (taban*yukseklik)/2
    print("Üçgenin Alanı:", alan)

def daire_cevre(yari_cap):
    cevre = 2*yari_cap*pi
    print("Dairenin Çevresi:", cevre)
def daire_alan(yari_cap):
    alan = pi*yari_cap**2
    print("Dairenin Alanı:", alan)

while True:
    sekil_cesitleri()
    if(sekil=="q"):
        print("Program Sonlandırılıyor...")
        break

    elif(sekil=="kare" or sekil=="Kare"):
        while True:
            hesap_turu()
            cevre_alan = input("Lütfen Bir Hesaplama Türü Seçiniz:")
            if (cevre_alan == "1"):
                kare_kenar = int(input("Karenin Bir Kenarını Girin:"))
                kare_cevre(kare_kenar)
                break
            elif (cevre_alan == "2"):
                kare_kenar = int(input("Karenin Bir Kenarını Girin:"))
                kare_alan(kare_kenar)
                break
            else:
                print("Yanlış Tuşlama!")

    elif (sekil == "dikdörtgen" or sekil == "Dikdörtgen"):
        while True:

            hesap_turu()
            cevre_alan = input("Lütfen Bir Hesaplama Türü Seçiniz:")
            if (cevre_alan == "1"):
                uzun_kenar = int(input("Uzun Kenarı Girin:"))
                kisa_kenar = int(input("Kısa Kenarı Girin:"))
                dikdortgen_cevre(uzun_kenar,kisa_kenar)
                break

            elif (cevre_alan == "2"):
                uzun_kenar = int(input("Uzun Kenarı Girin:"))
                kisa_kenar = int(input("Kısa Kenarı Girin:"))
                dikdortgen_alan(uzun_kenar,kisa_kenar)
                break

            else:
                print("Yanlış Tuşlama!")



    elif(sekil=="üçgen" or sekil=="Üçgen"):
        while True:

            hesap_turu()
            cevre_alan = input("Lütfen Bir Hesaplama Türü Seçiniz:")
            if (cevre_alan == "1"):
                ucgen_taban = int(input("Üçgen Taban Kenarını Girin:"))
                ucgen_ilk_kenar = int(input("Üçgen Birinci Kenarını Girin:"))
                ucgen_ikinci_kenar = int(input("Üçgen İkinci Kenarını Girin:"))
                ucgen_cevre(ucgen_taban, ucgen_ilk_kenar, ucgen_ikinci_kenar)
                break

            elif (cevre_alan == "2"):
                ucgen_taban = int(input("Üçgenin Taban Kenarını Girin:"))
                yukseklik = int(input("Üçgenin Yükskeliğini Girin:"))
                ucgen_alan(ucgen_taban, yukseklik)
                break

            else:
                print("Yanlış Tuşlama!")


    elif (sekil == "daire" or sekil == "Daire"):
        while True:

            hesap_turu()
            cevre_alan = input("Lütfen Bir Hesaplama Türü Seçiniz:")
            if (cevre_alan == "1"):
                yari_cap = int(input("Yarıçapı Girin:"))
                daire_cevre(yari_cap)
                break

            elif (cevre_alan == "2"):
                yari_cap = int(input("Yarıçapı Girin:"))
                daire_alan(yari_cap)
                break

            else:
                print("Yanlış Tuşlama!")
    else:
        print("******Eksik ya da Hatalı Tuşlama******")
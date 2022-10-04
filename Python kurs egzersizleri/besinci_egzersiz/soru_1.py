#Sayi tahmin oyunu
import random
import time
def kolay_sevye(tahmim):
    sayi = random.randrange(1,10)
    tahmin_sayaci = 1
    while True:
        if tahmim == sayi:
            print (f"Bravo {tahmin_sayaci}. tahminiz'de Bidiniz!") 
            break
        elif tahmim > sayi:
            print ("Tahmininizi Azaltin")
            tahmin_sayaci += 1 
            tahmim = int(input("Sayi Tekrar Giriniz: (1 ile 10 arasinda)"))
        elif tahmim < sayi:
            print ("Tahminizi Yükseltin")
            tahmin_sayaci += 1 
            tahmim = int(input("Sayi Tekrar Giriniz: (1 ile 10 arasinda)"))

def orta_sevye(tahmim):
    sayi = random.randrange(1,10)
    tahmin_sayaci = 1
    max_tahmin = 5
    while True:
        if tahmim == sayi:
            print (f"Bravo {tahmin_sayaci} tahminiz'de Bidiniz!") 
            break
        elif tahmim > sayi:
            print ("Tahmininizi Azaltin")
            tahmin_sayaci += 1 
            max_tahmin -=1
            tahmim = int(input(f"Sayi Tekrar Giriniz: (1 ile 10 arasinda) {max_tahmin}/5 "))
        elif tahmim < sayi:
            print ("Tahminizi Yükseltin")
            tahmin_sayaci += 1 
            max_tahmin -=1
            tahmim = int(input("Sayi Tekrar Giriniz: (1 ile 10 arasinda) {max_tahmin}/5 "))
        if   max_tahmin < 1 and tahmim != sayi:
            print (f"""
                     Oyunu Kaybetiniz 
                     Tahmin Etmeye Çaliştiniz sayir {sayi}'di
                     Dilerseniz Kolay Sevyeyi Deneyebilersiniz 
                     oynamak için 1 "q" tüşlamaniz yeterli
                     """)
            devem_durumu =input("Kolay sevyeyi Oynamak İçin 'q' tiklayiniz oyundan çikmak için 'Enter Tüşüna tiklayiniz")
            if devem_durumu == "q":
                print ("""
                          Tahmin Oyunun Kolay Seviyesine Hoşgeldiniz
                          Bu Seviyede Doğru tahmin Yapana kadar Oyanayabilirsiniz.
                          """)
                tahmim = int(input("Sayi Tahmininizi Giriniz: (1 ile 10 arasinda)"))
                kolay_sevye(tahmim)
            else:
                print ("Oyunu Sonladirdiniz")
                break
def geri_sayim():
    for i in range (3,0,-1):
        time.sleep(1)
        print (i)

 

print (""" 
    Sayi Tahmini oyununa Hoşgeldiniz
    Oyun oldukça  basitir, Bilgisayar 
    hafizasinda bir rastgele sayi tutuyor
    ve bilgisayarin rastgele tutuğu sayiyi
    tahmin etmeye çalişacaksiniz.
    Oyun iki sevyeden olüşmaktadir,Kolay Ve orta sevye.
    kolayi sevyeyi oynamak için '1'
    Orta sevyeyi oymak için '2' tiklayiniz
    Dilerseniz Oynamaya Başlayalim 
 """)
sevye = int(input("Oynamak İstediniz Sevye Giriniz:"))
while sevye <= 0 and sevye >= 3:
    print ("Yanliş Sevye Girişi Yatiniz")
    tahmim = int(input("Sayi Tahmininizi Tekrar Giriniz: (1 ile 10 arasinda)"))

if sevye == 1:
    print ("""
              Tahmin Oyunun Kolay Seviyesine Hoşgeldiniz
              Bu Seviyede Doğru tahmin Yapana kadar Oyanayabilirsiniz.
     """)
    tahmim = int(input("Sayi Tahmininizi Giriniz: (1 ile 10 arasinda)"))
    kolay_sevye(tahmim)
elif sevye == 2:
     print ("""
              Tahmin Oyunun Orta Seviyesine Hoşgeldiniz
              Bu Seviyede Beştane Tahmin Hakkiniz Var 
              Beş Tane Tahmim Hakkiniz Biterse Oyunu Kaybemiş Oluyorsunuz.
     """)
     tahmim = int(input("Sayi Tahmininizi Giriniz: (1 ile 10 arasinda)"))
     orta_sevye(tahmim)


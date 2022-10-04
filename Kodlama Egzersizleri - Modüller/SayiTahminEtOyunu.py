import time, random


def geri_sayim():
    for i in range(3, 0, -1):
        time.sleep(1)

        print(i)


def exit():
    for i in range(3, 0, -1):
        print("Program Sonlandırılıyor.")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print("..")
        time.sleep(0.5)
        print("...")
        break


def oyun_baslat():
    print("Oyun Başlatılıyor.")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    game_start()


def game_start(oyun_hakki=5):
    print("""Sayı Tahmin Oyunu Başlıyor""")
    print("""!!5 Tahmin Hakkının Olduğunu Unutma!!""")

    geri_sayim()

    dogru_deger = random.randint(0, 10)

    while (oyun_hakki > 0):
        tahmin = int(input("Aklımdan 0 ile 50 Arasında Bir Sayı Tuttum. Bil Bakalım Kaç?:"))

        if (tahmin > dogru_deger):
            print("Daha Küçük Bir Tahminde Bul  un!")
            oyun_hakki -= 1
        elif (tahmin < dogru_deger):
            print("Daha Büyük Bir Tahminde Bulun!")
            oyun_hakki -= 1
        else:
            print("Tebrikler Sayıyı Doğru Bildiniz")
            print("Doğru Sayı:", dogru_deger)
            break

    if (oyun_hakki == 0):
        print("Ne Yazık ki Tahmin Hakkın Bitti!")
        print("Doğru Sonuç", dogru_deger, "idi.")

    tuslama = input("Oyuna Devam Etmek İster Misin?Y/N:")

    if (tuslama == "N"):
        exit()
    else:
        oyun_baslat()


game_start()
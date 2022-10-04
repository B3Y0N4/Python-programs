import random, time



def geri_sayim():
    for i in range(3, 0,-1):
        time.sleep(1)
        print(i)

def exit():
    print("Program Sonlandırılıyor...")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)


def oyunu_baslat():
    print("Oyun Başlatılıyor.")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    start_game()


def start_game(tahmin_hakki = 5):


    print("**Sayı Tahmin Oyunu Başlamak Üzere**")
    print("!!5 Tahmin Hakkın Olduğunu Unutma!!")

    geri_sayim()

    dogru_deger = random.randint(0,5)

    while(tahmin_hakki>0):
        tahmin = int(input("Aklımdan 0 ile 50 Arasında Bir Sayı Tuttum. Bil Bakalım Kaç?:"))

        if(tahmin>dogru_deger):
            print("Tahminini Küçültmelisin!")
            tahmin_hakki -=1
        elif(tahmin<dogru_deger):
            print("Tahminini Büyüt!")
            tahmin_hakki -= 1
        else:
            print("Tebrikler! Doğru Tahmin")
            print("Aklımdan Tuttuğum Sayı", dogru_deger, "idi.")
            break

    if(tahmin_hakki==0):
        print("Son Tahmin Hakkını da Kullandın ve Ne Yazık ki Bilemedin!")
        print("Doğru Sayı", dogru_deger, "idi.")



    tuslama = input("Tekrar Oynamak İster Misin?Y/N:")

    if(tuslama=="Y"):
        oyunu_baslat()
    else:
        exit()



start_game()


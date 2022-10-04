def not_hesaplama(satir):
    satir = satir[:-1]
    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    sonuc =  (not1 * (3/10)) + (not2 * (3/10)) + (not3 * (4/10))

    if(sonuc >= 90):
        harf = "AA"
    elif(sonuc >= 85):
        harf = "BA"
    elif (sonuc >= 80):
        harf = "BB"
    elif (sonuc >= 75):
        harf = "CB"
    elif (sonuc >= 70):
        harf = "CC"
    elif (sonuc >= 65):
        harf = "DC"
    elif (sonuc >= 60):
        harf = "DD"
    elif (sonuc >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------------------>" + harf + "\n"


with open("../Exceptions ve Dosya İşlemleri/notlar.txt", "r+", encoding="utf-8") as file:
    for i in file:

        eklenecekler = []

        for i in file:
            eklenecekler.append(not_hesaplama(i))
        with open("../Exceptions ve Dosya İşlemleri/harf_notlar.txt", "a", encoding="utf-8") as file2:
            file2.writelines(eklenecekler)
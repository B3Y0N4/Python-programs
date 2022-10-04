kullanici_ates = int(input("Lütfen ateşinizi girin: "))

if(kullanici_ates > 38):
    print("Ateşiniz {} derece. AVM'ye Giremezsiniz!".format(kullanici_ates))
else:
    print("Ateşiniz {} derece. AVM'ye Girebilirsiniz.".format(kullanici_ates))
vize1 = int(input("Lütfen 1. Vize Notunuzu Girin: "))
vize2 = int(input("Lütfen 2. Vize Notunuzu Girin: "))
final = int(input("Lütfen final Notunuzu Girin: "))


sonuc_not = (vize1/100*30) + (vize2/100*30) + (final/100*40)

if(sonuc_not >= 90):
    print("Notunuz {} AA".format(sonuc_not))
elif(sonuc_not >= 85):
    print("Notunuz {} BA".format(sonuc_not))
elif(sonuc_not >= 80):
    print("Notunuz {} BB".format(sonuc_not))
elif(sonuc_not >= 75):
    print("Notunuz {} CB".format(sonuc_not))
elif(sonuc_not >= 70):
    print("Notunuz {} CC".format(sonuc_not))
elif(sonuc_not >= 65):
    print("Notunuz {} DC".format(sonuc_not))
elif(sonuc_not >= 60):
    print("Notunuz {} DD".format(sonuc_not))
elif(sonuc_not >= 50):
    print("Notunuz {} FD".format(sonuc_not))
else:
    print("Notunuz {} FF".format(sonuc_not))

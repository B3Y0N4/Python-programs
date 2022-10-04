#Koşullu Durumlar

#kullanici = int(input("Lütfen yaşınızı girin: "))

#if(kullanici >= 18):
#    print("Reşitsiniz")
#else:
#    print("Reşit değilsiniz!")


"""print("Lütfen toplama yapmak için '+', çıkarma yapmak içinse '-' işaretlerini girip entre'a basın.")

islem = input("Lütfen yapmak istediğiniz işlemi girin: ")

if(islem == "+"):
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a+b)
else:
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a-b)"""





















print("Lütfen aşağıdaki işlemlerden birisini seçerek entre'a basın.")
print("""Toplama = +
Çıkarma = -
Çarpma = *
Bölme = /""")

islem = input("Lütfen seçtiğiniz işlemi girin: ")

if(islem == "+"):
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a+b)
elif(islem == "-"):
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a - b)
elif(islem == "*"):
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a * b)
elif(islem == "/"):
    a = int(input("Lütfen ilk sayıyı girin: "))
    b = int(input("Lütfen ikinci sayıyı girin: "))
    print(a / b)
else:
    print("Geçersiz İşlem")










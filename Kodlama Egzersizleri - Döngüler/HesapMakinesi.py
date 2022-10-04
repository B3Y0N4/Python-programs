kontrol = 0

while(kontrol==0):



    print("Lütfen aşağıdaki işlemlerden birisini seçerek entre'a basın.")
    print("""Toplama = +
    Çıkarma = -
    Çarpma = *
    Bölme = /
    Çıkmak için 'q'""")


    islem = input("Lütfen seçtiğiniz işlemi girin: ")

    if(islem=="q"):
        print("Programdan çıkılıyor...")
        kontrol = 1
    elif(islem == "+"):
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

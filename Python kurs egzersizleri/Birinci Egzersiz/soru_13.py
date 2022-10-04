# eval() fonksiyonunu kullanarak bir hesap makinesi yapın.
hesaplama = input("""
Hesap Makinesi

İşleçler

Toplama =+
Çıkarma = -
Çarpma = *
Bölme =/

Yapmak istediğiniz işlemi şu şekilde girin: 43*12

işlem:
""")

print ("Sonuç: ", eval(hesaplama))
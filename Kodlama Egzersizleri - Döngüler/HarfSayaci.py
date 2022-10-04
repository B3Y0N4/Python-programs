metin = """Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır 
metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat 
numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 
1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. 
Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden 
elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren 
Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi 
Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur."""

harf = input("Lütfen Sayısını İstediğiniz Harfi Giriniz:")

harf_sayisi = 0
for i in metin:
    if (i == harf):
        harf_sayisi += 1

print(harf, "harfi metinde şu kadar sayıda geçmektedir:", harf_sayisi)


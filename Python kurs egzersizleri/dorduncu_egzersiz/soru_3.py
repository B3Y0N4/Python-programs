# Bir Metnin İçinde Geçen Harflerin Kaçar Adet Geçtiğini Tespit Etme
# Kullanıcıya uzun bir metin gösterin daha sonra kullanıcıdan hangi harften kaç tane geçtiğini öğrenmek istediğini sorun.
#  Daha sonra kullanıcının talep ettiği harfin metinde kaç defa geçtiğini tespit edin.

metin = """Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir
         matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri 
        endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı 
        zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının
        yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler
        olmuştur."""
harf = input("Bir harf giriniz: ")
sayac = 0
for i in metin:
    if i == harf:
        sayac += 1

print (f"{harf} harfi {sayac} defa metin de var")

    
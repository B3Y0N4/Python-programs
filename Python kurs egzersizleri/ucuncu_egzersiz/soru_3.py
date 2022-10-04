# Bir not hesaplayıcı programı yazın. Burada kullanıcıdan ilk ve ikinci vize notlarını ve final notunu girmesini talep edin. 
# Daha sonra kullanıcıya AA, BA, BB vb. gibi notunun harf karşılığını hesaplayıp yazdırın. 
#Vize 1: %30
#Vize 2: %30
#Final: %40

#Harf Notu Karşılıkları
#AA	90-100	
#BA	85-89	
#BB	80-84	
#CB	75-79	
#CC	70-74	
#DC	65-69	
#DD	60-64	
#FD	50-59	
#FF	0-49
vize1 = int(input("Birinci Vize Notunuzu Girin: "))
vize2 = int(input("İkinci Vize Notunuzu Girin: "))
final = int(input("Final Notunuzu Girin: "))
ort = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
if ort >= 90 and ort <= 100:
    print (f"Ortalamaniz {ort} Ve harf notounuz AA'dir") 
elif ort >= 85 and ort <= 89:
    print (f"Ortalamaniz {ort} Ve harf notounuz BA'dir") 
elif ort >= 80 and ort <= 84:
    print (f"Ortalamaniz {ort} Ve harf notounuz BB'dir") 
elif ort >= 75 and ort <= 79:
    print (f"Ortalamaniz {ort} Ve harf notounuz CB'dir") 
elif ort >= 70 and ort <= 74:
    print (f"Ortalamaniz {ort} Ve harf notounuz CC'dir") 
elif ort >= 65 and ort <= 69:
    print (f"Ortalamaniz {ort} Ve harf notounuz DC'dir") 
elif ort >= 60 and ort <= 64:
    print (f"Ortalamaniz {ort} Ve harf notounuz DD'dir") 
elif ort >= 50 and ort <= 59:
    print (f"Ortalamaniz {ort} Ve harf notounuz FD'dir")
elif ort >= 0 and ort <= 49:
    print (f"Ortalamaniz {ort} Ve harf notounuz FF'dir")
    
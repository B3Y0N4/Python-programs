import folium
import pandas as pd

veri = pd.read_excel("world_coronavirus_cases.xlsx")

enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
toplam_vakalar = list(veri["Toplam Vaka"])
vefatlar = list(veri["Vefat Edenler"])
aktif_vakalar = list(veri["Aktif Vakalar"])
nufus = list(veri["Nüfus"])
test_sayisi = list(veri["Toplam Test"])



toplam_vaka_haritasi = folium.FeatureGroup(name="ToplamVakaHaritası")
olum_orani_haritasi = folium.FeatureGroup(name="ÖlümOranıHaritası")
aktif_vaka_haritasi = folium.FeatureGroup(name="AktifVakaHaritası")
test_orani_haritasi = folium.FeatureGroup(name="TestOranıHaritası")
nufus_dagilim_haritasi = folium.FeatureGroup(name="NüfusDağılımHaritası")




def toplam_vaka_renk(vaka):
    if vaka < 100000:
        return "green"
    elif vaka < 300000:
        return "white"
    elif vaka < 750000:
        return "orange"
    else:
        return "red"

def toplam_vaka_yari_cap(vaka):
    if vaka < 100000:
        return 50000
    elif vaka < 300000:
        return 100000
    elif vaka < 750000:
        return 200000
    else:
        return 400000

def olum_orani_renk(vaka,vefat):
    if (vefat/vaka)*100 < 2.5:
        return "green"
    elif (vefat/vaka)*100 < 5:
        return "white"
    elif (vefat/vaka)*100 < 7.5:
        return "orange"
    else:
        return "red"

def olum_orani_yari_cap(vefat,vaka):
    if (vefat / vaka) * 100 < 2.5:
        return 25000
    elif (vefat / vaka) * 100 < 5:
        return 50000
    elif (vefat / vaka) * 100 < 7.5:
        return 100000
    else:
        return 200000


def aktif_vaka_renk(aktif):
    if aktif < 100000:
        return "green"
    elif aktif < 300000:
        return "white"
    elif aktif < 750000:
        return "orange"
    else:
        return "red"

def aktif_vaka_yari_cap(aktif):
    if aktif < 100000:
        return 50000
    elif aktif < 300000:
        return 100000
    elif aktif < 750000:
        return 200000
    else:
        return 400000

def test_orani_yari_cap(nufus, test):
    if (test / nufus) * 100 < 2.5:
        return 200000
    elif (test / nufus) * 100 < 5:
        return 100000
    elif (test / nufus) * 100 < 7.5:
        return 50000
    else:
        return 25000

def test_orani_renk(nufus, test):
    if (test / nufus) *100 < 2.5:
        return "red"
    elif (test / nufus) *100 < 5:
        return "orange"
    elif (test / nufus) *100 < 7.5:
        return "white"
    else:
        return "green"

world_map = folium.Map(tiles="Cartodb dark_matter")

for enlem, boylam, vakalar in zip(enlemler,boylamlar,toplam_vakalar):
    toplam_vaka_haritasi.add_child(folium.Circle(location=(enlem, boylam),
                                                 radius=toplam_vaka_yari_cap(vakalar),
                                                 color=toplam_vaka_renk(vakalar),
                                                 fill=toplam_vaka_renk(vakalar),
                                                 fill_opacity=0.5))

for enlem, boylam, vakalar, vefat in zip(enlemler,boylamlar,toplam_vakalar, vefatlar):
    olum_orani_haritasi.add_child(folium.Circle(location=(enlem, boylam),
                                                radius=olum_orani_yari_cap(vakalar, vefat),
                                                color=olum_orani_renk(vakalar, vefat),
                                                fill=olum_orani_renk(vakalar, vefat),
                                                fill_opacity=0.5))

for enlem, boylam, aktif_vaka in zip(enlemler,boylamlar,aktif_vakalar):
    aktif_vaka_haritasi.add_child(folium.Circle(location=(enlem, boylam),
                                                radius=aktif_vaka_yari_cap(aktif_vaka),
                                                color=aktif_vaka_renk(aktif_vaka),
                                                fill=aktif_vaka_renk(aktif_vaka),
                                                fill_opacity=0.5))

for enlem, boylam, ulke_nufusu, test in zip(enlemler,boylamlar, nufus, test_sayisi):
    test_orani_haritasi.add_child(folium.Circle(location=(enlem, boylam),
                                                radius=test_orani_yari_cap(ulke_nufusu, test),
                                                color=test_orani_renk(ulke_nufusu, test),
                                                fill=test_orani_renk(ulke_nufusu, test),
                                                fill_opacity=0.5))



nufus_dagilim_haritasi.add_child(folium.GeoJson(
                            data=(open("world.json", "r", encoding="utf-8-sig").read()),
                            style_function= lambda x : {'fillColor':'green'
                            if x["properties"]["POP2005"] < 20000000 else 'white'
                            if 20000000 <= x["properties"]["POP2005"]  <= 50000000 else 'orange'
                            if 50000000 <= x["properties"]["POP2005"] <= 100000000 else 'red'}))


world_map.add_child(toplam_vaka_haritasi)
world_map.add_child(olum_orani_haritasi)
world_map.add_child(nufus_dagilim_haritasi)
world_map.add_child(aktif_vaka_haritasi)
world_map.add_child(test_orani_haritasi)

world_map.add_child(folium.LayerControl())


world_map.save("koronavirüs_dünya_haritası.html")


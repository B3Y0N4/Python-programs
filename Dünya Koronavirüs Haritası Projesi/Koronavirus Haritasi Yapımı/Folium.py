import folium
import pandas as pd
import xlrd


map = folium.Map(location=[41,29],tiles="CartoDB positron")

veri = pd.read_excel("tr-cities.xlsx")


ilceler = list(veri["ilce"])
enlemler = list(veri["Enlem"])
boylamlar = list(veri["Boylam"])
import pandas as pd

# 1. Basit bir Series oluştur ve temel işlemler yap
seri = pd.Series([1, 2, 1, 'a', 'a', 6])
print("Oluşturulan Seies:\n", seri)
print(f"Serinin basi: {seri.head(1)}\nSerinin sonu: {seri.tail(1)}")

print("index deneme:", pd.Series([1, 2, 3], index=['x', 'y', 'z'])) # Etiket oluşturur
print("value deneme:", seri.values) # [1 2 1 'a' 'a' 6]
print("Value count:", seri.value_counts()) # elemanları sayıyor. 1-->2, a-->2, 2-->1 gibi

# 2. Dataframe oluştur, Satır/sütun isimleri ver, erişim pratiği yap 
# Python Sözlük(dictinory)
dict = {
    "books": ['aa', 'bb', 'cc', 'dd', 'ee', 'ff'],
    "cost": [12, 23, 34, 56, 67, 78]
} 

df = pd.DataFrame(dict)
print("Dataframe:\n", df)
print("1. satırı getirme:\n", df.loc[0]) # etiketi 0 olan satırı getirir
print("1. satırı getirme:\n", df.iloc[0]) # konumu 0 olan satırı getirir
print("1 den 3 e kadar yazma\n", df.loc[0:2])
print("aa kitabının fiyatı: ", df.iloc[0, 1])
print("ff kitabının fiyatı: ", df.loc[5, 'cost'])

# 3. Bir .csv dosyası oku ve analiz et
df2 = pd.read_csv('weather.csv', header=None).astype(int)
print("Weather dosyası:\n", df2.head(3)) # ilk 3'ü yazdırılır
print("Weather dosyas bilgisi:\n", df2.info())

print("Günlerin sıcaklık ortalamaları:\n", df2.mean(axis=1)) # axis 1 olunca satırlar, boş yanı 0 a eşit ise sütunlar kullanılır
print("30 derece üstü sıcaklıklar:", df2[df2 > 30]) # 30 derece ve üstü yazdırılır altta kalan değerler boş döner.

# Eksik veri kontrolü
print("Eksik veri var mi\n", df2.isnull().sum())
df3 = df2[df2 > 30]
print("Eksik veri var mi\n", df3.isnull().sum())

# Yeni sütun ekleme
df2.index = ['Pazartesi', 'Sali', 'Carsamba', 'Persembe', 'Cuma', 'Cumartesi', 'Pazar']
df2["Ort Sıcaklık"] = df2.mean(axis=1)
df2["Durum"] = ["Sicak" if ort > 26.25 else "Ilıman" for ort in df2["Ort Sıcaklık"]]
print(df2.head(7))
print("sıralı sıcaklık\n", df2["Ort Sıcaklık"].sort_values()) # Sıcaklık ortalmalarına göre sıralama
print("Sicak Günler Filtrelenmiş: \n", df2[df2["Durum"].isin(['Sicak'])]) # df[df["Stun ismi"].isin(["filtrelenecek içerik"])]

# 4. Fltreleme Yöntemleri
# Birden fazla koşulla seçim yapma.
print("Saat 8 de 25 dereceden yüksek ve Ilıman günler:\n", df2[(df2[8] > 25) & (df2["Durum"] == "Ilıman")])

# Belirli sütunları şeçip filtreleme
print("12 ye kadar olan saatlerdeki sıcaklıklar\n", df2.loc[: , 0:12])
print("Ort sıcaklığı 26.3 den büyük olan günerin ort sıcaklık ve durum bilgisi:\n", df2.loc[df2["Ort Sıcaklık"] < 26.3, ["Ort Sıcaklık", "Durum"]])

# query sütun isimleri ile sayı uyuşmazlığı yaşadığı için hata veriyordu bu yüzden stun isimlerini güncellendi
df2.columns = [f's{i}' for i in range(24)] + ['Ort Sıcaklık', 'Durum']
print("8. saat 12. saatten daha sıcak olduğu ve durumu sıcak olan günler:\n", df2.query("s8 > s12 and Durum == 'Sicak'"))

# Gruplama
print("Durumunların ortalamaları:\n", df2.groupby('Durum').mean()) # df2.groupby('Durum')["Ort Sıcaklık"].mean():  Durum -Ilıman    25.958333 -Sicak     26.406250

# Grup içi işlemler
print("Drumların standart sapma max ve minleri\n", df2.groupby('Durum')['s5'].agg(['min', 'max', 'mean', 'std', 'sum', 'size']))
print(df2.groupby('Durum').agg({'s3': ['min', 'max'], 'Ort Sıcaklık': ['mean']}))
print(df2.groupby("Durum")['s3'].agg(lambda x: min(x) + 2)) # 3. saatteki min değere 2 eklenmiş hali
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
df2 = pd.read_csv('weather.csv', header=None)
print("Weather dosyası:\n", df2.head(3))
print("Weather dosyas bilgisi:\n", df2.info())

print("Günlerin sıcaklık ortalamaları:\n", df2.mean(axis=1))

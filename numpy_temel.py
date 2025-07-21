import numpy as np

# 1. NumPy Array oluşturma
a = np.array([1, 2, 3])
print("Array:", a) # [1 2 3] konsola yazdırılır.

# 2. Sıfırlardan oluşan matris
zeros = np.zeros((2, 3))
print("Zeros:\n", zeros) # [[0. 0. 0.] \n [0. 0. 0.]] çıktısını verir.

# 3. 1 lerden oluşan matris
ones = np.ones((2, 2))
print("Ones:\n", ones) # [[1. 1.] \n [1. 1.]]

# 4. Aralıkla array oluşturma
aralik = np.arange(0, 10, 2)
print("Arange:", aralik) #[0,10) 0 ile 10 arası 10 dahil değil ikişerli artış ile giden array oluşur.

# 5. Rastgele sayılarla array oluşturma
random_arr = np.random.rand(2, 3)
print("Random Array:\n", random_arr) # 2 ye 3 lük rastgele matris üretir

# 6. Şekil değiştirme
b = np.arange(12).reshape(3, 4)
print("Reshaped:\n", b) # 12 ye kadar olan sayılarla belirtilen şekilde array oluşturma
"""
 [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 
 """
# 7. Temel istatistiksel işlemler
print("Toplam:", b.sum()) #65
print("Ortalama:", b.mean()) # 5.5
print("Standart SApma:", b.std()) # 3.452...

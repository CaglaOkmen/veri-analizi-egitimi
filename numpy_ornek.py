import numpy as np

# 1. 4x4’lük sadece 7 rakamı ile dolu bir array oluştur
sevens = 7 * np.ones((4, 4))
print("Sevens:\n", sevens)

# 2. 0 ile 1 arasında rastgele değerlerden oluşan 5x5 matris üret
random_arr = np.random.rand(5, 5)
print("Rondom Array (0,1) 5x5\n", random_arr)

# 3. np.linspace(0, 1, 10) fonksiyonunu dene
fonk = np.linspace(0, 1, 10)
print("fonksiyon deneme:\n", fonk) # belli bir aralık verilip belli bir miktarda(n) orantılı artan 1xn lik dizi üretir.

# 4. Şekli (2, 6) olan bir array oluştur, sonra onu (3, 4)'e yeniden şekillendir
arr2 = np.array([[1, 2, 3, 4, 5, 6],[6, 5, 4, 3, 2, 1]])
print("2x6 lık array:\n", arr2)
reshap_arr = arr2.reshape(3, 4)
print("3x4 lık yeni array:\n", reshap_arr)

###-------------------------------------------------------------###
# Bir şehirde 7 gün boyunca her saat sıcaklık ölçülmüş. Yani 7x24’lük bir matris. Bu veriyi analiz et.
weather_arr = 15 + (40 - 15) * np.random.rand(7, 24)# 15 ile 40 arası değerlerde hava sıcaklığı verilecek

for x in range(0, 7):
    print(f"{x + 1}. Gün Sıcaklıkları:", weather_arr[x].astype(int))
    print(f"{x + 1}. Gün Ortalama Sıcaklıkları:", weather_arr[x].astype(int).mean())

print("Haftanın en sıcak derecesi: ", weather_arr.max().astype(int))
print("Haftanın en soğuk derecesi: ", weather_arr.min().astype(int))
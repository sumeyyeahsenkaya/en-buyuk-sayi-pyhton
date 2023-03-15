#Bir dizi içindeki en büyük sayıyı en hızlı bulmak için en iyi algoritma lineer aramadır ve en hızlı şekilde en büyük sayıyı bulmamızı sağlar.
#Python ile
import random
import time

def max_element(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num

arr = [random.randint(1, 100000) for i in range(10000)]

start_time = time.time()
max_num = max_element(arr)
end_time = time.time()

print("En büyük sayı: ", max_num)
print("Süre: ", end_time - start_time, " saniye")

#En büyük sayı yaklaşık 0.000999 saniyede bulunur.

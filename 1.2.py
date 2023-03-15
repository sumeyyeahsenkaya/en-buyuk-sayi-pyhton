#BruteForce, her elemanı diğer elemanlarla karşılaştırdığından, O(n^2) zaman karmaşıklığına sahiptir ve büyük veri setleri için yavaş çalışabilir.
#Python ile
import random
import time

def max_element_bruteforce(arr):
    max_num = arr[0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] > arr[j]:
                max_num = arr[i]
    return max_num

arr = [random.randint(1, 100000) for i in range(10000)]

start_time = time.time()
max_num = max_element_bruteforce(arr)
end_time = time.time()

print("En büyük sayı: ", max_num)
print("Süre: ", end_time - start_time, " saniye")

#En büyük sayı yaklaşık 9.908 saniyede bulunur.

#BruteForce algoritması lineer zamanlı algoritmadan çok daha yavaş çalışır ve büyük veri setleri için uygun değildir.  

# Penyelesaian persoalan Partisi Bilangan bulat dengan relasi rekurens standar
import time
import sys

def part(a,b):
  if (a < 0 or b < 1):
    return 0
  elif (a < 2 or b == 1):
    return 1
  else:
    return (part(a-b,b) + part(a,b-1))
def integerPartition(n): return part(n,n)

sys.setrecursionlimit(3200)
start = time.time()
print(integerPartition(70))
end = time.time()
print(str((end - start)*1000) + " ms") # Waktu eksekusi

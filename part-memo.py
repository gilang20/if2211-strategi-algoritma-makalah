import time
import sys

# Fungsi untuk memoize
def memoize(fn):
  memo = {}
  def iterMemo(a,b):
    if ((a,b) not in memo):
      memo[a,b] = fn(a,b)
    return memo[a,b]
  return iterMemo
  
@memoize
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
print(integerPartition(400))
end = time.time()
print(str((end - start)*1000) + " ms") # Waktu eksekusi

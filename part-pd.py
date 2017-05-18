# Penyelesaian persoalan Partisi Bilangan bulat dengan pemrograman dinamis
import time

def integerPartition(n):
	tabel = [[0 for x in range(n)] for y in range(n+1)]
	for i in range(n+1):
		for j in range(n):
			if (i < 2 or j < 1):
				tabel[i][j] = 1
			else:
				tamp = 0
				brs = i-1
				kol = 0
				while (brs >= 0 and kol <= j):
					tamp += tabel[brs][kol]
					brs -= 1
					kol += 1
				tabel[i][j] = tamp
	return tabel[n][n-1]

start = time.time()
print(integerPartition(400))
end = time.time()
print((end - start)*1000)

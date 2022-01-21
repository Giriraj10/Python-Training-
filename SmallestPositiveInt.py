def seperate(arr, size):
	j = 0
	for i in range(size):
		if (arr[i] <= 0):
			arr[i], arr[j] = arr[j], arr[i]
			j += 1 
	return j

def findMissingPositive(arr, size):
	for i in range(size):
		if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
			arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
			
	for i in range(size):
		if (arr[i] > 0):
			
			return i + 1
	return size + 1

def findMissing(arr, size):
	shift = seperate(arr, size)
	return findMissingPositive(arr[shift:], size - shift)
	
N = int(input())
arr = list(map(int,input().split(' ')[:N]))
missing = findMissing(arr, N)
print(missing)



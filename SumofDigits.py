def reverse(n):
	rev = 0
	while (n != 0):
		rev = (rev * 10) + (n % 10)
		n //= 10
	return rev
def Sum(n):
	n = reverse(n)
	Odd = 0
	Even = 0
	c = 1

	while (n != 0):
		if (c % 2 == 0):
			Even += n % 10
		else:
			Odd += n % 10
		n //= 10
		c += 1

	print( Odd , Even)
	
n = int(input())
Sum(n)




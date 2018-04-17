a = input("A = ")
b = input("B = ")

def swap(a,b):
	a, b = b, a
	return (a,b)

a, b = swap(a,b)
print "A = ",a , "\nB = ", b
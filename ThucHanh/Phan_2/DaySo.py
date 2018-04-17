n = input("Nhap N = ")

print "Day so tu 1 den ", n, "la:"
for i in range(1,n+1):
		print i

sum = 0

for i in range(0,n+1):
	if i%2==0:
		sum+=i
print "Tong = ", sum
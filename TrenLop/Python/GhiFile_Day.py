N = input("Nhap N: ")
a=[]
for i in range(N):
	a.append(input("a[%d]= " %i))
print "Cac phan tu chan: "
for i in a:
	if(i % 2 == 0):
		print i
a.sort()
print "Day sau khi sap xep: "
for i in a:
	print i

fileData = open('Day.txt','w+')
fileData.write(str(N))
fileData.write("\n")
for i in a:
	fileData.write(str(i))
	fileData.write("\n")
fileData.close()
from HinhChuNhat import HinhChuNhat
N = input("Nhap N: ")
HCN = []
for i in range(N):
	Ten = str(input("Ten: "))
	Dai = input("Dai: ")
	Rong = input("Rong: ")
	H = HinhChuNhat(Ten, Dai, Rong)
	HCN.append(H)

for i in HCN:
	i.toString()
	print "Chu vi: %d" % i.getCV()
	print "Dien tich: %d" %i .getDT()
m = 0
for i in HCN:
	if(i.getDT() > m):
		m = i.getDT()
		t = i.getTen()
print "Hinh %s co dien tich lon nhat: %d" %(t,m)
file = open("GhiHCN.txt","w+")
for i in HCN:
	file.write("Ten: %s\tDai: %d\tRong: %d\tChu vi: %d\tDien tich: %d\t" %(i.getTen(),i.getDai(),i.getRong(),i.getCV(),i.getDT()))
	file.write("\n")
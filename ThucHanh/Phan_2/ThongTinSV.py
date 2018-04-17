class SinhVien:
	Mssv = ""
	HoTen = ""
	Khoa = ""
	def __init__(self, Mssv, HoTen, Khoa):
		self.Mssv = Mssv
		self.HoTen  = HoTen
		self.Khoa = Khoa
	def XuatDs(self):
		print self.Mssv, " -- ", self.HoTen, " -- ", self.Khoa


class Khoa:
	MaKhoa = ""
	TenKhoa = ""
	def __init__(self, MaKhoa, TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa

	def XuatDs(self):
		print self.MaKhoa, " -- ", self.TenKhoa

DsKhoa = []
DsKhoa.append(Khoa("56", "Khoa 56 CNTT"))
DsKhoa.append(Khoa("57", "Khoa 57 CNTT"))
DsKhoa.append(Khoa("58", "Khoa 58 CNTT"))
DsKhoa.append(Khoa("59", "Khoa 59 CNTT"))
print "---DANH SACH KHOA---"
for i in DsKhoa:
	i.XuatDs()

n = input("Nhap So SV: ")
DsSv = []
for i in range(1,n+1):
	Mssv = input("\nMSSV: ")
	HoTen = input("Ho Ten: ")
	Khoa = input("Khoa: ")
	DsSv.append(SinhVien(Mssv,HoTen,Khoa))

print "---DANH SACH SV VUA NHAP---"
for i in DsSv:
	i.XuatDs()

print "\n---DANH SACH SV KHOA K57---\n"
#ds sv khoa k57
for i in DsSv:
	if (int(i.Khoa) == 57):
		i.XuatDs()
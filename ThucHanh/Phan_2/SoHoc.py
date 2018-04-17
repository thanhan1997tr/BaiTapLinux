a = input("A = ")
b = input("B = ")

print "--CAC PHEP TOAN SO HOC TRONG PYTHON--"
print "Tong ", a,  " + ", b, " = ", a+b
print "Hieu ", a,  " - ", b, " = ", a-b
print "Tich ", a,  " * ", b, " = ", a*b
if b != 0:
	print "Thuong ", a,  " / ", b, " = ", float(a)/b
else:
	print "B phai khac 0"

print "Phep chia lay du ",a, "%",b, " = ", a%b
print "Luy thua ",a , "^", b, " = ", a**b
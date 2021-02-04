#
#	Sıfırı Taşı
#	@memrearal
#	03.02.2021
#
dizi = [0,2,5,1,4,6,8,1,7,9,1,0,5,7,9]
xSayisi = 0
for x in dizi:
	if x == 0:
		xSayisi = xSayisi + 1
index = 0
yeniDizi = []
for y in range(xSayisi):
    yeniDizi.append(0)
for v in dizi:
    index = index+1
    if v != 0:
        yeniDizi.append(v)
print(yeniDizi)
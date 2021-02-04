#
#	Mail Adresi Doğrulama
#	@memrearal
#	03.02.2021
#
import re
def kontrol(mailAdresi, uzantiUzunlugu):
	try:
		index = mailAdresi.index("@")
		kullaniciadi = mailAdresi[0:index]
		s = "";
		for i in range(index+1, len(mailAdresi)):
			s += mailAdresi[i]
		x = s.split('.')
		if len(x) != 3:
			return False
		elif len(x[1]) != uzantiUzunlugu:
			return False
		else:
			if not re.match("^[A-Za-z0-9_-]*$", kullaniciadi):
				return False
			return True
	except ValueError:
		return False

print("Uzantı uzunluğunu giriniz:")
uzantiUzunlugu = int(input())
print("Mail adresinizi giriniz:")
mailAdresi = input()
if kontrol(mailAdresi, uzantiUzunlugu) == False:
	print("Mail adresiniz yanlıştır.")
else:
	print("Mail adresiniz doğrudur.")
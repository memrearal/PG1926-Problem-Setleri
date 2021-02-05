#
#   Okul Problemi
#   @memrearal
#
class Okul1():
    def __init__(self,kurumIsmi,sehir):
        self.kurumIsmi=kurumIsmi
        self.sehir=sehir
        self.akademisyen=[{"AdSoyad":"Emre A","Unvan":"Prof.Dr.","Alan":"Bilgisayar Mühendisliği"}]
        self.bolum=[{"BolumAdi":"Bilgisayar Mühendisliği"},{"BolumAdi":"Yazılım Mühendisliği"},{"BolumAdi":"Bilgisayar Bilimleri"}]
        self.sinif=[{"SinifNo":1,"BolumNo":0},{"SinifNo":2,"BolumNo":0},{"SinifNo":3,"BolumNo":0},{"SinifNo":4,"BolumNo":0},{"SinifNo":1,"BolumNo":1},{"SinifNo":2,"BolumNo":1},{"SinifNo":3,"BolumNo":1},{"SinifNo":4,"BolumNo":1},{"SinifNo":1,"BolumNo":2},{"SinifNo":2,"BolumNo":2},{"SinifNo":3,"BolumNo":2},{"SinifNo":4,"BolumNo":2}]
        self.ogrenci=[{"sinifNo":0,"AdSoyad":"Emre A1"},{"sinifNo":1,"AdSoyad":"Emre A2"},{"sinifNo":2,"AdSoyad":"Emre A3"},{"sinifNo":3,"AdSoyad":"Emre A4"},{"sinifNo":4,"AdSoyad":"Emre A1"},{"sinifNo":5,"AdSoyad":"Emre A2"},{"sinifNo":6,"AdSoyad":"Emre A3"},{"sinifNo":7,"AdSoyad":"Emre A4"},{"sinifNo":8,"AdSoyad":"Emre A1"},{"sinifNo":9,"AdSoyad":"Emre A2"},{"sinifNo":10,"AdSoyad":"Emre A3"},{"sinifNo":11,"AdSoyad":"Emre A4"}]
    def bilgilerigoster(self):
        print("İsim : {}".format(self.kurumIsmi))
        print("Şehir: {}".format(self.sehir))
    def akademisyenleriListele(self):
        sayi = 1
        for a in self.akademisyen:
            print("{}. Akademisyen:\n\rİsim: {}\n\rÜnvanı: {}\n\rAlanı: {}\n\r".format(sayi, a["AdSoyad"],a["Unvan"],a["Alan"]))
            sayi = sayi+1
    def bolumleriListele(self):
        sayi = 1
        for a in self.bolum:
            print("{}. Bölüm Adı: {}".format(sayi, a["BolumAdi"]))
            sayi = sayi+1
    def siniflariListele(self):
        for a in self.sinif:
            print("{} Bölümü, {}.Sınıf".format(self.bolum[a["BolumNo"]]["BolumAdi"],a["SinifNo"]))
    def ogrencileriListele(self):
        sayi = 1
        for a in self.ogrenci:
            print("{}. Ad Soyad: {}, Bölümü: {}, Sınıfı: {}".format(sayi, a["AdSoyad"], self.bolum[self.sinif[a["sinifNo"]]["BolumNo"]]["BolumAdi"], self.sinif[a["sinifNo"]]["SinifNo"]))
            sayi = sayi+1

class Okul2():
    def __init__(self,kurumIsmi,sehir):
        self.kurumIsmi=kurumIsmi
        self.sehir=sehir
        self.akademisyen=[{"AdSoyad":"Emre A","Unvan":"Prof.Dr.","Alan":"Fizik"}]
        self.bolum=[{"BolumAdi":"Fizik Mühendisliği"},{"BolumAdi":"Fizik"},{"BolumAdi":"Kimya Mühendisliği"},{"BolumAdi":"Kimya"}]
        self.sinif=[{"SinifNo":1,"BolumNo":0},{"SinifNo":2,"BolumNo":0},{"SinifNo":3,"BolumNo":0},{"SinifNo":4,"BolumNo":0},{"SinifNo":1,"BolumNo":1},{"SinifNo":2,"BolumNo":1},{"SinifNo":3,"BolumNo":1},{"SinifNo":4,"BolumNo":1},{"SinifNo":1,"BolumNo":2},{"SinifNo":2,"BolumNo":2},{"SinifNo":3,"BolumNo":2},{"SinifNo":4,"BolumNo":2},{"SinifNo":1,"BolumNo":3},{"SinifNo":2,"BolumNo":3},{"SinifNo":3,"BolumNo":3},{"SinifNo":4,"BolumNo":3}]
        self.ogrenci=[{"sinifNo":0,"AdSoyad":"Emre A1"},{"sinifNo":1,"AdSoyad":"Emre A2"},{"sinifNo":2,"AdSoyad":"Emre A3"},{"sinifNo":3,"AdSoyad":"Emre A4"},{"sinifNo":4,"AdSoyad":"Emre A1"},{"sinifNo":5,"AdSoyad":"Emre A2"},{"sinifNo":6,"AdSoyad":"Emre A3"},{"sinifNo":7,"AdSoyad":"Emre A4"},{"sinifNo":8,"AdSoyad":"Emre A1"},{"sinifNo":9,"AdSoyad":"Emre A2"},{"sinifNo":10,"AdSoyad":"Emre A3"},{"sinifNo":11,"AdSoyad":"Emre A4"},{"sinifNo":12,"AdSoyad":"Emre A1"},{"sinifNo":13,"AdSoyad":"Emre A2"},{"sinifNo":14,"AdSoyad":"Emre A3"},{"sinifNo":15,"AdSoyad":"Emre A4"}]
    def bilgilerigoster(self):
        print("İsim : {}".format(self.kurumIsmi))
        print("Şehir: {}".format(self.sehir))
    def akademisyenleriListele(self):
        sayi = 1
        for a in self.akademisyen:
            print("{}. Akademisyen:\n\rİsim: {}\n\rÜnvanı: {}\n\rAlanı: {}\n\r".format(sayi, a["AdSoyad"],a["Unvan"],a["Alan"]))
            sayi = sayi+1
    def bolumleriListele(self):
        sayi = 1
        for a in self.bolum:
            print("{}. Bölüm Adı: {}".format(sayi, a["BolumAdi"]))
            sayi = sayi+1
    def siniflariListele(self):
        for a in self.sinif:
            print("{} Bölümü, {}.Sınıf".format(self.bolum[a["BolumNo"]]["BolumAdi"],a["SinifNo"]))
    def ogrencileriListele(self):
        sayi = 1
        for a in self.ogrenci:
            print("{}. Ad Soyad: {}, Bölümü: {}, Sınıfı: {}".format(sayi, a["AdSoyad"], self.bolum[self.sinif[a["sinifNo"]]["BolumNo"]]["BolumAdi"], self.sinif[a["sinifNo"]]["SinifNo"]))
            sayi = sayi+1

class Okul3():
    def __init__(self,kurumIsmi,sehir):
        self.kurumIsmi=kurumIsmi
        self.sehir=sehir
        self.akademisyen=[{"AdSoyad":"Emre A","Unvan":"Prof.Dr.","Alan":"Hukuk"}]
        self.bolum=[{"BolumAdi":"Hukuk"}]
        self.sinif=[{"SinifNo":1,"BolumNo":0},{"SinifNo":2,"BolumNo":0},{"SinifNo":3,"BolumNo":0},{"SinifNo":4,"BolumNo":0}]
        self.ogrenci=[{"sinifNo":0,"AdSoyad":"Emre A1"},{"sinifNo":1,"AdSoyad":"Emre A2"},{"sinifNo":2,"AdSoyad":"Emre A3"},{"sinifNo":3,"AdSoyad":"Emre A4"}]
    def bilgilerigoster(self):
        print("İsim : {}".format(self.kurumIsmi))
        print("Şehir: {}".format(self.sehir))
    def akademisyenleriListele(self):
        sayi = 1
        for a in self.akademisyen:
            print("{}. Akademisyen:\n\rİsim: {}\n\rÜnvanı: {}\n\rAlanı: {}\n\r".format(sayi, a["AdSoyad"],a["Unvan"],a["Alan"]))
            sayi = sayi+1
    def bolumleriListele(self):
        sayi = 1
        for a in self.bolum:
            print("{}. Bölüm Adı: {}".format(sayi, a["BolumAdi"]))
            sayi = sayi+1
    def siniflariListele(self):
        for a in self.sinif:
            print("{} Bölümü, {}.Sınıf".format(self.bolum[a["BolumNo"]]["BolumAdi"],a["SinifNo"]))
    def ogrencileriListele(self):
        sayi = 1
        for a in self.ogrenci:
            print("{}. Ad Soyad: {}, Bölümü: {}, Sınıfı: {}".format(sayi, a["AdSoyad"], self.bolum[self.sinif[a["sinifNo"]]["BolumNo"]]["BolumAdi"], self.sinif[a["sinifNo"]]["SinifNo"]))
            sayi = sayi+1

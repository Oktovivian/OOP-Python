'''
class Segitiga:

  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi
    self.luas = 0.5 * alas * tinggi 


segitiga_besar = Segitiga(100, 80)

# akses variabel alas, tinggi, dan luas dari luar kelas
print(f'alas: {segitiga_besar.alas}')
print(f'tinggi: {segitiga_besar.tinggi}')
print(f'luas: {segitiga_besar.luas}')
'''

class tabung:
    def __init__(self, jarijari, tinggi):
        self.jarijari = jarijari
        self.tinggi = tinggi
        self.volume = (1/3) * 3.14 * jarijari ** 2 * tinggi

tabung_besar = tabung(10, 20)

# akses variabel jarijari, tinggi, dan volume dari luar kelas
print(f'jarijari: {tabung_besar.jarijari}')
print(f'tinggi: {tabung_besar.tinggi}')
print(f'volume: {tabung_besar.volume}')
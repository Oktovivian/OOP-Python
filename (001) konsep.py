"""
# INI ADALAH PROSEDURE
def hitung_luas ():
  alas = float(input('Masukkan alas: '))
  tinggi = float(input('Masukkan tinggi: '))
  print('Luas =', 0.5 * alas * tinggi)

# kita bisa panggil berkali-kali
hitung_luas()
# panggil lagi
hitung_luas()
"""



"""
# INI ADALAH FUNGSI
def input_alas_dan_tinggi ():
  alas = float(input('Masukkan alas: '))
  tinggi = float((input('Masukkan tinggi: ')))

  return alas, tinggi

def hitung_luas (alas, tinggi):
  return 0.5 * alas * tinggi

# fungsional kita yang mengelola sendiri 
# hasil kembaliannya

# independen
print(hitung_luas(5, 10))

# contoh panggil alas dan tinggi
alas, tinggi = input_alas_dan_tinggi()
print(hitung_luas(alas, tinggi))
"""





# INI ADALAH OOP
class jajargenjang:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi

  def get_luas(self):
    return self.alas * self.tinggi

jajargenjang1 = jajargenjang(5, 10)
jajargenjang2 = jajargenjang(10, 10)

print('luas jajargenjang1:', jajargenjang1.get_luas())
print('luas jajargenjang2:', jajargenjang2.get_luas())

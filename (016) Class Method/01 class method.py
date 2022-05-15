

class mobil:
    jumlah_roda = 4 # class variable

    def __init__(self, merk):
        self.merk = merk    # instance variable

    @classmethod
    def pengertian(cls):
        print(f'mobil memiliki {cls.jumlah_roda}sroda')

# panggil secara langsung
mobil.pengertian()

# panggil via objek
sebuahMobil = mobil('tanpa merk')
sebuahMobil.pengertian()
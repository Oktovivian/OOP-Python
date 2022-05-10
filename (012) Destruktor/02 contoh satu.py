class Mobil:
    def __init__(self, merk):
        self.merk = merk
        print(f'mobil {self.merk} dibuat')

    def __del__(self):
        print(f'mobil {self.merk} dihapus')

ferrari = Mobil('Ferrari')
lamborghini = Mobil('Lamborghini')

# del lamborghini
# del ferrari
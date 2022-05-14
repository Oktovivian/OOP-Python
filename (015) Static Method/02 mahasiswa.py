class mobil:
    def __init__(self, merk):
        self.__merk = merk

    def getMerk(self):
        return self.__merk

    @staticmethod
    def merkBesar(merk):
        return merk.upper()

prius = mobil('prius')
print(prius.getMerk())
print(mobil.merkBesar(prius.getMerk()))
# parameter bisa dari luar kelas
print(mobil.merkBesar("prius"))
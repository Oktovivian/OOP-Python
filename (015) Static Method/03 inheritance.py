class mobil:
    def __init__(self, merk):
        self.__merk = merk
    def getMerk(self):
        return self.__merk

    @staticmethod
    def merkBesar(merk):
        return merk.upper()

class mobilKeluarga(mobil):
    def __init__(self, merk):
        super().__init__(merk)

    def getMerk(self):
        return mobil.merkBesar(super().getMerk())

Lenkruser = mobil('Lenkruser')
print(Lenkruser.getMerk())

gclass = mobilKeluarga('Gclass')
print(gclass.getMerk())
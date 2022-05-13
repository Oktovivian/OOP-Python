class Universitas:
    # static atau class variable
    Akreditasi = 'A'

    def __init__(self, nama):
        # instance variable
        self.nama = nama

Diponegoro = Universitas('Diponegoro')
print(Diponegoro.Akreditasi)

Brawijaya = Universitas('Brawijaya')
print(Brawijaya.Akreditasi)

Universitas.Akreditasi = 'B'

print(Diponegoro.Akreditasi)
print(Brawijaya.Akreditasi)

 
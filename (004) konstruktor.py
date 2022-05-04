class mahasiswa:
    def __init__(self, nama, nim, asal):
        self.nama = nama
        self.nim = nim
        self.asal = asal

    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dengan NIM {self.nim} dan alamat {self.asal}')

Vian = mahasiswa("Ramadhan Oktovivian Muhammad", "1301213040", "Lamongan")
Hua = mahasiswa(asal = "Sumatera", nama = "Hua Pramudita", nim = "1301213041")

Vian.perkenalan()
Hua.perkenalan()
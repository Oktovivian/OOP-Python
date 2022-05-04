class Kampus:
    def __init__(self, namaKampus, alamat, akreditasi):
        self.namaKampus = namaKampus
        self.alamat = alamat
        self.akreditasi = akreditasi

class Mahasiswa:
    def __init__(self, nama, asal, nim, kampus):
        self.nama = nama
        self.asal = asal
        self.nim = nim
        self.Kampus = kampus

    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dengan NIM {self.nim} dan alamat {self.asal}')
        print(f'Saya berkuliah di {self.Kampus.namaKampus} yang beralamat di {self.Kampus.alamat} dengan akreditasi {self.Kampus.akreditasi}')

Oktovivian = Mahasiswa(
    nama='Ramadhan Oktovivian Muhammad',
    asal='Lamongan',
    nim='18081010012',
    kampus = Kampus(
        namaKampus='Telkom University',
        alamat='Jl.Dayeuhkolot',
        akreditasi='A'
    )
)

Oktovivian.perkenalan()
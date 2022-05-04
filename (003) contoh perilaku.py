# buat kelasnya terlebih dahulu
class Mahasiswa:
    nama = None
    nim = None
    alamat = None
    

    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dengan NIM {self.nim} dan alamat {self.alamat}') 

Vian = Mahasiswa()
Vian.nama = "Ramadhan Oktovivian Muhammad"
Vian.nim = "18081010012"
Vian.alamat = "Jl.Kebon Jeruk"

Hua = Mahasiswa()
Hua.nama = "Hua Pramudita"
Hua.nim = "18081010013"
Hua.alamat = "Jl.Kebon Jeruk"

Vian.perkenalan() 
Hua.perkenalan()
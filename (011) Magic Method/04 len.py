class Siswa:
  def __init__(self):
    self.__list_siswa = []

  def tambah_siswa(self, siswa):
    self.__list_siswa.append(siswa)

  def __len__(self):
    return len(self.__list_siswa)

grup1 = Siswa()
grup1.tambah_siswa('Huda')
grup1.tambah_siswa('Mahmud')
grup1.tambah_siswa('Zaskia')

print(len(grup1))

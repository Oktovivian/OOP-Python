class Motor:
    def __init__(self, merk, cc):
        self._merk = merk
        self._cc = cc

class MotorBalap(Motor):
    def __init__(self, merk, cc, total_gear):
        super().__init__(merk, cc)
        self._total_gear = total_gear
    
    def pamer(self):
        # akses _merk dari subclass
        print(
            f'Ini motor {self._merk} dengan total gear {self._total_gear}'
        )

Ducati = MotorBalap('Ducati', 1000, 8)
Ducati.pamer()
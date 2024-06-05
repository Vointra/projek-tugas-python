class Mobil:

    def __init__(self, merk, tipe, tahun, kapasitas_mesin, warna):
        self.merk = merk
        self.tipe = tipe
        self.tahun = tahun
        self.kapasitas_mesin = kapasitas_mesin
        self.warna = warna

    def get_merk(self):
        return self.merk

    def set_merk(self, merk):
        self.merk = merk

    def get_tipe(self):
        return self.tipe

    def set_tipe(self, tipe):
        self.tipe = tipe

    def get_tahun(self):
        return self.tahun

    def set_tahun(self, tahun):
        self.tahun = tahun

    def get_kapasitas_mesin(self):
        return self.kapasitas_mesin

    def set_kapasitas_mesin(self, kapasitas_mesin):
        self.kapasitas_mesin = kapasitas_mesin

    def get_warna(self):
        return self.warna

    def set_warna(self, warna):
        self.warna = warna

    def __str__(self):
        return f"Mobil {self.merk} {self.tipe} {self.tahun} {self.kapasitas_mesin} {self.warna}"

mobil = Mobil("Toyota", "Avanza", 2023, 1500, "Hitam")

print("Merk mobil:", mobil.get_merk())
print("Tipe mobil:", mobil.get_tipe())
print("Tahun mobil:", mobil.get_tahun())
print("Kapasitas mesin mobil:", mobil.get_kapasitas_mesin())
print("Warna mobil:", mobil.get_warna())

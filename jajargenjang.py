# Input panjang sisi dan tinggi jajargenjang
panjang_sisi_a = float(input("Masukkan panjang sisi a: "))
panjang_sisi_b = float(input("Masukkan panjang sisi b: "))
tinggi = float(input("Masukkan tinggi: "))

# Menghitung luas jajargenjang
luas = panjang_sisi_a * tinggi

# Menghitung keliling jajargenjang
keliling = 2 * (panjang_sisi_a + panjang_sisi_b)

# Menampilkan hasil
print("Luas jajargenjang adalah:", luas)
print("Keliling jajargenjang adalah:", keliling)
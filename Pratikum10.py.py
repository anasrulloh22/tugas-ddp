#soal 1
def lulus_saja(data_nilai):
    siswa_lulus = [siswa['nama'] 
                   for siswa in data_nilai 
                   if siswa['nilai'] > 65]
    return siswa_lulus


hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

hasil_lulus = lulus_saja(hasil_akhir)
print(hasil_lulus)

print("=========================")
#soal 2
def balikan(daftar_buah):
    buah_terbalik = []
    for buah in reversed(daftar_buah):
        buah_terbalik.append(buah)
    return buah_terbalik

buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_terbalik = balikan(buah_asli)
print(hasil_terbalik)

print("=========================")

#soal 3
def duplikasi(daftar_buah):
    buah_duplikasi = []
    for buah in daftar_buah:
        buah_duplikasi.append(buah)
        buah_duplikasi.append(buah)
    return buah_duplikasi

buah_asli = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(buah_asli)
print(hasil_duplikasi)

print("=========================")
#soal 4
def filter_konsonan(kalimat):
    konsonan = ""
    for char in kalimat:
        if char.isalpha() and char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            konsonan += char
    return konsonan

kalimat_asli = "Nurul Fikri"
hasil_konsonan = filter_konsonan(kalimat_asli)
print(hasil_konsonan)
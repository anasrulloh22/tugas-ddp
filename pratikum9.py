# Soal No.1
def profil (nama,alamat,gender,umur,hobi):
    print ("hello nama saya adalah",nama)
    print ("alamat saya di",alamat)
    print ("gender saya adalah",gender)
    print ("umur saya adalah ",umur)
    print("hobi saya adalah", hobi)
profil("ahmad nasrulloh","Depok 2","Pria","18 tahun","Futsal")
print("============================================")
# Soal No.2
def kelulusan(nilai):
    if nilai >= 0 and nilai <=60:
        return "Gagal"
    elif nilai >=61 and nilai <=70:
        return "Baik"
    elif nilai >=71 and nilai <=80:
        return "sangat baik"
    elif nilai >=81 and nilai <=100:
        return "istimewa"
    else:
        return "Nilai tidak valid !"
    
print(kelulusan(60))
print("=============================================")
# Soal No.3
def bilangan_ganjil(bilangan):
    for i in range(bilangan):
        if i % 2!=0:
            print(i)
bilangan_ganjil(100)
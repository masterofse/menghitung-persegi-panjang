#main py

#fungsi untuk memeriksa apakah input adalah bilangan positif
def input_positif(prompt)
    while True:
        try:
            nilai = float(input(prompt))
            if nilai > 0:
                return nilai
            else:
                print("nilai harus lebih besar dari 0. coba lagi.")
        except ValueError:
            print("input tidak valid, masukan angka.")

# meminta input panjang dan lebar dari pengguna
panjang = float(input("masukan panjang pergi panjang:"))
lebar = float(input("masukan lebar persegi panjang:"))

#menghitung luas
luas = panjang * lebar

#menampilkan hasil keliling
keliling = 2 * (panjang + lebar)


#menampilkan hasil luas dan keliling dengan format yang lebih jelas
print(f"luas persegi panjang adalah: {luas} satuan persegi")
print(f"keliling persegi panjang adalah:{keliling} satuan")
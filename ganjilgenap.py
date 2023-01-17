#menginput angka
angka = int(input("masukkan angka:"))

#jika habis dibagi nol, maka genap
if (angka % 2) == 0:
    print("{0} adalah bilangan genap". format(angka))

#jika tidak habis dibagi nol, maka ganjil
else:
    print("{0} adalah bilangan ganjil". format(angka))
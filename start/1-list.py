#"""List adalah jenis kumpulan data terurut (ordered sequence), dan merupakan salah satu
#variabel yang sering digunakan pada Python. Serupa, namun tak sama dengan array pada 
#ahasa pemrograman lainnya. Bedanya, elemen List pada Python tidak harus memiliki tipe
#data yang sama. Mendeklarasikan List cukup mudah dengan kurung siku dan elemen yang
#dipisahkan dengan koma. Setiap data didalamnya dapat diakses dengan indeks yang dimulai
#dari 0."""

x=[1, 2, 3, 4, 5, 6]
x[2]='tiga'
x.append('enam')
del x[5]

print(x)
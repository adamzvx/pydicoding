#INPUT OUTPUT

#"""Untuk memberikan nilai pada sebuah variabel, kita menggunakan operator "=", antara nama 
#variabel dengan nilai yang ingin disimpan.Misalnya: x = 1Artinya kita akan menyimpan nilai
#1 (tipe int) ke variabel x."""
varA = 'lima'
varAA = 5
print('angka variabel a adalah', varA, ' atau', varAA)
# Menggunakan format
print('hello {}'.format('kakak'))

#"""Cara yang kedua mirip dengan sintaks C/C++, yakni menggunakan operator “%” yang #ditambahkan dengan "argument specifiers", misalnya "%s" and "%d". Contohnya saat kita #ingin menambahkan nama kita pada string hello:"""
nama = 'Jhon'
print('%s abangnya Jin umurnya %d tahun'% (nama, 16))
#Contoh menambahkan objek selain string (otomatis dikonversi):
mylist = [1,2,3]
print("A list: %s" % mylist)

a, b = 10, 31
print('a: %x and b: %X' % (a, b))
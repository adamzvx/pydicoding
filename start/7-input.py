num = input('masukkan nomor :')
num = float(num)
print(num/0.1)

#"""Berkas python dapat dipanggil sebagai skrip di konsol atau command prompt, serta dapat
#ditambahkan parameter tambahan saat memanggil skrip tersebut.
#Utamanya fungsi yang akan digunakan adalah sys.argv yang memuat seluruh argumen yang
#diterima. Anda juga dapat menggunakan len(sys.argv) untuk mengetahui banyaknya argumen
#yang ditampung""" 

#Contoh, sebuah berkas test.py yang akan menambahkan tiga argumen:
import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
print(sys.argv[1],sys.argv[0])
# in CLI >>python3.8 start/7-input.py arg1 arg2 arg3 
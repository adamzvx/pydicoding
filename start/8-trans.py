zx = 99
print(str(zx).zfill(4))

j='Judul ku'
print(j.upper())
print(j.lower())
print(j.isupper())
print(j.islower())
#'''Selain islower() and isupper(), terdapat beberapa metode lain yang dapat digunakan untuk
#memeriksa isi dari string. Semua method berikut mengembalikan nilai boolean:'''
# isalpha() mengembalikan True jika string berisi hanya huruf dan tidak kosong.
# isalnum() mengembalikan True jika string berisi hanya huruf atau angka, dan tidakkosong.
# isdecimal() mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
# isspace() mengembalikan True jika string berisi hanya spasi, tab, newline,atau whitespaces lainnya dan tidak kosong.
# istitle() mengembalikan True jika string berisi kata yang diawali huruf kapital dandilanjutkan dengan huruf kecil seterusnya.
# Fungsi startswith() dan endswith() akan mengembalikan nilai True berdasarkan nilai awalan atau akhiran string.
# Fungsi join() berguna saat Anda memiliki sejumlah string yang perlu digabungkan
print('- '.join(['My', 'name', 'is', 'Simon']))
# Sebaliknya metode split() memisahkan substring berdasarkan delimiter tertentu (defaultnya adalah whitespace - spasi, tab, atau newline):
print('My name is Simon'.split())
#Anda dapat merapikan pencetakan teks di layar dengan rjust(), ljust() atau center(). rjust() dan ljust() akan menambahkan spasi pada string untuk membuatnya sesuai (misalnya rata kiri atau rata kanan). 
print('Hello'.rjust(20,'%'))
#lstrip() dan rstrip() akan menghapus sesuai dengan namanya, awal saja atau akhir saja:
spam = '    Hello World     '
print(spam)
print(spam.strip())
# replace() adalah satu fungsi python yang mengembalikan string baru dalam kondisi substring telah tergantikan dengan parameter yang dimasukkan,param ke 2 jumlah yang diganti:
string = "geeks for geeks geeks geeks geeks"
print(string.replace("geeks", "GeeksforGeeks", 3))


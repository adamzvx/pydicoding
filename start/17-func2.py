# Argumen posisi dapat bersifat dinamis dengan menambahkan sintaksis tanda bintang (*),
# untuk menampung kontainer (Tuple). Kontainer (Tuple) ini bisa bersifat opsional, artinya
# tidak wajib diisi (boleh kosong), jika memang tidak ada argumen yang perlu ditambahkan.
# Pada saat diisi, seperti layaknya Tuple dapat memiliki jumlah/panjang yang dinamis.
def printinfo(fixedarg, *args):
    "This prints a variable passed arguments"
    print('Output: fixedarg {}'.format(fixedarg))
    for a in args:
        print('argumen posisi {}'.format(a)) 
# Panggil printinfo 
printinfo(10)
printinfo(70, 60, 50)

#Argumen kata kunci (keyword) dapat bersifat dinamis dengan menambahkan sintaksis dua tanda
# bintang (**) untuk menampung kontainer (Dictionary).
# Kontainer (Dictionary) ini bisa bersifat opsional, artinya tidak wajib diisi (boleh
# kosong), jika memang tidak ada argumen yang perlu ditambahkan. 
def printinfo2(*args, **kwargs):
    for a in args:
        print('argumen posisi 2 {}'.format(a))
    for key, value in kwargs.items():
        print('argument kata kunci 2 {}:{}'.format(key, value))
printinfo2()
printinfo2(1, 2, 3)
printinfo2(i=7, j=8, k=9)
printinfo2(1, 2, j=8, k=9)
printinfo2(*(2, 3), **{'i':7, 'j':8})
 
#FUNGSI LAMBDA ANONIM
# Fungsi Anonim (anonymous) tidak dideklarasikan seperti halnya fungsi pada umumnya dengan
# kata kunci def, melainkan menggunakan kata kunci (keyword) lambda. Sebuah fungsi lambda
# dapat menerima argumen dalam jumlah berapa pun, namun hanya mengembalikan satu nilai
# expression.
sum = lambda arg1, arg2: arg1 + arg2
x = lambda x,y: x**y
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", x( 2,2 ))

# CaKUPAN VARIABEL
# Variabel yang didefinisikan dalam fungsi bersifat lokal (di fungsi tersebut), dan yang
# didefinisikan di luar fungsi bersifat global. Perbandingkan kode berikut pada bagian yang
# ditebalkan dan keluarannya.
total = 0  # This is global variable.
# fungsi didefinisikan di bawah ini
def sum2(arg1, arg2):
    global total
    total = arg1 + arg2 # variabel lokal total
    print('Inside the function local total: ', total)
    return total
 
sum2(10, 20)
print('Outside the function (global) total: ', total)
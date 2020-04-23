# Pernyataan return [expression] akan membuat eksekusi program keluar dari fungsi saat itu,
# sekaligus mengembalikan nilai tertentu. Nilai return yang tidak mengembalikan (ekspresi)
# nilai bersifat sama dengan contoh di bawah ini. 

def sum(arg1, arg2):
    # Add both the parameters and return them.
    total = arg1 + arg2
    print('Inside the function: {}'.format(total))
    return total
# Panggil sum
total = sum(10, 20)
#########
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print('Nilai di dalam fungsi: {}'.format(mylist))
#########
myList =[10, 20, 30]
changeme(myList)
print('Nilai di luar fungsi : {}'.format(myList))

#Required arguments : Argumen yang wajib disertakan dan disusun secara terurut
# dalampemanggilan fungsi.
#Keyword arguments : Argumen yang ditambahkan dengan menyertakan nama variabelkeywordnya
# dalam pemanggilan fungsi.
#Default arguments : Argumen yang bersifat tidak wajib diisi, karena telah memilikinilai
# default.
# Variable-length arguments : Argumen yang bersifat opsional namun dapat
# disesuaikanbanyaknya #dan tidak didefinisikan secara spesifik dalam definisi fungsi.
def printinfo(name, age):
   "This prints a passed info into this function"
   print('Name: ', name)
   print('Age: ', age)

printinfo('adam',8)
#############################

# Sebuah fungsi yang memiliki sejumlah argumen, dapat diatur nilai bawaannya (default),
# agar pada saat pemanggilan nilainya bisa menjadi opsional untuk diisi.

def printinfo2(age, name='adam' ): #argumen default harus setelah argumen tanpa default
   "This prints a passed info into this function"
   print('Name: ', name)
   print ('Age: ', age)

printinfo2(age=2)
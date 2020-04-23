#  Di Python, fungsi khusus atau metode sebagai constructor ini bernama __init__ atau biasa
# diucapkan sebagai "double underscore init"
class Kalkulator:
    """contoh kelas kalkulator sederhana"""
 
    def __init__(self, i=12345):
        self.i = i  # i adalah variabel pada constructor, self.i adalah variabel dariclass
 
    def f(self):
        return 'hello world'

k = Kalkulator(i=1024)  # melakukan instantiation sekaligus mengisi atribut i jadi 1024
print(k.i)              # mencetak atribut i dari objek k dengan keluaran nilai 1024

#METHOD
# METHOD OBJEK
# Salah satu hal khusus yang dimiliki oleh metode dengan adanya argumen bernama self, Anda
# tentu bertanya-tanya tentang argumen self pada metode-metode dalam kelas tersebut
# sebetulnya apa?
# Argumen pertama dari metode-metode dalam class, biasa diberikan nama self sebagai suatu
# konvensi atau standar penamaan, meskipun Anda bisa juga menggunakan nama lain. 
print (Kalkulator.f(k)) # k untuk objek


# CLASS METHOD
# Classmethod adalah sebuah fungsi yang mengubah metode menjadi metode dari class (class
# method). Dalam penggunaannya, fungsi ini dijadikan sebagai fungsi decorator @classmethod, # kemudian pemanggilannya bisa langsung dari class yang terdefinisi ataupun melalui objek.
class Kalkulator2:
    """contoh kelas kalkulator sederhana"""
 
    def f(self):
        return 'hello world'
 
    @classmethod
    def tambah_angka(cls, angka1, angka2):
        return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)
#print(Kalkulator2.f())
#print(Kalkulator2.tambah_angka(1, 2))


# Static Method
# Staticmethod adalah sebuah fungsi yang mengubah metode menjadi metode statis (static
# method). Dalam penggunaannya, fungsi ini dijadikan sebagai fungsi decorator
# @staticmethod, kemudian pemanggilannya bisa langsung dari class yang terdefinisi ataupun
# melalui objek.
class Kalkulator3:
    """contoh kelas kalkulator sederhana"""
 
    def f(self):
        return 'hello world'
 
    @staticmethod
    def kali_angka(angka1, angka2):
        return '{} x {} = {}'.format(angka1, angka2, angka1 * angka2)
a = Kalkulator3.kali_angka(2, 3)
print(a)
b = Kalkulator3.kali_angka(3.0, 3)
print(b)

class KalkulatorTambah(Kalkulator):
    """contoh mewarisi kelas kalkulator sederhana"""
 
    def tambah_angka(self, angka1, angka2):
        if angka1 + angka2 <= 9:  # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
            super().tambah_angka(angka1, angka2)  # panggil fungsi dari Kalkulator lalu isi nilai
        else:  # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
            self.nilai = angka1 + angka2
        return self.nilai


class Pegawai:
    pass  # definisi class kosong
 
don = Pegawai()  # membuat Pegawai baru menjadi objek bernama don
 
# tambahkan item data pada objek sebagai record
don.nama = 'Don Doo'
don.bagian = 'IT'
don.gaji = 999
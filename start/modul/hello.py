# Kita akan membuat kelas Reviewer dengan atribut nama dan kelas, 
# serta fungsi review() yang akan mencetak atribut yang telah didefinisikan.
def world():
    print("Hello, World!")
nama = "Dicoding"
class Reviewer:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)
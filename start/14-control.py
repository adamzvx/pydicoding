for letter in 'Python':     # First Example
    if letter == 'h':
        break
    print('Current letter: {}'.format(letter))

var = 10                    # Second Example
while var > 0:             
    print('Current variable value: {}'.format(var))
    var = var - 1
    if var == 5:
        break

#Continue
for a in [0, 1, -1, 2, -2, 3, -3]:     #Second Example
    if a <= 0:
        continue
    print('Elemen positif: {}'.format(a))


# Pada Python juga dikenal fungsi else setelah for. Fungsinya diutamakan pada perulangan
# yang bersifat pencarian - untuk memberikan jalan keluar program saat pencarian tidak
# ditemukan.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

# Berbeda dengan Else setelah For, pada statement while, blok statement else akan selalu
# dieksekusi saat kondisi pada while menjadi salah
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
else:
    print("Loop is finished")
# Pass Digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement)
# namun tidak melakukan apapun - melanjutkan eksekusi sesuai dengan seharusnya
for letter in 'Python':
    if letter == 'h':
        pass
        print ("This is pass block")
    print('Current letter: {}'.format(letter))
import sys
data=''
while(data!='exit'):
    try:
        data=input('Please enter an integer (type exit to exit): ')

        print('got integer: {}'.format(int(data)))
    except:
        if data.lower() == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))

# List Comprehension (membuat list dengan inline loop dan if)
    #Cara 1
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
  squares.append(n**2)
print(squares)

    #Cara 2 List Comprehension
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)

#Contoh3 menemukan bilangan yang ada di kedua list
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
  for b in list_b:
    if a == b:
      common_num.append(a)
      
#Contoh4 Implementasi dengan list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]

# Contoh 5 kecilkan semua huruf
list_a = ["Hello", "World", "In", "Python"]
small_list_a = [_.lower() for _ in list_a]
print(small_list_a) # Output: ['hello', 'world', 'in', 'python']

# Contoh 6
list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)


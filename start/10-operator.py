l = [1,2,3,3,4,4,4,4,5,6]
s = set(l)
x = "Hello, World"
 
print(l);print(len(l))
print(s);print(len(s)) 
print(x);print(len(x))
t=[1, 2, 3] + ['A', 'B', 'C']*3
print(t)

#Fungsi range() memberikan deret bilangan dengan pola tertentu. Untuk melakukan perulangan
# (misalnya for) dalam mengakses elemen list, Anda dapat menggunakan fungsi range() pada
# Python. 
for i in range(9):
    print(i)
for i in range(2,9):
    print(i)
print([_ for _ in range(1, 9, 2)])  # list comprehension
# Untuk mengetahui sebuah nilai atau objek ada dalam list, Anda dapat menggunakan operator in dan not in.
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam);print('cat' not in spam) 

a, b = 'Alice', 'Bob'
a, b = b, a
print(a)
print(b)
x = [2, 5, 3.14, 1, -7];y = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
x.sort();y.sort(reverse=True)


#\'          Single quote
#\"          Double quote
#\t          Tab
#\n         Newline (line break)
#\\          Backslash
#Sebaliknya, Python juga menyediakan cara untuk memasukkan string sesuai dengan apapun
# input atau teks yang diberikan. Metode ini dinamakan Raw Strings. Umumnya digunakan untuk
# regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash.
print(r'That is Carol\'s cat.')
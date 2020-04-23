# CONTOH DASAR
z = 0
try:
    x=1/z
    print(x)
except ZeroDivisionError:
    print('tidak bisa dibagi 0')

#Contohh 2
try:
    with open('contoh_tidak_ada.py') as file:                   
         print(file.read())                          
except(FileNotFoundError, ):
        print('file tidak ditemukan')

#COntohhh
d = {'ratarata': '10.0'}
try:
    print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:                                 
    print('kunci tidak ditemukan di dictionary')
except ValueError:              
    print('nilai tidak sesuai')

#COntoh CPntoh.....
try:
     print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:                                 
     print('kunci tidak ditemukan di dictionary')
except ValueError:              
     print('nilai tidak sesuai')
#
try:
    print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:                                 
    print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
    print('nilai atau tipe tidak sesuai')
#
try:
    print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:         
    print('penangan kesalahan: {}'.format(e))

# Pengecualian Handling Error
d = {'ratarata': '10.0'}
if 'total' not in d:                                                                                                                         
    raise KeyError('harus memiliki total')   
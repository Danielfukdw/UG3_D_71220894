plat = input('Masukan plat nomor :').lower().split(" ")

try :
    x ='Plat nomor diperuntukan untuk mobil ' if plat  [1] == 0000 and plat[1] <= 3000 else 'Plat nomor diperuntukan untuk motor ' if plat [1] == 3001 and plat[1]<=4000 else 'Plat nomor diperuntukan untuk Angkutan umum ' if  plat[1] == 4001 and plat[1] <=5000 else 'Plat nomor tidak terindikasi ketiga angkutan tersebut'
    print(x)
except:
    print('Plat Nomor Tidak Terinidikasi, harus terdapat nomor kendaraan setelah kode daerah')

    
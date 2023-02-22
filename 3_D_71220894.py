nilai = int(input('Masukan nilai awal deret : '))
akhir = int(input('Masukan Akhir deret: '))
i = nilai
while i <= akhir:
    print (i)
    i += 1 if  i % 6 != 0 and i %8 != 0 else ' '
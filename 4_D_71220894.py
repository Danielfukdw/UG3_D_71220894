name = str(input('Masukan nama lengkap anda :'))
prodi = str(input('Masukan prodi anda : '))
nilai = str(input('Masukan nilai anda (dalam huruf) yang anda dapat: ')).lower

try:
    print('Nilai yang anda dapatkan adalah 4.0'if nilai == "a" else 'Nilai yang anda dapatkan adalah 3.75'if nilai == "a-" else 'Nilai yang anda dapatkan adalah 3.25'if nilai == 'b+' else 'Nilai yang anda dapatkan adalah 3 'if nilai =='b'else 'Nilai yang anda dapatkan adalah 2.75, Kurang semangat belajar nih 'if nilai == 'b-'else 'Nilai yang anda dapatkan adalah 2.25, Pas-pasan banget nih ?' if nilai =='c+'else 'Nilai yang anda dapatkan adalah 2.0, Males malesan aja terus!!'if nilai== 'c'else   "Nilai yang anda dapatkan adalah 1.0, apakah sudah ada pikiran buat pindah jurusan ?"if nilai== "d" else 'nilai yang kamu dapatkan adalah 0,niat kuliah gk sih ????' )
except:
    print('Inputan nilai yang anda masukan tidak valid')
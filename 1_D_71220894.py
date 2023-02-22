nilai_curah = float(input('Masukan nilai curah hujan : '))
x = 'Cuaca Terang/Berawan' if nilai_curah == 0 else 'Curah Hujan Ringan' if nilai_curah == 0.5 and nilai_curah <= 20 else 'Curah hujan sedang' if nilai_curah == 21 and nilai_curah <=50 else 'Curah Hujan Lebat'if nilai_curah == 51 and nilai_curah <= 100 else 'curah hujan Extrem 'if nilai_curah >= 100 else False 
print(x)
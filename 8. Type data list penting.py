print('Type Data Skalar atau Tipe data sederhana')
anak1 = 'Eko'
anak2 = 'Dwi'
anak3 = 'Tri'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nType data list/daftar/array')
anak = ['Eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('Panca')
print(anak)

print('\nSapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nSapa Semua Anak')
for a in anak:
    print(f'Hai {a}!')



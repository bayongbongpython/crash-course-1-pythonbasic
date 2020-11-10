print('data ini dikirimkan oleh server gojek, untuk memberikan informasi driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 15},
        {'nama': 'Tri', 'jarak': 20},
        {'nama': 'Catur', 'jarak': 25},
    ]}

print(data_dari_server_gojek)
print(f"Driver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][2]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][0]}")

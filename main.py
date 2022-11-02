"""
Demo Project Pertama Python
"""

# Sekuensial
print('Ibu Berkata, "Budi Tolong Pergi Ke Toko"')
print('Budi Jawab, "Baik, Beli Apa Bu?"')
print('Ibu Berkata, "Tolong beli 1 Susu"')
print('Ibu Berkata, "Jika Ada Telur, Beli 6"')
print('Budi Berangkat')

# percabangan
botol_susu = 2
jumlah_telur = 15

if botol_susu > 0:
    print('Budi Beli 1 Susu')
    print('Budi mengecek telur')
    print(f'Telur Ada {jumlah_telur}')
    if jumlah_telur > 0:
        print('Budi Beli 6 Telur')
    else:
            print('Budi Tidak Beli Telur')
else:
    print(f'Botol Susu Ada {botol_susu}')
    print('Budi Tidak Jadi Membeli')

print('Budi Pulang Ke Rumah')

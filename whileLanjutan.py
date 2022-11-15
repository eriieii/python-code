"""
Perulangan dengan while lanjutan
"""

book_count = 10
print('Ibu Berkata, Baca Semua Buku')
read_count = 0

understood_count = 0
print(f'Jumlah buku yang sudah di baca dan di pahami {understood_count}')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 6:
        print(f'Buku ke {understood_count + 1} belum paham')
    else:
        understood_count = understood_count + 1
        print(f'Buku ke {understood_count} sudah paham')

print(f'Jumlah buku yang sudah dibaca dan dipahami {understood_count}')
if understood_count == book_count:
    print('Bu, semua buku sudah dibaca dan paham')
else:
    print(f'Bu, tidak semua buku bisa dipahami. '
          f'Budi hanya bisa memahami {understood_count} buku')


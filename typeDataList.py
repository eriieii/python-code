book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
print('\nTampilkan Book List')
print(book_list)

print('\nProses dengan for')
for book in book_list:
    print(book)

print('\nList Indeks Tertentu')
print(book_list[0])

print('\nList Indeks Range')
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = [1, 'Buku Pelajaran', 3.14, -20]
print('\nList Indeks for in range type data tiap elemen berbeda beda')
for i in range(0, len(book_list)):
    print(book_list[i])


print('\nKembalikan nilai awal')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
print(book_list)
print('\nTambah data buku baru')
book_list.append('Sosiologi')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nClear Data')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
print('\nGanti elemen pertama')
book_list[0] = 'Sejarah'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nAmbil elemen ke dua')
book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nData yang tadi di hilangkan')
print(book)

book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
print('\nPop')
book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPop -1')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
book_list.pop(-1)
for i in range(0, len(book_list)):
     print(book_list[i])

print('\nPerintah Del')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
del book_list[3]
for i in range(0, len(book_list)):
     print(book_list[i])

print('\nPerintah Del dengan comprehension')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
del book_list[:] #start:END
for i in range(0, len(book_list)):
         print(book_list[i])

print('\nPerintah Del dengan comprehension start')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
del book_list[0:3] #start:END
for i in range(0, len(book_list)):
         print(book_list[i])

print('\nPerintah Del dengan comprehension start dengan minus')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
del book_list[0:-2] #start:END
for i in range(0, len(book_list)):
         print(book_list[i])

print('\nPerintah Del dengan comprehension start dengan step')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
del book_list[0::2] #start:END:STEP
for i in range(0, len(book_list)):
         print(book_list[i])

print('\nMembuat List Baru')
book_list = ['Matematika', 'IPA', 'PKN', 'Agama']
book_new_list = book_list[:]
for i in range(0, len(book_list)):
         print(book_list[i])

print('\nMembuat List Baru Lagi')
del book_list[:]
for i in range(0, len(book_new_list)):
         print(book_new_list[i])

print('\nMengambil List Baru : Ganjil')
book_list = ['1 Matematika', '2 IPA', '3 PKN', '4 Agama']
book_new_list = book_list[0::2]
for i in range(0, len(book_new_list)):
         print(book_new_list[i])

print('\nMengambil List Baru : Genap')
book_list = ['1 Matematika', '2 IPA', '3 PKN', '4 Agama']
book_new_list = book_list[1::2]
for i in range(0, len(book_new_list)):
         print(book_new_list[i])

print('\nMengambil List Baru : Data Terakhir Di Hilangkan')
book_list = ['1 Matematika', '2 IPA', '3 PKN', '4 Agama']
book_new_list = book_list[0:-1]
for i in range(0, len(book_new_list)):
         print(book_new_list[i])



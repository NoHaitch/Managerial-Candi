# Modul tools
# Berisi semua fungsi buatan sebagai pelengkap

# KAMUS
# type Data : < isi: matriks of string,
#               n_baris : int,
#               n_kolom : int >
# ALGORITMA
class Data:
    def __init__(self, isi, n_baris, n_kolom):
        self.isi = isi
        self.n_baris = n_baris
        self.n_kolom = n_kolom

# function string_split (stringx : string, key : string) -> array [0..count-1] of string
# Memisahkan suatu string "stringx" dengan pemisah "key" dan mengembalikan array yang berisi hasil pemisahan
def string_split(stringx: str, key: str) -> list[str]:
    # KAMUS LOKAL
        # count, i, index_str, index_hasil : int
        # part : string
        # hasil : array [0..count-1] of string
    # ALGORITMA
    # Mencari jumlah bagian hasil pemisahan string
    count = 1
    for i in range(len(stringx)):
        if(stringx[i] == key):
            count += 1
    if(count == 1):
        return [stringx]
    hasil = ["" for _ in range(count)]
    # Membagi string menjadi bagian kecil "part" dan digabungkan pada hasil
    index_str = 0
    index_hasil = 0
    while True:
        if(index_str == len(stringx)):
            break # semua karakter string sudah dicek
        part = ""
        for i in range(index_str,len(stringx)):
            if(stringx[i] == key): # karakter pemisah tidak dimasukkan ke hasil
                index_str += 1
                break
            else: # string[i] != key
                index_str += 1
                part += stringx[i]
        # Menyimpan bagian string pada array hasil
        hasil[index_hasil] = part 
        index_hasil += 1
    return hasil

# FUNGSI REKURSIF
# function string_slice (stringx : string, index_awal:integer, index_akhir: integer, index_sekarang:integer = 0)-> string
# Mengembalikan bagian stringx dari index_awal hingga index_akhir 
def string_slice(stringx: str, index_awal: int, index_akhir: int, index_sekarang: int = 0) -> str:
    # KAMUS LOKAL
        # index_sekarang : int
    # ALGORITMA
    if(index_sekarang < index_awal):
        return string_slice(stringx, index_awal, index_akhir, index_sekarang+1)
    elif(index_sekarang == len(stringx)):
        return ""
    elif(index_sekarang == index_akhir-1):
        return stringx[index_sekarang]
    else:
        return stringx[index_sekarang] + string_slice(stringx, index_awal, index_akhir, index_sekarang+1)

# function string_strip(stringx : string)-> array [index_awal..index_akhir-1] of string
# Membersihkan string dari karakter kosong / spasi (" ") pada awal dan akhir string
def string_strip(stringx: str) -> list[str]:
    # KAMUS LOKAL
        # index_awal, index_akhir, i : integer
        # hasil : string
    # ALGORITMA
    # cari index dimulai string asli (string yang bukan spasi string kosong " " yang tidak berguna)  
    index_awal = 0
    for i in range(len(stringx)):
        if(stringx[i] != " "):
            break
        else:
            index_awal += 1
    # cari index berakhirnya string asli (string yang bukan spasi string kosong " " yang tidak berguna)
    index_akhir = len(stringx)
    for i in range(len(stringx)-1,index_awal,-1):
        if(stringx[i] != " "):
            break
        else:
            index_akhir -= 1
    # mengembalikan string yang sudah bersih
    hasil = ""
    for i in range(index_awal,index_akhir):
        hasil += stringx[i]
    return hasil

# function string_append(array : array [0..length-1] of string, stringx : string, length : integer) -> array [0..length] of string
# Menambahkan string ke dalam array of string
def string_append(array: list[str], stringx: str, length: int) -> list[str]:
    # KAMUS LOKAL
        # i : integer
        # array_baru : array [0..length] of string
    # ALGORITMA
    array_baru = ["" for _ in range(length+1)]
    for i in range(length):
        array_baru[i] = array[i]
    array_baru[length] = stringx
    return array_baru

# function string_in_array(array : array [0..array_length-1] of string, stringx : string, array_length : integer) -> integer
# mengecek apakah string terdapat pada array jika iya maka mengembalikan indexnya jika tidak mditemukan mengembalikan nilai -1
def string_in_array(array : list[str], stringx: str, array_length: int) -> int:
    # KAMUS LOKAL
        # i : integer
    # ALGORTIMA
    for i in range(array_length):
        if(array[i] == stringx):
            return i
    return -1

# function string_leksikografis_min(array : array [0..length-1] of string, length : integer) -> string
# Menentukan string terkecil berdasarkan leksikografis
def string_leksikografis_min(array: list[str], length: int) -> str:
    # KAMUS LOKAL
        # i : integer
        # min : string
    # ALGORITMA
    min = array[0]
    for i in range(length):
        if(array[i] < min):
            min = array[i]
    return min

# function string_leksikografis_maks(array : array [0..length-1] of string, length : integer) -> string
# Menentukan string tertinggi berdasarkan leksikografis
def string_leksikografis_maks(array: list[str], length: int) -> str:
    # KAMUS LOKAL
        # i : int
        # maks : str
    # ALGORITMA
    maks = array[0]
    for i in range(length):
        if(array[i] > maks):
            maks = array[i]
    return maks

# FUNGSI REKURSIF    
# function int_min(array : array [0..length-1] of string, length : integer, index_sekarang : integer = 0,  min : integer = 999999 ) -> integer
# Program ini untuk mengembalikan nilai terkecil pada array integer, asumsi nilai maksimum tertinggi adalah 999999 
def int_min(array: list[int], length: int, index_sekarang: int = 0, min: int = 999999) -> int:
    # KAMUS LOKAL
        # min, length: integer
    # ALGORITMA
    if(array[index_sekarang] < min):
        min = array[index_sekarang]
    if(index_sekarang == length-1):
        return min
    else:
        return int_min(array, length, index_sekarang+1, min)

# function int_maks(array : array [0..length-1] of string, length : integer) -> integer
# Mengembalikan nilai terbesar pada array integer
def int_maks(array: list[int], length: int) -> int:
    # KAMUS LOKAL
        # maks, i : integer
    # ALGORITMA
    maks = array[0]
    for i in range(length):
        if(array[i] > maks):
            maks = array[i]
    return maks

# function int_join(array1 : array [0..length-1] of integer, array2 : array [0..length-1] of integer, length : integer) -> integer
# Menjumlahkan tiap index pada dua array integer yang sama ukuran
def int_join(array1: list[int],array2: list[int], length: int,) -> list[int]:
    # KAMUS LOKAL
        # i : integer
        # array_hasil : array [0..length-1] of integer
    # ALGORITMA
    array_hasil = [0 for _ in range(length)]
    for i in range(length):
        array_hasil[i] = array1[i] + array2[i]
    return array_hasil

# function Data_append(data : Data, elemen: array[0..data.n_kolom-1] of string)
# Menambahkan suatu elemen ke dalam array, Asumsi tipe array dan elemen pasti sama
def data_append(data: Data, elemen: list[str]) -> Data:
    # KAMUS LOKAL
        # n_baris, i : integer
        # hasil : array [0..n_baris) of string
        # isi_data : array [0..data.n_baris-1] of array [0..data.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_data = data.isi
    n_baris = data.n_baris
    hasil = ["" for _ in range(n_baris+1)]
    for i in range(n_baris):
        hasil[i] = isi_data[i]
    # meletakan elemen yang dimasukkan pada ujung matriks hasil
    hasil[n_baris] = elemen 
    data.isi = hasil  
    data.n_baris += 1
    return data

# Fungsi data_remove(data,index)
# Menghapuskan data pada index yang diberikan
def data_remove(data: Data, index: int) -> Data:
    # KAMUS LOKAL
        # n_baris, n_kolom, i : integer
        # data_baru : array [0..n_baris-2] of array [0..n_kolom-1] of string
        # isi_data : array [0..n_baris-1] of array [0..n_kolom-1] of string
    # ALGORTIMA
    # unpack data
    isi_data = data.isi
    n_baris = data.n_baris
    n_kolom = data.n_kolom
    data_baru = [["" for _ in range(n_kolom)] for _ in range(n_baris-1)]
    # menambahkan semua data selain data pada index yang diberikan
    for i in range(index):
        data_baru[i] = isi_data[i]
    for i in range(index+1,n_baris):
        data_baru[i-1] = isi_data[i]
    data.isi = data_baru
    data.n_baris -= 1
    return data

# Fungsi cari_index_username(users,username)
# Mencari username pada data users, jika tidak ditemukan maka mengembalikan -1, jika ditemukan maka mengembalikan index
def cari_index_username(users: Data, username: str) -> int:
    # KAMUS LOKAL
        # n_baris_users, i : integer
        # isi_data : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    n_baris_users = users.n_baris
    for i in range(n_baris_users):
        if(username == isi_users[i][0]): # username ditemukan
            return i
    return -1

# Fungsi cari_index_candi(candi, pembuat)
# Mencari semua indeks candi yang dibuat oleh jin_pembuat
def cari_index_candi(candi: Data, jin_pembuat: str) -> list[list[int],int]:
    # KAMUS LOKAL
        # n_baris_candi, i, count_candi : integer
        # indexs : array [0..count_candi-1] of integer
        # isi_candi : array [0..candi.n_baris-1] of array [0..candi.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    # hitung jumlah candi yang telah dibuat oleh jin_pembuat
    count_candi = 0
    for i in range(n_baris_candi):
        if(isi_candi[i][1] == jin_pembuat):
            count_candi += 1
    # mencari semua indeks candi yang telah dibuat oleh jin_pembuat
    indexs = [0 for _ in range(count_candi)]
    j = 0
    for i in range(n_baris_candi):
        if(isi_candi[i][1] == jin_pembuat):
            indexs[j] = i
            j += 1
    return [indexs,count_candi]

# Fungsi matrix_string_join(array, matriks, n_baris_matriks, n_kolom_matriks)
# Menggabungkan array of string ke dalam matrix of string
def matrix_str_join(array: list[str], matriks: list[list[str]], n_baris: int, n_kolom: int) -> list[list[str]]:
    # KAMUS LOKAL
        # i : integer
        # hasil : array [0..n_baris] of array [0..n_kolom-1] of string
    # ALGORITMA
    hasil = [["" for _ in range(n_kolom)] for _ in range(n_baris+1)]
    for i in range(n_baris):
        hasil[i] = matriks[i]
    hasil[n_baris] = array
    return hasil

# Prosedur candi_append(candi, array)
# Menambahkan data pembangun suatu candi ke dalam data Candi secara terurut dan mengisi index yang kosong
def candi_append(candi: Data, array: list[str]) -> None:
    # KAMUS LOKAL
        # n_baris_candi, n_kolom_candi, i, index: integer
        # isi_candi : array [0..candi.n_baris-1] of array [0..candi.n_kolom-1] of string
        # isi_candi_baru : array [0..candi.n_baris] of array [0..candi.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    n_kolom_candi = candi.n_kolom
    # mencari apakah seluruh index sudah terisi atau belum
    index = -1
    for i in range(n_baris_candi):
        if(isi_candi[i][0] != str(i+1)):
            index = i
            break
    if(index == -1): # seluruh index terisi
        candi = data_append(candi,[str(n_baris_candi+1),array[0],array[1],array[2],array[3]])
    else: # ada index yang belum terisi maka isi pada index tersebut
        isi_candi_baru = [["" for _ in range(n_kolom_candi)] for _ in range(n_baris_candi+1)]
        for i in range(0,index):
            isi_candi_baru[i] = isi_candi[i]
        for i in range(index+1,n_baris_candi+1):
            isi_candi_baru[i] = isi_candi[i-1]
        isi_candi_baru[index] = [str(index+1),array[0],array[1],array[2],array[3]]
        candi.isi = isi_candi_baru
        candi.n_baris += 1
    
# Fungsi generate_bahan_bangunan()
# Mengembalikan bahan bangunan yang sudah random
from numgen import randomize # import fungsi untuk angka random
def generate_bahan_bangunan() -> list[int]:
    # KAMUS LOKAL
        # pasir, batu, air : integer
    # ALGORITMA
    pasir = randomize(1,5)
    batu = randomize(1,5)
    air = randomize(1,5)
    return [pasir, batu, air]
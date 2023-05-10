# Modul data
# Berisi fungsi yang dapat membuat / mengakses file

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

# import fungsi bantuan
from tools import string_split, string_slice

# Fungsi load(path)
# Membaca data csv di lokasi "path" dan mengembalikan data dalam format [isi_data, n_baris, n_kolom] 
def data_load(path: str) -> Data:
    # KAMUS LOKAL
        # n_baris, n_kolom, i : integer
        # line : string
        # cek_kolom, first_row : boolean
        # file : array [0..len(file)-1] of string
        # data : Data
    # ALGORITMA
    # Mencari jumlah efektif data
    file = open(path, "r").readlines()
    n_baris = -1 # -1 karena anggap baris pertama (judul) tidak dimasukkan
    n_kolom = 1 # 1 karena pasti kolom berisi satu
    cek_kolom = True
    for line in file:
        n_baris += 1
        if(cek_kolom):
            # penghitungan jumlah kolom hanya perlu dilakukan sekali 
            cek_kolom = False
            for i in range(len(line)):
                if(line[i] == ";"):
                    n_kolom += 1
    # Pengambilan data
    data = Data([["" for _ in range(n_kolom)] for _ in range(n_baris)],n_baris,n_kolom)
    # pembukaan ulang file agar dapat terbaca lagi
    file = open(path, "r")
    i = 0
    first_row = True
    for line in file:
        if(first_row == False): # agar judul csv tidak masuk data contoh (username;password;role)
            # line dilakukan slicing agar new line hilang (\n) kecuali pada baris terkahir
            if(i != n_baris-1):
                data.isi[i] = string_split(string_slice(line,0,len(line)-1),";")
            else:
                data.isi[i] = string_split(line,";")
            i += 1
        else:
            first_row = False
    file.close()
    return data

# Fungsi save(path, nama_file, data)
# Membaca data csv di lokasi "path" dan mengembalikan [data, jumlah_baris, jumlah_kolom], data dalam bentuk matriks 
def data_save(path: str, nama_file: str, data: Data) -> None:
    # KAMUS LOKAL
        # n_baris, n_kolom, i, j : integer
        # line : string
        # file : array [0..len(file)-1] of string
        # isi_data : matriks of string
    # ALGORITMA
    file = open(path+"/"+nama_file+".csv","w+")
    isi_data = data.isi
    n_baris = data.n_baris
    n_kolom = data.n_kolom
    # Tulis ulang label/ baris 1
    if(nama_file == "user"):
        file.write("username;password;role\n")
    elif(nama_file == "candi"):
        file.write("id;pembuat;pasir;batu;air\n")
    elif(nama_file == "bahan_bangunan"):
        file.write("nama;deskripsi;jumlah\n")
    for i in range(n_baris):
        line = ""
        for j in range(n_kolom):
            line += isi_data[i][j]
            if(j != n_kolom-1):
                line += ";"
        if(i != n_baris-1):
            line += "\n"
        file.write(line)
    file.close()
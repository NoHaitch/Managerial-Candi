# Program main
# Program utama Manajerial Candi
# KAMUS
    # type Data : < isi : array [0..n_baris-1] of array [0..n_kolom-1] of string,
    #               n_baris : integer,
    #               n_kolom : integer  >
    # masukkan : string
    # semua_data : array[0..2] of Data
    # users, candi, bahan_bangunan : Data

# ALGORITMA
# import modul commands yang berisi semua fungsi dan procedure utama
import commands 
semua_data = commands.load() # load data
if(semua_data != []): # load berhasil
    users = semua_data[0]
    candi = semua_data[1]
    bahan_bangunan = semua_data[2] 
    while True:
        masukan = input(">>> ")
        commands.run(masukan,users,candi,bahan_bangunan)
        # commands.run adalah fungsi yang menghubungkan input user dengan fungsi dan procedur utama
        print()

# KETERANGAN :
    # UNTUK MENJALANKAN PROGRAM, KETIK PADA TERMINAL/CONSOLE :
    # python main.py nama_folder 
    # cth: python main.py abcde

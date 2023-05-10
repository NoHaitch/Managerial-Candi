# Modul Commands
# Berisi semua fungsi/prosedur untuk command-command yang dapat digunakan

# KAMUS
    # type Data : < isi : array [0..n_baris-1] of array [0..n_kolom-1] of string,
    #               n_baris : integer,
    #               n_kolom : integer  >
    # const undo_maks : integer = 100
    # undo_jin : array [0..(2*undo_maks)-1] of array [0..3] of string
    # undo_candi : array [0..(10*undo_maks)-1] of array [0..3] of string
    # current_login : array [0..2] of string

# ALGORITMA
# import modul dan fungsi buatan
import os
from tools import cari_index_username, data_remove, data_append, int_min, int_maks, int_join, generate_bahan_bangunan
from tools import string_split, string_strip, string_append, string_in_array, string_leksikografis_min, string_leksikografis_maks
from tools import cari_index_candi, matrix_str_join, candi_append
from data import data_save, data_load, Data

# deklarasi variabel
current_login = ["", "", ""]
undo_maks = 100
undo_jin = [["", "", "", ""] for _ in range(2 * undo_maks)]
undo_candi = [["", "", "", ""] for _ in range(10 * undo_maks)]

# procedure run (input command: string, input/output users: Data, input/output candi: Data, nput/output bahan_bangunan : Data)
# Membaca masukkan dari user dan menjalankan command tersebut berdasarkan akun login saat ini
def run(command: str, users: Data, candi: Data ,bahan_bangunan: Data) -> None:
    print(bahan_bangunan.isi)
    # KAMUS LOKAL
        # length : integer
        # command_list : array [0..length-1] of string
    # ALGORITMA
    command = string_strip(command) # Agar command bersih dari spasi kosong
    global current_login
    if(command == "login"):
        current_login = login(current_login, users)
    elif(command == "logout"):
        current_login = logout(current_login)
    elif(command == "help"):
        help(current_login)
    elif(command == "exit"):
        exit(users, candi, bahan_bangunan)
    elif(command == "save"):
        save(users, candi, bahan_bangunan)
    elif(current_login == ["" for _ in range(3)]):
        command_list = ["logout","summonjin","hapusjin","ubahjin","bangun","kumpul","batchkumpul","batchbangun","laporanjin","laporancandi","hancurkancandi","ayamberkokok","undohapus"]
        length = 13
        if(any(command == command_list[i] for i in range(length))):
            print(f"{command} gagal!")
            print("Anda perlu login terlebih dahulu!")
        else:
            print(f"command \"{command}\" tidak dikenal.")
    else:
        if(command == "summonjin"):
            if(current_login[2] == "bandung_bondowoso"):
                summonjin(users)
            else:
                print("summonjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "hapusjin"):
            if(current_login[2] == "bandung_bondowoso"):
                hapusjin(users,candi, undo_jin, undo_candi)
            else:
                print("hapusjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "undohapus"):
            if(current_login[2] == "bandung_bondowoso"):
                undohapus(users,candi, undo_jin, undo_candi)
            else:
                print("undo hapus hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "ubahjin"):
            if(current_login[2] == "bandung_bondowoso"):
                ubahjin(users)
            else:
                print("Ubahjin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "bangun"):
            if(current_login[2] == "jin_pembangun"):
                bangun(candi,bahan_bangunan,[current_login[0]],1,1,False)
            else:
                print("bangun hanya dapat diakses oleh akun Jin Pembangun")
        elif(command == "kumpul"):
            if(current_login[2] == "jin_pengumpul"):
                kumpul(bahan_bangunan,1,False)
            else:
                print("kumpul hanya dapat diakses oleh akun Jin Pengumpul")
        elif(command == "batchkumpul"):
            if(current_login[2] == "bandung_bondowoso"):
                batchkumpul(users,bahan_bangunan)
            else:
                print("Batch kumpul hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "batchbangun"):
            if(current_login[2] == "bandung_bondowoso"):
                batchbangun(users,candi,bahan_bangunan)
            else:
                print("Batch bangun hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "laporanjin"):
            if(current_login[2] == "bandung_bondowoso"):
                laporanjin(users,candi,bahan_bangunan)
            else:
                print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "laporancandi"):
            if(current_login[2] == "bandung_bondowoso"):
                laporancandi(candi)
            else:
                print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        elif(command == "hancurkancandi"):
            if(current_login[2] == "roro_jonggrang"):
                hancurkancandi(candi)
            else:
                print("Hancurkan candi hanya dapat diakses oleh akun Roro Jonggrang.")
        elif(command == "ayamberkokok"):
            if(current_login[2] == "roro_jonggrang"):
                ayamberkokok(candi)
            else:
                print("Ayamberkokok hanya dapat diakses oleh akun Roro Jonggrang.")
        else:
            print(f"command \"{command}\" tidak dikenal.")

# F01 - Login 
# function login(current_login: array [0..2] of string, users: Data ) -> array [0..2] of string
# Melakukan aksi login dan mengembalikan data hasil login yaitu array string [username,password,role]
def login(current_login: list[str], users: Data) -> list[str]: 
    # KAMUS LOKAL
        # index : integer
        # username, password : string
        # isi_users : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string
    # ALGORITMA
    # Cek apakah sudah login atau belum
    if(current_login != ["", "", ""]):
        print("Login gagal!")
        print(f"Anda telah login dengan username {current_login[0]}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
        return current_login
    else:
        # unpack data users
        isi_users = users.isi
        # Input data login (sudah dibersihkan dari spasi awal dan akhir)
        username = input("Username: ")
        password = input("Password: ")
        # mencari index username, jika tidak ditemukan maka bernilai -1
        index = cari_index_username(users,username)
        if(index != -1): # username ditemukan 
            # cek apakah password sesuai atau tidak
            if(password == isi_users[index][1]):
                print(f"Selamat datang, {username}!")
                print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")
                return isi_users[index]
            else: # password salah
                print("Password salah!")
                return ["", "", ""]
        else:
            print("Username tidak terdaftar!")
            return ["", "", ""]

# F02 - Logout 
# function logout(current_login: array [0..2] of string) -> array [0..2] of string
# Melakukan logout akun dengan cara mengosongkan data current_login
def logout(current_login: list[str]) -> list[str]:
    # KAMUS LOKAL
        # current_login : array [0..2] of string
    # ALGORITMA
    if(current_login == ["", "", ""]):
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return current_login
    else: # sudah login
        print("Logout berhasil! ")
        return ["", "", ""]

# F03 - Summon Jin
# procedure summonjin(input/output users: Data)
# Mensummon / membuat jin baru
def summonjin(users: Data) -> None:
    # KAMUS LOKAL
       # n_baris, i : integer
        # jenis_jin, username, password, role : string
        # username_valid : boolean
        # isi_users : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string 
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    n_baris = users.n_baris
    if(users.n_baris == 102): # 102 terdiri dari 100 jin, 1 Bandung bondowoso, 1 Roro Jonggrang
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
    else: # karena jumlah jin < 100
        print("Jenis jin yang dapat dipanggil:")
        print("  (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("  (2) Pembangun - Bertugas membangun candi")
        # menentukan jenis jin (pengumpul atau pembangun)
        while True:
            jenis_jin = string_strip(input("\nMasukkan nomor jenis jin yang ingin dipanggil: "))
            print()
            if(jenis_jin == "1"):
                role = "jin_pengumpul"
                print("Memilih jin \"Pengumpul\".")
                break
            elif(jenis_jin == "2"):
                role = "jin_pembangun"
                print("Memilih jin \"Pembangun\".")
                break
            else:
                print(f"Tidak ada jenis jin bernomor \"{jenis_jin}\"!")
        # membuat username yang valid
        while True:
            # ASUMSI : username alphanumeric (hanya terdiri dari angka dan huruf)
            username = input("\nMasukkan username jin: ") 
            if(username[0] == " "):
                print("Username tidak boleh dimulai dengan spasi (\" \")")
                continue
            username_valid = True
            # menentukan apakah username sudah diambil atau belum
            for i in range(n_baris):
                if(isi_users[i][0] == username):
                    print(f"\nUsername \"{username}\" sudah diambil!")
                    username_valid = False
                    break
            if(username_valid):
                break
        # membuat password yang valid
        while True:
            password = input("Masukkan password jin: ")
            if(5<=len(password)<=25):
                print()
                break
            else:
                print("\nPassword panjangnya harus 5-25 karakter!")
            print()
        # menambahkan data jin
        users = data_append(users,[username,password,role])
        print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
        print(f"\nJin {username} berhasil dipanggil!")

# F04 - Hilangkan Jin
# procedure hapusjin (input/output users: Data, 
#                     input/output candi: Data, 
#                     input/output undo_jin: array[0..2*undo_maks] of array[0..3] of string,
#                     input/output undo_candi: array[0..10*undo_maks] of array[0..3] of string )
# Menghapus jin serta candi yang dibuatnya
def hapusjin(users: Data, candi: Data, undo_jin: list[list[str]], undo_candi: list[list[str]]) -> None:
    # ASUMSI :
        # dalam satu permainan tidak mungkin menghapus lebih dari 2*undo_maks jin
        # dalam satu permainan tidak mungkin menghapus lebih dari 10*undo_maks candi
    # KAMUS LOKAL
        # n_baris_candi, count_candi_hapus, i, j, index : integer
        # username, jawab : string
        # candi_dihapuskan : < isi : array[0..length-1] of integer, length: integer >
        # isi_candi : array [0..candi.n_baris-1] of array [0..candi.n_kolom-1] of string
    # ALGORITMA
    # input username
    username = input("Masukkan username jin : ")
    # cek username, jika tidak ditemukan maka index bernilai -1 jika ditemukan maka index bernilai posisi index ditemukannya username
    index = cari_index_username(users,username)
    if(index == -1):
        print("Tidak ada jin dengan username tersebut.")
    else:
        jawab = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if(jawab == "Y"): # jin dihapuskan
            # menghapuskan candi yang dibuat oleh jin tersebut
            candi_dihapuskan = cari_index_candi(candi,username)
            count_candi_hapus = candi_dihapuskan[1]
            # menyimpan data candi-candi yang akan dihapus
            for i in range(count_candi_hapus-1,-1,-1):
                for j in range(10*undo_maks):
                    if(undo_candi[j][0] == ""):
                        undo_candi[j] = [candi.isi[candi_dihapuskan[0][i]][1],candi.isi[candi_dihapuskan[0][i]][2],candi.isi[candi_dihapuskan[0][i]][3],candi.isi[candi_dihapuskan[0][i]][4]]
                        break
            # menghapus candi-candi
            for i in range(count_candi_hapus):
                candi = data_remove(candi,candi_dihapuskan[0][i]-i)
            # menyimpan data jin yang akan dihapus
            for i in range(2*undo_maks):
                if(undo_jin[i][0] == ""):
                    undo_jin[i] = string_append(users.isi[index],str(count_candi_hapus),3)
                    break
            # menghapus data jin yang dihapus
            users = data_remove(users,index)
            print("\nJin telah berhasil dihapus dari alam gaib.")
        elif(jawab != "N"): 
            print(f"Tidak ada opsi \"{jawab}\". Ulangi!")
            hapusjin(users,candi)            

# B04 - Undo hapus jin
# procedure undohapus(input/output users: Data,
#                    input/output candi: Data,
#                    input/output undo_jin: array [0..(2*undo_maks)-1] of array [0..3] of string,
#                    input/output undo_candi: array [0..(10*undo_maks)-1] of array [0..3] of string )
# Mengembalikan keadaan jin serta candi hasil bangunnya yang telah dihapus
def undohapus(users : Data, candi: Data, undo_jin: list[list[str]], undo_candi: list[list[str]])-> None:
    # ASUMSI :
        # dalam satu permainan tidak mungkin menghapus lebih dari 2*undo_maks jin
        # dalam satu permainan tidak mungkin menghapus lebih dari 10*undo_maks candi
        # undo_jin dan undo_candi berkonsep stack
    # KAMUS LOKAL
        # i, j, count_undo_candi : integer
        # username : string
    # ALGORITMA
    if(undo_jin[0] == ["","","",""]):
        print("Undo gagal!")
        print("Tidak ada jin yang sudah dihapus")
    else:
        for i in range((2 * undo_maks)-1, -1, -1): # mengecek dari ujung matriks undo_jin untuk data yang terisi
            if(undo_jin[i][0] != ""): # ditemukan data paling terakhir dimasukkan
                count_undo_candi = int(undo_jin[i][3])
                username = undo_jin[i][0]
                users = data_append(users,[undo_jin[i][0],undo_jin[i][1],undo_jin[i][2]]) 
                undo_jin[i] = ["", "", "", ""] # karena sudah diundo maka data user dihapus dari matrix penyimpan
                break
        for i in range(count_undo_candi): # jumlah candi yang perlu di undo
            for j in range((10 * undo_maks)-1, -1, -1): # mengecek dari ujung matriks undo_candi untuk data yang terisi
                if(undo_candi[j][0] != ""):
                    candi_append(candi, undo_candi[j])
                    undo_candi[j] = ["", "", "", ""] # karena sudah diundo maka data candi dihapus dari matrix penyimpan
                    break
        print("Undo berhasil!")
        print(f"Jin \"{username}\" sudah kembali dengan {count_undo_candi} candi")

# F05 - Ubah Tipe Jin
# procedure ubahjin ( input/output users: Data )
# Mengubah role dari jin, jika role pembangun maka dapat diubah ke pengumpul dan sebaliknya
def ubahjin(users: Data) -> None:
    # KAMUS LOKAL
        # n_baris, i, index : integer
        # username, ubah: string
        # ditemukan : boolean
        # isi_users : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string
    # ALGORITMA
    # unpack data 
    isi_users = users.isi
    # input user
    username = input("Masukkan username jin: ")
    # Cari username jika ditemukan maka mengembalikan indexnya jika tidak ditemukan maka bernilai -1
    index = cari_index_username(users,username)
    if(index != -1): # username ditemukan
        if(isi_users[index][2] == "jin_pengumpul"): # role pengumpul menjadi pembangun
            ubah = input("Jin ini bertipe \"Pengumpul\". Yakin ingin mengubah ke tipe \"Pembangun\" (Y/N)? ")
            if(ubah == "Y"):
                isi_users[index][2] = "jin_pembangun"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
        else: # role pembangun menjadi pengumpul
            ubah = input("Jin ini bertipe \"Pembangun\". Yakin ingin mengubah ke tipe \"Pengumpul\" (Y/N)? ")
            if(ubah == "Y"):
                isi_users[index][2] = "jin_pengumpul"
                print("Jin telah berhasil diubah.")
            else:
                print("Jin tidak diubah.")
    else: # username tidak ditemukan
        print("\nTidak ada jin dengan username tersebut.")
    users.isi = isi_users

# F06 - Jin Pembangun .... REKURSIF!!
# function bangun (candi : Data, bahan_bangunan : Data, jin_pembangun : array [0..length-1] of string, 
#                  length : integer, jumlah_loop : integer, bangun_batch : boolean ) 
#                  -> array [0..length-1] of array [0..3] of string 
# Membangun candi, jika jumlah jin_pembangun > 1 maka pembangunan dilakukan secara rekursif
def bangun(candi: Data, bahan_bangunan: Data, jin_pembangun: list[str], length: int, jumlah_loop :int, bangun_batch: bool) -> list[list[str]]:
    # KAMUS LOKAL
        # n_baris_candi : integer
        # bahan_dimiliki, bahan_diperlukan : array[0..2] of integer
        # data_hasil : array[0..3] of string
        # isi_bahan_bangunan : array [0..bahan_bangunan.n_baris-1] of array [0..bahan_bangunan.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_bahan_bangunan = bahan_bangunan.isi 
    n_baris_candi = candi.n_baris
    # bahan dalam format [pasir,batu,air]
    bahan_dimiliki = [int(isi_bahan_bangunan[0][2]),int(isi_bahan_bangunan[1][2]),int(isi_bahan_bangunan[2][2])]
    bahan_diperlukan = generate_bahan_bangunan()
    data_hasil = [jin_pembangun[length-jumlah_loop],str(bahan_diperlukan[0]),str(bahan_diperlukan[1]),str(bahan_diperlukan[2])]
    if(bangun_batch == False): # bangun 1 candi saja
        if(bahan_dimiliki[0] < bahan_diperlukan[0] or bahan_dimiliki[1] < bahan_diperlukan[1] or bahan_dimiliki[2] < bahan_diperlukan[2]):
            # candi tidak dibangun
            print(f"# Men-generate bahan bangunan ({bahan_diperlukan[0]} pasir, {bahan_diperlukan[1]} batu, dan {bahan_diperlukan[2]} air)")
            print(f"# Memiliki {bahan_dimiliki[0]} pasir, {bahan_dimiliki[1]} batu, {bahan_dimiliki[2]} air")
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
        else: # candi dibangun
            # Mengurangi bahan bangunan yang dimiliki
            isi_bahan_bangunan[0][2] = str(int(isi_bahan_bangunan[0][2]) - bahan_diperlukan[0])
            isi_bahan_bangunan[1][2] = str(int(isi_bahan_bangunan[1][2]) - bahan_diperlukan[1])
            isi_bahan_bangunan[2][2] = str(int(isi_bahan_bangunan[2][2]) - bahan_diperlukan[2])
            bahan_bangunan.isi = isi_bahan_bangunan 
            if(n_baris_candi < 100): 
                candi_append(candi, data_hasil)
                print("Candi berhasil dibangun.")
                print(f"Sisa candi yang perlu dibangun: {100-n_baris_candi}")
            else:
                print("Candi berhasil dibangun.")
                print("Sisa candi yang perlu dibangun: 0")
    elif(jumlah_loop != 1): # karena jumlah_loop > 1 maka perlu rekursif (sebab batch_bangun)
        #return matrix_string_join(data_hasil,bangun(candi,bahan_bangunan,jin_pembangun,length,jumlah_loop-1,True),jumlah_loop,4)
        return matrix_str_join(data_hasil,bangun(candi,bahan_bangunan,jin_pembangun,length,jumlah_loop-1,True),jumlah_loop-1,4)
    else: # karena sudah loop terakhir maka rekursif dan berhenti
        return [data_hasil]

# F07 - Jin Pengumpul ....  REKURSIF!!
# function kumpul (bahan_bangunan : Data, jumlah_loop : integer, kumpul_batch : boolean )-> array [0..2] of string
# Mengumpulkan bahan bangunan yang jumlahnya secara acak, untuk batch kumpul dilakukan dengan rekursif
def kumpul(bahan_bangunan: Data, jumlah_loop: int, kumpul_batch: bool) -> list[int]:
    # KAMUS LOKAL
        # bahan_dikumpul : array[0..2] of integer
        # isi_bahan_bangunan : array [0..bahan_bangunan.n_baris-1] of array [0..bahan_bangunan.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_bahan_bangunan = bahan_bangunan.isi
    # menentukan jumlah bahan yang dikumpul (acak)
    # bahan_dikumpul dalam format [pasir, batu, air]
    bahan_dikumpul = generate_bahan_bangunan()
    # menambahkan bahan bangunan yang dikumpul ke bahan bangunan total
    isi_bahan_bangunan[0][2] = str(int(isi_bahan_bangunan[0][2]) + bahan_dikumpul[0])
    isi_bahan_bangunan[1][2] = str(int(isi_bahan_bangunan[1][2]) + bahan_dikumpul[1])
    isi_bahan_bangunan[2][2] = str(int(isi_bahan_bangunan[2][2]) + bahan_dikumpul[2])
    bahan_bangunan.isi = isi_bahan_bangunan
    if(kumpul_batch == False): # jika bukan batch kumpul maka tidak perlu diprint
        print(f"Jin menemukan {bahan_dikumpul[0]} pasir, {bahan_dikumpul[1]} batu, dan {bahan_dikumpul[2]} air.")
    elif(jumlah_loop != 1): # jika kumpul_batch = True, jika jumlah_loop yang perlu dilakukan lebih dari 1 maka perlu rekursif
        return int_join(bahan_dikumpul,kumpul(bahan_bangunan,jumlah_loop-1,True),3)
    else: # jika jumlah_loop = 1 maka rekursif berhenti
        return bahan_dikumpul

# F08 - Batch Kumpul
# procedure batchkumpul(input users: Data, input/output bahan_bangunan: Data )
# Melakukan pengumpulan bahan bangunan oleh semua jin pengumpul yang ada 
def batchkumpul(users: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # i, n_baris_users, count_jin_pengumpul : integer
        # hasil_kumpul : array[0..2] of integer
        # isi_users : array [0..users .n_baris-1] of array [0..users.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    n_baris_users = users.n_baris
    # Hitung jumlah jin pengumpul
    count_jin_pengumpul = 0
    for i in range(n_baris_users):
        if(isi_users[i][2] == "jin_pengumpul"):
            count_jin_pengumpul += 1
    if(count_jin_pengumpul == 0): # tidak ada jin pengumpul
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Sialhkan summon terlebih dahulu.")
    else: # ada jin pengumpul
        print(f"Mengerahkan {count_jin_pengumpul} jin untuk mengumpulkan bahan.")
        # mengumpulkan bahan
        hasil_kumpul = kumpul(bahan_bangunan,count_jin_pengumpul,True)
        print(f"Jin menemukan total {hasil_kumpul[0]} pasir, {hasil_kumpul[1]} batu, dan {hasil_kumpul[2]} air.")

# F08 - Batch Bangun    
# procedure batchbangun(input users: Data, input/output candi: Data, input/output bahan_bangunan: Data )
# Melakukan pembangunan candi oleh setiap jin pembangun yang ada
def batchbangun(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # i, index, n_baris_users, count_jin_pembangun, total_pasir, total_batu, total_air, kurang_pasir, kurang_batu, kurang_air : integer
        # bahan_dimiliki : array[0..2] of integer
        # jin_pembangun : array[0..count_jin_pembangun-1] of string
        # isi_users : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string
        # isi_bahan_bangunan : array [0..bahan_bangunan.n_baris-1] of array [0..bahan_bangunan.n_kolom-1] of string
        # data_pembangunan : array [0..count_jin_pembangun-1] of array [0..3] of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    isi_bahan_bangunan = bahan_bangunan.isi
    n_baris_users = users.n_baris
    bahan_dimiliki = [int(isi_bahan_bangunan[0][2]),int(isi_bahan_bangunan[1][2]),int(isi_bahan_bangunan[2][2])]
    # Hitung jumlah jin pembangun
    count_jin_pembangun = 0
    for i in range(n_baris_users):
        if(isi_users[i][2] == "jin_pembangun"):
            count_jin_pembangun += 1
    if(count_jin_pembangun == 0): # tidak ada jin pembangun
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else: # ada jin pembangun
        # Mengumpulkan nama semua jin pembangun
        jin_pembangun = ["" for _ in range(count_jin_pembangun)]
        index = 0
        for i in range(n_baris_users):
            if(isi_users[i][2] == "jin_pembangun"):
                jin_pembangun[index] = isi_users[i][0]
                index += 1
        # Menghitung jumlah candi yang sudah dibangun
        data_pembangunan = bangun(candi,bahan_bangunan,jin_pembangun,count_jin_pembangun,count_jin_pembangun,True)
        total_pasir = 0
        total_batu = 0
        total_air = 0
        for i in range(count_jin_pembangun):
            total_pasir += int(data_pembangunan[i][1])
            total_batu += int(data_pembangunan[i][2])
            total_air += int(data_pembangunan[i][3])
        print(f"Mengerahkan {count_jin_pembangun} jin untuk membangun candi dengan total bahan {total_pasir} pasir, {total_batu} batu, dan {total_air} air.")
        # Mengecek apakah bahan yang dimiliki kurang atau cukup untuk bangun candi-candi
        if(total_pasir > bahan_dimiliki[0] or total_batu > bahan_dimiliki[1] or total_air > bahan_dimiliki[2]):
            kurang_pasir = 0
            kurang_batu = 0
            kurang_air = 0
            if(total_pasir > bahan_dimiliki[0]):
                kurang_pasir = total_pasir - bahan_dimiliki[0]
                print(f"{kurang_pasir} pasir",end="")
            if(total_batu > bahan_dimiliki[1]):
                kurang_batu = total_batu - bahan_dimiliki[1]
            if(total_batu > bahan_dimiliki[2]):
                kurang_air = total_air - bahan_dimiliki[2]
            if(kurang_pasir != 0 and kurang_batu != 0 and kurang_air !=0):
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir, {kurang_batu} batu, dan {kurang_air} air.")
            elif(kurang_pasir != 0 and kurang_batu != 0):
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_batu} batu.")
            elif(kurang_pasir != 0 and kurang_air != 0):
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir dan {kurang_air} air.")
            elif(kurang_batu != 0 and kurang_air != 0):
                print(f"Bangun gagal. Kurang {kurang_batu} batu dan {kurang_air} air.")
            elif(kurang_pasir != 0):
                print(f"Bangun gagal. Kurang {kurang_pasir} pasir.")
            elif(kurang_batu != 0):
                print(f"Bangun gagal. Kurang {kurang_batu} batu.")
            else: # kurang_air != 0
                print(f"Bangun gagal. Kurang {kurang_air} air.")
        else: # bahan bangunan memenuhi bahan yang diperlukan untuk membangun
            isi_bahan_bangunan[0][2] = str(int(isi_bahan_bangunan[0][2]) - total_pasir)
            isi_bahan_bangunan[1][2] = str(int(isi_bahan_bangunan[1][2]) - total_batu)
            isi_bahan_bangunan[2][2] = str(int(isi_bahan_bangunan[2][2]) - total_air)
            bahan_bangunan.isi = isi_bahan_bangunan
            for i in range(count_jin_pembangun):
                if(candi.n_baris < 100):
                    candi_append(candi, data_pembangunan[i])
            print(f"Jin berhasil membangun total {count_jin_pembangun} candi.")

# F09 - Laporan Jin
# procedure laporanjin (input users: Data, input candi: Data, input bahan_bangunan: Data)
# Melakukan laporan jin mulai dari total jin masing-masing jenis, jin termalas dan terajin serta bahan bangunan
def laporanjin(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # n_baris_users, n_baris_candi, total_jin, total_pengumpul, total_pembangun, i, index, n_jin, count_maks, count_min, candi_maks candi_min, index_jin_maks, index_jin_min  : integer
        # count_candi_jin : array [0..n_jin-1] of integer
        # jin_maks : array [0..count_maks-1] of string 
        # jin min : array [0..count_min-1] of string 
        # jin : array [0..total_pembangun-1] of string
        # isi_users : array [0..users.n_baris-1] of array [0..users.n_kolom-1] of string
        # isi_bahan_bangunan : array [0..bahan_bangunan.n_baris-1] of array [0..bahan_bangunan.n_kolom-1] of string
        # data_pembangunan : array [0..count_jin_pembangun-1] of array [0..3] of string
    # ALGORITMA
    # unpack data
    isi_users = users.isi
    isi_candi = candi.isi
    isi_bahan_bangunan = bahan_bangunan.isi
    n_baris_users = users.n_baris
    n_baris_candi = candi.n_baris
    # menentukan jumlah jin dan tipenya
    total_jin = 0
    total_pengumpul = 0
    total_pembangun = 0
    for i in range(n_baris_users):
        if(isi_users[i][2] == "jin_pengumpul"):
            total_jin += 1
            total_pengumpul += 1
        elif(isi_users[i][2] == "jin_pembangun"):
            total_jin += 1
            total_pembangun += 1
    print(f"> Total Jin: {total_jin}")
    print(f"> Total Jin Pengumpul: {total_pengumpul}")
    print(f"> Total Jin Pembangun: {total_pembangun}")

    # mencari jin termalas dan terajin
    if(n_baris_candi == 0):
        print("> Jin Terajin: -")
        print("> Jin Termalas: -")
    else:
        # mencari semua jin pembangun 
        jin = ["" for _ in range(total_pembangun)]
        n_jin = total_pembangun
        index = 0
        for i in range(n_baris_users):
            if(isi_users[i][2] == "jin_pembangun"):
                jin[index] = isi_users[i][0]
                index += 1
        # memastikan semua pembuat candi ada dalam array jin, jika tidak maka ditambahkan
        for i in range(n_baris_candi):
            index = string_in_array(jin, isi_candi[i][1], n_jin)
            if(index == -1):
                jin = string_append(jin, isi_candi[i][1], n_jin)
                n_jin += 1
        count_candi_jin = [0 for _ in range(n_jin)]
        for i in range(n_baris_candi):
            index = string_in_array(jin,isi_candi[i][1],n_jin)
            if(index != -1):
                count_candi_jin[index] += 1
        # mencari maksimum dan minimum jumlah candi yang dibuat oleh seorang jin
        candi_maks = int_maks(count_candi_jin,n_jin)
        candi_min = int_min(count_candi_jin, n_jin)
        # Menghitung jumlah jin yang membangun candi dengan jumlah maksimum atau minimum
        count_maks = 0
        count_min = 0
        for i in range(n_jin): 
            if(count_candi_jin[i] == candi_maks):
                count_maks += 1
            if(count_candi_jin[i] == candi_min):
                count_min += 1
        # Mencari semua jin yang membangun candi dengan jumlah maksimum atau minimum ke dalam array of string
        jin_maks = ["" for _ in range(count_maks)]
        jin_min = ["" for _ in range(count_min)]
        index_jin_maks = 0
        index_jin_min = 0
        for i in range(n_jin): 
            if(count_candi_jin[i] == candi_maks):
                jin_maks[index_jin_maks] = jin[i]
                index_jin_maks += 1
            if(count_candi_jin[i] == candi_min):
                jin_min[index_jin_min] = jin[i]
                index_jin_min += 1
        # Mengembalikan jin termalas dan terajin berdasarkan leksikografis
        print(f"> Jin Terajin: {string_leksikografis_min(jin_maks,count_maks)}")
        print(f"> Jin Termalas: {string_leksikografis_maks(jin_min,count_min)}")

    # Menentukan jumlah bahan bangunan    
    print(f"> Jumlah Pasir : {isi_bahan_bangunan[0][2]} unit")
    print(f"> Jumlah Batu : {isi_bahan_bangunan[1][2]} unit")
    print(f"> Jumlah Air : {isi_bahan_bangunan[2][2]} unit")

# F10 - Ambil Laporan Candi
# procedure laporancandi( input candi: Data)
# Melakukan laporan candi mulai dari jumlah candi, bahan total yang diperlukan, serta candi termurah dan termahal
def laporancandi(candi: Data) -> None:
    # Kamus LOKAL
        # i, n_baris_candi, harga_maks, harga_min, total_pasir, total_batu, total_air : integer
        # harga : array [0..n_baris_candi-1] of integer
        # isi_candi : array [0..candi.n_baris-1] of array [0..candi.n_kolom-1] of string
    # ALGORTIMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    # menghitung bahan bangunan total pembuat semua candi
    total_pasir = 0
    total_batu = 0
    total_air = 0
    for i in range(n_baris_candi):
        total_pasir += int(isi_candi[i][2])
        total_batu += int(isi_candi[i][3])
        total_air += int(isi_candi[i][4])
    print(f"> Total Candi: {n_baris_candi}") # karena jumlah baris candi menandakan jumlah candi yang ada
    print(f"> Total Pasir yang digunakan: {total_pasir}")
    print(f"> Total Batu yang digunakan: {total_batu}")
    print(f"> Total Air yang digunakan: {total_air}")
    # Hitung Harga tiap candi
    harga = [0 for _ in range(n_baris_candi)]
    for i in range(n_baris_candi):
        harga[i] = 10000 * int(isi_candi[i][2]) + 15000 * int(isi_candi[i][3]) + 7500 * int(isi_candi[i][4])
    # Mencari harga maksimum dan minimum
    harga_maks = harga[0]
    harga_min = harga[0]
    for i in range(n_baris_candi):
        if(harga[i] > harga_maks):
            harga_maks = harga[i]
        if(harga[i] < harga_min):
            harga_min = harga[i]
    # Mengeluarkan candi denga harga termahal atau termurah denga index paling kecil
    for i in range(n_baris_candi):
        if(harga[i] == harga_maks):
            print(f"> ID Candi Termahal: {isi_candi[i][0]} (Rp {harga_maks})")
            break
    for i in range(n_baris_candi):
        if(harga[i] == harga_min):
            print(f"> ID Candi Termurah: {isi_candi[i][0]} (Rp {harga_min})")
            break

# F11 - Hancurkan Candi
# procedure hancurkancandi( input/output candi: Data)
# Menghancurkan candi dengan id yang diberikan
def hancurkancandi(candi: Data) -> None:
    # KAMUS LOKAL
        # i, index, n_baris_candi : integer
        # id, yakin : string
        # isi_candi : array [0..candi.n_baris-1] of array [0..candi.n_kolom-1] of string
    # ALGORITMA
    # unpack data
    isi_candi = candi.isi
    n_baris_candi = candi.n_baris
    id = string_strip(input("Masukkan ID candi: "))
    # mencari index adanya id tersebut, jika tidak ditemukan maka index bernilai -1
    index = -1
    for i in range(n_baris_candi):
        if(isi_candi[i][0] == id):
            index = i
            break
    if(index != -1): # candi ditemukan
        yakin = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        if(yakin == "Y"): 
            # candi dihancurkan
            candi = data_remove(candi,index)
            print("Candi telah berhasil dihancurkan.")
        elif(yakin != "N"): 
            print(f"Tidak ada opsi \"{yakin}\". Ulangi!")
            hancurkancandi(candi)      
    else: # index = -1, candi tidak ditemukan
        print("Tidak ada candi dengan ID tersebut.")

# F12 - Ayam Berkokok
# procedure ayamberkokok (input candi: Data)
# Menentukan pemenang dari game ini 
def ayamberkokok (candi: Data) -> None:
    # KAMUS LOKAL
        # i, banyak_candi : integer
    # ALGORITMA
    # unpack data
    banyak_candi = candi.n_baris
    print("Kukuruyuk.. Kukuruyuk..")
    print("Jumlah Candi: " ,banyak_candi )
    if(banyak_candi >= 100):
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else: # banyak_candi < 100
        print("\nSelamat, Roro Jonggrang memenangkan permainan!")
        print("\n*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    quit()

# F13 - Load (Gunakan argparse)
# function load() -> array [0..2] of Data
# Menggunakan argparse agar dapat meload / membuka kembali data yang sudah disave sebelumnya, 
# prosedur ini sendiri dijalankan hanya sekali saja pada command line / terminal
def load() -> list[Data]:
    # KAMUS LOKAL 
        # parser, args : objek dari modul argparse
        # args.nama_folder : string
        # users, candi, bahan_bangunan : Data
    # ALGORITMA
    import os
    import argparse
    parser = argparse.ArgumentParser(add_help=False,usage='%(prog)s <nama_folder>')
    parser.add_argument("nama_folder",nargs="?",type=str,default="")
    args = parser.parse_args() 
    path = "save/"+args.nama_folder # Perlu ditambah "save/" karena parent foldernya "save"
    if(path == "save/"): # jika args.nama_folder kosong 
        print("Tidak ada nama folder yang diberikan!\n")
        parser.print_usage()
        return []
    elif(os.path.exists(path)): # jika folder ditemukan
        print("Loading...")
        users = data_load(path+"/user.csv")
        candi = data_load(path+"/candi.csv")
        bahan_bangunan = data_load(path+"/bahan_bangunan.csv")
        print("Selamat datang di program \"Manajerial Candi\"!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.\n")
        return [users,candi,bahan_bangunan]
    else: # folder tidak ditemukan
        print(f"Folder \"{path}\" tidak ditemukan.")
        return []

# F14 - Save
# procedure save (input users: Data, input candi: Data, input bahan_bangunan: Data)
# Menyimpan data pada folder dengan parent folder "save"
def save(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # count_splitted, i : integer
        # path, current_path : string
        # file_baru : boolean
        # path_spilted : array [0..count_splitted-1] of string
    # ALGORITMA
    path = "save/" + input("Masukkan nama folder: ")
    print("Saving...")
    count_spiltted = 1
    for i in range(len(path)):
        if(path[i] == "/"):
            count_spiltted += 1
    path_splited = string_split(path,"/")
    current_path = ""
    file_baru = False
    for i in range(count_spiltted):
        current_path += path_splited[i]
        if(not os.path.exists(current_path)):
            file_baru = True
            print(f"Membuat folder {current_path}...")
            os.mkdir(current_path)
        current_path += "/"
    if(file_baru):
        print()
    data_save(path, "user", users)
    data_save(path, "candi", candi)
    data_save(path, "bahan_bangunan", bahan_bangunan)
    print(f"Berhasil menyimpan data di folder {path}!")

# F15 - Help
# procedure help( input current_login: array [0..2] of string)
# Memberikan list semua command yang dapat digunakan tergantung pada status login
def help(current_login: list[str]) -> None:
    # KAMUS LOKAL
        # current_login : array [0..2] of string
    # ALGORITMA
    print(" HELP ".center(28,"="))
    if(current_login == ["" for _ in range(3)]): # BELUM LOGIN
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. save")
        print("   Untuk menyimpan data permainan saat ini")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(current_login[2] == "bandung_bondowoso"): # BANDUNG BONDOWOSO
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin")
        print("4. undohapus")
        print("   Untuk mengembalikan jin yang terhapus")
        print("5. ubahjin")
        print("   Untuk mengubah tipe jin (pengumpul/pembangun)")
        print("6. batchkumpul")
        print("   Untuk melakukan pengumpulan oleh semua jin pengumpul")
        print("7. batchbangun")
        print("   Untuk melakukan pembangunan oleh semua jin pembangun")
        print("8. laporanjin")
        print("   Untuk mengambil laporan jin")
        print("9. laporancandi")
        print("   Untuk mengambil laporan candi")
        print("10. save")
        print("   Untuk menyimpan data permainan saat ini")
        print("11. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(current_login[2] == "roro_jonggrang"): # RORO JONGGRANG
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save")
        print("   Untuk menyimpan data permainan saat ini")
        print("5. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(current_login[2] == "jin_pengumpul"): # JIN PENGUMPUL
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan bahan bangunan")
        print("3. save")
        print("   Untuk menyimpan data permainan saat ini")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    else: # current_login[2] == "jin_pembangun" # JIN PEMBANGUN
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun sebuah candi")
        print("3. save")
        print("   Untuk menyimpan data permainan saat ini")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")

# F16 - Exit
# procedure exit (input users: Data, input candi: Data, input bahan_bangunan: Data )
# Untuk keluar dari program, serta opsi menyimpan data sebelum keluar
def exit(users: Data, candi: Data, bahan_bangunan: Data) -> None:
    # KAMUS LOKAL
        # jawab_exit : string
    # ALGORITMA
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ",end='')
    jawab_exit = input()
    if(jawab_exit == 'y'or jawab_exit == 'Y'): 
        save(users,candi,bahan_bangunan) 
        quit()
    elif(jawab_exit == 'n' or jawab_exit == 'N'):
        quit()
    else: # karena salah input maka prosedur diulang
        exit(users, candi, bahan_bangunan)
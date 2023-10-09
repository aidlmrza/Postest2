import os
from prettytable import PrettyTable
os.system('cls')

#VARIABLE YANG BERISI DATA DENGAN LIST BERSARANG
poster = [
    [1,"Poster Luffy GEAR 5 One Piece","Potrait","30.000"],
    [2,"Poster Zoro One Piece","Landscape","20.000"],
    [3,"Poster Naruto team 7 Sage Mode","Landscape","30.000"],
    [4,"Poster Counter Strike 2","Potrait","20.000"],
    [5,"Poster Raze Valorant","Potrait","25.000"],
    [6,"Poster Ender Dragon Minecraft","Landscape","25.000"],
    [7,"Poster HuTao Genshin Impact","Potrait","30.000"]
]

#FUNCTION UNTUK MENAMPILKAN ITEM MENGGUNAKAN PRETTYTABBLE YANG SUDAH DIKONVERT DARI DATA PADA POSTER
def lihat_item(): 
    table = PrettyTable()
    table.field_names = ["Etalase","Nama Poster","Jenis","Harga"]
    for item in poster:
        table.add_row(item)
    print(table)

#USERNAME DAN PASSWORD YANG DISEDIAKAN UNTUK ADMIN
nama_admin = ("admin")
pw_admin = ("adminbaik")

#DATA-DATA USER YANG SUDAH TERDAFTAR 
data_user = [
    {"username": "hisyam", "password": "hisym20"},
    {"username": "aidil", "password":"ai40"},
    {"username": "fajar", "password":"fajr60"},
    {"username": "ezra", "password":"ez52"},
    {"username": "coba", "password":"coba"}
]

#FUNCTION UNTUK REGISTER
def register():
    print("Silahkan lakukan Registrasi")
    while True:
        nama = input("Masukkan username: ").lower()
        pw = input("Masukkan password: ")
        username_ada = False #VARIABLE YANG DIGUNAKAN UNTUK MENGECEK APAKAH USERNAME TERDAFTAR ATAU TIDAK
        if nama == nama_admin:
            print("username sudah digunakan cobalagi yang lain")
            return
        for user in data_user:
            if user["username"].lower() == nama :
                print("username sudah digunakan cobalagi yang lain")
                username_ada = True #VARIABLE BERUBAH MENJADI TRUE SAAT USERNAME SUDAH TIDAK TERSEDIA
                break
        #JIKA USERNAME TERSEDIA DAN VARIBLENYA MASIH BERNILAI FALSE MAKA AKAN BERHASIL MENAMBAHKAN AKUN BARU
        if not username_ada: 
            akun_baru = {"username": nama, "password": pw}
            data_user.append(akun_baru)
            print("berhasil membuat akun")
            break

#FUNCTION UNTUK LOGIN
def login():
    print("Silahkan Login")
    while True:
        username = input("Masukkan username: ").lower()
        pw = input("Masukkan password: ")
        
        if username == nama_admin and pw == pw_admin:
            return menu_admin()
        user_ada = False #SEBUAH VARIABLE YANG DIGUNAKAN UNTUK MENGECEK APAKAH USERNAME TERDAFTAR ATAU TIDAK
        for user in data_user:
            if user["username"].lower() == username:
                user_ada = True #JIKA USERNAME DITEMUKAN MAKA VARIABLE AKAN MENJADI TRUE
                if user["password"] == pw:
                    return menu_user()
                else:
                    print("Password yang anda masukkan salah")
        if not user_ada: #JIKA USERNAME TIDAK DITEMUKAN MAKA AKAN MENGEKSEKUSI COMMAND INI
            print("akun anda tidak dikenal")

#FUNCTION YANG DITAMPILKAN KEPADA USER
def menu_user():
    while True:
        print("\nSelamat datang di ANIMANGAME berikut adalah produk yang kami jual: ")
        lihat_item()
        pilihan = (input("Apakah anda ingin melakukan pembelian? (y/n): ")).lower()
        if pilihan == "y":
            Transaksi()
        elif pilihan == "n":
            break
        else:
            print("invalid")

#FUNCTION TRANSAKSI UNTUK PELANGGAN
def Transaksi():
    while True:
        etalase = int(input("Masukkan Nomor etalase item yang ingin dibeli: "))
        item_ditemukan = False #VARIABLE YANG DIGUNAKAN SEBAGAI PENANDA KALAU ITEM BELUM DITEMUKAN
        for i in range(len(poster)):
            if poster[i][0] == etalase:
                nama_produk = poster[i][1]
                harga_produk = poster[i][3]
                print(f"Anda berhasil membeli Produk dengan nomor etalase {etalase}: {nama_produk} dengan harga {harga_produk}.")
                item_ditemukan = True #JIKA PRODUK DITEMUKAN AKAN MENJADI TRUE
                return
        if not item_ditemukan: #JIKA PRODUK TIDAK DITEMUKAN MAKA AKAN MENGEKSEKUSI COMMAND INI
            print(f"Tidak ada etalase bernomor {etalase}")

#FUNCTION UNTUK MENAMPILKAN MENU ADMIN
def menu_admin():
    while True:
        print("\nanda memasukki mode admin")
        print("1. Tambahkan Produk")
        print("2. Lihat Produk")
        print("3. Perbarui Produk")
        print("4. Hapus Produk")
        print("0. Keluar")
        opsi_admin = input("Pilih opsi (1/2/3/4/0): ") #PILIH OPSI UNTUK MENENTUKAN TINDAKAN SELANJUTNYA
        if opsi_admin == "1": 
            tambah()
        elif opsi_admin == "2": 
            lihat_item()
        elif opsi_admin == "3":
            perbarui()
        elif opsi_admin == "4":
            hapus()
        elif opsi_admin == "0":
            break
        else:
            print("Invalid")

#FUNCTION YANG DIGUNAKAN OLEH ADMIN UNTUK MENAMBAH PRODUK
def tambah():
    max_etalase = max([item[0] for item in poster])
    etalase = max_etalase + 1
    produk = input("Masukkan nama produk: ")
    jenis = input("Masukkan jenis produk: ")
    harga = input("Masukkan harga produk: ")
    tambahan = [etalase, produk, jenis, harga]
    poster.append(tambahan) #MENAMBAHKAN PRODUK BARU KE DALAM VARIABLE POSTER
    lihat_item()

#FUNCTION UNTUK MENGUBAH NAMA, JENIS, HARGA SUATU PRODUK PADA ETALASE
def perbarui():
    etalase = int(input("Masukkan nomor etalase barang yang mau diubah: "))
    for i in range(len(poster)): 
        if poster[i][0] == etalase: #AKAN MENGEKSEKUSI COMMAND INI JIKA NOMOR ETALASE TERDAPAT PADA DATABASE
            produk = input("Masukkan nama produk baru: ")
            jenis = input("Masukkan jenis produk baru: ")
            harga = input("Masukkan harga produk baru: ")
            poster[i][1] = produk
            poster[i][2] = jenis
            poster[i][3] = harga
            print("Berhasil mengubah data")
            lihat_item()
            break
    else:
        print("Produk tidak ada")

#FUNCTION UNTUK MENGHAPUS PRODUK DENGAN MEMILIH NOMOR ETALASENYA
def hapus():
    etalase = int(input("Masukkan nomor etalase barang yang mau dihapus: "))
    ada = False #VARIABLE YANG DIGUNAKAN SEBAGAI PENGECEK APAKAH PRODUK TERDAFTAR ATAU TIDAK

    for i in range(len(poster)):
        if poster[i][0] == etalase:
            del poster[i]
            ada = True #VARIABLE MENJADI TRUE KETIKA PRODUK SUDAH DITEMUKAN DAN DIHAPUS
            break

    if ada: #COMMAND INI DIGUNAKAN UNTUK MENYUSUN ULANG URUTAN PADA NOMOR ETALASE
        for i in range(len(poster)):
            poster[i][0] = i + 1
        print("Produk berhasil dihapus")
        lihat_item()
    else:
        print("Produk tidak ada")

#MAIN PROGRAM
while True:
    print("\nSelamat datang di toko Poster ANIMANGAME")
    print("Kami menjual Poster Anime Manga dan Game")
    print("1. Buat Akun")
    print("2. Login")
    print("3. Keluar")
    awal = input("Pilih opsi (1/2/3): ")
    if awal == "1":
        register()
    elif awal == "2":
        login()
    elif awal == "3":
        break
    else:
        print("Invalid")

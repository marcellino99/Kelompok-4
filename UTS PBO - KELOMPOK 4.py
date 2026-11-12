#clas Hotel
class Hotel: 
    def __init__(self, nama):
        self.nama = nama
        self.daftar_kamar = []
 
    def registrasi_kamar(self, item):
        self.daftar_kamar.append(item)
        print("Kamar Berhasil Diregistrasi!")
 
    def cek_ketersediaan(self):
        tersedia = []
 
        for daftar in self.daftar_kamar:
            if daftar.status == "TERSEDIA":
                tersedia.append(daftar)
        if len(tersedia) == 0:
            raise RoomNotAvailableException("Maaf, Kamar Tidak Tersedia!")
        return tersedia
 
    def check_in(self, data, nomor):
        kamar_ditemukan = None
 
        for kamar in self.daftar_kamar:
            if kamar.nomor == nomor:
                kamar_ditemukan = kamar
                break
        if kamar_ditemukan != None and kamar_ditemukan.status == "TERSEDIA":
            data.kamar = kamar_ditemukan
            data.status = "CHECK-IN"
            kamar_ditemukan.status = "TERISI"
 
            print("\nReservasi Berhasil Dikonfirmasi!")
            print("Nama Tamu    :", data.nama)
            print("Nomor Kamar  :", kamar_ditemukan.nomor)
            print("Status Kamar :", kamar_ditemukan.status)
        else:
            raise RoomNotAvailableException("Kamar Tidak Tersedia!")
 
#clas Kamar
class Kamar:
    def __init__(self, nomor, tipe, lantai, tarif, fasilitas, biaya_fasilitas):
        self.nomor = nomor
        self.tipe = tipe
        self.lantai = lantai
        self.tarif = tarif
        self.fasilitas = fasilitas
        self.biaya_fasilitas = biaya_fasilitas
        self.status = "TERSEDIA"
 
    def tampilkan_info(self):
        print("Nomor Kamar     :", self.nomor)
        print("Tipe Kamar      :", self.tipe)
        print("Lantai          :", self.lantai)
        print("Tarif Per Malam : Rp", self.tarif)
        print("Fasilitas       :")
 
        for fasilitas in self.fasilitas:
            print("-", fasilitas)
        print("Biaya Fasilitas : Rp", self.biaya_fasilitas)
        print("Status Kamar    :", self.status)
 
#clas layanan
class Layanan:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
 
    def hitung_biaya(self):
        return self.harga
 
#code inheritance dan polymorphisem
class RoomService(Layanan):
    def hitung_biaya(self):
        return self.harga
 
class Laundry(Layanan):
    def hitung_biaya(self):
        return self.harga
 
class Spa(Layanan):
    def hitung_biaya(self):
        return self.harga
 
#code exeption
class RoomNotAvailableException(Exception):
    pass
 
#clas reservasi
class Reservasi:
    def __init__(self, nama, tanggal_masuk, tanggal_keluar):
        self.nama = nama
        self.tanggal_masuk = tanggal_masuk
        self.tanggal_keluar = tanggal_keluar
        self.jumlah_malam = tanggal_keluar - tanggal_masuk
        self.kamar = None
        self.layanan = []
        self.status = "MENUNGGU KONFIRMASI"
        if self.jumlah_malam <= 0:
            raise ValueError("Tanggal keluar tidak valid!")
 
    def tambah_layanan(self, item):
        self.layanan.append(item)
        print("Layanan Berhasil Ditambahkan!")
 
    def hitung_malam(self):
        return self.jumlah_malam
 
    def hitung_total_layanan(self):
        total = 0
        for layanan in self.layanan:
            total += layanan.hitung_biaya()
        return total
 
    def hitung_total_tagihan(self):
        biaya_kamar = self.kamar.tarif * self.jumlah_malam
        biaya_fasilitas = (
            self.kamar.biaya_fasilitas * self.jumlah_malam)
        biaya_layanan = self.hitung_total_layanan()
        return biaya_kamar + biaya_fasilitas + biaya_layanan
 
hotel = Hotel("Hotel Bintang 5")
daftar_reservasi = []
 
#tipe kamar
daftar_tipe = {
    "1": ("Reguler", 250000),
    "2": ("Luxury", 500000),
    "3": ("VIP", 750000),
    "4": ("VVIP", 1000000)}
 
#fasilitas
daftar_fasilitas = {
    "1": ("AC", 50000),
    "2": ("TV", 30000),
    "3": ("Kolam Berenang", 100000),
    "4": ("Gazebo", 75000),
    "5": ("Kipas", 15000)}
 
while True:
    print("="*40)
    print("     SISTEM RESERVASI HOTEL")
    print("="*40)
    print("1. Registrasi Kamar")
    print("2. Tampilkan Kamar")
    print("3. Buat Reservasi")
    print("4. Order Layanan Tambahan")
    print("5. Laporan Tagihan")
    print("99. Keluar")
    print("="*40)
 
    pilihan = input("Masukkan Pilihan : ")
 
    #1.regis kamar
    if pilihan == "1":
        try:
            nomor = int(input("Nomor Kamar : "))
            lantai = int(input("Lantai Kamar : "))
 
            print("\n===== PILIH TIPE KAMAR =====")
            print("1. Reguler - Rp250000")
            print("2. Luxury  - Rp500000")
            print("3. VIP     - Rp750000")
            print("4. VVIP    - Rp1000000")
 
            pilihan_tipe = input("Pilih Tipe Kamar : ")
 
            if pilihan_tipe not in daftar_tipe:
                print("Tipe Kamar Tidak Valid!")
 
            else:
                tipe = daftar_tipe[pilihan_tipe][0]
                tarif = daftar_tipe[pilihan_tipe][1]
 
                print("\n===== PILIH FASILITAS =====")
                print("1. AC             - Rp50000")
                print("2. TV             - Rp30000")
                print("3. Kolam Berenang - Rp100000")
                print("4. Gazebo         - Rp75000")
                print("5. Kipas          - Rp15000")
                print("0. Tidak Ada Tambahan")
 
                print("\nPilih fasilitas")
                print("Contoh: 1,2,3")
 
                pilihan_fasilitas = input( "Masukkan Pilihan Fasilitas : ")
                fasilitas = []
                biaya_fasilitas = 0
 
                if pilihan_fasilitas != "0":
                    pilihan_list = pilihan_fasilitas.split(",")
 
                    for kode in pilihan_list:
                        kode = kode.strip()
 
                        if kode in daftar_fasilitas:
 
                            nama_fasilitas = daftar_fasilitas[kode][0]
                            harga_fasilitas = daftar_fasilitas[kode][1]
 
                            if nama_fasilitas not in fasilitas:
                                fasilitas.append(nama_fasilitas)
                                biaya_fasilitas += harga_fasilitas
                        else:
                            print("Pilihan Fasilitas", kode, "Tidak Valid!")
 
                data = Kamar(
                    nomor,
                    tipe,
                    lantai,
                    tarif,
                    fasilitas,
                    biaya_fasilitas)
 
                hotel.registrasi_kamar(data)
        except ValueError:
            print("Terjadi Value Error!")
 
    #2.menampilkan kamar
    elif pilihan == "2":
        if len(hotel.daftar_kamar) > 0:
            for item in hotel.daftar_kamar:
                item.tampilkan_info()
                print("="*40)
        else:
            print("Belum Ada Kamar Terdaftar!")
 
    #3.reservasi
    elif pilihan == "3":
        try:
            nama            = input("Nama Tamu                  : ")
            tanggal_masuk   = int(input("Tanggal Masuk (Angka)  : "))
            tanggal_keluar  = int(input("Tanggal Keluar (Angka) : "))
 
            data = Reservasi(
                nama,
                tanggal_masuk,
                tanggal_keluar)
            tersedia = hotel.cek_ketersediaan()
            print("\n===== KAMAR TERSEDIA =====")
 
            for item in tersedia:
                print(
                    item.nomor,
                    "-",
                    item.tipe,
                    "- Rp",
                    item.tarif)
 
            nomor = int(input("Pilih Nomor Kamar : "))
            hotel.check_in(data, nomor)
            daftar_reservasi.append(data)
 
        except RoomNotAvailableException as error:
            print("ERROR:", error)
 
        except ValueError as error:
            print("ERROR:", error)
 
    #4.layanan tmbhan
    elif pilihan == "4":
        if len(daftar_reservasi) > 0:
            nama = input("Masukkan Nama Tamu : ")
            ketemu = False
 
            for daftar in daftar_reservasi:
                if daftar.nama == nama and daftar.status == "CHECK-IN":
                    ketemu = True
                    break
            if ketemu:
                print("\n===== LAYANAN TAMBAHAN =====")
                print("1. Room Service - Rp100000")
                print("2. Laundry      - Rp50000")
                print("3. Spa          - Rp200000")
 
                pilihan_layanan = input("Pilih Layanan : ")
                if pilihan_layanan == "1":
                    daftar.tambah_layanan(
                        RoomService("Room Service", 100000))
                elif pilihan_layanan == "2":
                    daftar.tambah_layanan(
                        Laundry("Laundry", 50000))  
                elif pilihan_layanan == "3":
                    daftar.tambah_layanan(Spa("Spa", 200000))
                else:
                    print("Tolong Pilih Dengan Benar!")
            else:
                print("Data Tamu Tidak Ditemukan!")
        else:
            print("Pelanggan Belum Reservasi!")
 
    #5.lapotan tagihan
    elif pilihan == "5":
        if len(daftar_reservasi) > 0:
            nama = input("Masukkan Nama Tamu : ")
            ketemu = False
            for reservasi in daftar_reservasi:
                if reservasi.nama == nama:
                    ketemu = True
                    break
            if ketemu:
                biaya_kamar = (
                    reservasi.kamar.tarif *
                    reservasi.hitung_malam())
                biaya_fasilitas = (
                    reservasi.kamar.biaya_fasilitas *
                    reservasi.hitung_malam())
                biaya_layanan = reservasi.hitung_total_layanan()
 
                print("\n========== TAGIHAN HOTEL ==========")
                print("Nama Tamu      :", reservasi.nama)
                print("Tipe Kamar     :", reservasi.kamar.tipe)
                print("Jumlah Malam   :", reservasi.hitung_malam())
                print("="*40)
                print("Biaya Kamar    : Rp", biaya_kamar)
                print("Biaya Fasilitas: Rp", biaya_fasilitas)
                print("Biaya Layanan  : Rp", biaya_layanan)
                print("="*40)
                print("TOTAL TAGIHAN  : Rp",reservasi.hitung_total_tagihan())
                print("Status         :", reservasi.status)
                print("=" * 40)
            else:
                print("Data Pelanggan Yang Reservasi Tidak Ada")
        else:
            print("Pelanggan Belum Reservasi!")
 
    #keluar program
    elif pilihan == "99":
 
        print("Terimakasih Telah Mengunjungi Hotel Kami!")
        break
    else:
        print("Masukan Pilihan Dengan Benar!")


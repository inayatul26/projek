LAPORAN PROJEK AKHIR
PEMROGRAMAN BERORIENTASI OBJEK PRAKTIK
SISTEM PENYEWAAN MOBIL





















Disusun oleh:
Gebriella Wahyuni Sirait	(5220411231)
Shafira Nur Alfiah		(5220411292)
Andata Leonardo 		(5220411294)
Faras Sulthan Pratama 	(5220411318)
Siti Inayatul Mufidah  	(5220411319)







PROGRAM STUDI INFORMATIKA
FAKULTAS SAINS DAN TEKNOLOGI
UNIVERSITAS TEKNOLOGI YOGYKARTA 2023/2024
KATA PENGANTAR
Puji syukur kami panjatkan ke hadirat Allah swt atas rahmat dan karunia-Nya sehingga projek ini dapat kami selesaikan.
Kami ucapkan terima kasih kepada Irma Handayani,, S.kom., M.Sc., selaku Dosen Mata kuliah Pemrograman Berorientasi Objek yang telah memberikan tugas ini sehingga dapat menambah pengetahuan dan wawasan kami.
Kami ingin mengucapkan terima kasih kepada semua pihak yang telah mendukung dan berkontribusi dalam pengembangan proyek ini. Semangat kolaborasi dan dedikasi dari seluruh tim proyek menjadi kunci utama keberhasilan pelaksanaan. Harapn kami, sistem ini tidak hanya memenuhi ekspektasi, tetapi juga mampu memberikan nilai tambah bagi pengguna dan penyedia jasa penyewaan mobil.
Tanpa dukungan penuh dari berbagai pihak, proyek ini tidak akan mencapai titik ini. Oleh karena itu, apresiasi setinggi-tingginya kami sampaikan kepada semua pihak yang telah turut serta dalam perjalanan proyek ini. Semoga sistem peminjaman mobil yang dihasilkan dapat memberikan manfaat yang maksimal dan memberikan kontribusi positif dalam memajukan industri peminjaman mobil.


Yogyakarta, 08 Januari 2024



Kelompok 6






















	DAFTAR ISI	

COVER	i
KATA PENGANTAR	ii
DAFTAR ISI	iii
BAB I Pendahuluan	1
Latar Belakang	1
Rumusan Masalah	1
Solusi Masalah	1
Tujuan	1
Manfaat yang diharapkan	1
BAB II Pembahasan	2
Class Diagram	2
Program python	4
Tampilan GUI	14
Tampilan terminal python	15
Tampilan DataBase	16
BAB III Penutupan	17
Kesimpulan	17




















 
BAB I Pendahuluan
Latar Belakang
Dalam era modern ini, mobilitas menjadi aspek krusial dalam kehidupan sehari-hari. Kebutuhan akan transportasi yang fleksibel dan efisien mendorong munculnya industri penyewaan mobil. Menyadari peran pentingnya dalam memenuhi kebutuhan transportasi, proyek ini mengambil langkah maju dalam membangun sistem peminjaman mobil yang inovatif dan terintegrasi.
Sistem peminjaman mobil yang efisien dan terkelola dengan baik tidak hanya memberikan kemudahan akses bagi para pelangga tetapi juga memberikan keuntungan bagi penyedia jasa penyewaan mobil. Dalam konteks ini, pengembangan sistem ini diarahkan untuk mengatasi beberapa tantangan yang sering dihadapi dalam proses peminjaman mobil.
Rumusan Masalah 
1.	Kompleksitas proses peminjaman
2.	Keterbatasan informasi
3.	Manajemen armada yang tidak efisien
Solusi Masalah
1.	Antarmuka pengguna yang responsif
2.	Sistem informasi terpadu
3.	Manajemen armada otomatis
Tujuan 
Tujuan utama dari proyek ini adalah mengembangkan sistem peminjaman mobil yang dapat memberikan pengalaman yang lebih efisien, sepat, dan terjangkau nagi para pengguna. Selain itu proyek ini juga bertujuan untuk memberikan solusi manajemen armada yang efektif nagi penyedia jasa penyewaan mobil, sehingga dapat meningkatkan pengelolaan armada dan mengoptimalkan operasional bisnis.
Manfaat yang diharapkan
1.	Peningkatan efisiensi dalam proses peminjaman mobil
2.	Penyederhanaan administrasi terkait manajemen pelanggan dan armada
3.	Peningkatan pengalaman pelanggan melalui layanan yang lebih cepat dan responsive
4.	Pengoptimalan penggunaan armada melalui sistem manajemen yang terintegrasi








BAB II Pembahasan
Class Diagram
  
class diagram tersebut mempunyai 4 kelas yaitu:
1.	Kelas Aplikasi Peminjaman Mobil 
•	Memiliki Atribut:
-	daftar_kendaraan sebagai list untuk menyimpan daftar kendaraan yang tersedia untuk disewa
-	daftar_penyewa sebagai list untuk menyimpan daftar penyewa 
•	Memiliki Method:
-	tambah_kendaraan yang digunakan untuk menambahkan kendaraan baru ke daftar kendaraan
-	tambah_penyewa yang digunakan untuk menambahkan penyewa ke dalam list daftar penyewa
-	tambah_mobil yang digunakan untuk menambahkan mobil ke dalam kelas Mobil
-	setup_gui yang digunakan untuk menyiapkan antarmuka pengguna aplikasi
2.	Kelas Kendaraan
•	Memiliki Atribut:
-	id_kendaraan dengan tipe data string dan sebagai primary key
-	merk dengan tipe data string
-	model dengan tipe data string
-	tahun dengan tipe data string
-	ketersedian dengan tipe data Boolean
•	Memiliki Method:
-	informasi yang menampilkan tentang informasi kendaraan
3.	Kelas Mobil
Kelas Mobil merupakan kelas yang pewarisan atau inheritance dari Kelas Kendaraan 
•	Memiliki tambahin Atribut:
-	harga_sewa dengan tipe data Float
•	Memiliki tambahan Method:
-	Informasi yang menampilkan informasi tentang mobil termasuk harga sewa
4.	Kelas Penyewa
•	Memiliki Atribut:
-	id_penyewa dengan tipe data string dan sebagai primary key
-	nama_penyewa dengan tipe data string
-	nomor_telepon dengan tipe sata string
-	alamat dengan tipe data string
-	id_mobil_disewa dengan tipe data string
-	durasi_sewa dengan tipe data integer
-	total_harga_sewa dengan tipe data float
•	memiliki Atribut:
-	informasi yang berisi informasi tentang penyewa
Hubungan antar kelas: 
1.	kelas Aplikasi Peminjaman Mobil memiliki hubungan asosiasi dengan kelas Kendaran dan kelas Penyewa. Hubungan ini menunjukkan bahwa kelas Aplikasi Peminjaman Mobil dapat mengkases informasi tentang kendaraan dan penyewa
2.	kelas Kendaraan memiliki hubungan asosisasi dengan kelas Mobil. Hubungan ini menunjukkan bahwa kendaraan dapat berupa mobil atau kendaraan lain. Kelas Mobil mewarisi kelas Kendaraan.
Class diagram diatas menggambarkan tentang sistem aplikasi peminjaman mobil secara sederhana, Dalam sistem ini pengguna dapat menambahkan daftar kendaraan, menambahkan daftar penyewa,dan melakukan penyewaan.












Program python
1.	Import Library
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import mysql.connector
•	tkinter: Library untuk membuat GUI menggunakan Tk.
•	messagebox: Modul dalam Tkinter untuk menampilkan pesan pop-up.
•	datetime: Modul untuk bekerja dengan objek tanggal dan waktu.
•	mysql.connector: Library untuk menghubungkan dan berinteraksi dengan database MySQL.
2.	Kelas Kendaraan
class Kendaraan:
    def __init__(self, id_kendaraan, merk, model, tahun):
        self._id_kendaraan = id_kendaraan
        self._merk = merk
        self._model = model
        self._tahun = tahun
        self._ketersediaan = True

    def informasi(self):
        return f"{self._merk} {self._model} ({self._tahun})"
a.	Konstruktor (__init__)
 def __init__(self, id_kendaraan, merk, model, tahun):
•	Metode inisialisasi (konstruktor) yang dipanggil saat objek kelas dibuat.
•	Menerima empat parameter: id_kendaraan, merk, model, dan tahun.
•	Menginisialisasi atribut objek seperti _id_kendaraan, _merk, _model, _tahun, dan _ketersediaan.
•	Atribut _ketersediaan diatur secara default ke True.
b.	Metode informasi
def informasi(self):
•	Metode yang mengembalikan string berisi informasi tentang kendaraan.
•	Menggunakan atribut _merk, _model, dan _tahun untuk membentuk string yang berisi informasi merek, model, dan tahun kendaraan.
3.	Kelas Mobil
Kelas Mobil merupakan turunan dari kelas Kendaraan (implementasi koncep inheritance)
class Mobil(Kendaraan):
    def __init__(self, id_mobil, merk, model, tahun, harga_sewa):
        super().__init__(id_mobil, merk, model, tahun)
        self._harga_sewa = harga_sewa

    def informasi(self):
        return f"{super().informasi()} - Harga Sewa: {self._harga_sewa}"
a.	Konstruktor(__init__)
def __init__(self, id_mobil, merk, model, tahun, harga_sewa):
•	Metode inisialisasi (konstruktor) kelas Mobil.
•	Menerima lima parameter: id_mobil, merk, model, tahun, dan harga_sewa.
•	Memanggil konstruktor kelas induk (Kendaraan) menggunakan super().__init__ untuk menginisialisasi atribut yang dimiliki oleh kelas Kendaraan.
•	Menambahkan atribut khusus kelas Mobil, yaitu _harga_sewa.
b.	Metode informasi 
def informasi(self):
•	Metode yang menggantikan metode informasi dari kelas Kendaraan.
•	Memanggil metode informasi dari kelas induk menggunakan super().informasi() untuk mendapatkan informasi umum kendaraan.
•	Menambahkan informasi harga sewa kendaraan.
4.	Kelas Penyewa
class Penyewa:
    def __init__(self, id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, durasi_sewa):
        self._id_penyewa = id_penyewa
        self._nama = nama
        self._nomor_telepon = nomor_telepon
        self._alamat = alamat
        self._id_mobil_disewa = id_mobil_disewa
        self._durasi_sewa = durasi_sewa
        self._total_harga_sewa = 0

    def informasi(self):
        return f"Penyewa {self._nama} ({self._nomor_telepon}) - Alamat: {self._alamat}"
a.	Konstruktor(__init__)
•	Metode inisialisasi (konstruktor) kelas Penyewa.
•	Menerima enam parameter: id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, dan durasi_sewa.
•	Menginisialisasi atribut objek seperti _id_penyewa, _nama, _nomor_telepon, _alamat, _id_mobil_disewa, _durasi_sewa, dan _total_harga_sewa.
•	Atribut _total_harga_sewa diatur secara default ke 0.
b.	Metode Informasi
def informasi(self):
•	Metode yang mengembalikan string berisi informasi tentang penyewa.
•	Menggunakan atribut _nama, _nomor_telepon, dan _alamat untuk membentuk string yang berisi informasi tentang nama penyewa, nomor telepon, dan alamat
5.	Kelas Aplikasi Peminjaman Mobil
class AplikasiPeminjamanMobil:
Kelas AplikasiPeminjamanMobil ini berfungsi sebagai kontrol pusat aplikasi. Setelah objek aplikasi dibuat, koneksi ke database dibuat, tabel-tabel database dibuat, dan antarmuka pengguna diatur.
a.	Konstruktor(__init__)
def __init__(self):
        self.cursor = self.conn.cursor()    
        self._daftar_kendaraan = []
        self._daftar_penyewa = []
•	Metode inisialisasi (konstruktor) kelas AplikasiPeminjamanMobil.
•	Membuat koneksi ke database MySQL dengan menggunakan modul mysql.connector.
•	Menginisialisasi atribut _daftar_kendaraan dan _daftar_penyewa sebagai list kosong.
•	Membuat objek kursor (self.cursor) untuk berinteraksi dengan database.
b.	Koneksi ke Database
self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sewa'
        )
Membuat koneksi ke database MySQL dengan parameter host, user, password, dan nama database sewa.
c.	Inisialisasi Tabel Database
self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS kendaraan (
                id_kendaraan VARCHAR(255) PRIMARY KEY,
                merk VARCHAR(255),
                model VARCHAR(255),
                tahun VARCHAR(4),
                ketersediaan BOOLEAN,
                harga_sewa FLOAT            
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS penyewa (
                id_penyewa VARCHAR(255) PRIMARY KEY,
                nama VARCHAR(255),
                nomor_telepon VARCHAR(15),
                alamat VARCHAR(255),
                id_mobil_disewa VARCHAR(255),
                durasi_sewa INT,
                total_harga_sewa FLOAT
            )
        ''')
•	Menggunakan kursor, menjalankan perintah SQL untuk membuat dua tabel di database (kendaraan dan penyewa) jika tabel tersebut belum ada.
•	Tabel kendaraan berisi informasi tentang kendaraan, sedangkan tabel penyewa berisi informasi tentang penyewa.
d.	Metode setup_gui
self.setup_gui()
•	Metode untuk mengatur antarmuka pengguna (GUI) menggunakan Tkinter.
•	Membuat objek GUI yang mencakup elemen seperti Entry, Label, dan Button untuk menambahkan mobil dan penyewa.
e.	Metode tambah_kendaraan
def tambah_kendaraan(self, kendaraan):
	Eksekusi perintah SQL
self.cursor.execute('''
            INSERT INTO kendaraan (id_kendaraan, merk, model, tahun, ketersediaan, harga_sewa)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (kendaraan._id_kendaraan, kendaraan._merk, kendaraan._model, kendaraan._tahun, 1, kendaraan._harga_sewa ))
•	Menggunakan kursor, metode ini menjalankan perintah SQL untuk menambahkan data kendaraan ke dalam tabel kendaraan di database.
•	Menggunakan parameterized query untuk mencegah SQL injection.
•	Parameter yang diberikan berasal dari atribut-atribut objek kendaraan.
	Commit perubahan ke Database
self.conn.commit()
•	Melakukan commit untuk menyimpan perubahan yang telah dilakukan pada database.
•	Diperlukan agar perubahan yang dilakukan oleh perintah SQL sebelumnya menjadi permanen.
	Cetak informasi dan Tambahkan ke Daftar Kendaraan
print(f"Informasi Kendaraan Ditambahkan: {kendaraan.informasi()}")
self._daftar_kendaraan.append(kendaraan)
•	Mencetak informasi kendaraan yang telah ditambahkan ke dalam console atau output program.
•	Informasi tersebut diambil dari metode informasi pada objek kendaraan.
•	Menambahkan objek kendaraan ke dalam daftar kendaraan (self._daftar_kendaraan).
•	Daftar kendaraan ini bisa digunakan untuk melacak dan mengelola kendaraan yang ada dalam aplikasi.
f.	Metode tambah_mobil
def tambah_mobil(self):
	Mengambil data input
id_mobil = self.entry_id_mobil.get()
        merk = self.entry_merk.get()
        model = self.entry_model.get()
        tahun = self.entry_tahun.get()
        harga_sewa = int(self.entry_harga_sewa_mobil.get())

Mengambil data input dari elemen GUI (Entry) yang digunakan untuk memasukkan informasi mobil
	Membuat objek mobil baru
mobil_baru = Mobil(id_mobil, merk, model, tahun, harga_sewa)
membuat objek bau dari kelas Mobil menggunakan data input yang telah diambil
	Memeriksa keberadaan mobil
mobil_ditemukan = False
for mobil in self._daftar_kendaraan:
    if mobil._id_kendaraan == id_mobil:
       mobil_ditemukan = True
       break
Melakukan iterasi pada daftar kendaraan untuk memeriksa apakah mobil dengan ID yang sama sudah ada dalam sistem
	Tambahkan mobil atau tampilkan pesan kesalahan
if not mobil_ditemukan:
            self.tambah_kendaraan(mobil_baru)
            messagebox.showinfo("Informasi Mobil Ditambahkan",
                                f"ID Mobil \t\t: {mobil_baru._id_kendaraan}\n"
                                f"Merk \t\t: {mobil_baru._merk}\n"
                                f"Model \t\t: {mobil_baru._model}\n"
                                f"Tahun \t\t: {mobil_baru._tahun}\n"
                                f"Harga Sewa \t: {mobil_baru._harga_sewa}\n"
                                f"Ketersediaan \t: {'Tersedia' if mobil_baru._ketersediaan else 'Tidak Tersedia'}")
        else:
            messagebox.showerror("Error", "Mobil dengan ID yang sama sudah ada dalam sistem.")
•	Jika mobil belum ditemukan, maka metode tambah_kendaraan dipanggil untuk menambahkan mobil ke dalam sistem. Informasi mobil juga ditampilkan menggunakan messagebox.
•	Jika mobil sudah ada, tampilkan pesan kesalahan menggunakan messagebox.showerror.
g.	Metode tambah_penyewa
 def tambah_penyewa(self):
	Mengambil data input
id_penyewa = self.entry_id_penyewa.get()
        nama = self.entry_nama.get()
        nomor_telepon = self.entry_nomor_telepon.get()
        alamat = self.entry_alamat.get()
        id_mobil_disewa = self.entry_id_mobil_sewa.get()
        durasi_sewa = int(self.entry_durasi_sewa.get())
        harga_sewa = self.get_harga_sewa_from_database(id_mobil_disewa)
Mengambil data input dari elemen GUI (Entry) yang digunakan untuk memasukkan informasi penyewa dan mobil yang akan disewa.
	Memeriksa ketersedian mobil
mobil_ditemukan = False
        for mobil in self._daftar_kendaraan:
            if mobil._id_kendaraan == id_mobil_disewa and mobil._ketersediaan:
                mobil_ditemukan = True
                harga_sewa = mobil._harga_sewa
                break
Melakukan iterasi pada daftar kendaraan untuk memeriksa apakah mobil dengan ID yang diinginkan tersedia.
	Tambahkan penyewa jika mobil tersedia
if mobil_ditemukan or self.check_mobil_exist(id_mobil_disewa):
else:
            messagebox.showerror("Error", "Mobil belum tersedia atau ID Mobil tidak ditemukan.")
•	Jika mobil ditemukan atau ID mobil valid, lanjutkan ke langkah berikutnya.
•	Jika mobil tidak ditemukan atau ID mobil tidak valid, tampilkan pesan kesalahan menggunakan messagebox.showerror.
	Membuat objek penyewa baru dan menambahkannya ke dalam list daftar_penyewa
penyewa_baru = Penyewa(id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, durasi_sewa)
self._daftar_penyewa.append(penyewa_baru)
mmembuat objek dari kelas penyewa menggunakan data input yang telah diambil
	Memperbarui informasi mobil dan harga sewa
for mobil in self._daftar_kendaraan:
                if mobil._id_kendaraan == id_mobil_disewa:
                    mobil._ketersediaan = False
                    break
            total_harga_sewa = harga_sewa * durasi_sewa
            penyewa_baru._total_harga_sewa = total_harga_sewa
•	Memperbarui status ketersediaan mobil menjadi tidak tersedia.
•	Menghitung total harga sewa berdasarkan harga sewa mobil dan durasi sewa.
	Menyimpan data penyewa ke database
self.cursor.execute('''
            INSERT INTO penyewa (id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, durasi_sewa, total_harga_sewa)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (penyewa_baru._id_penyewa,penyewa_baru._nama, penyewa_baru._nomor_telepon, penyewa_baru._alamat,
                penyewa_baru._id_mobil_disewa, penyewa_baru._durasi_sewa, penyewa_baru._total_harga_sewa))
            self.conn.commit()
	Menampilkan informasi penyewa
print(f"Informasi Penyewa Ditambahkan: {penyewa_baru.informasi()}")
	Menampilkan mesagebox dengan informasi penyewa
messagebox.showinfo("Informasi Penyewa Ditambahkan",
                                f"ID Mobil Sewa \t        : {penyewa_baru._id_mobil_disewa}\n"
                                f"ID Penyewa \t        : {penyewa_baru._id_penyewa}\n"
                                f"Nama \t\t        : {penyewa_baru._nama}\n"
                                f"Nomor Telepon \t        : {penyewa_baru._nomor_telepon}\n"
                                f"Alamat \t\t        : {penyewa_baru._alamat}\n"
                                f"Durasi Sewa \t        : {penyewa_baru._durasi_sewa} hari\n"
                                f"Total Harga Sewa \t        : {penyewa_baru._total_harga_sewa}\n"
                                f"Tanggal Sewa \t        : {tanggal_sewa.strftime('%Y-%m-%d')}\n"
                                f"Tanggal Pengembalian : {tanggal_pengembalian.strftime('%Y-%m-%d')}")
	Menampilkan informasi penyewa di console
print("=========Informasi Penyewa Ditambahkan=========")
            print(f"| ID Mobil Sewa       : {penyewa_baru._id_mobil_disewa}")
            print(f"| ID Penyewa          : {penyewa_baru._id_penyewa}")
            print(f"| Nama                : {penyewa_baru._nama}")
            print(f"| Nomor Telepon       : {penyewa_baru._nomor_telepon}")
            print(f"| Alamat              : {penyewa_baru._alamat}")
            print(f"| Durasi Sewa         : {penyewa_baru._durasi_sewa} hari")
            print(f"| Total Harga Sewa    : {penyewa_baru._total_harga_sewa}")
            print(f"| Tanggal Sewa        : {tanggal_sewa.strftime('%Y-%m-%d')}")
            print(f"| Tanggal Pengembalian: {tanggal_pengembalian.strftime('%Y-%m-%d')}")
h.	Metode check_mobil_exist
Fungsi ini Digunakan untuk memeriksa keberadaan mobil dengan iD tertentu di dalam database
def check_mobil_exist(self, id_mobil):
        self.cursor.execute("SELECT COUNT(*) FROM kendaraan WHERE id_kendaraan = %s", (id_mobil,))
        count = self.cursor.fetchone()[0]
        return count > 0
•	Melalui self.cursor.execute, sebuah query SQL dieksekusi. Query ini menghitung jumlah mobil yang memiliki ID yang sesuai dengan parameter yang diberikan.
•	Query SQL menggunakan parameter %s untuk menghindari SQL injection. Pada saat eksekusi, nilai parameter diberikan sebagai tupel kedua dalam metode execute.
•	self.cursor.fetchone() digunakan untuk mengambil satu baris hasil dari query yang dieksekusi. Karena query hanya menghitung jumlah mobil, hasilnya berupa satu angka (integer).
•	Fungsi ini mengembalikan nilai boolean (True atau False) berdasarkan hasil pemeriksaan keberadaan mobil. Jika jumlah mobil dengan ID tertentu lebih dari 0, maka fungsi mengembalikan True, yang menandakan bahwa mobil tersebut ada dalam database. Sebaliknya, jika jumlahnya 0, fungsi mengembalikan False, menandakan bahwa mobil dengan ID tersebut tidak ditemukan dalam database.
i.	Metode get_harga_sewa_from_database
Fungsi ini Digunakan untuk mengambil harga sewa mobil dari database berdasarkan ID mobil yang diberikan sebagai parameter.
def get_harga_sewa_from_database(self, id_mobil):
        self.cursor.execute("SELECT harga_sewa FROM kendaraan WHERE id_kendaraan = %s", (id_mobil,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
•	Melalui self.cursor.execute, sebuah query SQL dieksekusi. Query ini memilih harga_sewa dari tabel kendaraan berdasarkan ID kendaraan yang sesuai dengan parameter yang diberikan.
•	Query SQL menggunakan parameter %s untuk menghindari SQL injection. Pada saat eksekusi, nilai parameter diberikan sebagai tupel kedua dalam metode execute.
•	self.cursor.fetchone() digunakan untuk mengambil satu baris hasil dari query yang dieksekusi. Hasilnya berupa tupel yang berisi nilai harga_sewa.
•	Dilakukan pengecekan if result: untuk memastikan bahwa hasil query tidak kosong. Jika hasilnya ada (tidak None), maka fungsi mengembalikan nilai harga_sewa yang terdapat pada indeks 0 dari tupel hasil query.
•	Jika hasil query kosong (tidak ada mobil dengan ID tersebut), maka fungsi mengembalikan None.
j.	Metode setup_gui
def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Sistem Peminjaman Mobil")
        width = 500
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)
        self.root.geometry(f"{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}")
        self.root.resizable(False, False)
        label_id_mobil = tk.Label(self.root, text="ID Mobil:", font=("Arial", 10, "bold"), fg="#333333")
        label_id_mobil.pack()
        self.entry_id_mobil = tk.Entry(self.root, width=40)
        self.entry_id_mobil.pack()
        label_merk = tk.Label(self.root, text="Merk:", font=("Arial", 10, "bold"), fg="#333333")
        label_merk.pack()
        self.entry_merk = tk.Entry(self.root, width=40)
        self.entry_merk.pack()
        label_model = tk.Label(self.root, text="Model:", font=("Arial", 10, "bold"), fg="#333333")
        label_model.pack()
        self.entry_model = tk.Entry(self.root, width=40)
        self.entry_model.pack()
        label_tahun = tk.Label(self.root, text="Tahun:", font=("Arial", 10, "bold"), fg="#333333")
        label_tahun.pack()
        self.entry_tahun = tk.Entry(self.root, width=40)
        self.entry_tahun.pack()
        label_harga_sewa_mobil = tk.Label(self.root, text="Harga Sewa per Hari:", font=("Arial", 10, "bold"), fg="#333333")
        label_harga_sewa_mobil.pack()
        self.entry_harga_sewa_mobil = tk.Entry(self.root, width=40)
        self.entry_harga_sewa_mobil.pack()
        btn_tambah_mobil = tk.Button(self.root, text="Tambah Mobil", command=self.tambah_mobil, bg="#4CAF50", fg="white")
        btn_tambah_mobil.pack(pady=10)
        label_id_penyewa = tk.Label(self.root, text="ID Penyewa:", font=("Arial", 10, "bold"), fg="#333333")
        label_id_penyewa.pack()
        self.entry_id_penyewa = tk.Entry(self.root, width=40)
        self.entry_id_penyewa.pack()
        label_nama = tk.Label(self.root, text="Nama:", font=("Arial", 10, "bold"), fg="#333333")
        label_nama.pack()
        self.entry_nama = tk.Entry(self.root, width=40)
        self.entry_nama.pack()
        label_nomor_telepon = tk.Label(self.root, text="Nomor Telepon:", font=("Arial", 10, "bold"), fg="#333333")
        label_nomor_telepon.pack()
        self.entry_nomor_telepon = tk.Entry(self.root, width=40)
        self.entry_nomor_telepon.pack()
        label_alamat = tk.Label(self.root, text="Alamat:", font=("Arial", 10, "bold"), fg="#333333")
        label_alamat.pack()
        self.entry_alamat = tk.Entry(self.root, width=40)
        self.entry_alamat.pack()
        label_id_mobil_sewa = tk.Label(self.root, text="ID Mobil Sewa:", font=("Arial", 10, "bold"), fg="#333333")
        label_id_mobil_sewa.pack()
        self.entry_id_mobil_sewa = tk.Entry(self.root, width=40)
        self.entry_id_mobil_sewa.pack()
        label_durasi_sewa = tk.Label(self.root, text="Durasi Sewa (hari):", font=("Arial", 10, "bold"), fg="#333333")
        label_durasi_sewa.pack()
        self.entry_durasi_sewa = tk.Entry(self.root, width=40)
        self.entry_durasi_sewa.pack()
        btn_tambah_penyewa = tk.Button(self.root, text="Tambah Penyewa", command=self.tambah_penyewa, bg="#4CAF50", fg="white")
        btn_tambah_penyewa.pack(pady=10)
self.root.mainloop()
	Inisialisasi GUI
•	self.root adalah objek utama dari aplikasi GUI yang mewakili jendela utama.
•	Beberapa konfigurasi seperti judul jendela, ukuran, dan posisi diatur pada inisialisasi
	Pengaturan komponen GUI untuk kendaraan
•	Label dan entry widgets ditambahkan untuk menerima input terkait kendaraan seperti ID Mobil, Merk, Model, Tahun, dan Harga Sewa per Hari.
•	Tombol "Tambah Mobil" juga ditambahkan, dan pada saat ditekan, memanggil metode tambah_mobil dari objek self.
	Pengatuuran komponen GUI untuk penyewa
•	Label dan entry widgets ditambahkan untuk menerima input terkait penyewa seperti ID Penyewa, Nama, Nomor Telepon, Alamat, ID Mobil Sewa, dan Durasi Sewa.
•	Tombol "Tambah Penyewa" juga ditambahkan, dan pada saat ditekan, memanggil metode tambah_penyewa dari objek self.
	Loop Utama
•	self.root.mainloop() memulai loop utama GUI, sehingga aplikasi tetap berjalan dan merespons input pengguna.
Seluruh antarmuka pengguna diatur dan ditampilkan melalui metode setup_gui. Saat tombol "Tambah Mobil" atau "Tambah Penyewa" ditekan, aplikasi akan memanggil metode yang sesuai untuk menambahkan entri baru ke dalam daftar kendaraan atau penyewa, serta menyimpan informasi tersebut di dalam database.
6.	Program utama 
if __name__ == "__main__":
    app = AplikasiPeminjamanMobil()
kode ini akan membuat objek AplikasiPeminjamanMobil dan menjalankan aplikasi tersebut jika skrip dieksekusi secara langsung.






Tampilan GUI
Tampilan awal GUI

 

Tampilan ketika button tambah mobil di klik 
 
Tampilan ketika button tambah penyewa di klik

 

Tampilan jika ingin menambahkan daftar mobil dan ID Mobil yang diinputkan sama 

 

Tampilan jika ingin menambahkan daftar penyewa dan ID Mobil yang diinputkan tidak terdaftar

 
Tampilan terminal python
Tampilan setelah di klik button tambah mobil
 







Tampilan setelah di klik button tambah penyewa
 
Tampilan DataBase
Tampilan database sewa
 

Tampilan tabel kendaraan
 
Tampilan tabel penyewa
 












BAB III Penutupan
Kesimpulan  
Antarmuka pengguna (GUI) yang telah didesain memastikan responsivitas tinggi, sehingga memberikan pengalaman pengguna yang efisien dan lancar. Elemen-elemen GUI, seperti tombol, input, dan label, ditempatkan dengan cara yang intuitif, memudahkan pengguna untuk berinteraksi dengan sistem. Sistem ini berhasil menghadapi tantangan dalam manajemen armada mobil dengan menggunakan class dan struktur data yang tepat, memungkinkan pengelolaan informasi armada, termasuk penambahan dan penghapusan mobil, dilakukan dengan baik.
Masalah keterbatasan informasi berhasil diatasi oleh sistem ini, yang menyediakan data yang akurat dan terkini. Penggunaan database, seperti MySQL Connector, memungkinkan akses dan penyimpanan informasi mengenai armada mobil dan data penyewa dengan efisien. Efisiensi proses peminjaman mobil meningkat berkat kemudahan dalam manajemen penyewaan, pelacakan armada, dan akses cepat ke informasi yang relevan, memberikan kontribusi positif terhadap efisiensi operasional penyedia jasa penyewaan mobil.































Pembagian Tugas :
1.	Program
- Andata Leonardo(5220411294)
- Faras Sulthan Pratama(5220411318)
- Siti Inayatul Mufidah(5220411319)
2.	Class Diagram
- Andata Leonardo(5220411294)
- Faras Sulthan Pratama(5220411318)
3.	Laporan
- Shafira Nur Alfiah(5220411292)
- Siti Inayatul Mufidah(5220411319)
4.	PPT
- Gebriella Wahyuni Sirait(5220411231)
- Shafira Nur Alfiah(5220411292)
Link Github
https://github.com/inayatul26/projek.git









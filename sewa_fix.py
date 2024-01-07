import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import mysql.connector

class Kendaraan:
    def __init__(self, id_kendaraan, merk, model, tahun):
        self._id_kendaraan = id_kendaraan
        self._merk = merk
        self._model = model
        self._tahun = tahun
        self._ketersediaan = True

    def informasi(self):
        return f"{self._merk} {self._model} ({self._tahun})"

class Mobil(Kendaraan):
    def __init__(self, id_mobil, merk, model, tahun, harga_sewa):
        super().__init__(id_mobil, merk, model, tahun)
        self._harga_sewa = harga_sewa

    def informasi(self):
        return f"{super().informasi()} - Harga Sewa: {self._harga_sewa}"

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

class AplikasiPeminjamanMobil:
    def __init__(self):
       
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='sewa'
        )
        self.cursor = self.conn.cursor()    
        self._daftar_kendaraan = []
        self._daftar_penyewa = []
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

        self.setup_gui()

    def tambah_kendaraan(self, kendaraan):
        self.cursor.execute('''
            INSERT INTO kendaraan (id_kendaraan, merk, model, tahun, ketersediaan, harga_sewa)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', (kendaraan._id_kendaraan, kendaraan._merk, kendaraan._model, kendaraan._tahun, 1, kendaraan._harga_sewa ))
        self.conn.commit()
        print(f"Informasi Kendaraan Ditambahkan: {kendaraan.informasi()}")
        self._daftar_kendaraan.append(kendaraan)

    def tambah_mobil(self):
        id_mobil = self.entry_id_mobil.get()
        merk = self.entry_merk.get()
        model = self.entry_model.get()
        tahun = self.entry_tahun.get()
        harga_sewa = int(self.entry_harga_sewa_mobil.get())

        mobil_baru = Mobil(id_mobil, merk, model, tahun, harga_sewa)
        mobil_ditemukan = False
        for mobil in self._daftar_kendaraan:
            if mobil._id_kendaraan == id_mobil:
                mobil_ditemukan = True
                break

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

    def tambah_penyewa(self):
        id_penyewa = self.entry_id_penyewa.get()
        nama = self.entry_nama.get()
        nomor_telepon = self.entry_nomor_telepon.get()
        alamat = self.entry_alamat.get()
        id_mobil_disewa = self.entry_id_mobil_sewa.get()
        durasi_sewa = int(self.entry_durasi_sewa.get())
        harga_sewa = self.get_harga_sewa_from_database(id_mobil_disewa)
        mobil_ditemukan = False
        for mobil in self._daftar_kendaraan:
            if mobil._id_kendaraan == id_mobil_disewa and mobil._ketersediaan:
                mobil_ditemukan = True
                harga_sewa = mobil._harga_sewa
                break

        if mobil_ditemukan or self.check_mobil_exist(id_mobil_disewa):
            penyewa_baru = Penyewa(id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, durasi_sewa)
            self._daftar_penyewa.append(penyewa_baru)
            for mobil in self._daftar_kendaraan:
                if mobil._id_kendaraan == id_mobil_disewa:
                    mobil._ketersediaan = False
                    break
            total_harga_sewa = harga_sewa * durasi_sewa
            penyewa_baru._total_harga_sewa = total_harga_sewa

            tanggal_sewa = datetime.now().date()
            tanggal_pengembalian = tanggal_sewa + timedelta(days=durasi_sewa)
            self.cursor.execute('''
            INSERT INTO penyewa (id_penyewa, nama, nomor_telepon, alamat, id_mobil_disewa, durasi_sewa, total_harga_sewa)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (penyewa_baru._id_penyewa, penyewa_baru._nama, penyewa_baru._nomor_telepon, penyewa_baru._alamat,
                penyewa_baru._id_mobil_disewa, penyewa_baru._durasi_sewa, penyewa_baru._total_harga_sewa))
            self.conn.commit()
            print(f"Informasi Penyewa Ditambahkan: {penyewa_baru.informasi()}")
            
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
        else:
            messagebox.showerror("Error", "Mobil belum tersedia atau ID Mobil tidak ditemukan.")
    def check_mobil_exist(self, id_mobil):
        self.cursor.execute("SELECT COUNT(*) FROM kendaraan WHERE id_kendaraan = %s", (id_mobil,))
        count = self.cursor.fetchone()[0]
        return count > 0
    def get_harga_sewa_from_database(self, id_mobil):
        self.cursor.execute("SELECT harga_sewa FROM kendaraan WHERE id_kendaraan = %s", (id_mobil,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None
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

        # Menambahkan komponen GUI untuk penyewa
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

if __name__ == "__main__":
    app = AplikasiPeminjamanMobil()

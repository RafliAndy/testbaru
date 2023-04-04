class Pengguna():
    def __init__(self, nama, umur, jenis_kelamin):
        self.nama = nama
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin

    def tampilkan_detail(self):
        print("data pribadi")
        print("")
        print("nama: ", self.nama)
        print("umur: ", self.umur)
        print("jenis_kelamin: ", self.jenis_kelamin)

class Bank(Pengguna):
    def __init__(self, nama, umur, jenis_kelamin):
        super().__init__(nama, umur, jenis_kelamin)
        self.saldo = 0

    def lihat_saldo(self):
        self.tampilkan_detail()
        print("Saldo: Rp", self.saldo)

    def setoran(self,jumlah):
        self.jumlah = jumlah
        self.saldo = self.saldo + self.jumlah
        print("Saldo anda telah diperbarui: Rp", self.saldo)

    def penarikan(self,jumlah):
        self.jumlah = jumlah
        if self.jumlah > self.saldo:
            print("Saldo anda tidak cukup untuk melakukan penarikan: Rp", self.saldo)
        else:
            self.saldo = self.saldo - self.jumlah
            print("Sisa saldo anda: Rp", self.saldo)

    def transfer(self, nama_tujuan, jumlah):
        self.jumlah = jumlah
        self.nama_tujuan = nama_tujuan
        if self.jumlah > self.saldo:
            print("Transfer ke rekening tujuan", self.nama_tujuan, "gagal, saldo tidak cukup: Rp", self.saldo)
        else:
            self.saldo = self.saldo - self.jumlah
            print("Transfer ke rekening tujuan", self.nama_tujuan, "berhasil, sisa saldo sebesar: Rp", self.saldo)

nama = str(input("Masukkan Username anda: "))
umur = int(input("Umur anda: "))
jenis_kelamin = input("Pria/Wanita: ")

akun = Bank(nama,umur,jenis_kelamin)
akun.tampilkan_detail()
pilihan = int(input("Apa yang ingin dilakukan? \n"
                    "1. lihat saldo\n"
                    "2. Setoran tunai\n"
                    "3. Tarik tunai\n"
                    "4. Transfer dana\n"
                    "5. Keluar\n"))
while pilihan>=1 and pilihan<=5:
    if pilihan == 1:
        akun.lihat_saldo()
        pilihan = int(input("Apa yang ingin dilakukan selanjutnya? \n"
                            "1. lihat saldo\n2. Setoran tunai\n"
                            "3. Tarik tunai\n4. Transfer dana\n5. Keluar\n"))
    elif pilihan == 2:
        setoran = int(input("Masukkan jumlah tunai setoran: "))
        akun.setoran(setoran)
        pilihan = int(input("Apa yang ingin dilakukan selanjutnya? \n"
                            "1. lihat saldo\n2. Setoran tunai\n"
                            "3. Tarik tunai\n4. Transfer dana\n5. Keluar\n"))
    elif pilihan == 3:
        tarik = int(input("Masukkan jumlah tunai penarikan: "))
        akun.penarikan(tarik)
        pilihan = int(input("Apa yang ingin dilakukan selanjutnya? \n"
                            "1. lihat saldo\n2. Setoran tunai\n"
                            "3. Tarik tunai\n4. Transfer dana\n5. Keluar\n"))
    elif pilihan == 4:
        tujuan = input("Nama tujuan: ")
        transfer = int(input("Masukkan jumlah tunai yang ingin di transfer: "))
        akun.transfer(tujuan, transfer)
        pilihan = int(input("Apa yang ingin dilakukan selanjutnya? \n"
                            "1. lihat saldo\n2. Setoran tunai\n"
                            "3. Tarik tunai\n4. Transfer dana\n5. Keluar\n"))
    else:
        print(f"Terimakasih {nama}")
        break
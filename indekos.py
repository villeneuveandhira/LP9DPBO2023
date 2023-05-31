""" Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Latihan 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin. """

""" import """
from hunian import Hunian

""" class """
class Indekos(Hunian):
    # constructor
    def __init__(self, nama_pemilik, nama_penghuni, jml_penghuni, size, foto):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.jml_penghuni = jml_penghuni
        self.size = size
        self.foto = foto

    # method(s)
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_jml_penghuni(self):
        return self.jml_penghuni
    
    def get_size(self):
        return self.size
    
    def get_foto(self):
        return self.foto

    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik = " + self.get_nama_pemilik() + "\nNama Penghuni = " + self.get_nama_penghuni() + "\nJumlah Penghuni = " + self.get_jml_penghuni() + "\nUkuran = " + self.get_size() + "\n"
""" Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Latihan 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin. """

""" import """
from hunian import Hunian

""" class """
class Rumah(Hunian):
    # constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, size, foto):
        super().__init__("Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.size = size
        self.foto = foto

    # method(s)
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_size(self):
        return self.size
    
    def get_foto(self):
        return self.foto
    
    def get_detail(self):
        return str(super().get_summary()) + "\nNama Pemilik: " + self.get_nama_pemilik() + "\nUkuran: " + self.get_size() + "\n"
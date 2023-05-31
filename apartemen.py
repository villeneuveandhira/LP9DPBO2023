""" Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Latihan 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin. """

""" import """
from hunian import Hunian

""" class """
class Apartemen(Hunian):
    # constructor
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, jml_lantai, size, foto):
        super().__init__("Apartemen", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik
        self.jml_lantai = jml_lantai
        self.size = size
        self.foto = foto

    # method(s)
    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_jml_lantai(self):
        return self.jml_lantai
    
    def get_size(self):
        return self.size
    
    def get_foto(self):
        return self.foto
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"
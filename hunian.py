""" Saya Villeneuve Andhira Suwandhi NIM 2108067 mengerjakan Latihan 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan.
Aamiin. """

""" class """
class Hunian():
    # constructor
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar

    # method(s)
    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.get_jenis() +"\nJumlah Penghuni = " + str(self.get_jml_penghuni()) + " orang.\n" + "Jumlah Kamar = " + str(self.get_jml_kamar()) + " Kamar.\n" + "Dokumen = " + str(self.get_dokumen())
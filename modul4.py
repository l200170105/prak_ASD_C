#Nama  : Inarotul Qolbiyah
#Nim   : L200170105
#Kelas : C
#Modul : 4

class Mahasiswa(object):
    """Class Manusia yang dibangun dari class manusia"""
    def __init__(self,nama,NIM,kota,us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
c0 = Mahasiswa ('Christopher',97,'Jakarta', 600000)
c1 = Mahasiswa ('Felix',9,'Sydney', 1000000)
c2 = Mahasiswa ('Kevin',3,'Amerika', 2000000)
c3 = Mahasiswa ('Mark',94,'Toronto',1000000)
c4 = Mahasiswa ('Jackson',93,'Bali', 300000)
c5 = Mahasiswa ('Mina',96,'Yogyakarta', 250000)
c6 = Mahasiswa ('Johnnny',95,'Surabaya', 40000)
c7 = Mahasiswa ('Tony',1,'Malang', 400000)
c8 = Mahasiswa ('Jeffrey',14,'Palangkaraya', 600000)
c9 = Mahasiswa ('Nancy',2,'Bandung', 500000)
c10 = Mahasiswa ('Timotee',98,'Bekasi', 700000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#1
def cariIndex(wadah,target):
    a = []
    b = 0
    for i in wadah:
        if i.kotaTinggal == target:
            a.append(b)
            b += 1
        else :
            b += 1
    return a
print ("Nomor 1")
print(cariIndex(Daftar, "Klaten"))

#2
def cariTerkecil (self):
    terkecil = self[0].uangSaku
    for i in self:
        if i.uangSaku < terkecil :
            terkecil = i.uangSaku
    return terkecil
print ("\nNomor 2")
print(cariTerkecil(Daftar))      

#3
def cariTerkecil (self):
    terkecil = self[0].uangSaku
    c = []
    for i in self:
        if i.uangSaku < terkecil :
            c.append ((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
    return c
print ("\nNomor 3")
print(cariTerkecil(Daftar))   

#4
def cariTerkecil (self):
    terkecil = 250000
    d = []
    for i in self:
        if i.uangSaku < 250000 :
            d.append((i.nama, i.NIM, i.kotaTinggal, i.uangSaku))
    for i in d :
        print (i)
print ("\nNomor 4")
print(cariTerkecil(Daftar))

#no5
class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Data", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Data", cari, "tidak ada linked list")
                break
a = node (12)
menu = a
a.next = node (34)
a = a.next
a.next = node (10)
a = a.next
a.next = node (45)

print ("\nNomor 5")
menu.cari(10)
menu.cari(110)

#no6
def binSe(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low <= high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            data.append(kumpulan.index(target))
            return True
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
        #Jika runtutnya tidak bisa dibelah lagi, berarti targetnya tidak ada
    return False

list = [35, 67, 89, 57, 689]
target1 = 345
target2 = 67

print ("\nNomor 6")
print ("nilai target :", target1)
print (binSe(list, target1))

print ("\n nilai target :", target2)
print (binSe(list, target2))

#no7
def binSearch(kumpulan, target):
    #Mulai dari seluruh runtutan elemen
    low = 0
    high = len(kumpulan) -1
    data = []

    #Secara berulang belah runtutan itu menjadi separuhnya
    #sampai targetnya ditemukan
    while low != high:
        #Temukan pertengahan runtut itu
        mid = (high + low) //2
        #Apakah pertengahannya memuat target?
        if kumpulan[mid] == target:
            break
        #ataukah targetnya di sebelah kirinya?
        elif target < kumpulan[mid]:
            high = mid -1
        #ataukah targetnya di sebelah kanannya?
        else :
            low = mid +1
    for i in range (low, high):
        if target == kumpulan[i]:
            data.append(i)
    return data
lis = [2, 3, 4, 5, 6, 7, 8, 9, 9, 12]
cari = 9

print ("\nNomor 7")
print ("posisi data ", cari, "pada list ", lis, "adalah ")
print (binSearch(lis, cari))

#8
print ("""\nNomor 8
Ada 2 kemungkinan pola yang bisa digunakan.
Misalkan, angka yang akan ditebak adalah 70.

Pola pertama :
    a = nilai tebakan pertama // 2
    tebakan selanjutnya = nilai tebakan "lebih dari" + a
    
    "jika hasil tebakab selanjutnya "kurang dari", maka nilai yang dipakai tetap
    nilai lebih dari sebelumnya"

    a = a // 2
    
Simulasi
    tebakan 1 : 50 (mengambil nilai tengah) jawaban "lebih dari itu"
    tebakan 2 : 75 (lebih dari 50) jawaban "kurang dari itu"
    tebakan 3 : 62 (kurang dari 75) jawaban "lebih dari itu"
    tebakan 4 : 68 (lebih dari 62) jawaban "lebih dari itu"
    tebakan 5 : 71 (lebih dari 68) jawaban "kurang dari itu"
    tebakan 6 : 69 (kurang dari 71) jawaban "lebih dari itu"
    tebakan 7 : antara 71 dan 69, jadi jawabannya 70

Pola kedua :
    menggunakan barisan geometri Sn = 2^n

    Barisan yang terjadi 2, 4, 8, 16, 32, 64
    Misal angka yang akan ditebak adalah 68
    tebakan 1 : 64 jawaban "lebih dari itu"
    tebakan 2 : 96 (64 + 32) jawaban "kurang dari itu"
    tebakan 3 : 80 (64 + 16) jawaban "kurang dari itu"
    tebakan 4 : 72 (64 + 8) jawaban "kurang dari itu"
    tebakan 5 : 68 (64 + 4) jawaban "lebih dari itu"
    tebakan 6 : 70 (64 + 2) jawaban "Pas"
""")

    

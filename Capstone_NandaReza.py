data_mahasiswa = {
    "101117043" : {
        "Nama" :"Julio Cesar",
        "Prodi" :"Teknik Industri",
        "Jenis Kelamin" :"Pria",
        "Kota":"Polewali"
    },
    "101117064" : {
        "Nama" :"Muhammad Nanda ",
        "Prodi" :"Teknik Geofisika",
        "Jenis Kelamin" :"Pria",
        "Kota":"Bengkulu"
    }
    
}

def MenuUtama():
    print(''' 
          
    ========= SELAMAT DATANG DI DATA MAHASISWA ========
    
    Menu Data Mahasiswa:
    1. Menampilkan Data Mahasiswa
    2. Menambahkan Data Mahasiswa
    3. Menghapus data mahasiswa
    4. Update Data Mahasiswa
    5. Exit
    
    ==================================================
    ''')
    pilihan = input("Masukkan Pilihan: ")
    if pilihan == '1':
        submenampilkan()
    elif pilihan == '2':
        Menambahkan()
    elif pilihan == '3':
        Menghapus()
    elif pilihan == '4':
        Mengupdate()
    elif pilihan == '5':
        keluar=input('''
                     Anda Yakin ingin meninggalkan aplikasi?  
                     1.YA  
                     2.TIDAK''')
        if keluar == "1":
            print("Terima kasih!")
        elif keluar == "2":
            MenuUtama()
        else:
            print("Data yang Anda Masukkan Salah")
            MenuUtama()
    else:
        print("Pilihan yang Anda Masukkan Malah.")
        MenuUtama()


def Menampilkan():
    for i in data_mahasiswa:
        print(f'{i}\t|{data_mahasiswa[i]["Nama"] :20}\t|  {data_mahasiswa[i]["Prodi"]:15}\t| {data_mahasiswa[i]["Jenis Kelamin"]:7} \t|  {data_mahasiswa[i]["Kota"] :10}')

def submenampilkan():
    print('''
          ======== Menu Data Mahasiswa ========

          1.Tampilkan semua data Mahasiswa  
          2.Cari Mahasiswa  
          3.Kembali
          
          
          ======================================
          ''')
    subtampil = (input("Masukkan Pilihan Anda: "))
    if subtampil == "1":
        Menampilkan()
        submenampilkan()
    elif subtampil =="2":
        Mahasiswa =(input("Masukkan NIM Mahasiswa : "))
        Mahasiswa.isdigit()
        if Mahasiswa in data_mahasiswa:
            print(data_mahasiswa[Mahasiswa])
            submenampilkan()
        else:
            print("Data tidak ada")
            print('='*50)
            submenampilkan()
    
    elif subtampil=="3":
        MenuUtama()
    
    else:
        print("data yang anda masukkan tidak valid")
        print('='*50)
        submenampilkan()


 
 
       
def Menambahkan():
    print('''
         ======Menu Menambahkan Data Mahasiswa======

        1.Apakah Anda Ingin Menambahkan Data?  
        2.Kembali
        
        ============================================
          
          
          ''')
    subtambah = input("Masukan pilihan anda: ")
    if subtambah == "1":
        kode_baru = (input("Masukkan NIM Baru: "))
        if (kode_baru) in data_mahasiswa.keys():
            print("Data Mahasiswa Sudah Ada")
            Menambahkan()
    
        else:
            nama_baru = input("Masukkan Nama Mahasiswa\t:")
            prodi_baru = input("Masukkan Prodi Mahasiswa\t:")
            Jenis_Kelamin = input("Masukkan Jenis Kelamin (Pria/Wanita)\t:")
            Kota_baru = input("Masukkan asal kota\t:")
        
            data_mahasiswa.update(
            {(kode_baru) : {
                    "Nama" : (nama_baru),
                    "Prodi" : (prodi_baru),
                    "Jenis Kelamin" : (Jenis_Kelamin),
                    "Kota" :(Kota_baru)
                }
            }
            )
            
        print('''
              Apakah Ingin Menyimpan Data? 
              1.YA 
              2.TIDAK
              ''')
        subtambah = input("Masukkan Pilihan Anda: ")
        if subtambah == "1":
            print("Data sudah Tersimpan")
            Menampilkan()
            Menambahkan()
            
            
           
        elif subtambah == "2":
            data_mahasiswa.pop(kode_baru)
            Menambahkan()
    elif subtambah =="2":
        MenuUtama()
    else:
        print("Data Yang anda Input Salah")
        Menambahkan()



def Menghapus():
    print('''
          
          ===== Menu Menghapus Data Mahasiswa =====
          
          
          1.Hapus data Mahasiswa  
          2.Kembali
          
          =========================================
           
          ''') 
    menu_hapus=input("Masukkan Pilihan Anda: ") 
    if menu_hapus =="1": 
        kode_hapus = (input("Masukkan NIM Mahasiswa: "))
        if kode_hapus in data_mahasiswa:
            print('''
                  Apakah Anda Ingin Menghapus Data Ini? 
                  1.YA  
                  2.TIDAK
                  ''')
            hapus = input("Masukkan Pilihan Anda: ")
            if hapus == "1":
                data_mahasiswa.pop(kode_hapus)
                print("Data Tersebut Telah dihapus")
                Menampilkan()
                Menghapus()
            elif hapus == "2":
                Menghapus()
            else:
                print("Data yang Anda Masukkan Salah!")
                Menghapus()
                
        else:
            print("Data Tidak Ada")
            Menghapus()
    elif menu_hapus == "2":
        MenuUtama()
    else:
        print("Data Input Anda Tidak Valid")
        print('='*50)
        Menghapus()



def Mengupdate():
    print('''
          ====== Menu Update Data Mahasiswa ======
          
          
          1.Update data Mahasiswa  
          2.kembali
          
          =======================================
          
          ''')
    menu_update =(input("Masukkan Pilihan Anda: "))
    if menu_update =="1":
        kode_update = (input("Masukkan NIM Mahasiswa: "))
        if kode_update in data_mahasiswa:
            pilih_update=input("Masukkan data yang ingin diupdate (Nama/Prodi/Jenis Kelamin/Prodi): ")
            x = pilih_update.capitalize()
            update=input(f"masukkan {pilih_update} baru: ")
            print('''
                  Anda Yakin Ingin Mengupdate Data? 
                  1.YA  
                  2.TIDAK
                  ''')
            update1=input("Masukkan Pilihan Anda: ")
            if update1 =="1":
                data_mahasiswa[kode_update][x]=update
                print("Data sudah diperbaharui")
                Menampilkan()
                Mengupdate()
            elif update1 == "2":
                Mengupdate()
            else:
                print("Data Tidak ada")
                Mengupdate()
        else:
            print("Data Yang Anda Cari Tidak Ada")
            Mengupdate()       
                
    elif menu_update =="2":
        MenuUtama()
    else :
        print("Data yang anda input tidak valid")
        Mengupdate()
        
        
        
MenuUtama()
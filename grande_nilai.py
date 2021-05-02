while True:
    name_siswa = input("Masukan Nama Anda : ")
    nilai_harian = float(input('Masukan Nilai Harian : '))
    nilai_uts = float(input("Masukan Nilai UTS : "))
    nilai_uas = float(input("Masukan Nilai UAS : "))
    nilai_akhir = ((nilai_harian*40)/100)+((nilai_uts*30)/100)+((nilai_uas*30)/100)

    if nilai_akhir >= 80:
        predikat_nilai = 'A'
        print("Nama Lengkap Anda =", name_siswa)
        print("Nilai Akhir Anda =", nilai_akhir)
        print("Predikat Anda =", predikat_nilai)
        
    elif nilai_akhir >= 70:
        predikat_nilai ='B'
        print("Nama Lengkap Anda =", name_siswa)
        print("Nilai Akhir Anda =", nilai_akhir)
        print("Predikat Anda =", predikat_nilai)

    elif nilai_akhir >= 60:
        predikat_nilai ='C'
        print("Nama Lengkap Anda =", name_siswa)
        print("Nilai Akhir Anda =", nilai_akhir)
        print("Predikat Anda =", predikat_nilai)

    elif nilai_akhir >=50:
        predikat_nilai ='C'
        print("Nama lengkap anda =", name_siswa)
        print("Nilai akhir anda=,", nilai_akhir)
        print("predikat adna=",predikat_nilai)
    else:
        predikat_nilai = 'E'
        print("Nama lengkap anda =", name_siswa)
        print("Nilai akhir anda=,", nilai_akhir)
        print("predikat adna=",predikat_nilai)

import random

def tebak_angka():
    angka_rahasia = random.randint(1, 10)
    percobaan = 0
    print("Selamat datang di game tebak angka")
    print("Saya sudah memilih angka 1 sampai 10 coba tebak !")

    while True:
        try:
            tebak = int(input("Masukan tebakanmu: "))
            percobaan += 1

            if tebak < angka_rahasia:
                print("Tebakan kamu terlalu rendah")
            elif tebak > angka_rahasia:
                print("Tebakan kamu terlalu tinggi")
            elif tebak == angka_rahasia:
                print(f"Selamat! kamu berhasil menebak {angka_rahasia} dalam {percobaan} percobaan.")
                break
        except ValueError:
            print('masukkan angka yang valid')
                
while True:
    tebak_angka()       
    lagi = str(input("ingin main lagi? (y/n): ").lower())
    if lagi != "y":
        print("Terimakasih")
        break


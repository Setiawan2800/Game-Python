import random

def gameSuit():
    bot = ['gunting','batu', 'kertas']
    # hasil = None
    score_bot = 0
    score_pemain = 0
    ronde = 1

    print("*"*50)
    print("*"*10 + " Selamat Datang di Game Suit  " + "*"*10)
    print("*"*50)
    print("Pilihan Terdiri Dari\nBatu\nGunting\nKertas\n")

    while True:
        print(f"\n========== Ronde {ronde} ==========")
        for i in range(5):
            x = random.choice(bot)
            print("Bot Telah memilih pilihannya")
            data = str(input("Tentukan pilihanmu sekarang: ")).lower()

            #Bagian Seri
            if data.lower() == x:
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Hasilnya Seri\n\n")

            #Bagian Menang
            elif x == 'batu' and data.lower() == 'kertas':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Menang\n\n")
                score_pemain +=1
            
            elif x == 'kertas' and data.lower() == 'gunting':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Menang\n\n")
                score_pemain +=1

            elif x == 'gunting' and data.lower() == 'batu':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Menang\n\n")
                score_pemain +=1

        #Bagian Kalah
            elif x == 'gunting' and data.lower() == 'kertas':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Kalah\n\n")
                score_bot +=1
            
            elif x == 'kertas' and data.lower() == 'batu':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Kalah\n\n")
                score_bot +=1

            elif x == 'batu' and data.lower() == 'gunting':
                print(f'pilihan Bot     : {x.capitalize()}')
                print(f'pilihan Kamu    : {data.capitalize()}')
                print("Kamu Kalah\n\n")
                score_bot +=1

            else:
                print("masukkan yang valid\n")

        print(f"\nSkor Sementara - Pemain: {score_pemain}, Bot: {score_bot}")


        tanya = input("Ingin bermain lagi?[y/n]: ").lower()
        if tanya != "y":
            print(f"\n========== Permainan Selesai ==========")
            print(f"Skor Akhir - Pemain: {score_pemain}, Bot: {score_bot}")
            if score_pemain > score_bot:
                print('Selamat! Kamu memenangkan permainan!\n')
            elif score_pemain < score_bot:
                print("Sayang sekali, Bot memenangkan permainan.\n")
            else:
                print("Permainan Berakhir Seri!\n")
            print("Terimakasih telah bermain")
            break
        ronde +=1
gameSuit()
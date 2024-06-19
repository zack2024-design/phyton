import time

print("--------------------------------------------------")
# Sambut pengguna
print("Selamat datang : Permainan Kuiz Maulidur Rasul!")
time.sleep(1)
print("--------------------------------------------------")

# Kesempatan
chances = 1
print(f"Anda harus memilih {chances} jawaban yang benar.\nAnda akan mendapatkan 1 skor jika memilih jawaban yang benar.\n")
time.sleep(2)

# Skor
score = 0

# Pertanyaan 1
print("==================================================")
print("1) Apakah nama ibu kandung Rasulullah SAW?\n(A) Aminah Binti Wahab\n(B) Halimah binti Abi Dzuaib\n(C) Maziatul binti Ahmad\n(D) Zahfrani binti Suib \n")
answer_1 = "a"

for i in range(chances):
    answer = input("Jawapan: ")
    if answer.lower() == answer_1:
        print("MASYALLAH HABIBI! BAGUS otak geliga!\n")
        score += 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print(f"JAWAPAN YANG BENAR ADALAH {answer_1}\n\n")

time.sleep(2)

# Pertanyaan 2
print("==================================================")
print("2) Siapakah nama datuk Rasulullah?\n(A) Abdullah ibn safaa\n(B) Abdul Muttalib Syaibah ibn Hashim\n(C) Jufri ibn nazwa\n(D) Safwan ibn safwanun\n")
answer_2 = "b"

for i in range(chances):
    answer = input("Jawapan: ")
    if answer.lower() == answer_2:
        print("MASYALLAH HABIBI! BAGUS otak geliga !\n")
        score += 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print(f"JAWAPAN YANG BENAR ADALAH {answer_2}\n\n")

time.sleep(2)

# Pertanyaan 3
print("==================================================")
print("3) Apakah maksud gelaran 'al-Amin' yang diberikan kepada Rasulullah ? \n(A) gagah perkasa\n(B) bergaya\n(C) setia, amanah\n(D) kacak\n")
answer_3 = "c"

for i in range(chances):
    answer = input("Jawapan: ")
    if answer.lower() == answer_3:
        print("MASYALLAH HABIBI! BAGUS otak geliga !\n")
        score += 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print(f"JAWAPAN YANG BENAR ADALAH {answer_3}\n\n")

time.sleep(2)

# Pertanyaan 4
print("==================================================")
print("4) Pada usia berapakah Nabi Muhammad meletakkan hajartul aswad pada kedudukan sekarang dengan damai dan dipersetujui oleh semua ketua kabilah?\n(A) 34\n(B) 30\n(C) 42\n(D)35\n")
answer_4 = "d"

for i in range(chances):
    answer = input("Jawapan: ")
    if answer.lower() == answer_4:
        print("MASYALLAH HABIBI! BAGUS otak geliga\n")
        score += 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print(f"JAWAPAN YANG BENAR ADALAH {answer_4}\n\n")

time.sleep(2)

# Pertanyaan 5
print("==================================================")
print("5) Pada usia berapakah selepas Baginda Rasulullah kematian isteri Saiditina Khadijah dan mengalami peristiwa israk dan mikraj?\n(A) 51\n(B) 45\n(C) 42\n(D)47\n")
answer_5 = "a"

for i in range(chances):
    answer = input("Jawapan: ")
    if answer.lower() == answer_5:
        print("MASYALLAH HABIBI! BAGUS otak geliga\n")
        score += 1
        break
    else:
        print("SALAH!\n")
        time.sleep(0.5)
        print(f"JAWAPAN YANG BENAR ADALAH {answer_5}\n\n")

time.sleep(2)

# Cetak skor
print("==================================================")
if score >= 2:
    print(f"Selamat! Skor Anda adalah {score}")
else:
    print(f"Semoga lebih beruntung lain kali! Skor Anda adalah {score}")

# Pesan perpisahan
print("Terima kasih telah bermain Permainan Kuiz Maulidur Rasul!")
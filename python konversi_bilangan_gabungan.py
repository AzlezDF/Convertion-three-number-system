def desimal_ke_biner_heksa():
    angka = int(input("Masukkan angka desimal: "))
    print(f"Desimal {angka} ke Biner: {bin(angka)[2:]}")
    print(f"Desimal {angka} ke Heksadesimal: {hex(angka)[2:].upper()}")


def biner_ke_desimal_heksa():
    angka = input("Masukkan angka biner: ").strip()
    desimal = int(angka, 2)
    print(f"Biner {angka} ke Desimal: {desimal}")
    print(f"Biner {angka} ke Heksadesimal: {hex(desimal)[2:].upper()}")


def heksa_ke_desimal_biner():
    angka = input("Masukkan angka heksadesimal (tanpa 0x): ").strip()
    desimal = int(angka, 16)
    print(f"Heksadesimal {angka.upper()} ke Desimal: {desimal}")
    print(f"Heksadesimal {angka.upper()} ke Biner: {bin(desimal)[2:]}")


def main():
    while True:
        print("\n=== PROGRAM KONVERSI BILANGAN ===")
        print("1. Desimal ke Biner dan Heksadesimal")
        print("2. Biner ke Desimal dan Heksadesimal")
        print("3. Heksadesimal ke Desimal dan Biner")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        try:
            if pilihan == "1":
                desimal_ke_biner_heksa()
            elif pilihan == "2":
                biner_ke_desimal_heksa()
            elif pilihan == "3":
                heksa_ke_desimal_biner()
            elif pilihan == "4":
                print("Program selesai. Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih 1 sampai 4.")
        except ValueError:
            print("Input tidak valid. Pastikan angka sesuai dengan basis yang dipilih.")


if __name__ == "__main__":
    main()
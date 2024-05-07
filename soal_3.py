def hitung_total_harga(jumlah_barang):
    total = 0
    for i in range(jumlah_barang):
        harga = float(input('Masukan Harga Barang ke-{}: '.format(i+1)))
        total += harga
    return total

def main():
    jumlah_barang = int(input('Masukan Jumlah Barang : '))
    total_harga = hitung_total_harga(jumlah_barang)
    print('Total Belanjaan : Rp.',total_harga)
    
if __name__ == "__main__":
    main()
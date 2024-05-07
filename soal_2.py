def tahun_kabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    else:
        return False
    
tahun = int(input('Masukan Tahun : '))

if tahun_kabisat(tahun):
    print('Tahun', tahun, 'merupakan TAHUN KABISAT')
else:
    print('Tahun', tahun, 'merupakan bukan TAHUN KABISAT')
    
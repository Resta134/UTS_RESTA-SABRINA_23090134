import soal_4perhitung

berat_badan = float(input("Masukkan berat badan Anda (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (m): "))

print('Berat Badan : ',berat_badan)
print('Tinggi Badan : ',tinggi_badan)

bmi = soal_4perhitung.hitung_bmi(berat_badan, tinggi_badan)
print('Nilai BMI Anda : ', bmi)

rekomendasi = soal_4perhitung.rekomendasi_kesehatan(bmi)
print('Kategori BMI : ', rekomendasi)

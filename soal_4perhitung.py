def hitung_bmi(berat, tinggi):
    bmi = berat / (tinggi ** 2)
    return bmi

def rekomendasi_kesehatan(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi >= 18.5 and bmi < 24.9:
        return "Berat badan normal"
    elif bmi >= 25 and bmi < 29.9:
        return "Kelebihan berat badan"
    else:
        return "Obesitas"


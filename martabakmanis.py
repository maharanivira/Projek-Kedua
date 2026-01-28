# Program Kalkulator BMI (Body Mass Index)
# Rumus: BMI = Berat (kg) / Tinggi (m)^2

def hitung_bmi(berat, tinggi):
    """Menghitung BMI dari berat badan dan tinggi"""
    bmi = berat / (tinggi * tinggi)
    return bmi

def kategorikan_bmi(bmi):
    """Mengkategorikan BMI sesuai standar WHO"""
    if bmi < 18.5:
        return "Kurus (Underweight)"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Gemuk (Overweight)"
    else:
        return "Obesitas (Obese)"

def main():
    print("=" * 50)
    print("     KALKULATOR BODY MASS INDEX (BMI)")
    print("=" * 50)
    
    # Input berat badan
    while True:
        try:
            berat = float(input("\nMasukkan berat badan (kg): "))
            if berat <= 0:
                print("Berat badan harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
    # Input tinggi badan
    while True:
        try:
            tinggi_cm = float(input("Masukkan tinggi badan (cm): "))
            if tinggi_cm <= 0:
                print("Tinggi badan harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Input tidak valid! Masukkan angka.")
    
    # Konversi tinggi dari cm ke meter
    tinggi_m = tinggi_cm / 100
    
    # Hitung BMI
    bmi = hitung_bmi(berat, tinggi_m)
    kategori = kategorikan_bmi(bmi)
    
    # Tampilkan hasil
    print("\n" + "=" * 50)
    print("HASIL PERHITUNGAN BMI")
    print("=" * 50)
    print(f"Berat badan     : {berat} kg")
    print(f"Tinggi badan    : {tinggi_cm} cm ({tinggi_m} m)")
    print(f"BMI             : {bmi:.2f}")
    print(f"Kategori        : {kategori}")
    print("=" * 50)
    
    # Tampilkan panduan kategori
    print("\nPanduan Kategori BMI:")
    print("  BMI < 18.5      : Kurus (Underweight)")
    print("  18.5 - 24.9     : Normal")
    print("  25 - 29.9       : Gemuk (Overweight)")
    print("  BMI >= 30       : Obesitas (Obese)")
    print("=" * 50)
    # Berikan saran berdasarkan kategori BMI
    print("\nSaran Kesehatan:")
    if bmi < 18.5:
        print("  • Anda kekurangan berat badan. Konsumsi makanan bergizi seimbang.")
        print("  • Tambahkan asupan protein dan kalori sehat.")
        print("  • Lakukan olahraga teratur untuk membangun massa otot.")
    elif 18.5 <= bmi < 25:
        print("  • Berat badan Anda ideal. Pertahankan gaya hidup sehat!")
        print("  • Lanjutkan pola makan seimbang dan olahraga teratur.")
    elif 25 <= bmi < 30:
        print("  • Anda memiliki berat badan berlebih. Mulai program diet.")
        print("  • Kurangi makanan tinggi lemak dan gula.")
        print("  • Tingkatkan aktivitas fisik minimal 30 menit sehari.")
    else:
        print("  • Anda mengalami obesitas. Konsultasikan dengan dokter.")
        print("  • Ikuti program diet dan olahraga yang terstruktur.")
        print("  • Pertimbangkan bantuan nutrisionis profesional.")
    print("=" * 50)
# Jalankan program
if __name__ == "__main__":
    main()

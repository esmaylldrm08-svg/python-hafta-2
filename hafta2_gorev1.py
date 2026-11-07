# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Görev 1 - Kullanıcıdan Celsius cinsinden sıcaklık alıp
#              Fahrenheit'a çeviren program.
# ==============================================================================

# Kullanıcıdan Celsius cinsinden sıcaklık değeri alınır
celsius = float(input("Sıcaklık (°C): "))

# Celsius'tan Fahrenheit'a dönüşüm formülü: F = (9 / 5) * C + 32
fahrenheit = (9 / 5) * celsius + 32

# Sonuç ekrana örnek çıktı formatında yazdırılır
print(f"{celsius} °C = {fahrenheit} °F")

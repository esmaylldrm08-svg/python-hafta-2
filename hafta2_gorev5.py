# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Görev 5 - Aylık bileşik faiz formülünü kullanarak yatırımın
#              gelecekteki değerini hesaplayan ve iki basamağa yuvarlayan program.
# ==============================================================================

# Kullanıcıdan anapara, yıllık faiz oranı ve süre bilgileri alınır
anapara = float(input("Anapara (TL): "))
yillik_faiz = float(input("Yıllık faiz (%): "))
sure_yil = float(input("Süre (yıl): "))

# Aylık bileşik faiz formülü:
# G = A * (1 + r / (12 * 100)) ** (12 * y)
aylik_oran = yillik_faiz / (12 * 100)
toplam_ay = 12 * sure_yil
gelecekteki_deger = anapara * ((1 + aylik_oran) ** toplam_ay)

# Sonuç round() fonksiyonu ile iki ondalık basamağa yuvarlanır
yuvarlanmis_deger = round(gelecekteki_deger, 2)

# Sonuç ekrana yazdırılır
print(f"Gelecekteki değer: {yuvarlanmis_deger} TL")

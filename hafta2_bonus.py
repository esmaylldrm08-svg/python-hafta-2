# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Bonus Görev - Gün, saat, dakika ve saniye alıp
#              tersine işlemle toplam saniyeyi hesaplayan program.
# ==============================================================================

# Kullanıcıdan gün, saat, dakika ve saniye değerleri tamsayı olarak alınır
gun = int(input("Gün: "))
saat = int(input("Saat: "))
dakika = int(input("Dakika: "))
saniye = int(input("Saniye: "))

# Toplam saniye hesabı:
# 1 gün = 86400 saniye (24 * 3600)
# 1 saat = 3600 saniye
# 1 dakika = 60 saniye
toplam_saniye = (gun * 86400) + (saat * 3600) + (dakika * 60) + saniye

# Sonuç ekrana yazdırılır
print(f"Toplam saniye: {toplam_saniye}")

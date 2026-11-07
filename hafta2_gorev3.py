# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Görev 3 - Girilen toplam saniyeyi yalnızca // ve %
#              operatörlerini kullanarak gün, saat, dakika ve saniyeye ayıran program.
# ==============================================================================

# Kullanıcıdan toplam saniye tamsayı olarak alınır
toplam_saniye = int(input("Saniye: "))

# 1 gün = 24 saat = 24 * 3600 = 86400 saniye
gun = toplam_saniye // 86400
kalan = toplam_saniye % 86400

# 1 saat = 3600 saniye
saat = kalan // 3600
kalan = kalan % 3600

# 1 dakika = 60 saniye
dakika = kalan // 60
saniye = kalan % 60

# Sonuç örnek çıktı biçiminde ekrana yazdırılır
print(f"{toplam_saniye} saniye = {gun} gün {saat} saat {dakika} dakika {saniye} saniye")

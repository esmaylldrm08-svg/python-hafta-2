# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Görev 4 - 0 ile 999 arasındaki bir tamsayının rakamlarını
#              // ve % operatörleri ile ayırıp toplayan program.
# ==============================================================================

# Kullanıcıdan 0 ile 999 arasında bir tamsayı alınır
sayi = int(input("Sayı (0-999): "))

# Son basamak (birler basamağı) % 10 ile elde edilir
birler = sayi % 10

# Sayının son basamağı atılır
kalan = sayi // 10

# Ortadaki basamak (onlar basamağı) % 10 ile elde edilir
onlar = kalan % 10

# En baştaki basamak (yüzler basamağı) // 10 ile elde edilir
yuzler = kalan // 10

# Rakamlar toplanır
rakamlar_toplami = yuzler + onlar + birler

# Sonuç ekrana yazdırılır
print(f"Rakamlar toplamı: {rakamlar_toplami}")

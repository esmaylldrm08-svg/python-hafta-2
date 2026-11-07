# ==============================================================================
# Ad Soyad   : Esma Yıldırım
# Öğrenci No : 20253004004
# Tarih      : 07.11.2026
# Açıklama   : Hafta 2 Görev 2 - Yarıçap ve yükseklik alarak silindirin taban
#              alanını ve hacmini hesaplayan program.
# ==============================================================================

# Pi sayısı için sabit tanımlanır
PI = 3.14159

# Kullanıcıdan silindirin yarıçapı ve yüksekliği float olarak alınır
yaricap = float(input("Yarıçap: "))
yukseklik = float(input("Yükseklik: "))

# Taban alanı ve hacim hesaplanır
# Taban Alanı = PI * r^2
# Hacim = Taban Alanı * h
taban_alani = PI * (yaricap ** 2)
hacim = taban_alani * yukseklik

# Sonuçlar ekrana yazdırılır
print(f"Taban alanı: {taban_alani}")
print(f"Hacim: {hacim}")

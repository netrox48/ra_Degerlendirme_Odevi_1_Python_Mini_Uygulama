import os

def ilac_ekle(ilac_sozlugu):
    """Kullanıcıdan ilaç bilgilerini alır, doğrular ve sözlüğe ekler."""
    print("\n--- Yeni İlaç Ekleme ---")
    
    # 1. Girdi ve Doğrulama: İlaç Adı
    while True:
        ad = input("İlaç adını giriniz: ").strip()
        if not ad:
            print("Hata: İlaç adı boş bırakılamaz! Lütfen tekrar deneyin.")
        else:
            break

    # 2. Girdi ve Doğrulama: Dozaj
    while True:
        doz = input(f"'{ad}' için dozaj bilgisini giriniz (örn: 1 tablet, 50mg): ").strip()
        if not doz:
            print("Hata: Dozaj bilgisi boş bırakılamaz! Lütfen tekrar deneyin.")
        else:
            break

    # 3. Girdi ve Doğrulama: Saat Aralığı
    while True:
        saat_str = input(f"'{ad}' kaç saatte bir alınacak? (Sadece sayı giriniz, örn: 8): ").strip()
        if not saat_str.isdigit():
            print("Hata: Lütfen geçerli bir tam sayı giriniz!")
        elif int(saat_str) <= 0:
            print("Hata: Saat aralığı 0'dan büyük olmalıdır!")
        else:
            saat = int(saat_str)
            break

    # Veriyi sözlüğe kaydetme
    ilac_sozlugu[ad] = {"doz": doz, "saat_araligi": saat}
    print(f"\nBaşarılı: {ad} ({doz}), {saat} saatte bir alınmak üzere sisteme eklendi.")


def ilaclari_listele(ilac_sozlugu):
    """Sözlükteki tüm ilaçları biçimlendirilmiş olarak ekrana yazdırır."""
    if not ilac_sozlugu:
        print("\nUyarı: Sisteme henüz eklenmiş bir ilaç bulunmuyor.")
        return

    print("\n" + "="*55)
    print(" GÜNCEL İLAÇ VE TEDAVİ LİSTESİ")
    print("="*55)
    for ad, detay in ilac_sozlugu.items():
        print(f"İlaç: {ad: <15} | Doz: {detay['doz']: <15} | Sıklık: {detay['saat_araligi']} saatte bir")
    print("="*55)


def dosyaya_kaydet(ilac_sozlugu, dosya_adi="yeni_rapor.csv"):
    """İlaç listesini projenin olduğu klasöre CSV dosyası olarak kaydeder."""
    if not ilac_sozlugu:
        print("\nUyarı: Kaydedilecek ilaç bulunmuyor. Lütfen önce ilaç ekleyin.")
        return

    try:
        # main.py dosyasının kayıtlı olduğu tam klasör yolunu alıyoruz
        proje_klasori = os.path.dirname(os.path.abspath(__file__))
        tam_dosya_yolu = os.path.join(proje_klasori, dosya_adi)

        # Dosyayı yazma (w) modunda açıyoruz
        with open(tam_dosya_yolu, "w", encoding="utf-8") as dosya:
            dosya.write("Ilac Adi,Dozaj,Saat Araligi\n")
            for ad, detay in ilac_sozlugu.items():
                dosya.write(f"{ad},{detay['doz']},{detay['saat_araligi']}\n")
                
        print(f"\nBaşarılı: İlaç listeniz güvenle kaydedildi!")
        print(f"Kaydedilen Konum: {tam_dosya_yolu}")
    except Exception as e:
        print(f"\nKritik Hata: Dosya kaydedilirken beklenmeyen bir sorun oluştu: {e}")


def ana_menu():
    """Programın ana döngüsünü ve menü yönetimini sağlar."""
    ilaclar = {}  # Tüm veriyi tutacağımız ana sözlük yapısı
    
    while True:
        print("\n--- İLAÇ/TEDAVİ HATIRLATICI PLANLAYICI ---")
        print("1. Yeni İlaç/Tedavi Ekle")
        print("2. İlaç Listesini Görüntüle")
        print("3. Listeyi Dosyaya Kaydet (.csv)")
        print("4. Çıkış")

        secim = input("Lütfen yapmak istediğiniz işlemi seçin (1-4): ").strip()

        # Karar Yapıları (if/elif/else)
        if secim == '1':
            ilac_ekle(ilaclar)
        elif secim == '2':
            ilaclari_listele(ilaclar)
        elif secim == '3':
            dosyaya_kaydet(ilaclar)
        elif secim == '4':
            print("\nProgramdan çıkılıyor. Sağlıklı günler dileriz!")
            break
        else:
            print("\nHatalı seçim! Lütfen 1 ile 4 arasında geçerli bir işlem numarası giriniz.")


if __name__ == "__main__":
    ana_menu()
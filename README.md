\# İlaç ve Tedavi Saatleri Hatırlatıcı Planlayıcı



\*\*Ders:\*\* GEP1316 Kodlama Okuryazarlığı  

\*\*Öğrenci:\*\* Berat Akça  



Bu uygulama, günlük alınması gereken ilaçları ve doz saatlerini kaydetmek, listelemek ve verileri `.csv` dosyası olarak dışa aktarmak için geliştirilmiş bir Python komut satırı (CLI) uygulamasıdır.



\## Özellikler ve Gereksinimler

\- \*\*Girdi Doğrulama:\*\* Boş bırakılan veya yanlış veri türü (harf, negatif sayı) girildiğinde program çökmez, kullanıcıyı uyarır.

\- \*\*Döngü ve Menü Yapısı:\*\* `while` döngüsü ile sürekli çalışan etkileşimli kullanıcı menüsü.

\- \*\*Karar Yapıları:\*\* Menü seçimleri ve veri kontrolleri için `if/elif/else` yapıları.

\- \*\*Veri Saklama:\*\* İlaç bilgileri dinamik Python sözlüğü (`dict`) içinde tutulur.

\- \*\*Dosya Kaydı:\*\* İlaç listesi istenildiği an `yeni\_rapor.csv` dosyasına yazılır.



\## Nasıl Çalıştırılır?

1\. Proje klasörüne gidin.

2\. \*\*`main.py`\*\* dosyasına çift tıklayın veya sağ tıklayıp \*\*Python\*\* ile açın.



\## Test Senaryoları Tablosu



| Senaryo No | Test Edilen Durum | Girilen Veri | Beklenen Sonuç | Gerçekleşen Sonuç | Durum |

| :--- | :--- | :--- | :--- | :--- | :--- |

| \*\*1\*\* | Normal İlaç Ekleme | Parol / 2 tablet / 6 | İlacın başarıyla eklenmesi | İlaç sisteme eklendi uyarısı alındı | Başarılı |

| \*\*2 (Uç)\*\* | Boş İlaç Adı Girişi | \*(Boş)\* | "Boş bırakılamaz" uyarısı | Uyarı verildi, tekrar veri istendi | Başarılı |

| \*\*3 (Hatalı)\*\*| Harf Girişi (Saat) | "beş" | "Tam sayı giriniz" uyarısı | Program çökmedi, tekrar sayı istendi | Başarılı |

| \*\*4 (Uç)\*\* | Negatif Saat Girişi | -8 | "0'dan büyük olmalı" uyarısı | Hata yakalandı, tekrar sayı istendi | Başarılı |

| \*\*5\*\* | Dosyaya Kaydetme | Menü seçeneği: 3 | CSV dosyası oluşturulması | `yeni\_rapor.csv` başarıyla oluşturuldu | Başarılı |



\## Ekran Görüntüleri



\### 1. Girdi Doğrulama ve Hata Testleri

!\[Girdi Doğrulama ve Hata Testleri](Hata.png)



\### 2. Dosya Kaydetme ve Başarılı Çalışma

!\[Dosya Kaydetme ve Başarılı Çalışma](Rapor Kaydetme.png)


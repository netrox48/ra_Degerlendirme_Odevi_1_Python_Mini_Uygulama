\# Yapay Zekâ Çalışma Günlüğü (PROMPTLAR.md)



\*\*Öğrenci:\*\* Berat Akça  

\*\*Ders:\*\* GEP1316 Kodlama Okuryazarlığı



Bu ödev sürecinde Google Gemini'yi sadece kod yazdırmak için değil, bir "çalışma arkadaşı" gibi kullanarak fikir aldım, hatalarımı çözdürdüm ve kodumu geliştirdim. Çıktıları doğrudan kopyalamak yerine test edip hatalı yerlere müdahale ettim.



\---



\### 1. Fikir ve Senaryo Bulma

\* \*\*Prompt:\*\* "GEP1316 dersi vize ödevi için Sağlık Bilimleri alanına uygun, günlük hayatta işe yarayacak bir Python komut satırı uygulaması fikri verir misin?"

\* \*\*YZ Yanıtı:\*\* İlaç Takip Sistemi, Su İçme Hatırlatıcısı ve Günlük Kalori Takipçisi olmak üzere 3 fikir sundu.

\* \*\*Kararım:\*\* İlaç takip senaryosunu kabul ettim. Çünkü ilaç saatlerini unutmak gerçek hayatta çok sık karşılaşılan bir sorun ve ödevdeki sözlük/liste yapılarını kullanmak için çok uygun bir projeydi.



\### 2. Kod İskeletini Oluşturma

\* \*\*Prompt:\*\* "En az 3 girdi alma, girdi doğrulama, karar yapısı (if/else), döngü, fonksiyonlar ve sözlük kullanan bir ilaç takip Python kodu yazar mısın?"

\* \*\*YZ Yanıtı:\*\* Menü yapısını, `while` döngüsünü ve `ilac\_ekle` gibi temel fonksiyonları içeren bir kod taslağı verdi.

\* \*\*Kararım:\*\* Düzenleyerek kabul ettim. Kodun temel mantığı ve döngüsü iyiydi ancak bilgileri bir dosyaya kaydeden kısım eksikti. Koda `.csv` formatında dışa aktarma yapan `dosyaya\_kaydet` fonksiyonunu eklettim.



\### 3. YZ Hatasının Yakalanması ve Çözülmesi (Kritik)

\* \*\*Prompt:\*\* "Kullanıcı saat aralığına sayı yerine harf girdiğinde (örn: 'beş') programın çökmesini nasıl engelleriz?"

\* \*\*YZ Yanıtı:\*\* YZ ilk başta doğrudan `saat = int(input())` yazmamı önerdi.

\* \*\*Kararım:\*\* \*\*Reddettim ve düzelttirdim.\*\* Yapay zekanın verdiği bu kod, kullanıcı harf girdiğinde `ValueError` hatası verip programı tamamen kapatıyordu. YZ'yi uyararak string kontrolü yapan `.isdigit()` metodunu ve bir `while True` döngüsünü kullanmasını sağladım. Böylece programın çökmesini engelledim.



\### 4. Dosya Kaydetme Hatası (Permission Denied)

\* \*\*Prompt:\*\* "Program 3 numaralı işlemi seçtiğimde `Permission denied: 'yeni\_rapor.csv'` hatası veriyor, bu sorunu nasıl çözeriz?"

\* \*\*YZ Yanıtı:\*\* Arka planda veya sistem klasöründe dosya izni kilitlenmesi olabileceğini, bu yüzden `os.path` modülüyle dosyanın projenin çalıştığı konuma kaydedilmesini önerdi.

\* \*\*Kararım:\*\* Kabul ettim. Koda `os.path.dirname` ve `os.path.join` komutlarını ekleyerek dosyanın nereye kaydedileceğini tam olarak belirttim ve kayıt sorununu kalıcı olarak çözdüm.



\### 5. Test Senaryoları ve Tablo

\* \*\*Prompt:\*\* "Bu uygulamanın sorunsuz çalıştığını kanıtlamak için 2 tanesi hatalı girdi olan toplam 5 maddelik bir test senaryosu tablosu oluşturur musun?"

\* \*\*YZ Yanıtı:\*\* Girdi, beklenen sonuç ve gerçekleşen sonucu içeren 5 satırlık Markdown tablosu üretti.

\* \*\*Kararım:\*\* Tabloyu kabul ettim. Senaryoları kendi komut satırımda tek tek test ettim, sonuçların doğru olduğunu teyit ettim ve ekran görüntülerini alarak README dosyama ekledim.


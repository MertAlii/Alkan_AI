# Alkan Ai - Kişisel Asistan

Alkan Ai, Python ile geliştirilmiş, terminal üzerinden çalışan akıllı bir kişisel asistandır. Notlarınızı tutabilir, etkinliklerinizi planlayabilir ve Google Gemini altyapısını kullanarak sizinle doğal dilde sohbet edebilir.

## Özellikler

*   **Not Yönetimi:** Kolayca not ekleyin ve mevcut notlarınızı listeleyin.
*   **Etkinlik Takibi:** Tarihli etkinlikler oluşturun ve ajandanızı takip edin.
*   **Akıllı Sohbet (Alkan Ai):**
    *   Yapay zeka ile sohbet edin.
    *   "Notlarımı özetle" gibi komutlarla veritabanınızdaki notlar hakkında AI'dan bilgi alın.
    *   "Yarın ne var?" gibi sorularla ajandanızı AI'ya yorumlatın.

## Kurulum

1.  Bu projeyi bilgisayarınıza klonlayın veya indirin.
2.  Gerekli Python kütüphanelerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3.  `.env` dosyasını oluşturun ve gerekli API anahtarlarını (Google Gemini API Key vb.) girin. Örnek içeriği `main.py` veya `assistant.py` dosyalarından kontrol edebilirsiniz.

## Kullanım

Uygulamayı başlatmak için terminalde şu komutu çalıştırın:

```bash
python main.py
```

### Komutlar

Ana menüde aşağıdaki komutları kullanabilirsiniz:

*   `1` veya `not ekle`: Yeni bir not oluşturur.
*   `2` veya `etkinlik ekle`: Yeni bir etkinlik ve tarihi kaydeder.
*   `3` veya `notları göster`: Kayıtlı tüm notları listeler.
*   `4` veya `etkinlikleri göster`: Kayıtlı etkinlikleri listeler.
*   `5` veya `sohbet et`: Alkan Ai ile sohbet moduna geçer. (Çıkmak için `q` yazın)
*   `6`, `q` veya `çıkış`: Uygulamadan çıkar.

## Teknolojiler

*   Python
*   Google Gemini API (Yapay Zeka desteği için)
*   SQLite / Yerel Veritabanı (Veri saklama için)

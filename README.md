# Alkan Ai - Kişisel Asistan 🤖

**Alkan Ai**, Python ile geliştirilmiş, terminal üzerinden çalışan akıllı bir kişisel asistandır. Notlarınızı tutabilir, etkinliklerinizi planlayabilir ve Google Gemini altyapısını kullanarak sizinle doğal dilde sohbet edebilir.

## 🌟 Özellikler

*   **📝 Not Yönetimi:** Kolayca not ekleyin ve mevcut notlarınızı listeleyin.
*   **📅 Etkinlik Takibi:** Tarihli etkinlikler oluşturun ve ajandanızı takip edin.
*   **🧠 Akıllı Sohbet (Alkan Ai):**
    *   Yapay zeka ile sohbet edin.
    *   **"Notlarımı özetle"** diyerek veritabanınızdaki notları analiz ettirin.
    *   **"Yarın ne var?"** diyerek ajandanızı kontrol ettirin.

## 🚀 Kurulum

1.  Bu projeyi bilgisayarınıza klonlayın veya indirin.
2.  Gerekli Python kütüphanelerini yükleyin:
    ```bash
    pip install -r requirements.txt
    ```
3.  `.env` dosyasını oluşturun ve `GEMINI_API_KEY` değerini ekleyin.

## 💻 Kullanım

### Web Arayüzü (Önerilen)

Web sunucusunu başlatmak için:

```bash
python app.py
```

Tarayıcınızda `http://127.0.0.1:5000` adresine gidin.

### Terminal (CLI)

Eski usül terminalden kullanmak isterseniz:

```bash
python main.py
```

### Komutlar (Terminal Modu İçin)

Ana menüde aşağıdaki komutları kullanabilirsiniz:

*   `1` | `not ekle`: Yeni bir not oluşturur.
*   `2` | `etkinlik ekle`: Yeni bir etkinlik kaydeder.
*   `3` | `notları göster`: Kayıtlı notları listeler.
*   `4` | `etkinlikleri göster`: Ajandanızı listeler.
*   `5` | `sohbet et`: Alkan Ai ile sohbet moduna geçer.
*   `6` | `çıkış`: Uygulamadan çıkar.

## 🛠 Teknolojiler

*   **Python 3.x**
*   **Flask** (Web Framework)
*   **Google Gemini API** (LLM Desteği)
*   **SQLite** (Veri Saklama)
*   **Dotenv** (Ortam Değişkenleri)

## 🔜 Gelecek Planları (Roadmap)
- [x] Web Arayüzü (Flask + HTML/JS)
- [ ] Sesli Komut Desteği

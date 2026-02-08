import os # Ortam değişkenleri ve dosya yolu
import requests # HTTP istekleri yapmak için
from dotenv import load_dotenv # .env dosyalarından ortam değişkenlerini yüklemek için

# .env dosyasını yükle
load_dotenv()

# .env dosyasından GEMINI_API_KEY değişkenini alalım
api_key = os.getenv("GEMINI_API_KEY")

# Api anahtarı kontrol etme
if not api_key:
    raise ValueError("GEMINI_API_KEY .env dosyasında tanımlı değil")

# Gemini 2.0 Flash modeline ait api url'i
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# Api çağrısı için gerekli http başlıkları
headers = {
    "Content-Type": "application/json", # JSON formatında veri göndereceğimizi belriliyoruz
    "X-Goog-Api-Key": api_key # Yetkilendirme için api anahtarı
}

def get_gemini_response(prompt: str) -> str: # Gemini api'sine promp gönderip yanıt return eden fonksiyon
    # Api'ye gönderilecek json yapısı
    payload = {
        "contents": [
            {
                "parts": [
                    {"text":prompt} # Kullanıcıdan gelen mesajı içeren bölüm
                ]
            }
        ]
    }

    # Gemini apiye http post isteği gönder
    response = requests.post(url, headers=headers, json= payload)

    # İstek başarılıysa
    if response.status_code == 200:
        try:
            result = response.json() # Json formatındaki yanıtı sözlüpe çevirir
            return result["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            # Eğer json beklendiği gibi değilse hata döndürür
            return f"Yanıt hatası: {e}"
    else:
        return f"Api hatası {response.status_code}: {response.text}"

# Kullanıcı mesajına göre niyet sınıflandırması yapan bir fonksiyon
def detect_intent(message):
    prompt = f"""
    Sen bir sınıflandırma asistanısın. Aşağıdaki kullanıcı mesajını analiz et ve niyetini belirle.
    Cevap olarak SADECE aşağıdaki etiketlerden birini döndür (başka hiçbir kelime veya açıklama yazma):
    
    ETİKETLER:
    - not_ozet      -> (Kullanıcı notlarını görmek, okumak, listelemek veya notlarıyla ilgili özet istiyorsa)
    - etkinlik_ozet -> (Kullanıcı takvimini, etkinliklerini, ajandasını, planlarını görmek veya özet istiyorsa)
    - cıkıs         -> (Kullanıcı sohbetten çıkmak istiyorsa)
    - normal        -> (Selamlaşma, genel sohbet, hal hatır sorma veya yukarıdaki kategorilere girmeyen her şey)
    
    Kullanıcı Mesajı: "{message}"
    
    Döndürülecek Etiket:
    """ 
    
    response = get_gemini_response(prompt)
    
    # Olası boşlukları ve büyük/küçük harf sorunlarını temizleyelim
    return response.strip().lower()
    

if __name__ == "__main__":
    user_input = input("Kullanıcı sorusu: ")
    yanıt = get_gemini_response(user_input)
    print(f"AI Asistan: {yanıt}")
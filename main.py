from assistant import *
from database import *

# Veritabanını başlat
initialize_db()

# Karşılama ekranı
print("Asistana Hoşgeldiniz")
print("-" * 20)

print("Komurtlar:")
print(" 1-Not ekle | 2-Etkinlik ekle | 3-Notları göster | 4-Etkinlikleri göster | 5-Sohbet et | 6-Çıkış (q)")

# Kullanıcıdan sürekli komut almak için sonsuz döngü başlat
while True:
    print("-" * 20)
    command = input("Komut giriniz: ").strip().lower()

    if command == "not ekle" or command == "1":
        content = input("Not içeriği: ")
        add_note(content)
        print("Not başarıyla kaydedildi.")

    elif command == "etkinlik ekle" or command == "2":
        content = input("Etlinlik açıklaması: ")
        date = input("Etkinlik tarihi: ")
        add_event(content,date)
        print("Etkinlik başarıyla kaydedildi.")

    elif command == "notları göster" or command == "3":
        print("--- Notlar ---")
        notes = get_notes()
        if notes:
            for content,created_at in notes:
                print(f" [{created_at}]: {content}")
        else:
            print("Heniz hiç not kaydedilmemiş.")

    elif command == "etkinlikleri göster" or command == "4":
        print("--- Etkinlikler ---")
        events = get_events()
        if events:
            for event, event_date in events:
                print(f"- {event_date}: {event}")
        else:
            print("Heniz hiç etkinlik kaydedilmemiş.")

    elif command == "sohbet et" or command == "5":
        print("Çıkmak için 'q' yazınız")
        while True:
            message = input("Kullanıcı: ").strip()

            if message.lower() == "q":
                print("Sohbetten çıkılıyor, ana menüye dönülüyor...")
                break

            intent = detect_intent(message)  # Kullanıcının niyetini anlama

            if intent == "not_ozet":
                notes = get_notes()
                if not notes:
                    print("Henüz özetlenecek not yok")
                    continue

                all_notes_text = "\n".join([f"- {note[0]}" for note in notes]) # Tüm notları birleştir
                
                # Eğer intent == "not_ozet" ise burası çalışacak
                prompt = f"""
                        Sen **Alkan Ai** adında, yardımsever ve zeki bir kişisel asistansın.

                        SİSTEM BİLGİSİ:
                        Kullanıcının gönderdiği mesaj analiz edildi ve niyeti **'not_ozet'** olarak belirlendi.
                        Yani kullanıcı veritabanındaki notları hakkında bilgi istiyor, özet istiyor veya belirli bir notu soruyor.

                        MEVCUT VERİTABANI (Kullanıcı Notları):
                        --- NOTLAR BAŞLANGIÇ ---
                        {all_notes_text}
                        --- NOTLAR BİTİŞ ---

                        KULLANICININ MESAJI: "{message}"

                        GÖREVİN:
                        Kullanıcının mesajını (sorusunu) baz alarak yukarıdaki notları analiz et ve cevapla.

                        DAVRANIŞ KURALLARI:
                        1. **Spesifik Soru:** Eğer kullanıcı belirli bir konuyu sorduysa (örn: "Market notum neydi?"), sadece o konuyla ilgili notları bul ve söyle.
                        2. **Genel Özet:** Eğer kullanıcı genel bir ifade kullandıysa (örn: "Notlarımı özetle", "Neler var?"), notları konularına göre gruplandırarak (İş, Kişisel vb.) genel bir durum özeti sun.
                        3. **Tanışma:** Cevaba kendini isminle (Alkan Ai) tanıtarak başla.
                        4. **Ton:** Samimi, profesyonel ve çözüm odaklı ol.
                        5. **Yokluk:** Eğer sorulan konuyla ilgili not yoksa, "Bununla ilgili bir not bulamadım" de.
                        """
                try:
                    yanıt = get_gemini_response(prompt)
                    print(f"🤖 {yanıt}")
                except Exception as e:
                    print(f"Hata oluştu: {e}")
                
                print("\n" + "-" * 30)
            
            elif intent == "etkinlik_ozet":
                events = get_events()
                if not events:
                    print("Henüz özetlenecek etkinlik yok")
                    continue
                
                all_events_text = "\n".join([f"- {event[0]}" for event in events])# Tüm etkinlikleri birleştiri

                # Eğer intent == "etkinlik_ozet" ise burası çalışacak
                prompt = f"""
                        Sen **Alkan Ai** adında, zaman yönetimi konusunda uzman bir kişisel asistansın.

                        SİSTEM BİLGİSİ:
                        Kullanıcının niyeti **'etkinlik_ozet'** olarak tespit edildi.
                        Kullanıcı takvimi, yaklaşan planları veya belirli bir tarihteki etkinliği hakkında bilgi istiyor.

                        MEVCUT VERİTABANI (Etkinlik Listesi):
                        --- ETKİNLİKLER BAŞLANGIÇ ---
                        {all_events_text}
                        --- ETKİNLİKLER BİTİŞ ---

                        KULLANICININ MESAJI: "{message}"

                        GÖREVİN:
                        Kullanıcının sorusuna göre takvimi yorumla.

                        DAVRANIŞ KURALLARI:
                        1. **Tarih Kontrolü:** Etkinlik tarihlerini bugünün tarihiyle kıyasla (Bugün, Yarın, Geçmişte kalanlar vb. şeklinde yorumla).
                        2. **Spesifik Soru:** Kullanıcı "Yarın ne var?" dediyse sadece yarını söyle. "Toplantı ne zaman?" dediyse o etkinliği bul.
                        3. **Genel Özet:** "Ajandamda ne var?" dediyse etkinlikleri "Yaklaşanlar" ve "İleri Tarihliler" olarak grupla.
                        4. **Ton:** Enerjik ve motive edici ol. Kendini Alkan Ai olarak tanıt.
                        """
                try:
                    yanıt = get_gemini_response(prompt)
                    print(f"🤖 {yanıt}")
                except Exception as e:
                    print(f"Hata oluştu: {e}")
                
                print("\n" + "-" * 30)
            
            # ... (Önceki if/elif blokları: not_ozet, etkinlik_ozet bitti)

            elif intent == "normal":
                # Genel sohbet için prompt
                prompt = f"""
                Sen **Alkan Ai** adında, yardımsever, zeki ve sohbeti keyifli bir kişisel asistansın.

                SİSTEM DURUMU:
                Kullanıcının mesajı analiz edildi ve özel bir veritabanı işlemi (not/etkinlik sorgusu) gerektirmediği anlaşıldı.
                Şu an "Genel Sohbet / Bilgi Alma" modundasın.

                KULLANICININ MESAJI: "{message}"

                GÖREVİN:
                Kullanıcının mesajına en uygun, doğal ve yardımsever cevabı ver.

                KURALLAR:
                1. **Kimlik:** Kendini her zaman "Alkan Ai" olarak benimse.
                2. **Yeteneklerin:** Sen sadece sohbet botu değilsin; not alabilir ve ajanda tutabilirsin. Eğer sohbetin akışı gerektirirse (örneğin kullanıcı "kafam çok dağınık" derse), "İstersen senin için not alabilirim veya programını düzenleyebilirim" gibi nazik hatırlatmalar yapabilirsin.
                3. **Tarz:** Arkadaş canlısı, nazik ve kısa/öz cevaplar ver. Uzun paragraflarla kullanıcıyı sıkma.
                4. **Bilgi:** Eğer genel kültür sorusuysa (örn: "Hava neden mavi?", "Python nedir?"), doğru ve net bilgi ver.
                """

                try:
                    yanıt = get_gemini_response(prompt)
                    print(f"🤖 Alkan Ai: {yanıt}")
                except Exception as e:
                    print(f"Hata oluştu: {e}")
                
                print("\n" + "-" * 30)


    elif command == "çıkış" or command == "6" or command == "q":
        break
    else:
        print("⚠️ Geçersiz komut!")
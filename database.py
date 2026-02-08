import sqlite3 # Veri tabanı
import os

# veritabanı dosyasının yolunu oluştur data/assistant.db
DB_PATH = os.path.join("data","assistant.db")

# Veritabanını başaltan fonksiyon
def initialize_db():
    # Eğer data klasörü yoksa oluştursun
    os.makedirs("data", exist_ok=True)

    # Veritabanına bağlan ve dosya yoksa oluştur
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Eğer notes tablosu yoksa oluştur
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,           -- otomatik artan birincil anahtar
            content TEXT NOT NULL,                          -- not içeriği
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- varsayılan olarak şu anki zaman
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calendar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,            -- Otomatik artan ID
            event TEXT NOT NULL,                             -- Etkinlik açıklaması (boş olamaz)
            event_date TEXT NOT NULL,                        -- Etkinlik tarihi (boş olamaz)
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- varsayılan olarak şu anki zaman

        )
    """)

    # Değişikleri kaydet
    conn.commit()

    # Bağlantıyı kapat
    conn.close()

# Veritabanına yeni not ekleme işlemi
def add_note(content):
    # Veritabanına bağlan
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Conten'i "notes" tablosuna ekle
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))

    # Değişikleri kaydet
    conn.commit()

    # Bağlantıyı kapat
    conn.close()

# Veritabanına yeni etkinlik ekleyen fonksiyon
def add_event(event, event_date):
    # Veritabanına bağlan
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Etkinlik ve tarih bilgilerini "calendar" tablosuna ekle
    cursor.execute("INSERT INTO calendar (event, event_date) VALUES (?,?)", (event, event_date))    
    # Değişikleri kaydet
    conn.commit()

    # Bağlantıyı kapat
    conn.close()

# Tüm notları veritabanından sıralı bir şekilde getiren fonksiyon
def get_notes():
    # Veritabanına bağlan
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # "notes" tablosundan içerik ve tarih bilgilerini zaman sırasına göre getir
    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")

    # Sonuçları liste olarak alalım
    notes = cursor.fetchall()
        
    # Bağlantıyı kapat
    conn.close()

    return notes

# Tüm etkinlikleri veritabanından sıralı şekilde getiren fonksiyon
def get_events():
    # Veritabanına bağlan
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # "calendar" tablosundan içerik ve tarih bilgilerini zaman sırasına göre getir
    cursor.execute("SELECT event, event_date FROM calendar ORDER BY created_at DESC")

    # Sonuçları liste olarak alalım
    events = cursor.fetchall()

    # Bağlantıyı kapat
    conn.close()

    return events

if __name__ == "__main__":
    initialize_db()
    add_event("Toplantı var", "11.12.2025")
    add_note("aaaaaaa")

    print(f"Notes: {get_notes()}")
    print(f"Events {get_events()}")


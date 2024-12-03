import requests
import pandas as pd
from datetime import datetime
import os
import sys

# API'dan veri çek
url = "https://api.btcturk.com/api/v2/ticker"
response = requests.get(url)
data = response.json()

# 'data' key'i içerisindeki verileri al
pairs = data.get('data', [])

# DataFrame oluştur
if pairs:
    df = pd.DataFrame(pairs)

    # Tarih ve saat bilgilerini ekle
    current_time = datetime.now()
    df['Sorgu_Tarihi'] = current_time.date()
    df['Sorgu_Saati'] = current_time.strftime("%H:%M")

    # Excel dosyasına yaz
    # Çalıştırılan script'in dizinini al
    if getattr(sys, 'frozen', False):
        script_directory = os.path.dirname(sys.executable)  # exe olarak çalıştırılıyorsa
    else:
        script_directory = os.path.dirname(os.path.abspath(__file__))  # py olarak çalıştırılıyorsa

    # Zaman damgası oluştur
    timestamp = current_time.strftime("%M_%H_%Y%m%d")
    # Excel dosyası yolu
    output_path = os.path.join(script_directory, f"{timestamp}_btcturk_ticker.xlsx")

    # Excel dosyasına yaz
    df.to_excel(output_path, index=False)
    print("Veriler Excel dosyasına başarıyla kaydedildi:", output_path)
else:
    print("API'dan veri alırken sorun oluştu veya veri bulunamadı.")

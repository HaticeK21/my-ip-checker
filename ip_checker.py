import socket
import urllib.request
import json
import os
import platform


def line():
    print("=" * 50)


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "Bulunamadı"


def get_public_ip():
    try:
        with urllib.request.urlopen(
            "https://api.ipify.org?format=json", timeout=5
        ) as response:
            data = json.loads(response.read().decode())
            return data.get("ip", "Bulunamadı")
    except Exception:
        return "İnternet bağlantısı yok veya IP alınamadı"


def get_hostname():
    try:
        return socket.gethostname()
    except Exception:
        return "Bilinmiyor"


def main():
    os.system("clear" if os.name != "nt" else "cls")

    line()
    print("        MY IP CHECKER")
    print("     Cyber Security Tool")
    line()

    print("\n[+] Cihaz bilgileri")
    print(f"    İşletim sistemi : {platform.system()}")
    print(f"    Cihaz adı       : {get_hostname()}")

    print("\n[+] Ağ bilgileri")
    print(f"    Yerel IP        : {get_local_ip()}")
    print(f"    Genel IP        : {get_public_ip()}")

    print("\n[!] Bilgi")
    print("    Yerel IP, bulunduğun ağ içindeki adresindir.")
    print("    Genel IP, internet üzerinde görünen adresindir.")
    print("    IP adresini paylaşırken dikkatli ol.")

    line()
    print("Program tamamlandı.")


if __name__ == "__main__":
    main()

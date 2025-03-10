from flask import Flask, request
import logging
import socket
import os
import tkinter as tk
from tkinter import messagebox
import colorama
import time
from colorama import Fore
from pyngrok import ngrok
from werkzeug.middleware.proxy_fix import ProxyFix

# Ngrok güncelleme kontrolünü devre dışı bırak
os.environ["NGROK_UPDATE"] = "false"

colorama.init()

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

logging.basicConfig(filename='ip_log.txt', level=logging.INFO)

@app.route('/')
def log_ip():
    return """
    <html>
        <head>
            <title>ATLANTIS</title>
            <style>
                body {
                    text-align: center;
                    font-family: Arial, sans-serif;
                    background-image: url('https://www.wallpaperbetter.com/en/hd-wallpaper-cvscm');
                    background-size: cover;
                    color: white;
                    overflow: hidden;
                    margin: 0;
                    padding: 0;
                }
                .banner {
                    font-size: 48px;
                    font-weight: bold;
                    color: cyan;
                    background-color: rgba(0, 0, 0, 0.5);
                    width: 100%;
                    position: fixed;
                    top: 0;
                    left: 0;
                    padding: 20px 0;
                    z-index: 1000;
                }
                .skull {
                    position: absolute;
                    font-size: 24px;
                    color: white;
                    pointer-events: none;
                }
            </style>
        </head>
        <body>
            <div class="banner">ATLANTIS</div>
            <script>
                document.addEventListener("mousemove", function(event) {
                    let skull = document.createElement("div");
                    skull.innerHTML = "💀";
                    skull.classList.add("skull");
                    document.body.appendChild(skull);
                    skull.style.left = event.clientX + "px";
                    skull.style.top = event.clientY + "px";
                    
                    setTimeout(() => {
                        skull.remove();
                    }, 1000);
                });
            </script>
        </body>
    </html>
    """

def start_flask():
    """Flask uygulamasını başlat ve ngrok tünelini aç."""
    tunnel = ngrok.connect(5000)
    public_url = tunnel.public_url  # Doğru URL alma yöntemi
    print(f"Ngrok Public URL: {public_url}")

    with open("ip_log.txt", "a") as log_file:
        log_file.write(f"Ngrok Public URL: {public_url}\n")

    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True, use_reloader=False)

logo = Fore.LIGHTRED_EX + '''
============================================================
  AAAAA   TTTTT  L       AAAAA  N   N  TTTTT III  SSSSS     
 A     A    T    L      A     A N   N    T    I  S         
 AAAAAAA    T    L      AAAAAAA N   N    T    I  SSSSS    
 A     A    T    L      A     A N   N    T    I      S   
 A     A    T    LLLLL  A     A N   N    T    III  SSSSS  
========================================================
maded by c4k1r      IP LOGGER
'''

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    time.sleep(2)
    
    cevap = input("Başlatmak istiyor musunuz? (evet/hayir): ").lower()
    if cevap == 'evet':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('ATLANTIS IP LOGGER STARTED...')
        time.sleep(2)
        print('SUNUCU OLUŞTURULUYOR...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        def get_ip():
            """Yerel makinenin IP adresini al."""
            hostname = socket.gethostname()
            ipadress = socket.gethostbyname(hostname)
            return ipadress

        print('Yerel IP adresiniz:', get_ip())
        print('Ngrok bağlantısı için ip_log.txt dosyasını kontrol edin.')

        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning('ATLANTIS BİLDİRİM', 'LOGGER OLUŞTURULDU')
        messagebox.showwarning('ATLANTIS BİLDİRİM', 'ip_log.txt yi kontrol edin')

        start_flask()
    else:
        print("Flask uygulaması başlatılmadı.")

from flask import Flask, request
import logging
import socket
import sys
import os
import tkinter as tk
from tkinter import messagebox
import colorama
import time
from colorama import Fore

colorama.init()

app = Flask(__name__)


logging.basicConfig(filename='ip_log.txt', level=logging.INFO)

@app.route('/')
def log_ip():
    ip_address = request.remote_addr
    logging.info(f'IP Address: {ip_address}')
    return f'Your IP is {ip_address}'

def start_flask():
    """Flask uygulamasını başlatmak için fonksiyon"""
    app.run(host='0.0.0.0', port=5000)

logo = Fore.LIGHTRED_EX + '''
============================================================
============================================================
  AAAAA   TTTTT  L       AAAAA  N   N  TTTTT III  SSSSS     /
 A     A    T    L      A     A N   N    T    I  S         /
 AAAAAAA    T    L      AAAAAAA N   N    T    I  SSSSS    /
 A     A    T    L      A     A N   N    T    I      S   /
 A     A    T    LLLLL  A     A N   N    T    III  SSSSS/  
========================================================
========================================================
maded by c4k1r      IP LOGGER
'''

if __name__ == '__main__':
   os.system('cls')
   print(logo)
   time.sleep(2)
   cevap = input("Başlatmak istiyor musunuz? (evet/hayir): ").lower()

   if cevap == 'evet':
        print(Fore.LIGHTCYAN_EX + ' ')
        os.system('cls')
        print('ATLANTIS IP LOGGER STRARTED...')
        time.sleep(2)
        print('SUNUCU OLUŞTURULUYOR...')
        print('sunucu oluşturuldu !!!!!!')
        time.sleep(1)
        os.system('cls')
        def get_ip():
             hostname = socket.gethostname()
             ipadress = socket.gethostbyname(hostname)

             return ipadress
        print('ip adresiniz ', get_ip())
        print('web sitesinin urlsini öğrenmek için log.txt ye bakınız.')
        root = tk.Tk()
        root.withdraw()
        messagebox.showwarning('ATLANTIS BİLDİRİM', 'LOGGER OLUŞTURULDU')
        messagebox.showwarning('ATLANTIS BİLDİRİM', 'log.txt yi kontrol edin')

        start_flask()
       
else:
        print("Flask uygulaması başlatılmadı.")
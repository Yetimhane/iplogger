from flask import Flask, request
import logging

app = Flask(__name__)


logging.basicConfig(filename='ip_log.txt', level=logging.INFO)

@app.route('/')
def log_ip():
    
    ip_address = request.remote_addr
    
    
    logging.info(f'IP Address: {ip_address}')
    
    return f'Your IP is {ip_address}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
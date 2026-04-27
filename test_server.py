import os
import threading
import http.server
import socketserver
import time
from pyngrok import ngrok

PORT = 8000

def start_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    # Start the HTTP server in a thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    print("伺服器已啟動，正在產生 ngrok 測試網址...")
    time.sleep(1) # Wait for server to be ready

    # Open a ngrok tunnel to the HTTP server
    public_url = ngrok.connect(PORT).public_url
    print(f"\n========================================================")
    print(f"Server and ngrok tunnel are ready!")
    print(f"Please open this URL on your phone:")
    print(f"-->  {public_url}  <--")
    print(f"========================================================\n")
    print("Press Ctrl+C to stop...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n正在關閉伺服器...")

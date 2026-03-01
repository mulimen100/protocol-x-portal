import http.server
import socketserver
import socket
import os
import webbrowser

def find_free_port(start_port=8080):
    port = start_port
    while port < 9000:
        if port in [3000, 3005]:
            port += 1
            continue
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
        port += 1
    return None

port = find_free_port()
if port:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    Handler = http.server.SimpleHTTPRequestHandler
    
    print(f"Starting server on port {port}...")
    url = f"http://localhost:{port}/index.html"
    
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Could not open browser automatically: {e}")
        
    print(f"\\nSUCCESS! Local Real-time Agent UI is running at:\\n{url}\\n")
    print("Press CTRL+C to stop the server.")
    
    with socketserver.TCPServer(("", port), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
else:
    print("Error: Could not find a free port.")

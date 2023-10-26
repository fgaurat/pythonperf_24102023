import http.server
import socketserver
import os
import time

class DelayedHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Ajouter une latence de 1 seconde
        time.sleep(1)
        # Appeler la méthode GET originale
        super().do_GET()

PORT = 8000

web_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.chdir(web_dir)

# Utilisez le nouveau gestionnaire pour servir les fichiers avec la latence
Handler = DelayedHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

print(f"Serveur démarré à http://localhost:{PORT}")
httpd.serve_forever()
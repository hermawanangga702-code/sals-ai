from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        data = json.loads(body)
        nilai = int(data.get("nilai", 0))

        if nilai >= 80:
            level = "Mahir"
            rekomendasi = "Project lanjutan"
        elif nilai >= 50:
            level = "Menengah"
            rekomendasi = "Latihan soal"
        else:
            level = "Pemula"
            rekomendasi = "Belajar dasar"

        response = {"level": level, "rekomendasi": rekomendasi}

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode())

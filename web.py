from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<html>
    <title>
        sample  webpage
    </title>
    <h1 align="center">Laptop Properties(Elavarasan M (24900162))</h1>
    <body>
        <ol>
            <li><b>Device Name   :</b>DESKTOP-MOHHBTU</li>
            <li><b>Processor     :</b>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</li>
            <li><b>Installed RAM :</b>16.0 GB (15.7 GB usable)</li>
            <li><b>Device ID     :</b>15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
            <li><b>Product ID    :</b>00342-42709-09763-AAOEM</li>
            <li><b>System Type   :</b>64-bit operating system, x64-based processor</li>
            <li><b>Pen and Touch :</b>No pen or touch input is available for this display</li>
        </ol>

    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
import usocket as socket

def load(path):
    with open(path, 'r') as content_file:
            return content_file.read()

def serve(ip):
    HEADER = """\
    HTTP/1.1 200 OK
    Server: tims_fun_server
    Content-Type: text/html

    """
    ai = socket.getaddrinfo(ip,80)
    addr = ai[0][4]

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(addr)
    s.listen(5)

    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        req = client_s.recv(4096)
        parts = req.decode('ascii').split(' ')
        path = parts[1]

        if path == '/off':
            # To power down the web server call /off
            client_s.send(bytes(HEADER + "Webserver shutting down", "ascii"))
            client_s.close()
            break
        elif path == "/":
            f = load("public/index.html")
            client_s.send(bytes(HEADER + f, "ascii"))
            client_s.close()
        else:
            # change status code
            client_s.send(bytes(HEADER + "Not found", "ascii"))
            client_s.close()

        

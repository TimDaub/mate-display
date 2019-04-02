import usocket as socket
import os
import _thread

from sin import sin_wave

files = {
    "html": "text/html",
    "png": "image/png"
}

binary = ["png"]

def load(path, ending):
    mode = ""
    if ending in binary:
        mode = "rb"
    else:
        mode = "r"
        
    with open(path, mode) as content_file:
            return content_file.read()

def serve(ip):
    HEADER = """\
HTTP/1.1 {status} {code}
Server: tims_fun_server
Content-Type: {content_type}
Content-Length: {content_length}

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
        print(parts)
        path = parts[1]

        if path == '/off':
            # To power down the web server call /off
            content = HEADER.format(
                status="OK",
                code="200",
                content_type="text/html"
            )

            client_s.send(bytes(content + "Webserver shutting down", "ascii"))
            client_s.close()
            continue
        elif "/rpc" in path:
            _thread.start_new_thread(sin_wave, (100, 100000))
            client_s.send(bytes("OK", "ascii"))
            client_s.close()
            continue
        elif path == "/cancel":
            pill = True
            client_s.send(bytes("OK", "ascii"))
            client_s.close()
            continue
        else:
            name = path[1:]
            
            if not name:
                name = "index.html"

            ending = ""
            try:
                ending = name.split(".")[1]
            except IndexError:
                content = HEADER.format(
                    status="BAD REQUEST",
                    code="400",
                    content_type="text/html",
                    content_length="0"
                )
                client_s.send(bytes(content, "ascii"))
                client_s.close()
                continue

            mimetype = ""
            try:
                mimetype = files[ending]
            except KeyError:
                content = HEADER.format(
                    status="NOT FOUND",
                    code="404",
                    content_type="text/html",
                    content_length="0"
                )
                client_s.send(bytes(content, "ascii"))
                client_s.close()
                continue
                                            
            try:
                f = load("public/"+name, ending)
            except:
                content = HEADER.format(
                    status="NOT FOUND",
                    code="404",
                    content_type="text/html",
                    content_length="0"
                )
                client_s.send(bytes(content + "Not found", "ascii"))
                client_s.close()
                continue
            else:
                content = HEADER.format(
                    status="OK",
                    code="200",
                    content_type=mimetype,
                    content_length=os.stat("public/"+name)[6]
                )
                if ending in binary:
                    content = f
                else:
                    content = bytes(content + f, "ascii")
                client_s.send(content) 
                client_s.close()
                continue

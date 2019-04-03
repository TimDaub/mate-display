import usocket as socket
import os
import _thread
import sys
import ure
import gc
from utime import sleep_us

from clear import main as clear

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

def query_string_to_dict(query):
    # This doesn't work with micropython :( as it doesn't have re.findall
    # search = ure.search(r'\/rpc\?(\w+)=(\w+)(&(\w+)=(\w+))*', query)
    re = ure.compile(r'[\?&]')
    query = re.split(query)
    d = {}
    for i in range(1, len(query)):
        [key, value] = query[i].split("=")
        d[key] = value
    return d

def kill():
    # Stop program
    sleep_us(1)
        
def serve(ip):
    HEADER = """\
HTTP/1.1 {code} {status}
Server: tims_fun_server
Content-Type: {content_type}
Content-Length: {content_length}

"""
    program = {"run": True}
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

        try:
            path = parts[1]
        except IndexError:
            # NOTE: I'm not sure how to handle this and when these requests
            # happen
            continue

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
            # Kill old program
            program["run"] = False
            gc.collect()

            # Launch new program
            program = query_string_to_dict(path)
            program["run"] = True

            name = program["program"]
            exec('import ' + name, {} )

            clear()
            _thread.start_new_thread(sys.modules[name].main, (program, ))
            client_s.send(bytes("OK", "ascii"))
            client_s.close()
            continue
        elif path == "/cancel":
            program["run"] = False
            clear()
            gc.collect()
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

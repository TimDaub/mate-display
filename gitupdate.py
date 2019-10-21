import urequests

def main():
    path = "https://raw.githubusercontent.com/TimDaub/mate-display/master/"
    filelist = open("filelist.txt","r")
    for line in filelist:
        response = urequests.get(path + line)
        code = open(line,"w")
        code.write(response.text)
        code.close()
    filelist.close()
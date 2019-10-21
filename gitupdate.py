import urequests


def main():
    path = "https://raw.githubusercontent.com/TimDaub/mate-display/master/"
    filelist = open("filelist.txt", "r")
    for line in filelist:
        filename = str.rstrip(line)
        response = urequests.get(path + filename)
        code = open(filename, "w")
        code.write(response.text)
        code.close()
        print(filenamscre)
    filelist.close()

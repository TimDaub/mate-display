import urequests


def main():
    path = "https://raw.githubusercontent.com/TimDaub/mate-display/master/"
    #update filelist first
    filename = "filelist.txt"
    response = urequests.get(path + filename)
    code = open(filename, "w")
    code.write(response.text)
    code.close()
    print(filename)
    filelist = open("filelist.txt", "r")
    for line in filelist:
        #update files from list
        filename = str.rstrip(line)
        if filename[:1] == "#":
            pass
        else:
            response = urequests.get(path + filename)
            if response.text[:3] == "404":
                pass
            else:
                with open(filename, "w") as code:
                    code.write(response.text)
                    code.close()
                    print(filename)
    filelist.close()

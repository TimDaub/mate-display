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
        print(filename[:1])
        if filename[:1] == "#":
            print("lalalala")
        else:
            response = urequests.get(path + filename)
            if response.text[:3] == "404":
                pass
            else:
                code = open(filename, "w")
                code.write(response.text)
                code.close()
                print(filename)
    filelist.close()

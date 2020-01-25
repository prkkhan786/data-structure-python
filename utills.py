def Duplicate(str):
    hash = dict()
    for i in range(len(str)):
        if(hash.get(str[i])==None):
            hash[str[i]] = 1
        else:
            hash[str[i]] = hash.get(str[i]) + 1
    return hash


def getExtensionOfFile(filename):
    if(len(filename)==0):
        return "Error"
    filenameArray = filename.split(".")
    return filenameArray[-1]


def getListOfFiles(basepath):
    pass







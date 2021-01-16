import os
def getFiles(_path):
    fileList = []
    path = os.walk(_path)
    for root, directories, files in path:
        for f in files:
            fileList.append(os.path.join(root,f))
    return fileList

def getDirectories(_path):
    path = os.walk(_path)
    directoryList = []
    for root, _, _ in path:
        directoryList.append(root)
    return directoryList
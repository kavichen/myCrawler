#coding=utf-8
import os
from hashlib import md5
import shutil

#current_path = os.getcwd()
#dir_list = os.listdir(current_path)

def trimPath(path):
    path = str(path)
    if path == '':
        return []
    if path != '/':
        path = path + '/'
    return path

def getDirListInPath(path):
    path = trimPath(path)
    List = os.listdir(path)
    #print List
    dirList = []
    #filter dir
    for x in List:
        #print x
        if  os.path.isdir(path+x):
            dirList.append(x)
    #dirname = [x for x in dirList if os.path.isdir(path+x)]
    return dirList

#用数字顺序命名文件夹
def numericRenameAllDirs(path):
    dirList = getDirListInPath(path)
    name = 1
    for x in dirList:
        os.rename(x,str(name))
        name = name +1
    return  dirList

def getFileListInPath(path):
    path = trimPath(path)
    #if path == '':
    #    return []
    #if path[-1]!='/':
    #    path=path+'/'
    dirList = os.listdir(path)
    fileList = [f for f in dirList if os.path.isfile(path+f)]
    return fileList


def moveAllFiles(currentPath,newPath):
    currentPath = trimPath(currentPath)
    newPath = trimPath(newPath)
    fileList = getFileListInPath(currentPath)
    for f in fileList:
        shutil.move(currentPath+f,newPath+f)

def numericRenameAllFilesInPath(path):
    path = trimPath(path)
    fileList = getFileListInPath(path)
    name = 1
    for f in fileList:
        os.rename(f,str(name))
        name=name+1
    return fileList


def md5File(name):
    m = md5()
    a_file = open(name,'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()

def deleteFileSmallerThan(path,size):
    fileSize = os.path.getsize(path)
    if fileSize < size:
        os.remove(path)
        print path+'is deleted!'

#currentPath = os.getcwd()+'/2'
#newPath = os.getcwd()
#moveAllFiles(currentPath,newPath)
#numericRenameAllFilesInPath(currentPath)




#!/usr/bin/python
#coding:utf-8

import os,time,socket
import urllib,re

def get_html(url):
    page = urllib.urlopen(url)
    time.sleep(0.5)
    html = page.read()
    return html


def get_startPage(url):
    startPage = get_html(url)
    startPagePattern = '<span class="current-comment-page">.*\d+.*</span>'
    startReg = re.compile(startPagePattern)
    startPageNumberList = re.findall(startReg,startPage)
    startNumList = []
    for startPageNumber in startPageNumberList:
        numPattern = '\d+'
        numReg = re.compile(numPattern)
        startNum = re.findall(numReg,startPageNumber)
        startNumList.append(startNum)
    return min(startNumList)[0]


def get_img(html):
    global globnum
    # reg = r'src="(.*?\.jpg)" />'
    reg = r'src="(.*?\.jpg)"[\s]*/>'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    for imgurl in imglist:
        try:
            urllib.urlretrieve(imgurl, '%s.jpg'%globnum)
            time.sleep(3)
            globnum +=1
        except IOError:
            time.sleep(0.5)
        except:
            print 'time out'

# html = get_html('http://jandan.net/ooxx/page-1')
ooxx = 'http://jiandan.net/ooxx/'
startPage = int(get_startPage(ooxx))
urlList = ['http://jandan.net/ooxx/page-%d' % i for i in range(startPage, 1, -1)]
socket.setdefaulttimeout(30)

globnum = 1
for i in urlList:
    print 'i is',i
    html = get_html(i)
    print get_img(html)
    if globnum < 500:
        pass
    else:
        exit()




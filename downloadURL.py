# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 23:13:49 2016
###stroing data
@author: an
"""

import os
import bs4
import urllib.request

baseUrl="http://pythonscraping.com"
html=urllib.request.urlopen("http://www.pythonscraping.com")
bsobj=bs4.BeautifulSoup(html.read())
SrcInTag=bsobj.findAll(src=True)

os.chdir("c:/users/an/desktop/pythonlearning")

for i in SrcInTag:
    print(i['src'])

def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url=source[4:]
        url="http://"+source
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path=absoluteUrl.replace("www.","")
    path=path.replace(baseUrl,"")
    path=downloadDirectory+path
    directory=os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

downloadDirectory="downloaded"

for download in SrcInTag:
    fileUrl=getAbsoluteURL(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
getDownloadPath(baseUrl,fileUrl,downloadDirectory)
os.path.dirname("downloaded/img/lrg%20(1).jpg")
os.path.dirname("ok/fuck/us4.exe")
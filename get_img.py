# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 17:43:38 2016

@author: an
"""

import os
os.getcwd()
os.chdir("./desktop/data clean")
os.path.exists("./pic")
os.makedirs("./pic")

url="http://apod.nasa.gov/apod/archivepix.html"
import urllib.request
html=urllib.request.urlopen(url)
import bs4
bsobj=bs4.BeautifulSoup(html)
hyperlink=bsobj.findAll("a")
pages=[]
len(pages)
for link in hyperlink:
    pages.append(link['href'])

def GetcorrectURL(pages):
    want=[]
    for link in pages:
        if not ("http" in link):
            correct="http://apod.nasa.gov/apod/"+link
            want.append(correct)
    return want

correct_page=GetcorrectURL(pages)

len(correct_page)
type(correct_page)
correct_page[len(correct_page)-1]

def GetpicUrl(correct):
    downloadUrl=[]
    k=0
    for link in correct:
        html=urllib.request.urlopen(link)
        bsobj=bs4.BeautifulSoup(html)
        pic=bsobj.find("img")
        try:
            if 'src' in pic.attrs:
                downloadUrl.append("http://apod.nasa.gov/apod/"+pic['src'])
        except AttributeError:
            pass
    return downloadUrl

picurl=GetpicUrl(correct_page)
len(picurl)

'''___________test part__________________'''
html=urllib.request.urlopen(correct_page[2572])
bsobj=bs4.BeautifulSoup(html)
pci=bsobj.find("img")
pci["src"]
'''______________________________________'''
base="./pic"

re.findall("r(.*\.jpg)",picurl[7542])
picurl[300]
import re
def GetdownloadPath(picurl,base):
    path=[]
    k=0
    for link in picurl:
        k +=1
        per=re.findall(r"image/.*/(.*\.jpg)",link)
        if len(per) > 0:
            path.append(base+'/'+per[0])
        else:
            per2=re.findall(r"image/(.*\.gif)",link)
            if len(per2)==0:
                path.append(base+"/"+"NoPICture")
            else:
                path.append(base+"/"+per2[0])
    return path
        
len(picurl)  
picpath=GetdownloadPath(picurl,base)
for k in range(len(picurl)):
    try:
        urllib.request.urlretrieve(picurl[k],picpath[k])
    except:
        pass
                      
            
            
    
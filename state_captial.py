# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:13:09 2016
### us_capital_city
@author: an
"""

def make_data():
    import urllib.request
    import urllib.parse
    import re
    url='https://simple.wikipedia.org/wiki/List_of_U.S._state_capitals'
    request=urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        the_page=response.read()
        filtrate_1=re.findall(r'<td><a href="/wiki/(.*?)" title=',str(the_page))
    
    data=dict()
    cap=stat=str()
    for i in filtrate_1:
        filt=re.findall(r'(.*),_(.*)',str(i))
        for j in filt:
            cap=str(j[0]).replace("_"," ")
            stat=str(j[1]).lower().replace("_"," ")
            data[stat]=cap
    return data
def input_ques():
    x=str(input("Please input a state: "))
    return(x.lower())

def input_cont():
    y=str(input())
    t_y=y.lower()
    if t_y!="yes":
        return False
    else:
        return True

def seach_answer(x,y):
    if x in y.keys():
        print("the capital of {0} is {1}".format(x,y[x]))
    else:
        print("something wrong with your input",end="\n")
    print('{0:^80}'.format("Do you want try again?"))
    print('{0:^80}'.format("please input yes for want"))

def main():
    print('{0:^80}'.format("Welcome to the game"))
    data=make_data()
    go_on=True
    k=0
    while go_on:
        ques=input_ques()
        seach_answer(ques,data)
        go_on=input_cont()
        k =+1
        if k==10:
            print("We need a rest!")
            go_on=False

if __name__=='__main__':
    main()
        
        
        
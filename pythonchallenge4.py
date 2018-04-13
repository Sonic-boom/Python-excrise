import urllib.request
import re  
import os  

#打开url
src = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831')
#下一个页面的地址  
nexturl = None  
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='  
#计数器
count=0
while True:  
    #通过url获取页面资源
    nexturl = src.readline()  
    #下一个页面的数字
    nextid = nexturl[-5:];count=count+1
    try:
        nextid = int(nextid)
    except:  
        break  
    #下一个页面的地址
    nexturl = url+str(nextid)  
    print(count,'next url-->'+nexturl) 
    #关闭url连接    
    src.close()  
    src = urllib.request.urlopen(nexturl)
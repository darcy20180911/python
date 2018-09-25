#http://www.lovewzly.com/api/user/pc/list/search?startage=21&endage=30
# &gender=2&cityid=52&startheight=161&endheight=170&marry=1&education=30&page=1

import os
import requests

def getage():
    print("******** selcet age **********")
    print("******** 1. 21-30   **********")
    print("******** 2. 31-40   **********")
    age=int(input("xuanze nianling duan"))
    if  age==1:
        startage,endage=21,30
    if  age==2:
        startage,endage=31,40
    #print(startage,endage)
    return startage,endage
#getage()

def getsex():
    print("********** select sex ************")
    print("********** 1.nan      ************")
    print("********** 2.nv       ************")
    sex=int(input("xuanze xing bie"))
    if  sex==1:
        gender=1
    if  sex==2:
        gender=2
    #print(gender)
    return gender
#getsex()

def getcity():
    print("************ selcet city *************")
    print("************ 1.beijing   *************")
    print("************ 2.shanghai  *************")
    print("************ 3.guangzhou *************")
    city=int(input("xuanze chengshi"))
    if city==1:
        cityid=52
    if city==2:
        cityid=321
    if city==3:
        cityid=76
    #print(cityid)
    return cityid
#getcity()

def get_urlandres():
    startage, endage = getage()
    gender = getsex()
    cityid = getcity()
    startheight, endheight = 161, 170
    marry = 1
    education = 30
    header={'Referer':'http://www.lovewzly.com/jiaoyou.html',
    'User-Agent':'Mozilla/5.0(Windows NT6.1;Win64;x64;rv:62.0) Gecko/20100101Firefox/62.0'}
    for page in range(1,6):
        base_url = "http://www.lovewzly.com/api/user/pc/list/search?startage={}&endage={}" \
        "&gender={}&cityid={}&startheight={}&endheight={}&marry={}&education={}&page={}". \
        format(startage, endage, gender, cityid, startheight, endheight, marry, education,page)
        respond=requests.get(base_url,headers=header)
        json=respond.json()
        for item in json['data']['list']:
            image_save(item)




def image_save(item):
    image_url=item['avatar']
    res=requests.get(image_url)
    if res.status_code==200:
        path = 'dong/{}.jpg'.format(item['username'])
        if not os.path.exists(path):
            print("正在下载。。。")
            with open(path,'wb') as f:
                f.write(res.content)
        else:
            print("已下载")

get_urlandres()


# -*- coding: utf-8 -*-
import json, urllib
import urllib.parse
import base64
import random
import time
import os
import urllib.request
from PIL import Image
import pytesseract
import subprocess
from PIL import Image
from PIL import ImageOps
from selenium import webdriver
import time,os,sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import string
token=''
itemid=8076
telnum=0
msgyzm=''
registid=''
parentname=''
localsfz=[]
idno='450103198111260011'
username='肖鹏'
cname='优胜辉煌教育科技有限公司'
addressname='东丽区振东物流集团院内'
driver = webdriver.Firefox() #打开火狐浏览器
driver.maximize_window()
driver.get('https://xyk.cebbank.com/cebmms/apply/ps/card-list.htm?level=124&pro_code=FHTG023556SJ226XMRO') #打开界面
time.sleep(5)  # 浏览器加载需要时间

    #driver.find_element_by_id('su').click()  #搜索完成
  # 浏览器加载需要时间
driver.find_element_by_class_name('submit').click()
  # 浏览器加载需要时间
time.sleep(2)
driver.find_element_by_id('name').send_keys(username)
time.sleep(1)
driver.find_element_by_id('id_no').send_keys(idno)

time.sleep(1)
#driver.find_element_by_id('provinceP2').find_element_by_tag_name('option')[2].click()
#m=driver.find_element_by_id("provinceP2")
#city = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"provinceP2")))

#m.find_element_by_xpath("//option[@value='5013|重庆市']").click()
Select(driver.find_element_by_id("provinceP2")).select_by_index(random.randint(1,30))
time.sleep(3)
Select(driver.find_element_by_id("cityC2")).select_by_index(1)
time.sleep(2)
Select(driver.find_element_by_id("areaA2")).select_by_index(1)
#text =getAuthCode(driver)
driver.find_element_by_id('comname').send_keys(cname)
driver.find_element_by_id('comaddr').send_keys(addressname)
time.sleep(1)

js="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
#截图保存验证码
driver.get_screenshot_as_file('E:\\a.png')
#left = 227
#top = 750
#right = 280
#bottom = 780
left = 210
top = 415
right = 270
bottom = 445
#print(top,left,right,bottom)
a = Image.open("E:\\a.png")
im = a.crop((left,top,right,bottom))
im.save('E:\\image\\b.png')


def main():


    #register()
    # 配置您申请的APPKey
    appkey = "6baa96eb72a2d478ce7ba4277426f55e"

    request1(appkey, "GET")
    #ver_code  图片验证码
    print('图片验证码：'+registid)
    driver.find_element_by_id('ver_code').send_keys(registid)
    request2()
    #request3()
    request4()
    #获取手机号码mobilephone
    print()
    driver.find_element_by_id('mobilephone').send_keys(telnum)
    time.sleep(2)
    #app_dt
    print('start...')
    driver.find_element_by_id('noteId').click()
    time.sleep(2)
    print('end')
    #getmessage()
    global msgyzm
    while True :
        request5()
        print(msgyzm)
        if '光大银行'  in msgyzm:

            break
        time.sleep(5)
    str2=msgyzm[msgyzm.find('：') +1 :]  #获取返回值

    str3=str2[str2.find('[')  :]  #截取验证码
    print(str2)
    print(str3)

    msgyzm=str2[0:len(str3)-2]
    print(token)
    print(itemid)
    print(telnum)
    print('消息:'+msgyzm)
    #手机验证码dynPasswd
    driver.find_element_by_id('dynPasswd').send_keys(msgyzm)
    driver.find_element_by_class_name('app_nexts').click()
    #第二步界面填写
    Select(driver.find_element_by_id("marriage")).select_by_index(2)
    Select(driver.find_element_by_id("education")).select_by_index(3)
    Select(driver.find_element_by_id("housetype")).select_by_index(4)
    #driver.find_element_by_id("marriage").find_element_by_xpath("//option[@value='2'").click()
    #driver.find_element_by_id("education").find_element_by_xpath("//option[@value='3'").click()
    #driver.find_element_by_id("housetype").find_element_by_xpath("//option[@value='4'").click()
    #email电子邮箱
    email=str(random.randint(1,9))  +''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''\
          +str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+'@qq.com'
    driver.find_element_by_id('email').send_keys(email)
    #Select(driver.find_element_by_id("areaA1")).select_by_index(2)
    #身份证是否长期有效longTime
    driver.find_element_by_id('longTime').click()
    #发证机构
    Select(driver.find_element_by_id("provinceO1")).select_by_index(random.randint(1,30))
    time.sleep(1)
    Select(driver.find_element_by_id("cityO2")).select_by_index(random.randint(1,6))
    time.sleep(2)
    Select(driver.find_element_by_id("areaO2")).select_by_index(1)
    time.sleep(2)
    #家庭住址
    Select(driver.find_element_by_id("areaA1")).select_by_index(2)

    driver.find_element_by_id('houseaddr').send_keys(addressname)
    Select(driver.find_element_by_id("cpy_kind")).select_by_index(5)
    Select(driver.find_element_by_id("cpy_vocation")).select_by_index(13)
    Select(driver.find_element_by_id("duty")).select_by_index(4)
    Select(driver.find_element_by_id("income")).select_by_index(3)
    #driver.find_element_by_id("cpy_kind").find_element_by_xpath("//option[@value='5'").click()
    #driver.find_element_by_id("cpy_vocation").find_element_by_xpath("//option[@value='5'").click()
    #driver.find_element_by_id("duty").find_element_by_xpath("//option[@value='4'").click()
    #driver.find_element_by_id("income").find_element_by_xpath("//option[@value='3'").click()
    #亲属信息familyname familymobile
    randomname()
    familymobile='156'+str(random.randint(0,9))  +''+str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))+''\
          +str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))
    driver.find_element_by_id('familyname').send_keys(parentname)
    #driver.find_element_by_id("relation").find_element_by_xpath("//option[@value='4'").click()
    Select(driver.find_element_by_id("relation")).select_by_index(4)
    driver.find_element_by_id('familymobile').send_keys(familymobile)
    #getsfz()
    #下一步 submitId
    driver.find_element_by_id('submitId').click()
    time.sleep(3)
    #第三步
    Select(driver.find_element_by_id("isloan")).select_by_index(2)
    Select(driver.find_element_by_id("isothercreditcard")).select_by_index(2)
    Select(driver.find_element_by_id("ishavesocial")).select_by_index(1)
    Select(driver.find_element_by_id("ishavegjj")).select_by_index(1)
    Select(driver.find_element_by_id("ishavecar")).select_by_index(1)
    time.sleep(1)
    driver.find_element_by_id('submitId').click()
    time.sleep(3)
    driver.get_screenshot_as_file('E:\\c.png')
def request1(appkey, m="GET"):
    f = open(r'E:\\image\\b.png', 'rb')  # 二进制方式打开图文件
    base64Str = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    f.close()

    url = "http://op.juhe.cn/vercode/index"
    params = {
        "key": appkey,  # 您申请的APPKEY
        "codeType": "1011",
        "base64Str": base64Str

    }
    params = urllib.parse.urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content1 = f.read()
    print(content1)
    content=str(content1.decode('utf-8'))
    #content=content.encode(encoding="utf-8")
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])
            global registid
            registid=res["result"]
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")

#获取token
def request2():

    uname='13310209351'
    passwd='smh128115'
    url = "http://api.shjmpt.com:9002/pubApi/uLogin"
    params = {
        "uName": uname,  # 您申请的APPKEY
        "pWord": passwd,
        "Developer": ''

    }
    params = urllib.parse.urlencode(params)

    f = urllib.request.urlopen("%s?%s" % (url, params))
    content1 = f.read()
    print(content1)
    content=str(content1.decode('utf-8'))
    print(content)
    str1=content[content.find('&')  :]
    global  token
    token=content[0:len(content)-len(str1)]
    print(token)

#获取项目 http://api.shjmpt.com:9002/uGetItems?token=token&tp=ut
def request3():


    url = "http://api.shjmpt.com:9002/uGetItems"
    params = {
        "token": token,  # 您申请的APPKEY
        "tp": 'ut'


    }
    params = urllib.parse.urlencode(params)

    f = urllib.request.urlopen("%s?%s" % (url, params))
    content1 = f.read()
    print(content1)
    content=str(content1.decode('utf-8'))
    print(content)
    str1=content[content.find('&')  :]
    global  itemid
    itemid=content[0:len(content)-len(str1)]
    print(itemid)
#获取号码 http://api.shjmpt.com:9002/pubApi/GetPhone?ItemId=项目ID&token=登陆token
def request4():


    url = "http://api.shjmpt.com:9002/pubApi/GetPhone"
    params = {
        "ItemId": itemid,
        "token": token , # 您申请的APPKEY
        "PhoneType":5,#非虚拟手机号码


    }
    params = urllib.parse.urlencode(params)

    f = urllib.request.urlopen("%s?%s" % (url, params))
    content1 = f.read()
    print(content1)
    content=str(content1.decode('utf-8'))
    print(content)
    str1=content[content.find(';')  :]
    global  telnum
    telnum=content[0:len(content)-len(str1)]
    print(telnum)

#获取消息 http://api.shjmpt.com:9002/pubApi/GMessage?token=登陆token&ItemId=项目ID&Phone=获取的号码
def request5():


    url = "http://api.shjmpt.com:9002/pubApi/GMessage"
    params = {
        "ItemId": itemid,
        "token": token , # 您申请的APPKEY
        "Phone": telnum #手机号码


    }
    params = urllib.parse.urlencode(params)

    f = urllib.request.urlopen("%s?%s" % (url, params))
    content1 = f.read()
    print(content1)
    content=str(content1.decode('utf-8'))
    global msgyzm
    msgyzm=content
def getmessage():

    while True :
        request5()
        time.sleep(3)
        if msgyzm != '':
            break



#随机姓名
def random_name(size=1, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def first_name(size=2, ln=None, fn=None):
    _lst = []
    for i in range(size):
        _item = random_name(1, fn)
        if ln:
            while _item in ln:
                _item = random_name(1, fn)
            _lst.append(_item)
        else:
            _lst.append(_item)
    return "".join(_lst)


def last_name(size=1, names=None):
    return random_name(size, names)


def full_name(lns, fns):
    _last = last_name(1, lns)
    return "{}{}".format(_last, first_name(random.randint(1, 2), _last, fns))

def randomname():
    last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '卫', '蒋', '沈', '韩', '杨', '秦', '许',
                  '何', '谢', '邹',  '章','马', '罗','熊', '纪', '舒', '董', '梁']

    first_names = [ '家', '可','慧','娴', '嘉','源','盈','锐', '娜','欣','玥', '成', '美','世','德', '兴','丽', '香', '琴', '亮'
                    , '健','乱', '景','富', '梦','福', '城','乾', '坤','顺','艺','波','群','雪', '雨','展', '阳', '强','影','意',
                    '理', '德','安'
                   ]


















    global parentname
    parentname=full_name(last_names, first_names)
    print(parentname)

#获取发证机构
#def getsfz():
    #driver1 = webdriver.Firefox() #打开火狐浏览器
    #driver1.get('http://qq.ip138.com/idsearch/') #打开界面
    #driver1.find_element_by_name('userid').send_keys(idno)
    #driver1.find_element_by_class_name('B1').click()
    #print(driver1.find_element_by_name('driver1'))
    #driver1.quit()
def getlocalsfz():
    s=''
    ss=[]
    f = open("E:\\1.txt", "r")
    while True:
        line = f.readline()
        if line:
            s=line
            #print(line)    # do something here
        else:
            break
    s1=s.split('----')
    for i in range(1,len(s1)-1):
        s3=s1[i+1][0:18]+s1[i][18:len(s1[i])]
        ss.insert(i,s3)
    global localsfz
    localsfz=ss
    f.close()

if __name__ == '__main__':
    main()

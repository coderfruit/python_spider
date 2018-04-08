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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException
import string
token=''
itemid=8076
telnum=0
msgyzm=''
registid=''
parentname=''
wxno=''
localsfz=[]
idno=''
username=''
cname=''
addressname=''
familyaddress=''
mdir='E:\\1'

surl='https://xyk.cebbank.com/cebmms/apply/ps/card-list.htm?level=124&pro_code=FHTG023556SJ226XMRO'

def main():
    getlocalsfz()
    print(localsfz)
    for sss in localsfz :
        global  idno

        idno=sss[0:18]
        global  username
        username=sss[18:len(sss)]
        print(idno)
        print(username)
        getcompanyname()
        print(2)
        getaddressname()
        print(3)
        main1()
        print('end......start....')
def main1():
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    driver = webdriver.Firefox() #打开火狐浏览器
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(surl) #打开界面
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    #time.sleep(2)  # 浏览器加载需要时间

    #driver.find_element_by_id('su').click()  #搜索完成
  # 浏览器加载需要时间
    #driver.find_element_by_class_name('submit').click()
    #js = 'document.getElementsByClassName("submit")[0].click();'
    #driver.execute_script(js)
    driver.find_element_by_xpath("//div[@id='dd1']/li[1]/div/div[3]/div[2]/a").click()
    #submit11=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME,"submit")))
    #print(nodecode)
    #submit11.click()
    #driver.find_element_by_xpath("//div[@class='applicant-infomation-item-subdiv']/span/a").click()
    #WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME,"submit")[0])).click()
    #driver.switch_to_window(driver.window_handles[1])
  # 浏览器加载需要时间
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)
    driver.find_element_by_id('name').click()
    driver.find_element_by_id('name').send_keys(username)
    driver.find_element_by_id('name').click()
    #time.sleep(1)
    driver.find_element_by_class_name('applicant-infomation-item-subdiv').click()
    driver.find_element_by_id('namepy').click()
    #namepy=driver.find_element_by_tag_name('namepy').get_attribute('value')

    #time.sleep(1)
    driver.find_element_by_id('id_no').send_keys(idno)

    #time.sleep(1)
#driver.find_element_by_id('provinceP2').find_element_by_tag_name('option')[2].click()
#m=driver.find_element_by_id("provinceP2")
    provinceP2 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"provinceP2")))

#m.find_element_by_xpath("//option[@value='5013|重庆市']").click()
    #Select(driver.find_element_by_id("provinceP2")).select_by_index(random.randint(1,30))
    try:
        Select(provinceP2).select_by_index(random.randint(1,30))
    except NoSuchElementException as msg:
        Select(provinceP2).select_by_index(random.randint(1,30))
    else:
        Select(provinceP2).select_by_index(random.randint(1,30))

    #time.sleep(2)
    cityC2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"cityC2")))
    #Select(driver.find_element_by_id("cityC2")).select_by_index(1)
    #time.sleep(1)
    try:
        Select(cityC2).select_by_index(1)
    except NoSuchElementException as msg:
        Select(cityC2).select_by_index(1)
    else:
        Select(cityC2).select_by_index(1)
    #time.sleep(2)
    areaA2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"areaA2")))
    try:
        Select(areaA2).select_by_index(1)
    except NoSuchElementException as msg:
        Select(areaA2).select_by_index(1)
    else:
        Select(areaA2).select_by_index(1)

#text =getAuthCode(driver)
    driver.find_element_by_id('comname').send_keys(cname)


    driver.find_element_by_id('comaddr').send_keys(addressname)
    #time.sleep(1)

    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
#截图保存验证码
    driver.get_screenshot_as_file(mdir+'a.png')
    #left = 227
    #top = 750
    #right = 280
    left = 210
    top = 550
    right = 270
    bottom = 580
    #bottom = 780

#print(top,left,right,bottom)
    a = Image.open(mdir+"a.png")
    im = a.crop((left,top,right,bottom))
    im.save(mdir+'b.png')

    #register()
    # 配置您申请的APPKey
    appkey = "6baa96eb72a2d478ce7ba4277426f55e"

    request1(appkey, "GET")
    #ver_code  图片验证码
    print('图片验证码：'+registid)
    driver.find_element_by_id('ver_code').send_keys(registid)
    request2()
    #request3()
    while True:

        request4()
        if telnum[0:3]=='184':
            continue
        else:
            break
    #request4()
    #获取手机号码mobilephone

    driver.find_element_by_id('mobilephone').send_keys(telnum)
    #time.sleep(2)
    #app_dt
    print('start...')
    #wait = ui.WebDriverWait(driver,10)

    #wait.until(lambda driver: driver.find_element_by_xpath("//a[@id='noteId']"))
    nodecode=WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID,"noteId")))
    #print(nodecode)
    nodecode.click()
    #driver.find_element_by_xpath("//div[@class='applicant-infomation-item-subdiv']/span/a").click()
    driver.find_element_by_xpath("//a[@id='noteId']").click()
    #driver.find_element_by_class_name('input-one-time-password-refresh').find_element_by_xpath("//@a[id='noteId']").click()
    #js = 'document.getElementbyId("noteId").click();'
    #driver.execute_script(js)
    #driver.find_element_by_id('noteId').click()
    #time.sleep(2)
    print('end')
    #getmessage()
    i=0
    global msgyzm
    while True :
        time.sleep(5)
        i=i+1
        request5()
        print(msgyzm)
        if i>6:
            driver.close()
            return
        if '光大银行'  in msgyzm:

            break


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
    marriage=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"marriage")))
    Select(marriage).select_by_index(2)
    education=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"education")))
    Select(education).select_by_index(3)
    housetype=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"housetype")))
    Select(housetype).select_by_index(4)

    #Select(driver.find_element_by_id("marriage")).select_by_index(2)
    #Select(driver.find_element_by_id("education")).select_by_index(3)
    #Select(driver.find_element_by_id("housetype")).select_by_index(4)
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
    provinceO1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"provinceO1")))
    Select(provinceO1).select_by_index(random.randint(1,30))
    #Select(driver.find_element_by_id("provinceO1")).select_by_index(random.randint(1,30))
    #time.sleep(1)
    cityO2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"cityO2")))
    #time.sleep(2)
    try:
        Select(cityO2).select_by_index(1)
    except NoSuchElementException as msg:
        time.sleep(2)
    else:
        Select(cityO2).select_by_index(1)
    areaO2=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"areaO2")))
    #time.sleep(1)
    try:
        Select(areaO2).select_by_index(1)
    except NoSuchElementException as msg:
        time.sleep(2)
    else:
        Select(areaO2).select_by_index(1)

    #Select(driver.find_element_by_id("cityO2")).select_by_index(1)
    #time.sleep(2)
    #Select(driver.find_element_by_id("areaO2")).select_by_index(1)
    #time.sleep(2)
    #家庭住址
    areaA1=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"areaA1")))
    #time.sleep(1)
    try:
        Select(areaA1).select_by_index(1)
    except NoSuchElementException as msg:
        Select(areaA1).select_by_index(1)
    else:
        Select(areaA1).select_by_index(1)

    #Select(driver.find_element_by_id("areaA1")).select_by_index(2)

    driver.find_element_by_id('houseaddr').send_keys(familyaddress)
    Select(driver.find_element_by_id("cpy_kind")).select_by_index(5)
    cpy_kind=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"cpy_kind")))
    Select(cpy_kind).select_by_index(5)
    cpy_vocation=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"cpy_vocation")))
    Select(cpy_vocation).select_by_index(13)
    #Select(driver.find_element_by_id("cpy_vocation")).select_by_index(13)
    duty=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"duty")))
    Select(duty).select_by_index(4)
    #Select(driver.find_element_by_id("duty")).select_by_index(4)
    income=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"income")))
    Select(income).select_by_index(3)
    #Select(driver.find_element_by_id("income")).select_by_index(3)
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
    #Select(driver.find_element_by_id("relation")).select_by_index(4)
    relation=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"relation")))
    Select(relation).select_by_index(4)
    driver.find_element_by_id('familymobile').send_keys(familymobile)
    #getsfz()
    #下一步 submitId
    driver.find_element_by_xpath("//a[@id='submitId']").click()
    time.sleep(1)
    #第三步
    #Select(driver.find_element_by_id("isloan")).select_by_index(2)
    isloan=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"isloan")))
    Select(isloan).select_by_index(2)
    #Select(driver.find_element_by_id("isothercreditcard")).select_by_index(2)
    isothercreditcard=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"isothercreditcard")))
    Select(isothercreditcard).select_by_index(2)
    #Select(driver.find_element_by_id("ishavesocial")).select_by_index(1)
    ishavesocial=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"ishavesocial")))
    Select(ishavesocial).select_by_index(1)
    #Select(driver.find_element_by_id("ishavegjj")).select_by_index(1)
    ishavegjj=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"ishavegjj")))
    Select(ishavegjj).select_by_index(1)
    #Select(driver.find_element_by_id("ishavecar")).select_by_index(2)
    ishavecar=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"ishavecar")))
    Select(ishavecar).select_by_index(2)
    qqno=str(random.randint(1,9))  +''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''\
          +str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))+''+str(random.randint(1,9))
    driver.find_element_by_id('qqno').send_keys(qqno)
    getwx()
    driver.find_element_by_id('wxno').send_keys(wxno)
    randomname()
    driver.find_element_by_id('otherrename').send_keys(parentname)
    Select(driver.find_element_by_id("otherrelation")).select_by_index(3)
    othermobile='158'+str(random.randint(0,9))  +''+str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))+''\
          +str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))+''+str(random.randint(0,9))
    driver.find_element_by_id('othermobile').send_keys(othermobile)
    #wxno qqno
#otherrelation 3  otherrename   othermobile

    time.sleep(1)
    driver.find_element_by_xpath("//div[@id='subDivButton']/a").click()
    #driver.find_element_by_id('submitId').click()
    #time.sleep(1)
    driver.get_screenshot_as_file('E:\\image\\'+str(time.strftime('%Y%m%d%H%M%S'))+username+'.png')
    #time.sleep(1)
    #driver.quit()
    driver.close()
def request1(appkey, m="GET"):
    #f = open(r'E:\\image\\b.png', 'rb')  # 二进制方式打开图文件
    f = open((mdir+'b.png'), 'rb')
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

    uname='18983705616'
    passwd='asdf1234'
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
        time.sleep(5)
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
    #f = open("E:\\1.txt", "r")
    #while True:
     #   line = f.readline()
      #  if line:
     #       s=line
            #print(line)    # do something here
     #   else:
     #       break
    #s1=s.split('----')
    #for i in range(1,len(s1)-1):
      #  s3=s1[i+1][0:18]+s1[i][18:len(s1[i])]
      #  ss.insert(i,s3)
    f = open(mdir+".txt", "r")
    i=0
    while True:
        line = f.readline()
        if line:

            s=line.strip('\n')
            s=s.strip()
            s=s.replace(' ','')
            s1=s[s.find('----'):]
            s2=s[0:len(s)-len(s1)].strip()
            s3=s1[len(s1)-18:len(s1)].strip()
            if s2+s3 =='':
                continue
            ss.insert(i,s3+s2)
            i=i+1
        else:
            break
    global localsfz
    localsfz=ss
    f.close()
#随机生成微信号
def getwx():
    src_digits = string.digits              #string_数字
    src_uppercase = string.ascii_lowercase  #string_大写字母
    src_lowercase = string.ascii_lowercase  #string_小写字母
    for i in range(10):

    #随机生成数字、大写字母、小写字母的组成个数（可根据实际需要进行更改）
        digits_num = random.randint(1,6)
        uppercase_num = random.randint(1,8-digits_num-1)
        lowercase_num = 8 - (digits_num + uppercase_num)

    #生成字符串
        password = random.sample(src_uppercase,digits_num) + random.sample(src_digits,uppercase_num) + random.sample(src_lowercase,lowercase_num)

    #打乱字符串
        random.shuffle(password)

    #列表转字符串
        new_password = ''.join(password)
    global wxno
    wxno='a'+new_password
    #
#随机获取公司名称
def getcompanyname():
    s=''
    ss=[]
    f = open("E:\\公司名称.txt", "r")
    i=0
    while True:
        line = f.readline()
        if line:
            s=line.strip('\n')
            ss.insert(i,s)
            i=i+1
            #print(line.strip('\n'))    # do something here
        else:
            break
    f.close()
    global cname
    cname=ss[random.randint(0,len(ss)-1)]
#随机获取公司地址
def getaddressname():
    s1=''
    ss1=[]
    f = open("E:\\地址.txt", "r")
    i=0
    while True:
        line = f.readline()
        if line:
            s1=line.strip('\n')
            ss1.insert(i,s1)
            i=i+1
            #print(line.strip('\n'))    # do something here
        else:
            break
    f.close()
    global addressname
    addressname=ss1[random.randint(0,len(ss1)/2)]
    global familyaddress
    familyaddress=ss1[random.randint(len(ss1)/2+1,len(ss1)-1)]
if __name__ == '__main__':
    main()

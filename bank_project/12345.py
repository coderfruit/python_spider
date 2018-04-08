# coding=utf-8
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
# 227 750 280 780
left = 210
top = 550
right = 270
bottom = 580
print(top,left,right,bottom)
a = Image.open("E:\\a.png")
im = a.crop((left,top,right,bottom))
im.save('E:\\d.png')
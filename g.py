import mechanize
from bs4 import BeautifulSoup
import datetime
import os
import _winreg as wreg
br = mechanize.Browser()
page = br.open("http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-IN")
soup = BeautifulSoup(page, "lxml")
for link in soup.find("url"):
    l = link.strip()
    url = "http://bing.com" + l.replace('1366x768', '1920x1080')
    print "Downloading from    "  + url
now = datetime.date.today()
now1 = now.strftime('%Y-%m-%d') +".jpg"
br.retrieve(url, now1)
pic_path = "C:\Python27\ " + now1
print "Downloading at       " + pic_path
print "Downloaded"
def setwallpaper(pic_path):
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, "Control Panel\\Desktop",0, wreg.KEY_ALL_ACCESS)
    wreg.SetValueEx(key, 'Wallpaper', 0, wreg.REG_SZ, pic_path) 
setwallpaper(pic_path)






    

    

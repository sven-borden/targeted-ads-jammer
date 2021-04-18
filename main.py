import subprocess
import re
import urllib.request
import time
import os

C_PATH = "chrome.exe"

AMA_URL = "http://randomking.com"


while True:
    contents = str(urllib.request.urlopen(AMA_URL).read())

    p =  re.compile('https://www.amazon.com/\S+')
    list_amazon_link = p.findall(contents)
    pid = []
    for link in list_amazon_link:
        cmd = "{0} {1}".format(C_PATH, link)
        print(cmd)
        pid.append(subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True))
        time.sleep(5)
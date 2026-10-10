import os
import sys
import shutil
import xml.dom.minidom
from datetime import datetime

import requests

chrome_version = sys.argv[1] if len(sys.argv) > 1 else "latest"
arch = sys.argv[2] if len(sys.argv) > 2 else "x64"

print(f"Requested version: {chrome_version}")
print(f"Requested arch: {arch}")

url = 'https://tools.google.com/service/update2'

if arch == "x86":
    app_arch = "x86"
    app_channel = "x86-stable-multi-chrome"
else:
    app_arch = "x64"
    app_channel = "x64-stable-multi-chrome"

data = f"""<?xml version="1.0" encoding="UTF-8"?>
<request protocol="3.0" updater="Omaha" updaterversion="1.3.36.112" shell_version="1.3.36.111"
    installsource="update3web-ondemand" dedup="cr" ismachine="0" domainjoined="0">
    <os platform="win" version="10.0.22000.282" arch="{app_arch}"/>
    <app appid="{{8A69D345-D564-463C-AFF1-A69D9E530F96}}" ap="{app_channel}" lang="en-us">
        <updatecheck />
    </app>
</request>"""

response = requests.post(url, data=data)

dom = xml.dom.minidom.parseString(response.text)
print(dom.toprettyxml(indent='  '))

url = dom.getElementsByTagName("url")[0].getAttribute("codebase")
name = dom.getElementsByTagName("action")[0].getAttribute("run")

response = requests.get(url + name)

with open("chrome.7z.exe", "wb") as file:
    file.write(response.content)

os.system('chmod +x ./7zzs')
os.system('./7zzs x chrome.7z.exe')
os.system('./7zzs x chrome.7z')

version = '0.0.0.0'
path = 'Chrome-bin'
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        version = i
        break

print(version)
if version == '0.0.0.0':
    exit(1)

shutil.move(r'version.dll', 'Chrome-bin')
shutil.move(r'chrome++.ini', 'Chrome-bin')

os.rename(r'Chrome-bin', 'Chrome')
shutil.move(r'Chrome', 'build/release/Chrome')

if chrome_version != "latest":
    version = chrome_version

env = os.getenv('GITHUB_ENV')
with open(env, 'a') as f:
    f.write(f'BUILD_NAME=Win{app_arch.upper()}_{version}_{datetime.now().strftime("%Y-%m-%d")}')

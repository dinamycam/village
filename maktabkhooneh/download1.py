#!/bin/python
import requests
import glob
import re
import subprocess
from sys import *
directory = glob.glob('*')
first = int(argv[2])
last = int(argv[3])
i = first
while i<=last:
    if ((str(i)+".mp4" in directory) or (str(i) in directory)) and str(i)+".aria2" not in directory :
        print("File:"+str(i)+" Exist")
        i=i+1
        continue
    try:
        url= argv[1]+str(i)+"/"
        res = requests.get(url)
        print(url)
        for line in res.text.split("\n"):
            if re.findall("https://box.maktabkhooneh.org/videos/",line) and re.findall("meta",line):
                myline = line
                break
        for text in myline.split('"'):
            if re.findall("https://box.maktabkhooneh.org/videos/",text):
                try:
                    subprocess.call(['aria2c','-x','16',text,'-o',str(i)+".mp4"])
                except:
                    try:
                        subprocess.call(['axel','-n','16',text,'-o',str(i)+".mp4"])
                    except:
                        try:
                            subprocess.call(['wget',text,'-o',str(i)+".mp4"])
                        except:
                            try:
                                subprocess.call(['curl',text,'-o',str(i)+".mp4"])
                            except:
                                print("go fuck ur self")
    except:
        print("You must enter the Url in This format")
        print("https://maktabkhooneh.org/course/{course_id}/chapter/{chapter_id}/lesson/")
    i=i+1
try:
    if argv[4]=='suspend':
        print("suspend")
        subprocess.call(['systemctl','suspend','-i'])
except:
    print("Finish")
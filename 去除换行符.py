#!/usr/bin/env python
# coding: utf-8


import os,re,copy

file_names = os.listdir('./')

def change(name):
    with open(name,'r',encoding='utf-8') as f1:
        subtitle = f1.read()
    rule = re.compile("[a-z]\n[a-z]")
    for i in range(len(subtitle)-2):
        if rule.match(subtitle[i:i+3]):
            subtitle = re.sub(subtitle[i:i+3], 
                              subtitle[i]+' '+subtitle[i+2], 
                              subtitle)
    with open("0-"+name,'w',encoding='utf-8') as f2:
        f2.write(subtitle)

for name in file_names:
    if ".srt" in name:
        change(name)
        print(name + " has been changed")


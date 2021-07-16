#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import os
import cv2
import csv
from pythainlp.tag.named_entity import ThaiNameTagger
from pythainlp import word_tokenize, Tokenizer
from pythainlp.corpus.common import thai_words
from pythainlp import Tokenizer

def lcs(X, Y):
    m = len(X)
    n = len(Y)
  
    L = [[None]*(n + 1) for i in range(m + 1)]
  
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    return L[m][n]

  
def Convert(string):
    li = list(string.split(","))
    return li

def createFileList(myDir, format='.txt'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    fileList.sort()
    return fileList

with open('D:\\iris_project\\massure\\list_name\\name.csv', newline='',encoding = "utf-8-sig") as f:
    reader = csv.reader(f)
    data = list(reader)

floder = ["gauss","s&p","poisson","normal"]
#floder = ["gauss"]
score = []
lost = []

for dirr in floder:
    print("--------------------------{}-------------------------------------".format(dirr))
    file_path = "D:\\iris_project\\massure\\list_name\\text\\{}\\result_{}.txt".format(dirr,dirr)    
    
    PERSON=""
    found1 = 0
    found2 = 0
    listt = [[],[],[]]
    listt[0] = dirr
    
    text_file = open(file_path, "r",encoding="utf-8")
    ner = ThaiNameTagger()
    for line in text_file.readlines():
        tag = ner.get_ner(line)
        for item in tag:
            if item[2].find("PERSON") != -1:
                if item[2][0] == "B" and PERSON != "":
                    PERSON += " , "  
                PERSON += item[0]
    text_file.close()            
    PERSON = Convert(PERSON)
    
    for people in data:
        status1 = "not found"
        status2 = "not found"
        
        for string in PERSON:
            if(string.find(people[0]) != -1):
                status1 = "found"
                found1 = found1 + 1
            if(len(people[0]) - lcs(people[0],string) <= 2):
                status2 = "found"
                found2 = found2 + 1
            if (status1 != "not found" or status2 != "not found" ):
                break
    
        if(status1 == "not found"):
            listt[1].append(people[0])
        if(status2 == "not found"):
            listt[2].append(people[0])
                
        print("{} normal = {} , lcs = {}".format(people[0],status1,status2))

    score.append((dirr,found1,found2))
    lost.append(listt)

    
print(score)
print(lost)

file = open("D:\\iris_project\\massure\\list_name\\result.txt", "w+",encoding="utf-8")
file.write("จำนวนคนที่เจอ [ประเภท noise,no lcs,lcs(2)] = {}\n".format(str(score)))
for i in range(len(lost)):
    file.write("รายชื่อคนหายคนหายโดย noise แบบ {}\n".format(str(lost[i][0])))
    file.write("ไม่ใช้ LCS\n")
    for j in range (len(lost[i][1])):
        file.write("{} ,".format(lost[i][1][j]))
        if (j%10 == 9):
            file.write("\n")
    file.write("\nใช้ LCS\n")    
    for j in range (len(lost[i][2])):
        file.write("{} ,".format(lost[i][1][j]))
        if (j%10 == 9):
            file.write("\n")
file.close()
        

    

    

#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

def Average(lst):
    return sum(lst) / len(lst)

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

def main():
    corection1 = []
    corection2 = []
    trash1 = []
    trash2 = []
    
    dir_path = 'D:\\iris_project\\massure\\Doc\\realtxt\\'
    fileList = createFileList(dir_path)
    length = len(dir_path)
    for files in fileList:
        name = files[length:]
        print(name)
        #make real word similar to result
        
        text1 = (open(files,encoding="utf8")).read()
     
        result_file = open("D:\\iris_project\\massure\\Doc\\resultxt1\\{}".format(name),"r",encoding="utf8")
        text2 = ""
        for word in result_file:
            text2 += word
        result_file.close()

        new_file = open("D:\\iris_project\\massure\\Doc\\resultxt2\\{}".format(name),"r",encoding="utf8")
        text3 = ""
        for word in new_file:
            text3 += word
        new_file.close()

        print("-------------------------------------------------------------------------------")
        print(text1)
        print("-------------------------------------------------------------------------------")
        print(text2)
        print("-------------------------------------------------------------------------------")
        print(text3)

        text1 = text1.replace(" ","")
        text1 = text1.replace("\n","")
        text1 = text1.replace("\t","")
        
        text2 = text2.replace(" ","")
        text2 = text2.replace("\n","")
        text2 = text2.replace("\t","")
        
        text3 = text3.replace(" ","")
        text3 = text3.replace("\n","")
        text3 = text3.replace("\t","")
        
        
        print("real text len = {} result1 text len = {} result2 text len = {}".format(len(text1),len(text2),len(text3)))
        print("lcs of real and result1 = {} lcs of real and result2 = {}".format(lcs(text1,text2),lcs(text1,text3)))
        print("% of result1 corection = {} % of result2 corection = {}".format(lcs(text1,text2)/len(text1)*100,lcs(text1,text3)/len(text1)*100))
        corection1.append(lcs(text1,text2)/len(text1)*100)
        corection2.append(lcs(text1,text3)/len(text1)*100)
        trash1.append((len(text2)-len(text1))/len(text1)*100)
        trash2.append((len(text3)-len(text1))/len(text1)*100)

    
    file = open("D:\\iris_project\\massure\\Doc\\result.txt", "w+",encoding="utf-8")
    file.write("% ความถูกต้องแบบ 1 = {}\n".format(str(corection1)))
    file.write("เฉลี่ย= {}\n".format(round(Average(corection1),2)))
    file.write("% ขยะแบบ 1 = {}\n".format(str(trash1)))
    file.write("เฉลี่ย= {}\n".format(round(Average(trash1),2)))
    file.write("% ความถูกต้องแบบ 2 = {}\n".format(str(corection2)))
    file.write("เฉลี่ย= {}\n".format(round(Average(corection2),2)))
    file.write("% ขยะแบบ 2 = {}\n".format(str(trash2)))
    file.write("เฉลี่ย= {}\n".format(round(Average(trash2),2)))
    file.close()
    
if __name__ == "__main__":
    main()

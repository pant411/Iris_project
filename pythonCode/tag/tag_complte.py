import os
from pythainlp.tag.named_entity import ThaiNameTagger
from pythainlp import word_tokenize, Tokenizer
from pythainlp.corpus.common import thai_words
from pythainlp import Tokenizer

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

dir_path = 'text_complete\\'
fileList = createFileList(dir_path)

for files in fileList:
    print(files)
    DATE=""
    TIME=""
    EMAIL=""
    LEN=""
    LOCATION=""
    ORGANIZATION=""
    PERSON=""
    PHONE=""
    URL=""
    ZIP=""
    MONEY=""
    LAW=""

    text_file = open(files, "r",encoding="utf-8")
    ner = ThaiNameTagger()
    for line in text_file.readlines():
        tag = ner.get_ner(line)
        for item in tag:
            if item[2].find("DATE") != -1:
                if item[2][0] == "B" and DATE != "":
                    DATE += " , "    
                DATE += item[0]
            elif item[2].find("TIME") != -1:
                if item[2][0] == "B" and TIME != "":
                    TIME += " , "  
                TIME += item[0]
            elif item[2].find("EMAIL") != -1:
                if item[2][0] == "B" and EMAIL != "":
                    EMAIL += " , "  
                EMAIL += item[0]
            elif item[2].find("LEN") != -1:
                if item[2][0] == "B" and LEN != "":
                    LEN += " , "  
                LEN += item[0]
            elif item[2].find("LOCATION") != -1:
                if item[2][0] == "B" and LOCATION != "":
                    LOCATION += " , "  
                LOCATION += item[0]
            elif item[2].find("ORGANIZATION") != -1:
                if item[2][0] == "B" and ORGANIZATION != "":
                    ORGANIZATION += " , "  
                ORGANIZATION += item[0]
            elif item[2].find("PERSON") != -1:
                if item[2][0] == "B" and PERSON != "":
                    PERSON += " , "  
                PERSON += item[0]
            elif item[2].find("PHONE") != -1:
                if item[2][0] == "B" and PHONE != "":
                    PHONE += " , "  
                PHONE += item[0]
            elif item[2].find("URL") != -1:
                if item[2][0] == "B" and URL != "":
                    URL += " , "  
                URL += item[0]
            elif item[2].find("ZIP") != -1:
                if item[2][0] == "B" and ZIP != "":
                    ZIP += " , "  
                ZIP += item[0]
            elif item[2].find("MONEY") != -1:
                if item[2][0] == "B" and MONEY != "":
                    MONEY += " , "  
                MONEY += item[0]
            elif item[2].find("LAW") != -1:
                if item[2][0] == "B" and LAW != "":
                    LAW += " , "  
                LAW += item[0]

    DATE = Convert(DATE)
    TIME = Convert(TIME)
    EMAIL = Convert(EMAIL)
    LEN = Convert(LEN)
    LOCATION = Convert(LOCATION)
    ORGANIZATION = Convert(ORGANIZATION)
    PERSON = Convert(PERSON)
    PHONE = Convert(PHONE)
    URL = Convert(URL)
    ZIP = Convert(ZIP)
    MONEY = Convert(MONEY)
    LAW = Convert(LAW)

    for item in PERSON:
        if item.find("นาย") == -1 and item.find("นาง") == -1 and item.find("เด็ก") == -1 and item.find("คุณ") == -1 and item.find("จารย์") == -1 and item.find("ดร.") == -1:
            PERSON.remove(item)
            
    name = files[13:]
    file = open("tag\\{}.txt".format(name), "w+")
    file.write("วัน = {}\n".format(DATE))
    file.write("เวลา = {}\n".format(TIME))
    file.write("อีเมล์ = {}\n".format(EMAIL))
    file.write("ระยะทาง = {}\n".format(LEN))
    file.write("ที่ตั้ง = {}\n".format(LOCATION))
    file.write("หน่วยงาน = {}\n".format(ORGANIZATION))
    file.write("บุคคล = {}\n".format(PERSON))
    file.write("มีกี่คน = {}\n".format(len(PERSON)))
    file.write("เบอร์โทร = {}\n".format(PHONE))
    file.write("URL = {}\n".format(URL))
    file.write("รหัสไปรษณีย์ = {}\n".format(ZIP))
    file.write("เงิน = {}\n".format(MONEY))
    file.write("กฎหมาย = {}\n".format(LAW))

    file.close()
            


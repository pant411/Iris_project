import os
from pythainlp.tag.named_entity import ThaiNameTagger

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
    DATE=[]
    TIME=[]
    EMAIL=[]
    LEN=[]
    LOCATION=[]
    ORGANIZATION=[]
    PERSON=[]
    PHONE=[]
    URL=[]
    ZIP=[]
    MONEY=[]
    LAW=[]

    text_file = open(files, "r",encoding="utf-8")
    ner = ThaiNameTagger()
    for line in text_file.readlines():
        tag = ner.get_ner(line)
        for item in tag:
            if item[2].find("DATE") != -1:
                DATE.append(item[0])
            elif item[2].find("TIME") != -1:
                TIME.append(item[0])
            elif item[2].find("EMAIL") != -1:
                EMAIL.append(item[0])
            elif item[2].find("LEN") != -1:
                LEN.append(item[0])
            elif item[2].find("LOCATION") != -1:
                LOCATION.append(item[0])
            elif item[2].find("ORGANIZATION") != -1:
                ORGANIZATION.append(item[0])
            elif item[2].find("PERSON") != -1:
                PERSON.append(item[0])
            elif item[2].find("PHONE") != -1:
                PHONE.append(item[0])
            elif item[2].find("URL") != -1:
                URL.append(item[0])
            elif item[2].find("ZIP") != -1:
                ZIP.append(item[0])
            elif item[2].find("MONEY") != -1:
                MONEY.append(item[0])
            elif item[2].find("LAW") != -1:
                LAW.append(item[0])

    name = files[13:]
    file = open("tag\\{}.txt".format(name), "w+")
    file.write("วัน = {}\n".format(DATE))
    file.write("เวลา = {}\n".format(TIME))
    file.write("อีเมล์ = {}\n".format(EMAIL))
    file.write("ระยะทาง = {}\n".format(LEN))
    file.write("ที่ตั้ง = {}\n".format(LOCATION))
    file.write("หน่วยงาน = {}\n".format(ORGANIZATION))
    file.write("บุคคล = {}\n".format(PERSON))
    file.write("URL = {}\n".format(URL))
    file.write("รหัสไปรษณีย์ = {}\n".format(ZIP))
    file.write("เงิน = {}\n".format(MONEY))
    file.write("กฎหมาย = {}\n".format(LAW))

    file.close()
            


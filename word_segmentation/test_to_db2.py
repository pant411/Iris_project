import os
     
path = os.getcwd()+'/docs_for_test'
#dir_list = os.listdir(path)
dir_list = [".".join(f.split(".")[:-1]) for f in os.listdir(path)]
print("Files and directories in '", path, "' :")   
# print the list
print(dir_list)
cutfile = ["test001","test002","test003","test004","test005","test006","test007","test008","test009",
            "test010","test011","test012","test013","test014","test015"
          ]
from manTextV5 import send2db
from database_update import newdocumentAdd

#fileName = input("file: ")  # เลือกไฟล์ test001 ถึง test015 เท่านั้น
for ele in dir_list:
    if ele in cutfile:
        continue
    res0, res1, res2, res5, day, month, year = send2db(ele)
    newdocumentAdd("/~amstel/download/"+ele+".pdf", res1, res5, res0, res2, "สังกัดผู้รับ", "เนื้อหา", year, month, day)
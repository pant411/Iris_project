#from manTextV5 import send2db
#from database_update import newdocumentAdd

#fileName = input("file: ")  # เลือกไฟล์ test001 ถึง test015 เท่านั้น
#res0, res1, res2, res5, day, month, year = send2db(fileName)
#newdocumentAdd("/~pluem/Iris_project/word_segmentation/docs_source/"+fileName+".pdf", res1, res5, res0, res2, "สังกัดผู้รับ", "เนื้อหา", year, month, day)

# Python program to explain os.getcwd() method
         
# importing os module
import os
     
path = os.getcwd()+'/docs_for_test'
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")   
# print the list
print(dir_list)
cutfile = ["test001.txt","test002.txt","test003.txt","test004.txt","test005.txt","test006.txt","test007.txt","test008.txt","test009.txt",
            "test010.txt","test011.txt","test012.txt","test013.txt","test014.txt","test015.txt"
          ]
from manTextV5 import send2db
from database_update import newdocumentAdd

#fileName = input("file: ")  # เลือกไฟล์ test001 ถึง test015 เท่านั้น
for ele in dir_list:
    if ele in cutfile:
        continue
    res0, res1, res2, res5, day, month, year = send2db(ele)
    newdocumentAdd("/~amstel/public_html/download/"+fileName+".pdf", res1, res5, res0, res2, "สังกัดผู้รับ", "เนื้อหา", year, month, day)
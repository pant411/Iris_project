from manTextV4 import send2db
from database_update import newdocumentAdd

fileName = input("file: ") #เลือกไฟล์ test001 ถึง test015 เท่านั้น
res0,res1,res2,res5,day,month,year = send2db(fileName)
newdocumentAdd("http://www.copperpod.cpe.ku.ac.th/~pluem/Iris_project/word_segmentation/docs_source/"+fileName+".pdf", res1, res5, res0, res2, "สังกัดผู้รับ", "เนื้อหา", year, month, day)
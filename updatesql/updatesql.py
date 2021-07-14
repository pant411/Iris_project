import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="ppunn",
  password="ppunn-password",
  database="ppunn_Document"
  )
mycursor = mydb.cursor()


def addUnit(Name, Telephone, Parent):
  try:
    search = "SELECT Name, ID FROM Unit WHERE Name = %s"
    keyword = (Parent,)
    mycursor.execute(search, keyword)
    myresult = mycursor.fetchall()
    #print(type(myresult))
    #for x in myresult:
      #print(type(x))
      #print(x)
    if len(myresult) == 0:
      sql = "INSERT INTO Unit (Name, Telephone, Typeedit) VALUES (%s, %s, %s)"
      val = (Name, Telephone, "ComputerEdit")
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print("ID number = ", mycursor.lastrowid)
    else:
      sql = "INSERT INTO Unit (Name, Telephone, ParentID, Typeedit) VALUES (%s, %s, %s, %s)"
      val = (Name, Telephone, (myresult[0])[1], "ComputerEdit")
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print("ID number = ",mycursor.lastrowid)
    
    return mycursor.lastrowid
  except:
    return -1

def addPerson(Name, Unit, Position):
  try:
    search = "SELECT Name, ID FROM Unit WHERE Name = %s"
    keyword = (Unit,)
    mycursor.execute(search, keyword)
    myresult = mycursor.fetchall()
    print(type(myresult))
    #for x in myresult:
      #print(type(x))
      #print(x)
    if len(myresult) == 0:
      sql = "INSERT INTO Person (Name) VALUES (%s)"
      val = (Name, )
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print("ID number = ",mycursor.lastrowid)

    else:
      sql = "INSERT INTO Person (Name, Unit_ID) VALUES (%s, %s)"
      val = (Name, Position, (myresult[0])[1])
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print("ID number = ",mycursor.lastrowid)
    
    return mycursor.lastrowid
  #return person ID
  #date sql "2021-05-18"
  except:
    return -1

def makeDay(day, month, year):
  uday = str(day)
  umonth = str(month)
  uyear = str(year)
  if day<10:
    uday =  "0" + uday
  if month<10:
    umonth = "0" + umonth
  
  return uyear + "-" + umonth + "-" + uday

#ถ้า ไม่ระบุวันหรือเดือนไม่ต้องใส่ ในช่อง day หรือ month
def addDocument(filename, name, day = 0, month = 0, year = 0 , content = "Not found"):
  try:
    if (day != 0) and (month != 0):
      date = makeDay(day, month, year)
      #print(date)
      sql = "INSERT INTO Document (filename, name, date, day, month, year, content) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      val = (filename, name, date, day, month, year, content)
      mycursor.execute(sql, val)

      mydb.commit()

      print(mycursor.rowcount, "record inserted.")
      print("Document ID number = ",mycursor.lastrowid)
    else:
      if month == 0:
        sql = "INSERT INTO Document (filename, name, year, content) VALUES (%s, %s, %s, %s)"
        val = (filename, name, year, content)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print("Document ID number = ",mycursor.lastrowid)
      else:
        sql = "INSERT INTO Document (filename, name, month, year, content) VALUES (%s, %s, %s, %s, %s)"
        val = (filename, name, month, year, content)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        print("Document ID number = ",mycursor.lastrowid)

    return mycursor.lastrowid
  except:
    return -1

def addKeyword(docid, tagtype, word):
  try:
    sql = "INSERT INTO Keyword (word, tag, Document_ID) VALUES (%s, %s, %s)"
    val = (word, tagtype, docid)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    print("Keyword ID number = ",mycursor.lastrowid)

    return mycursor.lastrowid
  except:
    return -1

def addTransaction(docid, senderid, sunitid, recipentid, runitid):
  try:
    sql = "INSERT INTO Transaction (Document_ID ,Sender_ID ,SenderUnit_ID ,Recipient_ID	,RecipientUnit_ID) VALUES (%s, %s, %s, %s, %s)"
    val = (docid, senderid, sunitid, recipentid, runitid)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    print("Keyword ID number = ",mycursor.lastrowid)

    return mycursor.lastrowid
  except:
    return -1

def searchoraddUnit(unitname):
  try:
    #หาองค์กรคนส่งว่าเคยมีไหม ถ้าหาเจอจะคือ id องค์กรณ์ให้ ถ้าไม่เจอจะ add ใหม่
    search = "SELECT Name, ID FROM Unit WHERE Name = %s"
    keyword = (unitname,)
    mycursor.execute(search, keyword)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
      #ตอนนี้ยังลังเลว่าถ้ามี telephone ใส่มาเลยอาจจะใส่เบอร์ได้ 
      return addUnit(unitname, "insertifyoucan", "-")
    else:
      #คืนผลค้นหาแรก
      return (myresult[0])[1]
  except:
    return -1

def searchoraddPerson(Personname, UnitID):
  try:
    search = "SELECT Name, ID FROM Person WHERE Name = %s"
    keyword = (Personname,)
    mycursor.execute(search, keyword)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
      #ตอนนี้ยังลังเลว่าถ้ามี telephone ใส่มาเลยอาจจะใส่เบอร์ได้ 
      sql = "INSERT INTO Person (Name, Unit_ID, Typeedit) VALUES (%s, %s, %s)"
      val = (Personname, UnitID, "ComputerEdit")
      mycursor.execute(sql, val)
      mydb.commit()
      #print(mycursor.rowcount, "record inserted.")
      #print("ID number = ",mycursor.lastrowid)
      return mycursor.lastrowid
    else:
      #คืนผลค้นหาแรก
      return (myresult[0])[1]
  except:
    return -1

def makethemback(mode, DocID):
  if mode >= 1:
    sql = "DELETE FROM Document WHERE ID = %s"
    val = ((str(DocID)), )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
  #Sender กับ SenderUnit RecipientUnit Sender Recipent มีโอกาสที่จะมาจาก search ดังนั้นเราไม่ควรลบ
  if mode > 5:
    sql = "DELETE FROM Transaction WHERE Document_ID = %s"
    val = ((str(DocID)), )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
  if mode >= 6:
    sql = "DELETE FROM Keyword WHERE Document_ID = %s"
    val = ((str(DocID)), )
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")
  return -1


def newdocumentAdd(filename, topicname, sender, senderunit, recipent, recipentunit, content, year, month ,day = 0):
  try:
    DocID = addDocument(filename, topicname, day, month, year, content)
    if DocID == -1:
      return -1
    SenderUnitID = searchoraddUnit(senderunit)
    if SenderUnitID == -1:
      return makethemback(1, DocID)
    RecipentUnitID = searchoraddUnit(recipentunit)
    if RecipentUnitID == -1:
      return makethemback(2, DocID)
    SenderID = searchoraddPerson(sender, SenderUnitID)
    if SenderID == -1:
      return makethemback(3, DocID)
    RecipentID = searchoraddPerson(recipent, RecipentUnitID)
    if RecipentID == -1:
      return makethemback(4, DocID)
    TranID = addTransaction(DocID, SenderID, SenderUnitID, RecipentID, RecipentUnitID)
    if TranID == -1:
      return makethemback(5, DocID)
    keyword = 0
    keyword = addKeyword(DocID, topicname, "Topic")
    if keyword == -1:
      return makethemback(6, DocID)
    keyword = addKeyword(DocID, sender, "Person")
    if keyword == -1:
      return makethemback(6, DocID)
    keyword = addKeyword(DocID, senderunit, "Org")
    if keyword == -1:
      return makethemback(6, DocID)
    keyword = addKeyword (DocID, recipent, "Person")
    if keyword == -1:
      return makethemback(6, DocID)
    keyword = addKeyword (DocID, recipentunit, "Org")
    if keyword == -1:
      return makethemback(6, DocID)
    keyword = addKeyword (DocID, year, "Year")
    if keyword == -1:
      return makethemback(6, DocID)
    if month != 0:
      keyword = addKeyword (DocID, month, "Month")
      if keyword == -1:
        return makethemback(6, DocID)
    return 0
  except:
    return -1
#ทำเคส error ด้วย  
#print(newdocumentAdd("wtf16", "ทดสอบ + เพิ่มแท็ก ครั้งที่เท่าไหร่หลังอัพเดท", "มิว", "แลปปริศนาหมายเลข1", "top", "แลปปริศนาหมายเลข2", "ได้เหอะขอล่ะ" ,2021, 8, 8))
#addDocument("te3t", "te3st", 0 , 5, 2021, "bah")
#print(makethemback(6, 13))
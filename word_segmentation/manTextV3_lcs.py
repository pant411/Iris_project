#! -*- coding: UTF8 -*-
from wordcut import Wordcut
import pylcs

#keyword = ['ส่วนราชการ','ที่','เรื่อง','วันที่','โทร.','ส่วนงาน','(นาย','(นาง','(นางสาว','(รศ. ดร.',
# '(รองศาสตราจารย์ ดร.','(น.ส.','(รองศาสตราจารย์','(ผู้ช่วยศาสตราจารย์ ตร.','(ผศ. ดร.','(รศ.คร.','(ผศ.ดร.']

def main():
    doc = input("file: ")
    data = open("docs/{}.txt".format(doc),"r")
    org,tel,topic,toUser,byUser,date,no = [],[],[],[],[],[],[] #org=ส่วนงานหรือส่วนราชการ tel=เบอร์โทร topic=เรื่อง toUser=เรียน byUser=คนเซ็น date=วันที่ no=ที่ศธ
    keyword = ['ส่วนราชการ','ส่วนงาน','เรื่อง','เรียน','วันที่','โทร.','ที่','นาย','นาง','นางสาว',
               'น.ส.','รองศาสตราจารย์','ผู้ช่วยศาสตราจารย์','รศ.คร.','ผศ.ดร.','ดร.','ผศ.','รศ.']
    line_no = 0
    tag1,tag2,tag3 = [],[],[] #tag1=ภาค tag2=คณะ tag3=มหาวิทยาลัย
    with open('dict.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
        for line in data.readlines():
            res = ''
            inline = wordcut.tokenize(line)
            inline = list(map(lambda s: s.strip(), inline))
            inline.append('\n')
            lock_keep = True #initial value
            op = -1
            for ele in inline:
                candidate = pylcs.lcs_of_list(ele,keyword)
                chosen = max(candidate)
                indexOFchosen = candidate.index(chosen)
                if 'ภาควิชา' in ele: tag1.append(ele)
                if 'คณะ' in ele: tag2.append(ele)
                if 'มหาวิทยาลัย' in ele: tag3.append(ele)
                if (abs(len(keyword[indexOFchosen]) - chosen) <= 2) or '\n' in ele:
                    #print(f'candidate is {candidate}, chosen is {chosen}, index is {indexOFchosen}, text is {keyword[indexOFchosen]}')
                    #print(f'chosen: {inline}, {keyword[indexOFchosen]}')
                    #print(f'ele: {ele}')
                    if (lock_keep == False and line_no > 0) or '\n' in ele: 
                        #print(f'op: {op}, res: {res}')        
                        if op == 1: 
                            org.append(res)
                        elif op == 2: 
                            topic.append(res)
                        elif op == 3: 
                            toUser.append(res)
                        elif op == 4: 
                            date.append(res)
                        elif op == 5: 
                            tel.append(res)
                        elif op == 6: 
                            no.append(res)
                        elif op >= 7:
                            byUser.append(res)
                        res = ''
                        lock_keep = True
                    if lock_keep == True and '\n' not in ele:
                        #print('gayray') 
                        if indexOFchosen == 0 or indexOFchosen == 1: 
                            op = 1 #collect in org
                        elif indexOFchosen == 2: 
                            op = 2 #keep in topic
                        elif indexOFchosen == 3: 
                            op = 3 #keep in toUser
                        elif indexOFchosen == 4: 
                            op = 4 #keep in date
                        elif indexOFchosen == 5: 
                            op = 5 #keep in tel
                        elif indexOFchosen == 6: 
                            op = 6 #keep in no
                        elif indexOFchosen >= 7: 
                            op = 7 #keep in byuser
                        lock_keep = False
                    line_no += 1
                    continue             
                if lock_keep == False and ele != ')':
                    res = res + ele
                    if (op == 7 or op == 4):
                        res += ' '
                #print(f'op: {op}, res: {res}')
            line_no += 1  
    #print(org,topic,toUser,byUser,tel,date,no)  
    print(f'org: {org}')
    print(f'topic: {topic}')
    print(f'toUser: {toUser}')
    print(f'byUser: {byUser}')
    print(f'tel: {tel}')
    print(f'date: {date}')
    print(f'no: {no}')
    print(f'tag1: {tag1},tag2: {tag2},tag3: {tag3}')  
    #print(org[0],topic[0],toUser[0],tel[0],date[0])   
    index_org = 0
    '''if temp1[0] not in org[0]:
        org.append(temp1[0])
        index_org = len(org)-1
    if temp3[0] not in org[0]:
        org.append(temp3[0])
        index_org = len(org)-1 '''
    if len(org) == 0:
        org.append("ไม่พบข้อมูล")
    if len(topic) == 0:
        topic.append("ไม่พบข้อมูล")
    if len(toUser) == 0:
        toUser.append("ไม่พบข้อมูล")
    if len(byUser) == 0:
        byUser.append("ไม่พบข้อมูล")
    if len(tel) == 0:
        tel.append("ไม่พบข้อมูล")
    if len(date) == 0:
        date.append("ไม่พบข้อมูล")
    if len(no) == 0:
        no.append("ไม่พบข้อมูล")
    print(f'ส่วนราชการ หรือ ส่วนงาน: {org[index_org]}')
    print(f'เรื่อง: {topic[0]}')
    print(f'เรียน: {toUser[0]}')
    print(f'โทร: {tel[0]}')
    print(f'วันที่ี: {date[0]}')
    print(f'คนเช็น: {byUser[-1]}')
    print(f'ที่: {no[0]}')

main()
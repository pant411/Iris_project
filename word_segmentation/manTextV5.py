#! -*- coding: UTF8 -*-
from wordcut import Wordcut
import pylcs
import pyuca
from pythainlp.util import normalize, thai_digit_to_arabic_digit
import re
from spell_correcting import my_autocorrect
from pythainlp.corpus import thai_stopwords
stopwords = list(thai_stopwords())

def read_text(file):
    #doc = input("file: ")
    data = open("docs_for_test/{}.txt".format(file), "r")
    return data

def read_text2(file):
    #doc = input("file: ")
    data = open("docs_source/{}.txt".format(file), "r")
    return data

def read_dict(choose="bigthai.txt"):
    with open(choose, encoding="UTF-8") as dict_file:
        dict_file2 = sorted(dict_file, key=pyuca.Collator().sort_key)
        word_list = list(set([w.rstrip() for w in dict_file2]))
        wordcut = Wordcut(word_list)
    return wordcut, word_list

def select_tag(indexOFchosen):
    if indexOFchosen <= 1:
        op = 1  # store in org
    elif indexOFchosen >= 7:
        op = 7  # store in byuser
    else:
        op = indexOFchosen
    return op

def store_tag(op, text, org, tel, topic, toUser, byUser, date, no):
    text = normalize(text)
    text = thai_digit_to_arabic_digit(text)
    if op == 1 and text != '':
        org.append(text)
    elif op == 2 and text != '':
        topic.append(text)
    elif op == 3 and text != '':
        toUser.append(text)
    elif op == 4 and text != '':
        date.append(text)
    elif op == 5 and text != '':
        tel.append(text)
    elif op == 6 and text != '':
        no.append(text)
    elif op >= 7 and text != '':
        byUser.append(my_autocorrect(text).iloc[0]["Word"])
    return org, tel, topic, toUser, byUser, date, no

def read_keyword():
    my_file = open("keyword.txt", "r")
    content = my_file.read()
    content_list = content.split(",")
    my_file.close()
    return content_list

def read_key(file):
    my_file = open(f"docs_source/{file}_key.txt", "r")
    content = my_file.read()
    content_list = content.split(",")
    my_file.close()
    return content_list

def org_tag(ele, tag1):
    x_tag1 = ele.find('ภาควิชา')
    x_tag2 = ele.find('คณะ')
    x_tag3 = ele.find('มหาวิทยาลัย')
    x_tag4 = ele.find('กอง')
    x_tag5 = ele.find('สำนัก')
    x_tag6 = ele.find('กรม')
    x_tag7 = ele.find('สภา')
    x_tag8 = ele.find('สถาน')
    x_tag9 = ele.find('บริษัท')
    res = ''
    if x_tag1 != -1:
        res = ele[x_tag1:len(ele)-1]
    elif x_tag2 != -1:
        res = ele[x_tag2:len(ele)-1]
    elif x_tag3 != -1:
        res = ele[x_tag3:len(ele)-1]
    elif x_tag4 != -1:
        res = ele[x_tag4:len(ele)-1]
    elif x_tag5 != -1:
        res = ele[x_tag5:len(ele)-1]
    elif x_tag6 != -1:
        res = ele[x_tag6:len(ele)-1]
    elif x_tag7 != -1:
        res = ele[x_tag7:len(ele)-1]
    elif x_tag8 != -1:
        res = ele[x_tag8:len(ele)-1]
    elif x_tag9 != -1:
        res = ele[x_tag9:len(ele)-1]
    '''space = res.find(' ')
    if space != -1:
        res = res[:space]'''
    if res != '':
        tag1.append(res)
    return tag1

def main_mantext(file):
    data = read_text(file)
    keyword = read_keyword()
    line_no = 0
    # org=ส่วนงานหรือส่วนราชการ tel=เบอร์โทร topic=เรื่อง toUser=เรียน byUser=คนเซ็น date=วันที่ no=ที่ศธ
    org, tel, topic, toUser, byUser, date, no = [], [], [], [], [], [], []
    tag1 = []  # tag1=tagสถานที่
    wordcut, wordcutlist = read_dict("bigthai.txt")
    wordcut22, wordcutlist22 = read_dict(choose="dictPeople.txt")
    select_list_org = -1
    status_select_org = True
    list_of_month = ["มกราคม", "กุมภาพันธ์", "มีนาคม", "เมษายน", "พฤษภาคม",
                     "มิถุนายน", "กรกฎาคม", "สิงหาคม", "กันยายน", "ตุลาคม", "พฤศจิกายน", "ธันวาคม"]
    date2 = []
    text = ''
    for line in data.readlines():
        res = ''
        tag1 = org_tag(line, tag1)
        inline = wordcut.tokenize(normalize(line))
        inline = list(map(lambda s: s.strip(), inline))
        inline.append('\n')
        lock_store = True  # สถานะการเก็บข้อมูลลงlist
        op = -1
        text += line
        find_key = 0
        for ele in inline:
            candidate = pylcs.lcs_of_list(ele, keyword)
            chosen = max(candidate)
            indexOFchosen = candidate.index(chosen)
            if select_list_org == -1 and status_select_org:
                if len('บันทึกข้อความ') - pylcs.lcs("บันทึกข้อความ", ele) <= 3:
                    select_list_org = 1  # use org
                    status_select_org = False
            if abs(len(keyword[indexOFchosen]) - chosen) <= 2 or '\n' in ele or ele in keyword:
                find_key += 1
                if (lock_store == False and line_no > 0 and (find_key == 1 or indexOFchosen == 5 or op == 5 or (op == 7 and (" " in ele or "\n" in ele)))) or '\n' in ele:
                    org, tel, topic, toUser, byUser, date, no = store_tag(
                        op, res, org, tel, topic, toUser, byUser, date, no)
                    res = ''
                    lock_store = True
                    continue
                if lock_store == True and '\n' not in ele and (find_key == 1 or indexOFchosen == 5 or op == 5):
                    op = select_tag(indexOFchosen)
                    lock_store = False
                    continue
                line_no += 1
            if lock_store == False and ele != ')':
                if ('ดร' in ele or 'ดร.' in ele or 'ตร.' in ele or 'ตร' in ele or ele == ' ' or 'นาย' in ele or 'นาง' in ele or 'นางสาว' in ele) and (op == 7 or op == 4):
                    continue
                match_name = pylcs.lcs_of_list(ele, wordcutlist22)
                max_match_name = max(match_name)
                if abs(len(ele)-max_match_name) > 4 and op >= 7:
                    continue
                if (re.findall("[-+*.|()${}]:", ele) or re.compile(r'^[ะา]').search(ele) or len(ele) == 1) and op >= 7:
                    continue
                if ele in stopwords and op >= 7:
                    continue
                res = res + ele
                if (op == 7 or op == 4):
                    res += ' '
            if ele in list_of_month:
                posMonth = inline.index(ele)
                date2.append(thai_digit_to_arabic_digit(
                    inline[posMonth-2]+' '+inline[posMonth]+' '+inline[posMonth+1]))
        line_no += 1
    select_org = []
    if select_list_org == 1:
        if len(org) > 0:
            select_org.append(org[0])
    elif select_list_org == -1:
        if len(tag1) > 0:
            select_org.append(tag1[0])
    index_org = 0
    if len(select_org) == 0:
        select_org.append("ไม่พบข้อมูล")
    if len(topic) == 0:
        topic.append("ไม่พบข้อมูล")
    if len(toUser) == 0:
        toUser.append("ไม่พบข้อมูล")
    if len(byUser) == 0:
        byUser.append("ไม่พบข้อมูล")
    if len(tel) == 0:
        tel.append("ไม่พบข้อมูล")
    if len(date2) == 0:
        date2.append("ไม่พบข้อมูล")
    if len(no) == 0:
        no.append("ไม่พบข้อมูล")
    return select_org, topic, toUser, tel, date2, byUser, text

def write_txt(inPut, file):
    with open('file_txt/a_'+file+'.txt', 'w') as f:
        for line in inPut:
            f.write(line)
            f.write('\n')

def test_dict(file):
    res = main_mantext(file)
    with open('bigthai.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
    print(wordcut.tokenize(res[0]))
    print(wordcut.tokenize(res[1]))
    print(wordcut.tokenize(res[2]))
    print(wordcut.tokenize(res[3]))
    print(wordcut.tokenize(res[4]))
    print(wordcut.tokenize(res[5]))

def add_space(text):
    res = ''
    lnum = ['๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    character = ['(', ')', '|', '!', '@', '&', '“']
    for i in range(len(text)):
        if text[i] in lnum and text[i-1] not in lnum:
            res += (' '+text[i])
        elif text[i] in character and text[i-1] not in character:
            res += (' '+text[i]+' ')
        else:
            res += text[i]
    return res

def count_score(file):
    res = main_mantext(file)
    with open('bigthai.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
    key = read_key(file)
    score_result = [0, 0, 0, 0, 0, 0]
    score_full = []
    for i in range(6):
        res[i] = add_space(normalize(res[i]))
        it = wordcut.tokenize(normalize(res[i]))
        space = 0
        for wc in it:
            if wc == ' ' or wc == '  ' or wc == '   ' or wc == '    ' or wc == '     ':
                space += 1
                continue
            if key[i].find(wc) != -1:
                score_result[i] += 1
        score_full.append(len(it)-space)

def send2db(file):
    try:
        select_org, topic, toUser, tel, date2, byUser, text = main_mantext(file)
        _TH_FULL_MONTHS = {
            "มกราคม": 1,
            "กุมภาพันธ์": 2,
            "มีนาคม": 3,
            "เมษายน": 4,
            "พฤษภาคม": 5,
            "มิถุนายน": 6,
            "กรกฎาคม": 7,
            "สิงหาคม": 8,
            "กันยายน": 9,
            "ตุลาคม": 10,
            "พฤศจิกายน": 11,
            "ธันวาคม": 12,
        }
        print(f'ส่วนราชการ หรือ ส่วนงาน: {select_org[0]}')
        print(f'เรื่อง: {topic[0]}')
        print(f'เรียน: {toUser[0]}')
        print(f'โทร: {tel[0]}')
        print(f'วันที่: {date2[0]}')
        print(f'คนเช็น: {byUser[-1]}')
        x = date2[0].split(" ")
        day, month, year = 0, 0, 0
        if '' in x:
            x.remove('')
        try:
            month = _TH_FULL_MONTHS[x[1]]
            if x[0].isnumeric():
                if int(x[0]) >= 1 and int(x[0]) <= 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
                    day = int(x[0])
                elif int(x[0]) >= 1 and int(x[0]) <= 30 and (month == 4 or month == 6 or month == 9 or month == 11):
                    day = int(x[0])
                elif int(x[0]) >= 1 and int(x[0]) <= 29 and month == 2:
                    day = int(x[0])
                else:
                    day = 0
            else:
                day = 0
            if x[2].isnumeric():
                if len(x[2]) <= 4:
                    year = int(x[2]) - 543
                else:
                    year = 0
            else:
                year = 0
            #newdocumentAdd("dummydoc", res[1], res[5], res[0], res[2], "สังกัดผู้รับ", "เนื้อหา", x[2], x[1], x[0])
            return select_org[0], topic[0], toUser[0], byUser[-1], day, month, year, text
        except:
            print("ไม่ครบ")
            return select_org[0], topic[0], toUser[0], byUser[-1], 0, 0, 0, text
    except:
        print("exit!!!")

def display_list(file):
    select_org, topic, toUser, tel, date2, byUser, text = main_mantext(file)
    try:
        return select_org, topic, toUser, byUser, date2, text
    except:
        print("error")

# display()
# main_mantext()

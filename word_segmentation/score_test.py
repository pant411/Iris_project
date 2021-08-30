from os import replace
from Levenshtein import editops
from manTextV4 import main_mantext

def read_key(File):
    my_file = open('docs_source/'+File+'_key.txt', "r")
    content = my_file.read()
    content_list = content.split(",")
    my_file.close()    
    return content_list

def recall(test,source,Insert,Replace,Delete):
    return (len(test)-Replace-Delete)/len(source)

def precision(test,source,Insert,Replace,Delete):
    return (len(test)-Replace-Delete)/len(test)

def cal_score(test,source):
    if test == '' or source == '':
        return 0.0,0.0
    t = editops(test,source)
    #print(f'data: {t}')
    Insert,Delete,Replace = 0,0,0
    for ele in t:
        Insert += ele.count('insert')
        Delete += ele.count('delete')
        Replace += ele.count('replace')
    #print(f'insert {Insert}')
    return recall(test,source,Insert,Replace,Delete),precision(test,source,Insert,Replace,Delete)

def test_score():
    File = input('please input file: ')
    source = read_key(File)
    data_test = main_mantext('score program',File)
    '''print(f'ส่วนราชการ หรือ ส่วนงาน: {org}')
    print(f'เรื่อง: {topic}')
    print(f'เรียน: {toUser}')
    print(f'โทร: {tel}')
    print(f'วันที่ี: {date}')
    print(f'คนเช็น: {byUser}')'''
    #print(source)
    #print(f'data: {data_test}')
    #print('doc_test                  doc_real')
    for i in range(6):
        print(f'doc_test: {data_test[i]} doc_real: {source[i]}')
        Recall,Precision = cal_score(data_test[i],source[i])
        print(f'recall: {Recall} precision: {Precision}')

test_score()
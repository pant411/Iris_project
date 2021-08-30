#! -*- coding: UTF8 -*-
from wordcut import Wordcut
if __name__ == '__main__':
    with open('bigthai.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
    #wordcut = Wordcut.bigthai()
    print(wordcut.tokenize("ภาควิชาวิศวกรรมคอมพิวเตอร์"))
    print(wordcut.tokenize("นเชิญกล่าวปิดโครงการการจัดแข่งขัน0ล๑5๕๕ก๐๕8๐๐1CampAsai1"))
    print(wordcut.tokenize('คณบดีคณะวิศวกรรมศาสตร์'))
    print(wordcut.tokenize('.๐๒๓๕๓๐๕๕๕ต่อ๑๕๐๓-๑๕๐๕'))
    print(wordcut.tokenize('๑๕  สิงหาคม ๒๕๐๑ '))
    print(wordcut.tokenize('พันธุ์ปิติ เปียมสง่า '))
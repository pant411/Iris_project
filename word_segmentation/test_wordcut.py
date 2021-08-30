from wordcut import Wordcut

def main():
    with open('dict.txt', encoding="UTF-8") as dict_file:
        word_list = list(set([w.rstrip() for w in dict_file.readlines()]))
        wordcut = Wordcut(word_list)
        doc = input("file: ")
        data = open("docs/{}.txt".format(doc),"r")  
        for line in data.readlines():      
            #print(wordcut.tokenize(line))
            res = wordcut.tokenize(line)
            res = list(map(lambda s: s.strip(), res))
            res.append('\n')
            print(res)

main()
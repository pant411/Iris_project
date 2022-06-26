import pandas as pd
import textdistance
from collections import Counter

words = []
with open('auto.txt', 'r', encoding="utf-8") as f:
    data = f.read()
    data= data.lower()
    data = data.replace("\n","\t")
    words = data.split("\t")
# This is our vocabulary
V = set(words)
word_freq = {}  
word_freq = Counter(words)
probs = {}     
Total = sum(word_freq.values())    
for k in word_freq.keys():
    probs[k] = word_freq[k]/Total

def my_autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in V:
        return('Your word seems to be correct')
    else:
        sim = [1-(textdistance.Jaccard(qval=2).distance(v,input_word)) for v in word_freq.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word', 0:'Prob'})
        df['Similarity'] = sim
        output = df.sort_values(['Similarity', 'Prob'], ascending=False).head()
        return(output)

print(my_autocorrect('ประดนเดช คุปต์').iloc[0]["Word"])
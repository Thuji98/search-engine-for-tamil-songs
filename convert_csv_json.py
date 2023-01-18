import json
import codecs
import pandas as pd


fileToWrite = codecs.open('C:/ELK/180482C/corpus/180482C_corpus.json', 'w', encoding='utf-8')
df = pd.read_csv('C:/ELK/180482C/corpus/180482C_corpus.csv')

def checkStr(val):
    return isinstance(val, str)
    
fieldsList = [   [["உருவகம்_1",'metaphor_1'], ["மூலம்_1",'source_domain_1'], ["இலக்கு_1", 'target_domain_1'], ["விளக்கம்_1",'interpretation_1' ]],
            [["உருவகம்_2",'metaphor_2'], ["மூலம்_2",'source_domain_2'], ["இலக்கு_2", 'target_domain_2'], ["விளக்கம்_2",'interpretation_2' ]],
            [["உருவகம்_3",'metaphor_3'], ["மூலம்_3",'source_domain_3'], ["இலக்கு_3", 'target_domain_3'], ["விளக்கம்_3",'interpretation_3' ]],
            [["உருவகம்_4",'metaphor_4'], ["மூலம்_4",'source_domain_4'], ["இலக்கு_4", 'target_domain_4'], ["விளக்கம்_4",'interpretation_4' ]],
            [["உருவகம்_5",'metaphor_5'], ["மூலம்_5",'source_domain_5'], ["இலக்கு_5", 'target_domain_5'], ["விளக்கம்_5",'interpretation_5' ]],
            [["உருவகம்_6",'metaphor_6'], ["மூலம்_6",'source_domain_6'], ["இலக்கு_6", 'target_domain_6'], ["விளக்கம்_6",'interpretation_6' ]]
]

for i in range(df.shape[0]):
    
    dict_ = {}
    dict_["பாடல் வரிகள்"] = df['Lyrics'][i]
    dict_["திரைப்படம்"] = df['Album'][i]
    dict_["பாடலாசிரியர்"] = df['Lyricist'][i]
    dict_["பாடகர்கள்"] = df['Singers'][i]
    dict_["வருடம்"] = json.dumps(int(df['Year'][i]))

    for j in range(6):
        for k in range(4):
            val = df[fieldsList[j][k][1]][i]
            if  checkStr(val):
                dict_[fieldsList[j][k][0]] = val
    

    fileToWrite.write('{ "index" : { "_index" : "lyrics_metaphor_db", "_id" :' + str(i) + ' } }\n')
    json.dump(dict_, fileToWrite, ensure_ascii=False)
    fileToWrite.write('\n')
    i += 1

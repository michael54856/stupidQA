
import json
import jieba
from opencc import OpenCC

punc = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 

finalIndex = dict()

articleCount = 0

with open("wiki_2021_08_05_1215639.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(len(data))
    print(data[0])
    
    for article in data:
        str = article['articles']
        str = OpenCC('t2s').convert(str)
        seg_list = jieba.lcut(str)
        articleWord = dict()
        for seg in seg_list:
            if(seg not in punc):
                word = OpenCC('s2t').convert(seg)
                if word in articleWord:
                    articleWord[word] += 1
                else:
                    articleWord[word] = 1
        for key,value in articleWord.items():
            if key not in finalIndex:
                finalIndex[key] = list()
            finalIndex[key].append({'id': article['id'], 'count': value})
        articleCount += 1
        print(articleCount)


with open('invertedIndex.json', 'w', encoding="utf-8") as jsonfile:
    json.dump(finalIndex, jsonfile, ensure_ascii=False)
            



import json
import ijson

punc = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 

finalIndex = dict()

articleCount = 0

with open("wiki_tokenize_2021_08_05_1215639.json", "r", encoding="utf-8") as f:
    for record in ijson.items(f, "item"):
        wordList = []
        for line in record['tokens']:
            for word in line:
                if word[0] not in wordList:
                    wordList.append(word[0])


        for element in wordList:
            if(element not in finalIndex):
                finalIndex[element] = list()
            finalIndex[element].append(record['id'])

        if articleCount % 10000 == 0:
            print(articleCount)
        
        articleCount += 1



with open('invertedIndex.json', 'w', encoding="utf-8") as jsonfile:
    json.dump(finalIndex, jsonfile, ensure_ascii=False)
        


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
                idx = -1
                for i,item in enumerate(wordList):
                    if(word[0] == item[1]):
                        idx = i
                        break
                if idx == -1:
                    wordList.append([record['id'],word[0],1])
                else:
                    wordList[idx][2] += 1

        for element in wordList:
            if(element[1] not in finalIndex):
                finalIndex[element[1]] = list()
            finalIndex[element[1]].append([element[0],element[2]])
        articleCount += 1
        print(articleCount)



with open('invertedIndex.json', 'w', encoding="utf-8") as jsonfile:
    json.dump(finalIndex, jsonfile, ensure_ascii=False)
        


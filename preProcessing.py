import json
import ijson

punc = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 

finalIndex = dict()

fileCounter = 0
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

        if articleCount % 100000 == 0 and articleCount != 0:
            #output
            with open('preProcessed'+ str(fileCounter) +'.txt', 'w', encoding="utf-8") as output:
                print(len(finalIndex), file=output)
                for key,value in finalIndex.items():
                    print(key, end = ' ', file=output)
                    print(len(value), end = ' ', file=output)
                    for e in value:
                        print(e, end=' ', file=output)
                    print('',file=output)
            fileCounter += 1
            finalIndex.clear()
            print(articleCount)
        
        articleCount += 1


if articleCount % 100000 != 0:
    with open('preProcessed'+ str(fileCounter) +'.txt', 'w', encoding="utf-8") as output:
        print(len(finalIndex), file=output)
        for key,value in finalIndex.items():
            print(key, end = ' ', file=output)
            print(len(value), end = ' ', file=output)
            for e in value:
                print(e, end=' ', file=output)
            print('',file=output)
        


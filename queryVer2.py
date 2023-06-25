import json
from udicOpenData.dictionary import *
from udicOpenData.stopwords import *
import math

punc = '！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 

data = None


with open("invertedIndex.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print('inverted index loaded')

questionCount = 0

FinalAnswerOutput = []

with open("test.json", "r", encoding="utf-8") as questionFile:
    questions = json.load(questionFile)
    for question in questions:
        seg_list = list(rmsw(question['Question']))
        wordList = []
        for seg in seg_list:
            if(seg not in punc):
                if seg not in wordList:
                    wordList.append(seg)

        FINAL_Answer_Score = 0
        finalAnswer = ''

        score = 0
        answerList = list(rmsw(question['A']))
        for answer in answerList:
            answerCountList = data[answer]
            intersectionScore = 0
            for word in wordList:
                if (word not in data) or (answer not in data):
                    continue
                
                intersectionCount = 0
                compareList = data[word]
                p1 = 0
                p2 = 0
                while(p1 < len(answerCountList)  and p2 < len(compareList)):
                    if answerCountList[p1] == compareList[p2]:
                        intersectionCount += 1
                        p1 += 1
                        p2 += 1
                    elif answerCountList[p1] > compareList[p2]:
                        p2 += 1
                    elif answerCountList[p1] < compareList[p2]:
                        p1 += 1


                intersectionScore += ((intersectionCount*len(answer))/len(compareList))
            
            score += intersectionScore
        
        score = score / len(answerList)


                
        if(score > FINAL_Answer_Score):
            FINAL_Answer_Score = score
            finalAnswer = 'A'

        score = 0
        answerList = list(rmsw(question['B']))
        for answer in answerList:
            answerCountList = data[answer]
            intersectionScore = 0
            for word in wordList:
                if (word not in data) or (answer not in data):
                    continue
                
                intersectionCount = 0
                compareList = data[word]
                p1 = 0
                p2 = 0
                while(p1 < len(answerCountList)  and p2 < len(compareList)):
                    if answerCountList[p1] == compareList[p2]:
                        intersectionCount += 1
                        p1 += 1
                        p2 += 1
                    elif answerCountList[p1] > compareList[p2]:
                        p2 += 1
                    elif answerCountList[p1] < compareList[p2]:
                        p1 += 1

                intersectionScore += ((intersectionCount*len(answer))/len(compareList))
            
            score += intersectionScore
        
        score = score / len(answerList)

                
        if(score > FINAL_Answer_Score):
            FINAL_Answer_Score = score
            finalAnswer = 'B'


        score = 0
        answerList = list(rmsw(question['C']))
        for answer in answerList:
            answerCountList = data[answer]
            intersectionScore = 0
            for word in wordList:
                if (word not in data) or (answer not in data):
                    continue
                
                intersectionCount = 0
                compareList = data[word]
                p1 = 0
                p2 = 0
                while(p1 < len(answerCountList)  and p2 < len(compareList)):
                    if answerCountList[p1] == compareList[p2]:
                        intersectionCount += 1
                        p1 += 1
                        p2 += 1
                    elif answerCountList[p1] > compareList[p2]:
                        p2 += 1
                    elif answerCountList[p1] < compareList[p2]:
                        p1 += 1

                intersectionScore += ((intersectionCount*len(answer))/len(compareList))
            
            score += intersectionScore
        
        score = score / len(answerList)
                
        if(score > FINAL_Answer_Score):
            FINAL_Answer_Score = score
            finalAnswer = 'C'

        print(questionCount,end=": ")
        print(finalAnswer)
        FinalAnswerOutput.append(finalAnswer)
        questionCount += 1

with open("output.json", "w") as outfile:
    json.dump(FinalAnswerOutput, outfile)
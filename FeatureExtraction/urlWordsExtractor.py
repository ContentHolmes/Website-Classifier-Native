import requests
from bs4 import BeautifulSoup
import sys
import operator
import csv
import re
from collections import defaultdict

import nltk
from nltk import pos_tag
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer

def dataExtractor(category):
    fd = open("../Data/data_" + category + ".csv",'r')
    urls = []
    for line in fd:
        lineContent = line.split(',')
        urls.append(lineContent[1])
    
    fd.close()
    return urls


regexp = '\W+'
wordCount = defaultdict(int)
lemmatizer = WordNetLemmatizer()
stopWords = set(nltk.corpus.stopwords.words('english'))


def urlExtractor(category):
    urls = dataExtractor(category)

    with open("wordsPerCategory/words_"+category,'w') as fileOut:
        
        writer = csv.writer(fileOut)
        urlWords = []

        print("Extracting url data...")
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            metas = soup.find_all('meta')
            title = soup.find_all('title')

            for meta in metas:
                if 'name' in meta.attrs:
                    if meta.attrs['name'] == 'description':
                        urlWords += re.split(regexp,meta.attrs['content'])

                    if meta.attrs['name'] == 'keywords':
                        urlWords += re.split(regexp,meta.attrs['content'])

                if 'property' in meta.attrs:
                    if meta.attrs['property'] == 'og:description':
                        urlWords += re.split(regexp,meta.attrs['content'])

                    if meta.attrs['property'] == 'og:keywords':
                        urlWords += re.split(regexp,meta.attrs['content'])

            urlWords += re.split(regexp,title[0].string)
            
        print("Lemmatizing Words...")
        for word in urlWords:
            if word != "":
                word = word.lower()
                tag = pos_tag(word_tokenize(word))[0][1][0].lower()
                
                if tag in ['a','v','r']:
                    lemmatizedWord = (lemmatizer.lemmatize(word,tag))
                else:
                    lemmatizedWord = lemmatizer.lemmatize(word)
                
                if lemmatizedWord not in stopWords\
                    and not lemmatizedWord.isdigit():
                    wordCount[lemmatizedWord] += 1

        maxValueKey = max(wordCount, key = lambda key: wordCount[key])
        maxValue = wordCount[maxValueKey]
        for word in wordCount:
            rowNew = [word] + [float(wordCount[word])/maxValue]
            writer.writerow(rowNew)

# urlExtractor("Health")
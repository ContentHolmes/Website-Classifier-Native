#! /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os
import sys
import csv
import re
from collections import defaultdict
from urlWordsExtractor import dataExtractor
import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def getUrlFtrVector(wordList, ftrWords):

	ftrVector = [0]*len(ftrWords)

	for word in wordList:
		if word != "":
			word = word.lower()
			tag = pos_tag(word_tokenize(word))[0][1][0].lower()

			if tag in ['a','v','r']:
			    lemmatizedWord = (lemmatizer.lemmatize(word,tag))
			else:
			    lemmatizedWord = lemmatizer.lemmatize(word)

			if lemmatizedWord in ftrWords:
				ftrVector[ftrWords.index(lemmatizedWord)] = 1

	return ftrVector


def readFtrWords(fileCount, thMin, thMax):
	ftrWords = []

	with open(fileCount, "r") as csvfileIn:
		reader = csv.reader(csvfileIn)
		for row in reader:
			if thMin <= float(row[1]) <= thMax and row[0] not in ftrWords:
				ftrWords.append(row[0])
	return ftrWords


classDict = {
	"Adult":0,
	"Arts":1,
	"Computers":2,
	"Health":3,
	"otpothr":4,
	"tickets":5,
	"prsonal":6,
}

wordFile = "wordsPerCategory/words_dmoz.txt"
regexp = '\W+'			
wordount = defaultdict(int)
lemmatizer = WordNetLemmatizer()
stopwords = set(nltk.corpus.stopwords.words('english'))
ftrWords = readFtrWords(wordFile, 0.30, 1.0)

def featureExtractor(category):
	urls = dataExtractor(category)

	with open("../Features/ftr_"+category+".txt", "w+") as fileOut:
    
		classNo = classDict[category]

		print("Extracting url data...")
		for url in urls:
			urlWords = []
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

			print("Creating Feature Vector...")
			urlFtrVector = getUrlFtrVector(urlWords,ftrWords)
			fileOut.write(str([urlFtrVector,classNo]))
			fileOut.write('\n')

featureExtractor("Health")
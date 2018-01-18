#! /usr/bin/python3

import os
import sys
import csv
import re
from collections import defaultdict

import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



def getTextFtrVector(text, ftrWords):
	words = re.split(regexp, text)

	ftrVector = [0]*len(ftrWords)

	for word in words:
		lemmatizedWord = lemmatizer.lemmatize(word)
		lemmatizedWord = lemmatizedWord.lower()
		
		if lemmatizedWord in ftrWords:
			ftrVector[ftrWords.index(lemmatizedWord)] = 1
	
	return ftrVector


def readFtrWords(fileCount, thMin, thMax):
	ftrWords = []

	with open(fileCount, "r", newline="") as csvfileIn:
		reader = csv.reader(csvfileIn)
		for row in reader:
			if thMin <= float(row[1]) <= thMax and row[0] not in ftrWords:
				ftrWords.append(row[0])
	return ftrWords



classDict = {
	"unknown":0,
	"svcnpro":1,
	"netwkop":2,
	"transac":3,
	"otpothr":4,
	"tickets":5,
	"prsonal":6,
}

regexp = '\W+'			
wordount = defaultdict(int)
lemmatizer = WordNetLemmatizer()
stopwords = set(nltk.corpus.stopwords.words('english'))
ftrwords = readFtrWords(fileCount, 0.30, 1.0)

with open(fileIn, "r", newline="") as csvfileIn,\
	open(fileOut, "w", newline="") as csvfileOut:
	
	writer = csv.writer(csvfileOut)

	for line in :
		
		classNo = classDict[row[]]
		sender_ftr = sender_dict[row[col_sender]]
		iscontact_ftr = 0 if row[col_iscontact]=="N" else 1
		text_ftr_vector = get_text_ftr_vector(row[col_text], ftr_words)

		# row_new = [class_num] + [sender_ftr] + [iscontact_ftr] + text_ftr_vector
		row_new = [class_num] + text_ftr_vector
		writer.writerow(row_new)

		# print(row_new)
		# break

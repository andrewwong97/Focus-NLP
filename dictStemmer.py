import os, csv
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

# exports csv files for a folder of .txt essays
# input must be a string

def main(directory):
	os.chdir(directory)
	fileList = [item for item in os.listdir(os.getcwd())]
	fileList.remove('.DS_Store'), fileList.remove('case-refs.csv')
	fileList.remove('jhudesc-1.txt')

	for i in fileList:
		os.chdir(directory)
		data = open(i).read()
		tokenizer = RegexpTokenizer(r'\w+')
		token = tokenizer.tokenize(data)
		stop = [str(word) for word in stopwords.words('english')]
		data = [j for j in token if j not in stop]

		uniData = [word.decode("utf-8", "ignore") for word in data]
		allData = [word.encode("ascii", "ignore") for word in uniData]
		allCountDict = {}

		h = open('/Users/Andrew/Dropbox/python/focus/Word_Analysis/input/jhudesc-1.txt').read()
		hop = tokenizer.tokenize(h)
		hopData = [word.decode("utf-8", "ignore") for word in hop]
		hopData = [word.encode("ascii", "ignore") for word in hopData]

		for word in allData:
			for item in hopData:
				if word  == item:
					allCountDict.update({word: allData.count(word)})

		os.chdir('/Users/Andrew/Dropbox/python/focus/Word_Analysis/output/')

		writer = csv.writer(open(str(i[:-4]) + '.csv', 'wb'))
		for key, value in allCountDict.items():
		   writer.writerow([key, value])



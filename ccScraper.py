import os, csv, requests, time
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

start = time.time()

os.chdir('/Users/Andrew/Dropbox/python/focus/ccscrape')

f = open('ccEssayLinks.csv', 'rU')
reader = csv.reader(f)

essayData = [row for row in reader]

# tokenizes hopkins data, later to be used to compare to EACH essay in essayData

tokenizer = RegexpTokenizer(r'\w+')
h = open('/Users/Andrew/Dropbox/python/focus/Word_Analysis/input/jhudesc-1.txt').read()
hop = tokenizer.tokenize(h)
hopData = [word.decode("utf-8", "ignore") for word in hop]
hopData = [word.encode("ascii", "ignore") for word in hopData]

os.chdir('/Users/Andrew/Desktop/CC')

# time to analyze each essay

allPosts = []
for row in essayData:
	r = requests.get(row[0])
	soup = BeautifulSoup(r.content)
	divMessages = soup.find_all('div', class_="Message") # takes all user submitted posts
	for item in divMessages[0:1]:
		t = tokenizer.tokenize(item.get_text()) # makes it possible to analyze with NLTK
		t = [char.decode("utf-8", "ignore") for char in t]
		t = [char.encode("ascii", "ignore") for char in t]
	if len(t) >= 300: # saves all essays greater than 300 words
		with open("output_" + str(enumerate(essayData)) + ".txt", "w") as txtFile:
			txtFile.write("%s" % t)


end = time.time()
print end - start

import os, csv, requests, time
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

start = time.time()

os.chdir('/Users/Andrew/Dropbox/python/focus/ccscrape')

f = open('ccEssayLinks.csv', 'rU')
reader = csv.reader(f)

essayData = [row for row in reader]

tokenizer = RegexpTokenizer(r'\w+')
h = open('/Users/Andrew/Dropbox/python/focus/Word_Analysis/input/jhudesc-1.txt').read()
hop = tokenizer.tokenize(h)
hopData = [word.decode("utf-8", "ignore") for word in hop]
hopData = [word.encode("ascii", "ignore") for word in hopData]

os.chdir('/Users/Andrew/Desktop')

os.chdir('CC')

# attempt to scrape messages off CC links
allPosts = []
# divMessages = soup.find_all('div', class_="Message")

for row in essayData:
	for string in row:
		r = requests.get(string)
		soup = BeautifulSoup(r.content)
		divMessages = soup.find_all('div', class_="Message")


		# takes all divs with class Message, adds it to allPosts

		for item in divMessages[0:1]:
			t = tokenizer.tokenize(item.get_text())
			t = [char.decode("utf-8", "ignore") for char in t]
			t = [char.encode("ascii", "ignore") for char in t]
			allPosts.append(t)

		# creates separate files for each user post

		for i in range(1, len(essayData) + 1):
			with open("output_" + str(i) + ".txt", "w") as txtFile:
				txtFile.write("%s" % allPosts)

		for word in allPosts:
			for item in set(hopData):
				if word  == item:
					allCountDict.update({word: allData.count(word)})


end = time.time()
print end - start
				
			

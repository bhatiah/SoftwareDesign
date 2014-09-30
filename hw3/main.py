# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 13:54:37 2014
This program is supposed to take in a URL of a book from ProjectGutenburg and tell you whether
if the book can be read by a 5th grader. The program dissects the book by splitting all the words
up in to a list and then compares each word to another list that contains vocab for 5th graders.
The program also creates a file for the words that were not similar to the original list. The 
program ignores words that are 2 letters or less. Thinking about making it 3. 

*** I still need to tweak this a bit *** 
So far most childrens books I have tested have given me a 70 plus percent on similarity. While 
adult books are below sixty. 


@author: Harshvardhan Bhatia
"""

from pattern.web import *
import string

# Downloads book from the website and puts it in a temporary file
def dload_book(url):
    text = encode_utf8(plaintext(URL(url).download()))
    bload = open('temp_load.txt', 'w')
    bload.write(text)
    bload.close()

# Downloads the 5th grader words from a file and puts it in a list that is returned    
def word_list():
	words_load = open('words2.txt', 'r')
	words = list(words_load)
	x = 0
	while x < len(words):
		words[x] = words[x].rstrip()
		x = x + 1
	words_load.close()
	return words

# This function does a bunch of things.
# 1. Compares every word in the book to the words in the list.
# 2. Traverses the book to the point where the book starts. 
# 3. Takes words from the book that are not in the original list and puts them in another file. 
# 4. Counts total similar words, and total words in the book. 
# 5. Returns percentage of similar words to the main function.  
def analysis(words):
	q = open('temp_load.txt', 'r')
	g = open('nwords.txt', 'w')
	book = q.read()
	book = string.split(book)
	x = 0
	y = 0
	while x < 2:
		if book[y] == '***':
			x = x + 1
			y = y + 1
		else:
			y = y + 1
	#f = total similar words
	f = 0
	#t = total words 
	t = 0
	# nwords = array of words not in our dictionary, k = traversal of said list
	nwords = []
	k = 0
	prev = 0
	u = 0
	while book[y] != '***':
		if len(book[y]) <= 2:
			y = y + 1
			continue
		if f == prev:
			u = 1
			for m in range(len(nwords)):
				if book[y - 1] == nwords[m]:
					u = 0
					break
		if u == 1:
			nwords.append(book[y - 1])
		prev = f
		u = 0
		v = 0
		for v in range(len(words)):
			book[y] = book[y].translate(None, string.punctuation)
			book[y] = book[y].lower()
			if (book[y] == words[v]):
				f = f + 1
		t = t + 1
		y = y + 1
	g.write('\n'.join(map(lambda x: str(x), nwords)))	
	return (float(f) / (t)) * 100		

# Main Code
url = str(raw_input('Enter your URL: '))      
dload_book(url)
words = word_list()
percent = analysis(words)
print 'The book has received a readability score of ' + str(percent)
if percent > 70:
	print "The book is good for the 5th grader"
if percent > 60 and percent < 70:
	print "The book is okay for the 5th grader"
if percent < 60:
	print 'Not for a 5th grader'


    

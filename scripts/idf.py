import csv
import pandas as pd
import math
import argparse
import re
import json

def cleaned(row):
	row = re.sub("[^a-zA-Z_-]+",' ', row)
	return row.lower()
	
def idf(row, dic):
	for word in row.split(' '):
		if dic.get(word) == None:
			dic[word] = 1
		else:
			dic[word] += 1
	

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('input')
	parser.add_argument('output')
	args = parser.parse_args()
	words = {}
	words2 = {}
	with open(args.input,'r') as f:
		for i in f:
			j = json.loads(i)	
			title = j['data']['title']
			#print(cleaned(title))
			idf(cleaned(title),words)
		for i in words:
			if words[i] != 1:
				words2[i]=words[i]
	with open(args.output,'w') as h:
		json.dump(words2,h)

if __name__ == '__main__':
	main()



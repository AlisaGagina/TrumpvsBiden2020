#note, didn't actually end up using this code file. This was the initial brainstorming attempt
import argparse
import pandas as pd
import os
import csv
import math

def tfidf(df):
	total = {}
	subCount={}
	for index,row in df.iterrows():
		sub = row['subreddit']
		coding = row['coding']	
		if (sub not in subCount):
			subCount[sub]={}
			subCount[sub][coding] = 1
		elif (coding not in subCount[sub]):
			subCount[sub][coding] = 1
		else:
			subCount[sub][coding] += 1
		if (coding not in total):
			total[coding] = 1
		else:
			total[coding] += 1
	
	tfidf={}
	for (key,value) in subCount.items():
		tfidf[key]=value
		for (code,coding) in value.items():
			tfidf[key][code]=math.log10(total[code]/coding)
	for (key,value) in subCount.items():
		print(key)
		for (code,coding) in value.items():
			print("\t"+str(code)+", "+str(coding))

def main():
	total={}
	subCount={}
	parser = argparse.ArgumentParser()
	parser.add_argument("input",help="files containing the posts")

	args = parser.parse_args()
	df = pd.read_csv(args.input,sep="\t")	
	tfidf(df)

if __name__ == '__main__':
	main()

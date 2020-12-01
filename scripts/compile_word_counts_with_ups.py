import argparse
import pandas as pd
import json
import math
from collections import Counter

def clean(df):
	#drop unneeded columns
	#df=df.drop('ups', axis=1)
	df=df.drop('upvote_ratio', axis=1)
	df=df.drop('downs', axis=1)
	
	#regex, lowercase
	df['title']=df['title'].str.replace(r'[^a-z0-9A-Z_-]+', ' ')
	#df['title']=df['title'].str.replace(r'[^G20a-zA-Z_-]+', ' ')

	
	df['title']=df['title'].str.lower()
	return df


def getwordcounts(df):	
	count={'politics':{}, 'conservatives':{}}
	#get counts
	for index,row in df.iterrows():
		sub=row['subreddit']
		t=row['title']
		up=int(row['ups'])
		#words = t.split()
		words = [ x for x in t.split() if x.isnumeric() ==False and len(x)>2 ]

		for word in words:
			#print(word)

			if (word not in count[sub]):
				count[sub][word] = 1*math.log10(up+.01)
			else:
				count[sub][word] += 1*math.log10(up+.01)
	abovefive={'politics':{}, 'conservatives':{}}
	#get counts above four
	for sub, words in count.items():
		for word in words:
			if words[word]>=2:
				abovefive[sub][word]=words[word]
	return abovefive
'''
def tfidf(count,idf):
	errors = []
	tfidf = {}
	for (topic,dic) in count.items():
		tfidf[topic]={}
		for sub in dic:
			tfidf[topic][sub]={}
			for (word,count) in dic[sub].items():
				if word not in idf:
					errors.append(word)
					continue
				else:
					tfidf[topic][sub][word]=count*math.log(idf['total']/idf[word])					
	print(errors)
	for (topic,dic) in tfidf.items():
		for (sub,dic2) in dic.items():
			tfidf[topic][sub]=dict(Counter(dic2).most_common(10))

	return tfidf
'''

def alisatdidf(word, subreddit, topic, d):
	freqone=d[topic][subreddit][word]	
	freqall=0
	for topic, subreddit in d.items():
		for sub, words in subreddit.items():
			if word in words:
				freqall=freqall+1
	score = round(freqone* math.log10(16/freqall), 2)
	return score

def alisascores(d):
	scores= {'T':{'politics':{},'conservatives':{}},'D':{'politics':{},'conservatives':{}},'AT':{'politics':{},'conservatives':{}},
	 'AB':{'politics':{},'conservatives':{}}, 'C':{'politics':{},'conservatives':{}}, 'E':{'politics':{},'conservatives':{}}, 
	 'IR':{'politics':{},'conservatives':{}}, "O":{'politics':{},'conservatives':{}}}
	for topic, subreddit in d.items():
		for sub, words in subreddit.items():
			for word in words:
				#get score
				scores[topic][sub][word]=alisatdidf(word, sub, topic, d)
	for topic, subreddit in scores.items():
		for sub, words in subreddit.items():
			#sort in descending order
			scores[topic][sub] = dict( sorted(scores[topic][sub].items(), key=lambda item: item[1], reverse=True))
	return scores

def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="shuffled.tsv file")
	parser.add_argument('-o', '--output', help='output file')

	args = parser.parse_args()
	df = pd.read_csv(args.input, sep='\t')	
	df=clean(df)
	topics=['T','D','AT', 'AB', 'C', 'E', 'IR', "O"]
	count={'T':{},'D':{},'AT':{}, 'AB':{}, 'C':{}, 'E':{}, 'IR':{}, "O":{}}
	for topic in topics:
		posts = df[df['coding'] == topic]
		count[topic]=getwordcounts(posts)
	scores=alisascores(count)
	result={'T':{'politics':{},'conservatives':{}},'D':{'politics':{},'conservatives':{}},'AT':{'politics':{},'conservatives':{}},
	 'AB':{'politics':{},'conservatives':{}}, 'C':{'politics':{},'conservatives':{}}, 'E':{'politics':{},'conservatives':{}}, 
	 'IR':{'politics':{},'conservatives':{}}, "O":{'politics':{},'conservatives':{}}}
	'''
	for topic, subreddit in scores.items():
		for sub, words in subreddit.items():
			
			l=[]	
			for i in list(scores[topic][sub])[0:10]:	
				l.append(i)
			result[topic][sub]=l
	'''
	for (topic,dic) in scores.items():
		for (sub,dic2) in dic.items():
			result[topic][sub]=dict(Counter(dic2).most_common(10))
	print(result)
	with open(args.output, 'w') as f:
		json.dump(result, f)
	
if __name__ == '__main__':
	main()


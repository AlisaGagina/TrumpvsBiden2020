import argparse
import pandas as pd
import json
import math
from collections import Counter

def clean(df):
	#drop unneeded columns
	df=df.drop('ups', axis=1)
	df=df.drop('upvote_ratio', axis=1)
	df=df.drop('downs', axis=1)
	
	#regex, lowercase
	df['title']=df['title'].str.replace(r'[^a-zA-Z_-]+', ' ')
	df['title']=df['title'].str.lower()
	return df


def getwordcounts(df):	
	count={'politics':{}, 'conservatives':{}}
	#get counts
	for index,row in df.iterrows():
		sub=row['subreddit']
		t=row['title']
		words = t.split()
		for word in words:
			#print(word)
			if (word not in count[sub]):
				count[sub][word] = 1
			else:
				count[sub][word] += 1
	abovefive={'politics':{}, 'conservatives':{}}
	#get counts above four
	for sub, words in count.items():
		for word in words:
			if words[word]>=2:
				abovefive[sub][word]=words[word]
	return abovefive

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
def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="shuffled.tsv file")
	parser.add_argument('-o', '--output', help='output file')
	parser.add_argument('idf')

	args = parser.parse_args()
	df = pd.read_csv(args.input, sep='\t')	
	df=clean(df)
	topics=['T','D','AT', 'AB', 'C', 'E', 'IR', "O"]
	count={'T':{},'D':{},'AT':{}, 'AB':{}, 'C':{}, 'E':{}, 'IR':{}, "O":{}}
	for topic in topics:
		posts = df[df['coding'] == topic]
		count[topic]=getwordcounts(posts)
	with open(args.idf,'r') as idf:
		idfDic = json.load(idf)
		final = tfidf(count,idfDic)
		
	
	with open(args.output, 'w') as f:
		json.dump(final, f)
	
if __name__ == '__main__':
	main()


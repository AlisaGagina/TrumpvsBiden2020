import argparse
import pandas as pd
import json


def clean(df):
	#drop unneeded columns
	df=df.drop('ups', axis=1)
	df=df.drop('upvote_ratio', axis=1)
	df=df.drop('downs', axis=1)
	
	#regex, lowercase
	df['title']=df['title'].str.replace(r'[^\w\s\']+', ' ')
	df['title']=df['title'].str.replace(r'\d+', ' ')
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
	
	
	with open(args.output, 'w') as f:
		json.dump(count, f)
	
if __name__ == '__main__':
	main()


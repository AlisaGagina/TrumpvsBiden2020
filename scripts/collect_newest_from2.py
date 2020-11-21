import argparse
import requests
import json

def get_posts(subreddit_name, aftern):
	print(subreddit_name)
	data=requests.get(f"http://api.reddit.com{subreddit_name}/new?limit=100&after={aftern}", headers={'User-Agent': 'windows:requests (by /u/alisa)'})
	content=data.json()['data']
	lastfullname=content['after']
	posts= content['children']
	return lastfullname, posts


def getNum (sname, num):
	l=[]
	after=''
	#  int(333/100) 3, 3+1 = 4
	for i in range(0, int(num/100)+1):
		after, posts = get_posts(sname, after)
		l.extend(posts)
	return l[:num]
        


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('subreddit1', help="input first subreddit")
	parser.add_argument('subreddit2', help='input second subreddit')
	parser.add_argument('-o','--output', required=True, help='name of output file')
	parser.add_argument('-n','--num', required=True, help='num of posts to collect per subreddit')

	args = parser.parse_args()
	iname1=args.subreddit1
	iname2=args.subreddit2
	oname=args.output
	num=int(args.num)

	o1=getNum(iname1, num)
	o2=getNum(iname2, num)

	with open(oname, 'w') as f:
		for line in o1:
			print(json.dumps(line), file = f)
		for line in o2:
			print(json.dumps(line), file=f)	

if __name__=='__main__':
        main()

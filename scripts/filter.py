import os.path as osp
import argparse
import json
import pandas as pd

def main():
    script_dir = osp.dirname(__file__)
    names = []
    titles = []
    subreddit = []
    #urls = []
    upvote_ratio = []
    ups = []
    downs = []


    # Extracts Json lines from the files in data and adds it to the names and title list
    for i in range(1,4):
        with open(osp.join(script_dir,'..','data',f'reddit2020112{i}.json')) as fin:
            lines = fin.readlines()
            for x in range(len(lines)):
                data = json.loads(lines[x])['data']
                names.append(data['name'])
                titles.append(data['title'])
                subreddit.append(data['subreddit'])
                upvote_ratio.append(data['upvote_ratio'])
                ups.append(data['ups'])
                downs.append(data['downs'])
            #urls.extend([json.loads(lines[x])['data']['url'] for x in range(len(lines))])

    #print(len(urls))

    index_to_keep = [] #has the index of all lines we wanna keep
    president_names = ['donald', 'trump', 'joe', 'biden', 'president']
    #populates the index_to_keep
    for i in range(len(titles)):
        title = titles[i].lower()
        if any(name in title for name in president_names):
            index_to_keep.append(i)



    #keeps data we wanna keep
    names = [names[i] for i in index_to_keep]
    titles = [titles[i] for i in index_to_keep]
    subreddit = [subreddit[i] for i in index_to_keep]
    upvote_ratio = [upvote_ratio[i] for i in index_to_keep]
    ups = [ups[i] for i in index_to_keep]
    downs = [downs[i] for i in index_to_keep]
    #print(len(titles))
    #politics = [1 for x in subreddit if x =='politics']
    #print(sum(politics))

    df = pd.DataFrame({'name': names,'subreddit': subreddit, 'title': titles, 'upvote_ratio': upvote_ratio, 'ups': ups,"downs":downs })
    df["coding"] = ""

    output_file_tsv = osp.join(script_dir,'..','data','filtered_data.tsv')
    df.to_csv(output_file_tsv, sep='\t', index=False)

    output_file_csv = osp.join(script_dir, '..', 'data', 'filtered_data.csv')
    df.to_csv(output_file_csv, index=False)


    #print(names, titles)

if __name__ =='__main__':
    main()
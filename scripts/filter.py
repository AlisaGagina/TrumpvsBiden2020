import os.path as osp
import argparse
import json
import pandas as pd

def main():
    script_dir = osp.dirname(__file__)
    names = []
    titles = []
    subreddit = []
    urls = []


    # Extracts Json lines from the files in data and adds it to the names and title list
    for i in range(1,4):
        with open(osp.join(script_dir,'..','data',f'reddit2020112{i}.json')) as fin:
            lines = fin.readlines()
            names.extend([json.loads(lines[x])['data']['name'] for x in range(len(lines))])
            titles.extend([json.loads(lines[x])['data']['title'] for x in range(len(lines))])
            subreddit.extend([json.loads(lines[x])['data']['subreddit'] for x in range(len(lines))])
            #urls.extend([json.loads(lines[x])['data']['url'] for x in range(len(lines))])

    #print(len(urls))

    index_to_keep = [] #has the index of all lines we wanna keep

    #populates the index_to_keep
    for i in range(len(titles)):
        if ("trump" or "biden" or "donald" or "joe") in titles[i].lower():
            index_to_keep.append(i)

    #keeps data we wanna keep
    names = [names[i] for i in index_to_keep]
    titles = [titles[i] for i in index_to_keep]
    subreddit = [subreddit[i] for i in index_to_keep]

    df = pd.DataFrame({'name': names, 'title': titles, 'subreddit': subreddit})
    df["coding"] = ""

    output_file_tsv = osp.join(script_dir,'..','data','filtered_data.tsv')
    df.to_csv(output_file_tsv, sep='\t', index=False)

    output_file_csv = osp.join(script_dir, '..', 'data', 'filtered_data.csv')
    df.to_csv(output_file_csv, index=False)

    #print(len(names),len(titles))
    #print(names, titles)

if __name__ =='__main__':
    main()
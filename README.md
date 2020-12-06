# TrumpvsBiden2020  
We wanted to look into the aftermath of the 2020 election. We acquired and annotated 2000 posts from reddit over the course of 3 days. We then analyzed the topics that the reddit users were most engaged in regards to the presidential candidates Trump and Biden. 

The following are just notes through out the process:
## Git
- code
  - `git clone https://username@github.com/AlisaGagina/TrumpvsBiden2020`
  - `git commit -a -m "did a thing"`
  - `git push https://username@github.com/AlisaGagina/TrumpvsBiden2020`
- note 
  - should ask for a password everytime
  - might also need to do:
    - `git config --global user.name "username"`
    - `git add newfile_not_yet_on_git`

## Data Collection:
 To get data from two subreddits, input all 4 args! Returns a file of length n*2
 - `python3 collect_newest_from2.py /r/politics /r/conservatives -n 333 -o ../data/reddit20201121.json   `
 -  note that I am using python3
 -  also note that we got 333 posts Nov 21. and Nov. 22, 334 Nov 23
 
 ### Possibly useful reddit file parameters?
 - "name": "t3_jyj67n"
 - "subreddit": "politics"
 - "title": "Trump privately plots his next act \u2014 including a potential 2024 rematch"
 - "upvote_ratio": 0.67
 - "ups": 6, "downs": 0
 
 ### Cleaning data
  was done in filter.py and shuffle.py
 
 ## Topics to annotate:
 International Relations(IR), Anti-Trump(AT), Anti-Biden(AB), Transition(T), Domestic Policy(D), Elections(E), Commentary(C) and Other(O)
 We perforemed three different tf-idf analyses to categorie the distinct words in each category.
 - See `compile_word_counts_derek.py` (topics only), `compile_word_counts.py` (topics and subreddits combined), `compile_word_counts_upvotes.py` (topics and subreddits combined with ups to represent popularty)
 
 ### Statistics ideas:
 - average upvote per topic
 - pie chart of topics / subreddit
 - top 20 titles  (or topics)/ subredddit (or all) 
   - top sorted by like amount
 - AB, AT, C differences across the two subreddits, and the average reaction to them (upvote)
 


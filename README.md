# TrumpvsBiden2020   

## Git
- code
  - `git clone https://username@github.com/AlisaGagina/TrumpvsBiden2020`
  - `git commit -a -m "did a thing"`
  - `git push https://username@github.com/AlisaGagina/TrumpvsBiden2020`
- note 
  - should ask for a password everytime
  - might also need to do
    -`git config --global user.name "username"`
    -`git add README.md source/ src/ data/`

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


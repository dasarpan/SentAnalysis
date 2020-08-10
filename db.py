import asyncio
import sqlite3 
import twitter

def init_db(db_name):
    if __name__ == "__main__":
        import sys
        init_db(int(sys.argv[1]))
    else:
        conn = sqlite3.connect(db_name)
        c = conn.cursor()
        c.execute('''CREATE TABLE tweets
                        (tid INTEGER PRIMARY KEY, body TEXT, user TEXT, sentiment REAL, tags TEXT)''')
    conn.commit()
    return conn


def load_db(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def build_sample_db(db_curs):
    for i in range(20):
        #Vulnerable use ? syntax
        db_curs.execute("INSERT INTO tweets (body,user) VALUES('Tweet%s','User%s');"% (i,i))

def calc_sentiment(db_curs):
    db_curs.execute('SELECT * FROM tweets WHERE sentiment IS NULL')
    active_tweets = []
    for t in db_curs:
        active_tweets.append((0,t["tid"]))
    db_curs.executemany("UPDATE TWEETS SET sentiment = ? WHERE tid = ?", active_tweets)

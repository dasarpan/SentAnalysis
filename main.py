import asyncio
import multiprocessing
import concurrent.futures # Unused
from db import *
from os import path

def main():
    db = "example.db"
    conn = load_db(db) if path.exists(db) else init_db(db)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()

    # build_sample_db(c)

    # Handle processes with pools
    fill_db = multiprocessing.Process(target=calc_sentiment, args=(c,))
    fill_db.start()



    fill_db.join()
    conn.commit()
    conn.close()

main()

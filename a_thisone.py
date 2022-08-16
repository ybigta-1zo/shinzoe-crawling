from crawling_thisone import naver_crawling, pan_crawling, maily_crawling, youtube_crawling, dc_crawling
import pandas as pd

n_db = naver_crawling('mz세대')
pan_db = pan_crawling('mz세대')
maily_db = maily_crawling('mz세대')
youtube_db = youtube_crawling('mz세대')
dc_db = dc_crawling('mz세대')

pd.concat([n_db, pan_db, maily_db, youtube_db, dc_db]).to_csv('DB_thisone.csv', index=False)

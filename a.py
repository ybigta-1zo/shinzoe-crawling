from crawling import *
import pandas as pd

n_db = naver_crawling('mz세대')
pan_db = pan_crawling('mz세대')
maily_db = maily_crawling('mz세대')
youtube_db = youtube_crawling('mz세대')
dc_db = dc_crawling('mz세대')

trend_db = naver_search_trend('mz세대')

pd.concat([n_db, pan_db, maily_db, youtube_db, dc_db]).to_csv('context_DB.csv', index=False)
trend_db.to_csv('trend_DB.csv', index=False)
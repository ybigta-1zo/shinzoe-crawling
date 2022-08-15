from crawling import naver_crawling, pan_crawling, maily_crawling
import pandas as pd

n_db = naver_crawling('mz세대')
pan_db = pan_crawling('mz세대')
maily_db = maily_crawling('mz세대')

pd.concat([n_db, pan_db, maily_db]).to_csv('DB.csv', index=False)
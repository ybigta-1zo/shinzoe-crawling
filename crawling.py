def naver_crawling(keyword):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    n_api_news = f'https://openapi.naver.com/v1/search/news.xml?query={keyword}'
    n_api_web = f'https://openapi.naver.com/v1/search/webkr.xml?query={keyword}'
    n_api_cafe = f'https://openapi.naver.com/v1/search/cafearticle.xml?query={keyword}'
    naver_api = [n_api_news, n_api_web, n_api_cafe]

    headers = { 'X-Naver-Client-Id' : "G5yG2v2TKiOu77qmrEeq",
                'X-Naver-Client-Secret' : "8SzLOPImH7"}

    NapiDb = pd.DataFrame(columns=['출처', 'index', '내용'])

    for url in naver_api:
        # start = 1000까지 설정 가능
        # mz세대라는 용어 앞뒤로 적힌 문장들 위주로 사용할 수 있다.
        start = 1
        for st in range(10):
            q = '&display=100&start=' + str(start + st*100)
            response = requests.get(url + q, headers=headers)
            soup = BeautifulSoup(response.content, 'xml')
            des_lst = soup.find_all('description')

            index_ = 1
            api_lst = list()
            for description in des_lst[1:]:
                api_lst.append([url.split('search/')[1].split('?')[0], (start-1)*100 + index_, description.get_text()])
                index_ += 1
            api_df = pd.DataFrame(api_lst, columns=['출처', 'index', '내용'])
            NapiDb = pd.concat([NapiDb, api_df])
            start += 1
    return NapiDb

def pan_crawling(keyword):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    pan = f'https://pann.nate.com/search/talk?q={keyword}&page='

    pan_db = pan_df = pd.DataFrame(columns=['출처', 'index', '내용'])
    index_ = 1
    for page in range(1, 19):
        response = requests.get(pan + str(page))
        soup = BeautifulSoup(response.content, 'html.parser')

        pan_datas = soup.select('ul.s_list > li > div.txt')
        pan_lst = list()
        for pan_data in pan_datas:
            pan_data = pan_data.get_text().replace('\n', '')
            pan_lst.append(['pan', index_, pan_data])
            index_ += 1
        pan_df = pd.DataFrame(pan_lst, columns=['출처', 'index', '내용'])
        pan_db = pd.concat([pan_db, pan_df])
    return pan_db

def maily_crawling(keyword):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    mail_ = f'https://maily.so/?keyword={keyword}'

    mail_db = mail_df = pd.DataFrame(columns=['출처', 'index', '내용'])

    response = requests.get(mail_)
    soup = BeautifulSoup(response.content, 'html.parser')

    page_lst = list()
    href_lst = soup.find_all('div', class_='block')
    for page_url in href_lst:
        page_lst.append(page_url.find('a', class_='w-full').attrs['href'])

    index_ = 1
    for page in page_lst:
        response = requests.get(page)
        soup = BeautifulSoup(response.content, 'html.parser')

        mail_datas = soup.find_all('p')
        mail_lst = list()
        for p in mail_datas:
            mail_data = p.get_text().replace('\n', '')
            if 'mz세대' in mail_data or 'MZ세대' in mail_data:
                mail_lst.append(['maily', index_, mail_data])
                index_ += 1
        mail_df = pd.DataFrame(mail_lst, columns=['출처', 'index', '내용'])
        mail_db = pd.concat([mail_db, mail_df])

    return mail_db
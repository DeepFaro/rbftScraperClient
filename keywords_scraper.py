from utils.sys import systemSpec
import requests
import sys
import os

systemSpec_obj =  systemSpec()
sys.path.append(os.getcwd())


def make_scrap(keywords:[] = []):
    url =systemSpec_obj.get_keyword_scrape_url()
    json_data = {"keywords": keywords}
    print("server call url :", url)
    x = requests.post(url, json=json_data)
    print(x.text)
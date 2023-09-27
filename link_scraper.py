from utils.sys import systemSpec
import requests
import sys
import os

systemSpec_obj =  systemSpec()
sys.path.append(os.getcwd())


def make_scrap(link:str = "ict.com.mm"):
    url =systemSpec_obj.get_link_scrape_url()
    json_data = {"link": link}
    print("server call url :", url)
    x = requests.post(url, json=json_data)
    print(x.text)
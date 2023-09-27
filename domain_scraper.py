from utils.sys import systemSpec
import requests

systemSpec_obj =  systemSpec()

def make_scrap(domainName:str = "ict.com.mm"):
    url =systemSpec_obj.get_domain_scrape_url()
    json_data = {"domainName": domainName}
    x = requests.post(url, json=json_data)
    print(x.text)
import os



class systemSpec:
    def __init__(self):
        self.localhost_ip = "http://localhost"
        self.sever_port = "3000"
        
        self.link_scrape = "link-scrape"
        self.keyword_scrape = "keyword-scrape"
        self.domain_scrape = "domain-scrape"



    def get_link_scrape_url(self):
        url ="{}:{}/{}".format(self.localhost_ip,self.sever_port,self.link_scrape)
        return url

    def get_keyword_scrape_url(self):
        url ="{}:{}/{}".format(self.localhost_ip,self.sever_port,self.keyword_scrape)
        return url
    
    def get_domain_scrape_url(self):
        url ="{}:{}/{}".format(self.localhost_ip,self.sever_port,self.domain_scrape)
        return url


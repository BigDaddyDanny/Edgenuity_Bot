'''
Created on May 3, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

headers = {'User-Agent': user_agent}


def get_page_content(url):  

    req = urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        
    return str(page)
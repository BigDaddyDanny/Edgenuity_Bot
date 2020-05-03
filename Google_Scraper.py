'''
Created on May 3, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

import urllib.request

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

headers = {'User-Agent': user_agent}

def get_answer(question, possible_answers):
    
    words = question.split()
    
    words = '+'.join(words)
            
    google_url = 'https://www.google.com/search?q=' + words
    
    page_content = get_page_content(google_url)
    print(page_content)
    


def get_page_content(url):  

    req = urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        
    return str(page)

get_answer('yoyo whats up', 'haha')
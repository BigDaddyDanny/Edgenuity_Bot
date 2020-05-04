'''
Created on May 3, 2020

@author: Danny
'''
from Edgenuity_Bot.Brainly import get_brainly_answer
from Edgenuity_Bot.Quizlet import get_quizlet_answer

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
    
    #search for brainly.com and quizlet.com

    brainly_link = page_content[page_content.find('https://brainly.com/') : ]
    brainly_link = brainly_link[ : brainly_link.find('&')]
    
    quizlet_link = page_content[page_content.find('https://quizlet.com/') : ]
    quizlet_link = quizlet_link[ : quizlet_link.find('&')]
    
    brainly_answer = ''
    quizlet_answer = ''
    
    if(brainly_link != ''):
        brainly_answer = get_brainly_answer(get_page_content(brainly_link), possible_answers)
    
    
    if(quizlet_link != ''):
        quizlet_answer = get_quizlet_answer(get_page_content(quizlet_link), possible_answers)    
    
    
    
        
    if brainly_answer != '' and quizlet_answer == brainly_answer:
        return brainly_answer
    
    if brainly_answer == '' and quizlet_answer != '':
        
    

def get_page_content(url):  

    req = urllib.request.Request(url,headers=headers)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        
    return str(page)

get_answer('mcdonalds', 'haha')
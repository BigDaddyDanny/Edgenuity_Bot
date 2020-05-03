'''
Created on Apr 29, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

import urllib.request
from bs4 import BeautifulSoup

minimum_rating = 3.5

#returns set of question and answers
def clean_brainly_page(page_content):
    
    temp = page_content
    
    answers = list()
    
    start_index = temp.find('data-test="answer-content"') + 26
    
    while start_index != 25:
        
        end_index = temp[start_index:].find('</div>')
         
        answers.append(temp[start_index: start_index + end_index])
        
        temp = temp[start_index + end_index:]
        
        start_index = temp.find('data-test="answer-content"') + 26
        
    temp = page_content
    
    ratings = list()
    
    index = temp.find('data-rating-value=') + 19
    
    while index != 18:
           
        ratings.append(temp[index : index + 3])
        
        temp = temp[index + 3: ]
        
        index = temp.find('data-rating-value=') + 19

    
    print(ratings)
    print(answers)
    
    vetted_answers = list()
    
    for i in range(len(ratings)):
        if float(ratings[i]) > minimum_rating:
            vetted_answers.append(answers[i])
            
    print(vetted_answers)
    
    return vetted_answers


def extract_letter_answer(string):
    
    string = string.lower()
    
    print(string)
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
            
    a += check_for_choice(string, 'a') + check_for_choice(string, '1')

    b += check_for_choice(string, 'b') + check_for_choice(string, '2')

    c += check_for_choice(string, 'c') + check_for_choice(string, '3')

    d += check_for_choice(string, 'd') + check_for_choice(string, '4')

    e += check_for_choice(string, 'e') or check_for_choice(string, '5')

    if a > b and a > c and a > d and a > e:
        return 'a'
    elif b > c and b > d and b > e:
        return 'b' 
    elif c > d and c > e:
        return 'c'
    elif d > e:
        return 'd'
    elif e > 0: 
        return 'e'
    
    
    return None

def check_for_choice(string, choice):
    
    total = 0    
    
    if string.find(' ' + choice + ' ') != -1 and choice != 'a':
        total += 1
    if string.find(' ' + choice + '.') != -1:
        total += 1
    if string.find(' ' + choice + ')') != -1:
        total += 1
    if string.find(choice + ' ') == 0:
        total += 1
    if string.find(choice + '.') == 0:
        total += 1
    if string.find(choice + ')') == 0:
        total += 1
    if string.find('>' + choice + ' ') != -1:
        total += 1
    if string.find('>' + choice + '.') != -1:
        total += 1
    if string.find('>' + choice + ')') != -1:
        total += 1
    if string.find('>' + choice + '<') != -1:
        total += 1    
    
    return total

def extract_full_answer(string, possible_answers):
    
    counter = 1
    
    for poss_answer in possible_answers:
        
        if string.find(poss_answer) != -1:
            
            if counter == 1:
                return 'a'
            if counter == 2:
                return 'b'
            if counter == 3:
                return 'c'
            if counter == 4:
                return 'd'
            if counter == 5:
                return 'e'

def get_brainly_answer(page_content, possible_answers):
    
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    
    for x in clean_brainly_page(page_content):
        choice = extract_letter_answer(x)
        if choice != None:
            
            if choice == 'a':
                a += 1
            if choice == 'b':
                b += 1
            if choice == 'c':
                c += 1
            if choice == 'd':
                d += 1
            if choice == 'e':
                e += 1
    
        choice = extract_full_answer(x, possible_answers)
    
    
'''
- add system to get ranking of answers
- add system to get full answers 
'''
        
url = 'https://brainly.com/question/7067287'
answer_choices = ()

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'

headers = {'User-Agent': user_agent}

req = urllib.request.Request(url,headers=headers)
with urllib.request.urlopen(req) as response:
    page = response.read()
    
soup = BeautifulSoup(str(page), 'html.parser')

'''
urls = set()

for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if href == "" or href is None:
        
        continue
    urls.add(href)
'''

clean_brainly_page(str(soup))

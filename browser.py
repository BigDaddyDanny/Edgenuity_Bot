'''
Created on Apr 30, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def quiz_handler():
    
    driver.switch_to.frame('stageFrame')
    
    elm = driver.find_element_by_id('navBtnList')
    
    children = elm.find_elements_by_xpath('*')
    
    num_questions = len(children) - 2
    
    #for i in range(num_questions):
        
    question = driver.find_element_by_class_name('Practice_Question_Body').text
        
    choices = driver.find_elements_by_class_name('answer-choice-label')
    for i in range(len(choices)):
        choices[i] = choices[i].text
        
    #answer = get_answer(question, choices)
    answer = 'b'
        
    inputs = driver.find_elements_by_class_name('answer-choice-button')
    for letter in answer:
        if letter == 'a':
            inputs[0].click()
        if letter == 'b':
            inputs[1].click()
        if letter == 'c':
            inputs[2].click()
        if letter == 'd':
            inputs[3].click()
        if letter == 'e':
            inputs[4].click()

    driver.find_element_by_id('nextQuestion').click()
        
    
    

url = 'https://auth.edgenuity.com/Login/Login/Student'
opts = Options()
opts.add_argument('Mozilla/5.0 (Windows NT 6.1; Win64; x64)')

driver = webdriver.Chrome(executable_path = 'C:\\General\\scripts\\chromedriver.exe')
driver.get(url)

input('type anything to start')

quiz_handler()


'''
title = driver.find_element_by_id('activity-title')

end = False
counter = 1

while end == False:
    try:
        x = 'frame' + str(counter)
        driver.find_element_by_id(x)
        counter += 1
    except:
        end = True
'''
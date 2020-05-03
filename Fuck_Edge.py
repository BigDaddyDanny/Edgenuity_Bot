'''
Created on Apr 30, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'https://www.google.com/search?q=According+to+the+article+what+is+the+primary+cause+of+the+decline+in+poverty+rates+in+China'


opts = Options()
opts.add_argument("user-agent=whatever you want")


driver = webdriver.Chrome(executable_path = 'C:\\General\\scripts\\chromedriver.exe')
driver.get(url)

list = driver.find_elements_by_class_name("st")

for i in range(5):
    print(list[i].text)



driver.close()
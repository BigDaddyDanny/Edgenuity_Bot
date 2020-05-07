'''
Created on Apr 29, 2020

@author: Danny
'''

if __name__ == '__main__':
    pass

minimum_rating = 3.5

#returns set of question and answers
def get_brainly_results(page_content):#needs to be fixed, taking off letter from answer
    
    temp = page_content
    
    answers = list()
    
    start_index = temp.find('data-test="answer-content"') + 29
    
    while start_index != 25:
        
        end_index = temp[start_index:].find('</div>') - 2
         
        answers.append(temp[start_index: start_index + end_index])
        
        temp = temp[start_index + end_index:]
        
        start_index = temp.find('data-test="answer-content"') + 26
        
    temp = page_content
    
    print(answers)
    
    for i in range(len(answers)):
        answer = answers[i]
    
        index = answer.find('\\')
        while index != -1:
            if answer[index + 1] == 'n':
                answer = answer[: index] + answer[index + 2:]
            else:
                answer = answer[: index] + answer[index + 4:]
            index = answer.find('\\')
            print(answer)
            
        index = answer.find('<')
        end_index = answer[index:].find('>') + index
        while index != -1 and end_index != -1:
            answer = answer[: index] + ' ' + answer[end_index + 1:]
            index = answer.find('<')
            end_index = answer[index:].find('>') + index
            
        answer = answer.replace(',', ' ').replace('.', ' ').replace(':', ' ').replace(')', ' ').replace('(', ' ')
            
        answers[i] = answer
    
    print(answers)
    
    ratings = list()
    
    temp = page_content
    
    index = temp.find('data-rating-value=') + 19
    
    while index != 18:
           
        ratings.append(temp[index : index + 3])
        
        temp = temp[index + 3: ]
        
        index = temp.find('data-rating-value=') + 19

    
    vetted_answers = list()
    
    for i in range(len(ratings)):
        if float(ratings[i]) > minimum_rating:
            vetted_answers.append(answers[i])
                
    return vetted_answers


def extract_letter_answer(string):
    
    string = string.lower()
           
    occur = [0, 0, 0, 0, 0, 0]

    occur[0] += check_for_choice(string, 'a') + check_for_choice(string, '1')
    occur[1] += check_for_choice(string, 'b') + check_for_choice(string, '2')
    occur[2] += check_for_choice(string, 'c') + check_for_choice(string, '3')
    occur[3] += check_for_choice(string, 'd') + check_for_choice(string, '4')
    occur[4] += check_for_choice(string, 'e') + check_for_choice(string, '5')
    
    return occur

def check_for_choice(string, choice):
        
    if string.find(' ' + choice + ' ') != -1 and choice != 'a':
        return 1
    
    if(choice == 'a'):
        if string.find('  ' + 'a' + ' ') != -1:
            return 1
        if string.find(' ' + 'a' + '  ') != -1:
            return 1

    
    return 0

def extract_sentence_answer(answer_content, possible_answers):
    
    answer_content = answer_content.lower()
    
    occurences = [0, 0, 0, 0, 0, 0]
        
    for i in range(len(possible_answers)):
        
        poss_answer = possible_answers[i].lower()
        
        occurences[i] = occurences[i] + answer_content.count(poss_answer)
    
    m = max(occurences)
    for num in occurences:
        if num != m and num != 0:
            return [0, 0, 0, 0, 0, 0]
    
    return occurences

def get_brainly_answer(page_content, possible_answers):
    
    occurences = [0, 0, 0, 0, 0, 0]
    
    for x in get_brainly_results(page_content):
        print(x)
        
        results = extract_letter_answer(x)
        print('letters: ', results)
        occurences = [a + b for a, b in zip(occurences, results)] 
    
        results = extract_sentence_answer(x, possible_answers)
        print('sentences: ', results)

        occurences = [a + b for a, b in zip(occurences, results)]
  
    m = max(occurences)
    indexes = [i for i, j in enumerate(occurences) if j == m]
    for i in range(len(indexes)):
        
        if indexes[i] == 0:
            indexes[i] = 'a'
        if indexes[i] == 1:
            indexes[i] = 'b'
        if indexes[i] == 2:
            indexes[i] = 'c'
        if indexes[i] == 3:
            indexes[i] = 'd'
        if indexes[i] == 4:
            indexes[i] = 'e'
        if indexes[i] == 5:
            indexes[i] = 'f'
   
    return indexes
    
'''
- modify to address multiple choice questions
'''

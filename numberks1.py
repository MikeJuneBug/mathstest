import random
import time

a1 = 0
correct_ans = 9999
correct_counter = 0
total_questions = 0
lives = 3

def rand_num():
    pass

def sums(a1, correct_ans, correct_counter, total_questions, lives):
    num_1 = random.randrange(1,100)
    num_2 = random.randrange(1,100)
    operator_list = ['+', '-', '*', '/']
    operator_choice1 = random.choice(operator_list)
    operator_dict = {'+': '+', '-':'-', '*':'x', '/':'÷'}
    correct_ans = round(eval(f'{num_1} {operator_choice1} {num_2}'),2)
    
    while lives > 0:
        if correct_ans <= 100 and correct_ans >= 0 and type(correct_ans) == int:

            while total_questions <= 5:

                a1 = float(input(f'{num_1} {operator_dict[operator_choice1]} {num_2} = '))


                if correct_ans == a1:
                    print("Correct")
                    correct_counter += 1
                    total_questions += 1
                    print(f'{correct_counter} right out of {total_questions}\n')
                    sums(a1, correct_ans, correct_counter, total_questions, lives)
                elif correct_ans != a1:
                    print("Try again")
                    total_questions += 1
                    lives -= 1
                    print(f'{correct_counter} right out of {total_questions}')
                    print(f'1 life lost. Lives left: {lives}\n')
                    #print('*'*{lives}')
                    sums(a1, correct_ans, correct_counter, total_questions, lives)
               
                break
        else:
            sums(a1, correct_ans, correct_counter, total_questions, lives)
        
        break 
    return


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n***********************************************************************\n')
print('                         Mike\'s Maths Quiz\n')
print('     Input the right answer using the number keys. You have 3 lives\n')
print('                    See how many you can get right\n')
print('***********************************************************************\n\n\n\n\n')

sums(a1, correct_ans, correct_counter, total_questions, lives)

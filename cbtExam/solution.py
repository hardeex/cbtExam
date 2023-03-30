from questions import Questions
import login

login

getUserCommand = ""
myAnswer = ""
                

intro = ''''
    A TERMINAL CBT ALIKE TASK
    Student/Coder: Adewale

    ANSWER THE FOLLOWING QUESTIONS

    INSTRUCTION: 
        Use the option A, B, C or D to select your answer. 
        You can also type your answer in text/word
        The case, either small or capital letter do not matter

        help --> to seek info or system assistance
        start --> to start the quiz
        exit --> to end the quiz and close the prompt
        user ---> to change logged-in user

'''
print(intro)



def question5():
     Questions.question5()

     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "Python code is both compiled and interpreted"):
                print("Correct... Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")
                question6()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question5()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()

            else: 
                 print(f"{myAnswer} is WRONG")
                 print("A or Python code is both compiled and interpreted is the correct answer \n Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")
                 question6()
  

       
def question6():
    Questions.question6()

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "D" or myAnswer == "Guido van rossum"):
                print("Correct... \n True, False and None are capitalized while the others are in lower case.")
                question7()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question6()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
            

            else:
                 print(f"{myAnswer} is WRONG")
                 print("D or None of the above is the correct answer\n True, False and None are capitalized while the others are in lower case.")
                 question7()


def question7():
    Questions.question7()
    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "7"):
                print("Correct... \n The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")
                question8()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question7()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("A or 7 is the correct answer\n he order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")
                 question8()


def question8():
    Questions.question8()

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "Indentation"):
                print("Correct...\n In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.")
                question9()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question8()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("A or Indentation is the correct answer\n In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.")
                 question9()


def question9():
    Questions.question9()

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == "def"):
                print("Correct... \n The def keyword is used to create, (or define) a function in python.")
                question10()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question9()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or def is the correct answer \n The def keyword is used to create, (or define) a function in python.")
                 question10()


def question10():
     Questions.question10()
     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == "#"):
                print("Correct... \n To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes.")
                print("\n\n CONGRATULATIONS!!! You have completed the Quiz")
                # print the number of total questions
                # print the number of answered questions
                # print the score
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question10()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or # is the correct answer \n To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes.")
                 print("CONGRATULATIONS!!! You have completed the Quiz")
                # print the number of total questions
                # print the number of answered questions
                # print the score



def question4():
     Questions.question4()
     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == ".py"):
                print("Correct...\n ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.")
                question5()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question4()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or .py is the correct answer--->\n ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.")
                 question5()


def question3():
    Questions.question3()
    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == "Yes"):
                print("Correct...\n Case is always significant while dealing with identifiers in python.")
                question4()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question3()
                isTrue = False
                

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or Yes is the correct answer--->\n Case is always significant while dealing with identifiers in python.")
                 question4()


def question2():
     Questions.question2()   
     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "D" or myAnswer == "All of the above"):
                print("Correct...\n Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                question3()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n\n ")
                Questions.question2()
                isTrue = False
               
            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                welcome()
                
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                 question3()

def solve():
      
      is_true = True

     #tackling question 1
      Questions.question1()
      while is_true:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "C" or myAnswer == "Guido van rossum"):
                print("Correct... He is a Dutch programmer that developed Python in Netherland")
                question2()      
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\n\nYou have not provided an the asnswer to this question")
                Questions.question1()
                isTrue = False
                
            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
            # make this elif a global for th solve fun
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("C or Guido van Rossum is the correct answer--- He is a Dutch programmer that developed Python in Netherland")
                 question2()


def welcome():
     info = ''''
                help ---> to seek system assistance
                start ---> to begin the quiz
                exit ---> to exit the prompt
                user ---> to change user
                '''
     print(info)

     prompt = True
     while prompt:
          getUserCommand = input("> ").capitalize()
          if(getUserCommand == "Help"):
                print(info)
          
          elif (getUserCommand == "Exit" or getUserCommand == "Stop"):
                print("Are you sure you want to close this terminal? yes or no")
                exitQuiz = input("yes or no: > ")
                while (exitQuiz == ""):
                    exitQuiz  = input("yes or no: > ")
                if(exitQuiz == "yes"):
                    print("Prompt Closed....")
                    break
                elif (exitQuiz == "no"):
                    print(info)
                else:
                    print("Invalid Response")
                    exitQuiz  = input("yes or no: > ")
          elif(getUserCommand == "User"):
              make = login()
              make

          elif(getUserCommand == "Start"):
                print("\n QUIZ SESSION COMMENCE..........\n")
                solve()
                # login interface
                # create a set and append new users
                # add register user to the set 
                
          elif(getUserCommand == "" or getUserCommand == " "):
             getUserCommand
          
          else:
                print(f"ERROR>>> {getUserCommand.casefold()} is an invalid command.... \n\t\tYou can use the help command")
                    
welcome()



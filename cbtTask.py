import math
import random, string


getUserCommand = ""
myAnswer = ""
correctAnswer = ""


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

'''
print(intro)

def question5():
     q5 = f"5. Is Python code compiled or interpreted\n"
     option5 = {
            'A': "Python code is both compiled and interpreted",
            'B': "Python code is neither compiled nor interpreted",
            'C': "Python code is only compiled",
            'D': "Python code is only interpreted"
        }
     print("\n\n")
     print(q5, option5)

     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "Python code is both compiled and interpreted"):
                print("Correct... Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")
                question6()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q5, option5)
                isTrue = False
                if(myAnswer == "A" or myAnswer == "Python code is both compiled and interpreted"):
                    print("Correct... Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")
                    question6()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else: 
                 print(f"{myAnswer} is WRONG")
                 print("A or Python code is both compiled and interpreted is the correct answer \n Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.")
                 question6()
  

       
def question6():
    q6 = f"6. All keywords in Python are in _________\n"
    option6 = {
            'A': "Capitalized",
            'B': "Lowercase",
            'C': "Upper",
            'D': "None of the above"
        }
    print("\n\n")
    print(q6, option6)

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "D" or myAnswer == "Guido van rossum"):
                print("Correct... \n True, False and None are capitalized while the others are in lower case.")
                question7()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q6, option6)
                isTrue = False
                if(myAnswer == "D" or myAnswer == "None of the above"):
                    print("Correct... \n True, False and None are capitalized while the others are in lower case.")
                    question7()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
            

            else:
                 print(f"{myAnswer} is WRONG")
                 print("D or None of the above is the correct answer\n True, False and None are capitalized while the others are in lower case.")
                 question7()


def question7():
    q7 = f"7. What will be the value of the following Python expression?\n 4 + 3 % 5"
    option7 = {
            'A': "7",
            'B': "2",
            'C': "4",
            'D': "1"
        }
    
    print("\n\n")
    print(q7, option7)

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "7"):
                print("Correct... \n he order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")
                question8()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q7, option7)
                isTrue = False
                if(myAnswer == "A" or myAnswer == "7"):
                    print("Correct...\n he order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")
                    question8()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("A or 7 is the correct answer\n he order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.")
                 question8()


def question8():
    q8 = f"8. Which of the following is used to define a block of code in Python language?\n"
    option8 = {
            'A': "Indentation",
            'B': "Key",
            'C': "Bracket",
            'D': "All of the above"
        }
    
    print("\n\n")
    print(q8, option8)

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "A" or myAnswer == "Indentation"):
                print("Correct...\n In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.")
                question9()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q8, option8)
                isTrue = False
                if(myAnswer == "A" or myAnswer == "Indentation"):
                    print("Correct...\n In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.")
                    question9()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("A or Indentation is the correct answer\n In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.")
                 question9()


def question9():
    q9 = f"9. Which keyword is used for function in Python language?\n"
    option9 = {
            'A': "Function",
            'B': "def",
            'C': "fun",
            'D': "Define"
        }
    
    print("\n\n")
    print(q9, option9)

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == "def"):
                print("Correct... \n The def keyword is used to create, (or define) a function in python.")
                question10()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q9, option9)
                isTrue = False
                if(myAnswer == "B" or myAnswer == "def"):
                    print("Correct...\n The def keyword is used to create, (or define) a function in python.")
                    question10()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or def is the correct answer \n The def keyword is used to create, (or define) a function in python.")
                 question10()


def question10():
     q10 = f"10.  Which of the following character is used to give single-line comments in Python?\n"
     option10 = {
            'A': "//",
            'B': "#",
            'C': "/* ",
            'D': "!"
        }
     
     print("\n\n")
     print(q10, option10)

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
                print(q10, option10)
                isTrue = False
                if(myAnswer == "B" or myAnswer == "#"):
                    print("Correct... \n To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes.")
                    question2()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or # is the correct answer \n To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes.")
                 print("CONGRATULATIONS!!! You have completed the Quiz")
                # print the number of total questions
                # print the number of answered questions
                # print the score



def question4():
     q4 = f"4. Which of the following is the correct extension of the Python file?\n"
     option4 = {
            'A': ".python",
            'B': ".py",
            'C': ".pl",
            'D': ".p"
        }
     print("\n\n")
     print(q4, option4)
     
     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == ".py"):
                print("Correct...\n ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.")
                question5()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q4, option4)
                isTrue = False
                if(myAnswer == "B" or myAnswer == ".py"):
                    print("Correct...\n ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.")
                    question5()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or .py is the correct answer--->\n ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.")
                 question5()


def question3():
    q3 = f"3. Is Python case sensitive when dealing with identifiers?\n"
    option3 = {
            'A': "machine dependent",
            'B': "yes",
            'C': "no",
            'D': "none of the above"
        }
    print("\n\n")
    print(q3, option3)

    while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "B" or myAnswer == "Yes"):
                print("Correct...\n Case is always significant while dealing with identifiers in python.")
                question4()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q3, option3)
                isTrue = False
                if(myAnswer == "B" or myAnswer == "Yes"):
                    print("Correct...\n Case is always significant while dealing with identifiers in python.")
                    question4()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("B or Yes is the correct answer--->\n Case is always significant while dealing with identifiers in python.")
                 question4()


def question2():
      q2 = f"2. Which type of Programming does Python support?\n"
      option2 = {
            'A': "object-oriented programming",
            'B': "structured programming",
            'C': "functional programming",
            'D': "All of the above"
        }
      print("\n\n")
      print(q2, option2)

      while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "D" or myAnswer == "All of the above"):
                print("Correct...\n Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                question3()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q2, option2)
                isTrue = False
                if(myAnswer == "D" or myAnswer == "All of the above"):
                    print("Correct...\n Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                    question3()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                 question3()

def question1():
        q1 = f"1. Who developed Python Programming Language?\n"
        option1 = {
            'A': "Wick van Rossum",
            'B': "Rasmus Lerdorf",
            'C': "Guido van Rossum",
            'D': "Niene Stom"
        }
        print(q1, option1)
        while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "C" or myAnswer == "Guido van rossum"):
                print("Correct... He is a Dutch programmer that developed Python in Netherland")
                question2()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                print(q1, option1)
                isTrue = False
                if(myAnswer == "C" or myAnswer == "Guido van rossum"):
                    print("Correct... He is a Dutch programmer that developed Python in Netherland")
                    question2()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("C or Guido van Rossum is the correct answer--- He is a Dutch programmer that developed Python in Netherland")
                 question2()
            
def welcome():
     info = ''''
                help ---> to seek system assistance
                start ---> to begin the quiz
                exit ---> to exit the prompt
                '''
     print(info)

     prompt = True
     while prompt:
          getUserCommand = input("> ").capitalize()
          if(getUserCommand == "Help"):
                print(info)
          
          elif (getUserCommand == "Exit" or getUserCommand == "Stop"):
                print("Prompt Closed...")
                prompt = False
                  
          elif(getUserCommand == "Start"):
                print("\n QUIZ SESSION COMMENCE..........\n\n")
                question1()
                    
welcome()


          

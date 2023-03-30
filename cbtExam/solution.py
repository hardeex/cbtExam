from questions import Questions

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

'''
print(intro)


def question2():
     Questions.question2()   
     while True:
            myAnswer = str(input("Enter your Answer->: ")).capitalize()
            if(myAnswer == "D" or myAnswer == "All of the above"):
                print("Correct...\n Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                Questions.question3()
        
            elif (myAnswer == ""):
              isTrue = True      
              while isTrue:
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question2()
                isTrue = False
                if(myAnswer == "D" or myAnswer == "All of the above"):
                    print("Correct...\n Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                    Questions.question3()

            
            elif (myAnswer == "Quit" or myAnswer == "Exit" or myAnswer == "Stop"):
                print("\n Quiz Prompt is Closed....\n\n")
                break
                

            else:
                 print(f"{myAnswer} is WRONG")
                 print("Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.")
                 Questions.question3()

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
                print("\nYou have not provided an the asnswer to this question\n ")
                Questions.question1()
                isTrue = False
                if(myAnswer == "C" or myAnswer == "Guido van rossum"):
                    print("Correct... He is a Dutch programmer that developed Python in Netherland")
                    question2()
            
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
                solve()
                # login interface
                # create a set and append new users
                # add register user to the set 
                
          elif(getUserCommand == "" or getUserCommand == " "):
             getUserCommand
          
          else:
                print(f"ERROR>>> {getUserCommand.casefold()} is an invalid command.... \n\t\tYou can use the help command")
                    
welcome()



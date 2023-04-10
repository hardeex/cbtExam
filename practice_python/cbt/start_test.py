import os
import sqlite3


def db_user():
    print("CBT PYTHON TEST LOGIN/REGISTER INTERFACE\n")

    prompt = True
    while prompt:
        logorreg = input("Login or Register:> ").lower()
        # remeber to trim all spaces

        if logorreg == "register" or logorreg == "r":
           register_user()
            

        elif logorreg == "l" or logorreg == "login":
                loggedIn_user()

        elif logorreg == "exit" or logorreg == "stop":
            print("<<<<< Login/Register Prompt Closed >>>>>")
            prompt = False
            
        else:
            print(f"({logorreg}) is an invalid command for this interface \n")
            print(''' 
            Type l or login in your terminal to login
            Type r or register in your terminal to register
            NB: The case of the text do not matter
            exit --> to close the login/register prompt
            ''')


def register_user():
    if os.path.exists("cbtuser.db"):
        conn = sqlite3.connect("cbtuser.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("cbtuser.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE cbtuser (username text, password text)''')
    print(''' 
            Type l or login in your terminal to login
            Type r or register in your terminal to register
            NB: The case of the text do not matter
            exit --> to close the login/register prompt
            ''')


    print("\n Enter your username and password to create an account\n")
    username = input("Username: ").lower()
    password = input("Password: ")

    c.execute("INSERT INTO cbtuser VALUES (?, ?)", [username, password])
    conn.commit()
    #conn.close()
    print("\t\t Account created successfully")
    loggedIn_user()
            

               
def loggedIn_user():
           
    if os.path.exists("cbtuser.db"):
        conn = sqlite3.connect("cbtuser.db")
        c = conn.cursor()
    else:
        conn = sqlite3.connect("cbtuser.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE cbtuser (username text, password text)''')
    print(''' 
            Type l or login in your terminal to login
            Type r or register in your terminal to register
            NB: The case of the text do not matter
            exit --> to close the login/register prompt
            ''')
    print("\n Login with your username and password\n")
    username = input("Username: ")
    password = input("Password: ")

    c. execute("SELECT * FROM cbtuser WHERE username=? and password=?", [username, password])
    if c.fetchone() == None:
        print("username or password is wrong")
        print("\n Kindly register to have access to the quiz session\n")
        register_user()
           
    else:
        print("logged In")
        #navigate to the questions


def getUserCommand():
        
        prompt = True
        while prompt:
            command = input("> ").lower()
            
            if command == 'test' or command == "t":
                print("\n Login/Register interface\n")
                db_user()

            elif command == 'help':
                intro()
                break
            
            elif command == "r" or command == "register": 
                register_user()

            elif command == "l" or command == "login":
                loggedIn_user()

            elif command == 'exit':
                print(">>>>> PROMPT CLOSED >>>>>>> \n")
                prompt = False
                
            else:
                print(f">>>>>>> ({command}) is an invalid command for this program")

    
def intro():
    print('''
        WELCOME TO OUR CBT PLATFORM

            NB: The case of your command do not matter. That is, 
            it doesn't matter if you type in capital, 
            small or combination of both

        help --> For system assistance
        exit --> to quit the test
        test --> Navigate to the test interface
        l or login --> to login into the system database
        r or register --> to register your data in the database
    ''')
    getUserCommand()
    
intro()


    
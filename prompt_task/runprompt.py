import datetime

prompt = ""
is_true = True
staandcap = {
                    "Abia": "Umuahia",
                    "Adamawa": "Yola",
                    "Akwa-Ibom": "Uyo",
                    "Anambra": "Awka",
                    "Bauchi": "Bauchi",
                    "Bayelsa": "Yenagoa",
                    "Benue": "Makurdi",
                    "Borno": "Maikudiri",
                    "Cross River": "Calabar",
                    "Delta": "Asaba",
                    "Ebonyi":"Abakaliki",
                    "Edo": "Benin CIty",
                    "Ekiti": "Ado-Ekiti",
                    "Enugu": "Enugu",
                    "Gombe": "Gombe",
                    "Imo": "Owerri",
                    "Jigawa": "Dutse",
                    "Kaduna": "Kaduna",
                    "Kano": "Kano",
                    "Kastina": "Kastina",
                    "Kogi": "Lokoja",
                    "Kwara": "Ilorin",
                    "Lagos": "Ikeja",
                    "Nasarawa": "Lafia",
                    "Niger": "Minna",
                    "Ogun": "Abeokuta",
                    "Ondo": "Akure",
                    "Osun":"Oshogbo",
                    "oyo": "Ibadan",
                    "Plateau": "Jos",
                    "Rivers": "Port Harcourt",
                    "Sokoto": "Sokoto",
                    "Taraba": "Jalingo",
                    "Yobe":"Damaturu",
                    "Zamfara": "Gusau",
                    "Federal Capital Territory (FCT)": "Abuja \n"
                    }



class MyPrompt():
    def __init__(self):
        print(f'''
            Welcome to Applishell Version 1.0 developed by Adewale, 
            running at {datetime.datetime.now()}.
        ''')

        while is_true:
            prompt = input("applishell> ").lower()
            if prompt == "exit" or prompt == 'stop' or prompt == "quit":
                print("\n <<<< PROMPT CLOSED >>>>> \n")
                break

            elif prompt == "nigeria" or prompt == "ls"  or prompt == "nig":
                print(f" Count: {len(staandcap)}")
                print("\n STATE \t\t\t CAPITAL\n")
                for state, capital in staandcap.items():               
                    print(f"{state} \t\t\t {capital}") 
                    
            
            elif prompt == "nigeria state" or prompt == "nigeria_state":
                for states in staandcap:
                    print(states)

            elif prompt == "nigeria_capital" or prompt == "nigeria capital":
                for capitals in staandcap:
                    print(staandcap[capitals])

            elif prompt == "nigeria first two":
                first_two = list(staandcap.items())[:2]
                print("STATE \t\t CAPITAL\n")
                for state, capital in first_two:
                    print(f"{state} \t\t\t {capital}") 
            else:
                print("<<<< Invalid command for this program >>>>>")
                print("DO you want to see the command list for this program")
                showCommand = input("yes or no:> ").lower()
                if showCommand == "yes" or showCommand == "y":
                    print('''
                    nigeria or nig or ls --> To see the 36 states and capital in nigeria
                    nigeria first two ---> To see the first two state and capital 
                    nigeria state --> To view the states only
                    nigeria capital --> To view the capital in the state only
                    ''')
                else:
                    prompt
MyPrompt()




    

import solution

print("Name: ")
getUser = input("> ").title()
users = {'Adewale'}
newUser = {}


def register():
    print("Enter your name to be registered on this terminal...")
    getUser = input("Your Name:  ").capitalize()
    users.add(getUser)
    print("Your registration is sucessful................................")
    print("\n\nThe list of REGISTERED USERS on this TERMINAL...\n")
    print(users)
    



if(getUser in users):
    print(f"Welcome Back {getUser}")
    #start the quiz
else:
    print("\n\nSearching.................................\n")
    print(f"{getUser} not found in our database\n\t\t Enter your name to start the quiz")
    for user in users:
        print(f"\n\n Current Users in this TERMINAL.... \n\n {user}\n\n")
    #register the user
    register()

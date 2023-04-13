import cmd
import datetime



class MyPrompt(cmd.Cmd):
    prompt = 'applishell> '
    
    def do_hello(self, arg):
        print('Hello,', arg)
    
    def do_quit(self, arg):
        return True

    def create_commands(self, arg):

        create_prompt = input("ade>")
        if create_prompt == "nigeria":
            print("This is Nigeria", arg)

if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.cmdloop(f"\n Welcome to Applishell Version 1.0, developed by Jamiu Adewale Yusuf, running at {datetime.datetime.now()} \n")

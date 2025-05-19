import random
#Number guessing game
def game():
    print("\nLet's play a number guessing game")
    print("Rule: You have to correctly guess the number from (1-9)")
    print("You only have 5 chances")
    print("Warning:You can't skip the game without completing the 5 chances")
    print("Go ahead! and try your luck but don't worry you will get the hints for a wrong answer")
    comp=random.randint(1,9)
    t=5
    while(t>0):
        try:
            s=int(input("Enter your guessed number from(1-9):"))
        except ValueError:
            print("Invalid! Please Enter a number:")
            continue
        if(s==comp):
            print("Congrats! You won this round")
            return 1
        elif(s>comp):
            print("Oops! You didn't won, but your given answer is greater than the actual answer")
            t=t-1
            if(t>0):
                print("No worries! Still you have {} chances left".format(t))
        elif(s<comp):
            print("Oops! You didn't won, but your given answer is smaller than the actual answer")
            t=t-1
            if(t>0):
                print("No worries! Still you have {} chances left".format(t))
        if(t==0):
            print("Unfortunately, You lost the round")
            print("The actual answer was {}".format(comp))
            return 0
            
p=0        
while True:
    p=p+game()
    n=input("Do you want to play another round?(yes/no):").lower()
    if(n!="yes"):
        print("Thanks for playing!")
        print("Your total score for the rounds you played is {}".format(p))
        break
    
        
            
            
    

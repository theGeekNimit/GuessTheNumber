import random
import sys 

def guess1():
    k=int(input("Enter the number you want between 0 to - 99 "))
    n = random.randint(0,k)
    valid_att=int(k/3)
 
    i=int(input(f"Enter the number of attempts you want \n(Attempts cannot exceed one-third of total number i.e. {valid_att}) - ")) #number of guess
    while(True) :   
        if i>valid_att:
            print("Enter valid number of attempts!")
            break
        x=int(input(f"Enter your number between 0 to {k}. \n")) #user's input
        if n==x:
            print("You won!The number you entered is correct.")
            break
        if x>k:
            print("Enter valid number.")
        elif x>n:
            print("HINT : Enter a smaller number.")
            i-=1
            print("Number of guesses left - ",i)
            if i<1:
                print("You lose!game over.")
                print("The number is ",n)
                break
            else:
                continue
        elif x<n:
            print("HINT : Enter a greater number.") 
            i-=1
            print("Number of guesses left - ",i)  
            if i<1:
                print("You lose!game over.")
                print("The number is ",n)
                break
        else:
            continue  
    
while(True):
    again=int(input('To play press 0 \nTo exit press 9\n'))
    if again==0:
        guess1()
        # attempt()
    elif again==9:
        sys.exit()
   
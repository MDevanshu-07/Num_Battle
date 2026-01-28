import numpy as np; # For Data 
import random # For Difficulty
import matplotlib.pyplot as plt # For Performance 

# Data set
values=np.arange(1,1001)
operations=["+","-","*","/"]


# Generate Equations 
def Questions(mode): 
    op=random.choice(operations)
    if(mode=="easy"): # Easy 
         num1=random.choice(values.flatten()[:100])
         num2=random.choice(values.flatten()[:50])
    elif(mode=="medium"): # Medium
          num1=random.choice(values.flatten()[100:500])
          num2=random.choice(values.flatten()[:250])
    else: # Hard
         num1=random.choice(values.flatten()[500:])
         num2=random.choice(values.flatten()[250:])
    print(num1,op,num2,"= ?")
    return num1,op,num2 

# Correction
def Checking(ans,num1,op,num2):
   # Matching Cases to find and check the correct answer
   match op:
        case "+":
               return num1+num2==ans
        case "-":
               return num1-num2==ans
        case "*":
               return num1*num2==ans
        case "/":
               return int(num1/num2)==ans
        case _:
             print("")

# Marks Allotment
def Modes(play,len):
    i=0
    total=[]
    marks=0

    while(i<len):
        print(f"Question {i+1}:")
        num1,op,num2=Questions(play)

        ans=int(input("Enter Your Answer: "))
        check=Checking(ans,num1,op,num2)

        if(i<len and check):
            print("Right +5")
            marks+=5
        else:
            print("Wrong -2")
            marks-=2
        total.append(marks)
        print()
        i+=1

    return total,marks

# Performance
def Stats(total):
     x=np.arange(len(total))
     y=np.array(total)
     plt.title("Your Performance")
     plt.xlabel("Number of Question")
     plt.ylabel("Performace Per Question")
     plt.plot(x,y)
     plt.show()


# Input
mode=(input("Enter mode(Easy  Medium  Hard): ").strip()).lower()
num=int(input("Enter number of Questions: "))
print("Marking Pattern:\nRight: +5\nWrong: -2")
print()
total,marks=Modes(mode,num)
print(f"Game Over!\nMarks Obtained: {marks}/{num*5}")
print("Loading Your Performace Graph....")
Stats(total)
import random
def select():
    print("""Select a difficulty:
    Easy = 1
    Medium = 2
    Hard = 3""")
    a = input('> ')
    print("""Select Test type:
    Short = 1
    Medium = 2
    Long = 3""")
    b = input('> ')
    #Checking input validity and reprompting the input until a valid input is entered
    while ((a == "")|(a.isdigit() == False)|(a!='1')&(a!='2')&(a!='3')):
        print('Please enter a valid input!')
        a = input('> ')
    while ((b == "")|(b.isdigit() == False)|(b!='1')&(b!='2')&(b!='3')):
        print('Please enter a valid input!')
        b = input('> ')
    #Converting the entered string to an int
    a = int(a)
    b = int(b)
    #Assigning lives and maxNumbers according to the difficulty
    if (a == 1):
            lives = 3
            maxNum = 10

    elif (a == 2):
            lives = 2
            maxNum = 25

    elif (a == 3):
            lives = 1
            maxNum = 50
    #Assigning list length
    if (b == 1):
        testLen = 5

    elif (b == 2):
        testLen = 10

    elif (b == 3):
        testLen = 20
    #return parameters, for the future use
    return(maxNum, lives, testLen)

def generateQuestion(maxNum, lives, testLen):
    correctCount=0
    #generate questions using a for loop
    for num in range(1,testLen+1):
        print('')
        if (lives>=2):#differentiate lives and life
            print('Question',num,'of',testLen,',',lives,'lives remaining.')
        elif (lives==1):
            print('Question',num,'of',testLen,',',lives,'life remaining.')
        #selecting random numbers between 1 and maxNum
        c = random.randint(1,maxNum)
        d = random.randint(1,maxNum)
        ops = ['+','-']
        operator = random.choice(ops)#randomly choosing operators
        #print the generated question
        print('What is',c,operator,d,'?')
        x=input('> ')
        while ((x == "")|(x.isalpha() == True)&(x.isalnum() == True)):
            print('Please enter a valid input!')
            x = input('> ')
        x=int(x)
        maths = eval(str(c)+operator+str(d))#calculating the answer

        if (maths == x):
            print('Correct!')
            correctCount=correctCount+1#storing the number of correct answers
        else:
            print('Incorrect! The correct answer is',maths)
            lives = lives-1#remaining lives after an incorrect answer
            if (lives == 0):
                print(""" 
                Out of lives, Game Over!""")
                break
    #return parameters to calculateResults
    return (correctCount, testLen)

def calculateResults(correctCount, testLen):
    print("""
Results:
You scored""",correctCount,'/',testLen)
    if((correctCount/testLen)*100 >= 50):
        print(int((correctCount/testLen)*100),'% - You Pass!')
    else:
        print(int((correctCount/testLen)*100),'% - You Fail!')

def main():
    print('Welcome to Maths Tester Pro.')
    calculateResults(*generateQuestion(*select()))
    print("""
Retake the test? yes = 1, no = 0""")
    z=input('> ')
    while z=="1":
        main()
    else:
        print('')
        print('Thank you!')
        import sys
        sys.exit()
    
main()

import json

def inputInt():
    while True:
        prompt = input('> ')
        try:
            numResponse = int(prompt)
        except ValueError:
            print('Invalid input, try again.')
            continue
        break
    return numResponse

def inputSomething():
    while True:
        prompt = input('> ')
        something = prompt.strip()
        if len(something) == 0:
            print("You can't leave it empty. Enter a valid input.")
            continue
        break
    return something

def saveChanges():
    f = open('questions.txt','w')
    json.dump(questions, f)
    f.close()

def main():
    print('\nChoose: [l]ist, [s]earch, [v]iew, [a]dd, [d]elete or [q]uit')
    choice = inputSomething()
    if choice == 'l':
        if len(questions) != 0:
            for index,item in enumerate(questions):
                print(index+1,')', questions[index]['question'])
                continue
        else:
            print('There are No Saved Questions')
        main()

    elif choice == 's':
        search = input ('Enter a term to search: ')
        newSearch = search.lower()
        for index,item in enumerate(questions):
            lowerQ=questions[index]['question'].lower()
            if newSearch in lowerQ:
                print(index+1,')',questions[index]['question'])
        main()
    
    elif choice == 'v':
        if len(questions) != 0:
            print('Enter Index of the question to view:')
            value = inputInt()
            value=value-1
            for index in range(len(questions)+1):
                if index == value:
                    print(index+1,")", questions[index]['question'])
                    print("  (a)",questions[index]['answer'],"(correct)\n  (b)",questions[index]['wrong1'],"(incorrect)\n  (c)",questions[index]['wrong2'],"(incorrect)\n  (d)",questions[index]['wrong3'],'(incorrect)\n')
                    break
                index+=1
                continue
            else:
                print('Invalid Index Number') 
        else:
            print('No Questions Saved')
        main()

    elif choice == 'a':
        for index,item in enumerate('questions'):
            if index == len(questions):
                questions.append({})
                saveChanges()
                print('Enter Question:')
                questions[index]['question'] = inputSomething()
                print('Enter Correct Answer:')
                questions[index]['answer'] = inputSomething()
                print ('Enter Wrong Answers:\n Wrong Answer 1:')
                questions[index]['wrong1'] = inputSomething()
                print('Wrong Answer 2:')
                questions[index]['wrong2'] = inputSomething()
                print('Wrong Answer 3:')
                questions[index]['wrong3'] = inputSomething()
                saveChanges()
                print('Question Added')
                break
            index+=1
            saveChanges()
        main()

    elif choice == 'd':
        if len(questions) != 0:
            print('Enter Index of the question to delete:')
            value = inputInt()
            value=value-1
            for index,item in enumerate(questions):
                if index == value:
                    questions.pop(value)
                    saveChanges()
                    print('Question Deleted')
                    break
                index+=1
                continue
            else:
                print('Invalid Index Number')   
            saveChanges()
        else:
            print('No Questions Saved')
        main()

    elif choice == 'q':
        print('\nGoodbye!')
        import sys
        sys.exit()

    else:
        print('Invalid Input')
        main()

print('Welcome to the Quizbox Admin Program.')
f = open('questions.txt','r')
questions = json.load(f)
f.close()
main()

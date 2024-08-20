def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 0
    
    for key in questions:
        print("------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("What is your answer?: ").upper()
        guesses.append(guess)    
        
        correct_guesses += check_answers(questions.get(key), guess)
        check_answers(questions.get(key), guess)          
        question_num += 1
        
    check_score(correct_guesses, guesses)
    play_again()        
        
#-------------------------------------------------
def check_answers(answers, guess):
    if answers == guess:
        print("You got it right!")
        return 1
    else:
        print("You got it wrong!")
        return 0
#-------------------------------------------------
def check_score(correct_guesses, guesses):
    print("------------------")
    print("Results")
    print("------------------")
    
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
        
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()    
    
    score = int((correct_guesses/len(questions))*100)
    if score == 100:
        print("Congratulations! You got a perfect score! You got", score, "%.")
    else:
            print("You got", score, "%.")
#-------------------------------------------------
def play_again():
    response = input("Do you want to play again? (YES or NO): ")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False
#-------------------------------------------------

questions = { "What year this project was created?: ": "B",
              "What is my GitHUB nickname?: ":"A",
              "What am I using to code this?: ":"A",
              "Is the sky blue?: ":"C",
              "Are you having fun?: ":"B"
}

options =[["A.  2038", "B.  2024", "C.   1993"],
          ["A.  alexmedinasf", "B.  medinasfalex", "C.   none"],
          ["A.   Python", "B.   C++", "C.  JavaScript"],
          ["A.  No", "B.  Idk, Idc", "C.   Ofc dude lol"],
          ["A.  No", "B.  BEST GAME EVER", "C.  Who are you??"]]

new_game()

while play_again():
    True
    new_game()
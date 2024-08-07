#!/usr/bin/env python3

# imports
import html

# data

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    # print the question
    print("\n")
    print(trivia["question"])
    print("\n")
    
    # format answer choices
    answers = {
            "A":html.unescape(trivia["correct_answer"]),
            "B":html.unescape(trivia["incorrect_answers"][0]),
            "C":html.unescape(trivia["incorrect_answers"][1]),
            "D":html.unescape(trivia["incorrect_answers"][2])
            }

    # print the answer choices
    for key in answers:
        print(f"{key}: {answers[key]}")

    # collect user choice
    while True:
        try:
            user_choice = input("\nSubmit your answer [A-D]: ")
            if user_choice.lower().strip() in ['a', 'b', 'c', 'd']:
                if user_choice.lower().strip() == 'a':
                    print("\nCORRECT!")
                    break
                else:
                    print("\nSorry, that's not right")
            else:
                print("\nPlease enter an answer choice using the letters A, B, C, or D: ")
        except ValueError:
            print("\nInput Error. Try again using letters A, B, C, or D.")



if __name__ == "__main__":
    main()


def question_one():
    """The user enters 1 or 0 in response to a true or false statement. Compare the response to the correct answer
     and return a 1 if they got it right and a 0 if not."""

    response = input("1. Alaska was the last state to enter the Union, true or false? Please enter 1 for True or 0 for False.")
    correct_answer = "0"

    if response == correct_answer:
        print("Correct")
        return 1
    elif response != correct_answer:
        print("That was incorrect, the correct answer was " + correct_answer)
        return 0

def question_two():
    """The user enters in a character "a" through "e" for their answer."""

    response = input("2. What is the rough estimate of the population of New York City? Please enter a character a-e.\n a. 1 million \n b. 3 million \n c. 5 million \n d. 8 million \n e. 10 million")
    correct_answer = "d"

    if response == correct_answer:
        print("Correct")
        return 1

    elif response != correct_answer:
        print("That was incorrect, the correct answer was " + correct_answer)
        return 0  
            

#Code to run the quiz
total_score = 0
result = question_one() + question_two()
total_score += result
print(total_score)        


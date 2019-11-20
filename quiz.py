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

def question_three():
    """The user enters in a numeric response to an open ended question.
    I recommend prompting the user to enter an integer. If you choose to use floats,
    be specific to the user about how they should enter their response
    (i.e. rounded and/or a certain number of decimal places)."""

    response = input("3. How many states are there in the United States? Please enter an integer.")
    correct_answer = "50"

    if response == correct_answer:
        print("Correct")
        return 1
    elif response != correct_answer:
        print("That was incorrect, the correct answer was " + correct_answer)
        return 0

def question_four():
    """The user enters 1 or 0 in response to a true or false statement. Compare the response to the correct answer
     and return a 1 if they got it right and a 0 if not."""

    response = input("4. Washington, DC is the capital of the United States of America, true or false? Please enter 1 for True or 0 for False. ")
    correct_answer = "1"

    if response == correct_answer:
        print("Correct")
        return 1
    elif response != correct_answer:
        print("That was incorrect, the correct answer was " + correct_answer)
        return 0    

def question_five():
    """The user enters in a numeric response to an open ended question.
    I recommend prompting the user to enter an integer. If you choose to use floats,
    be specific to the user about how they should enter their response
    (i.e. rounded and/or a certain number of decimal places)."""

    response = input("5. Trump is the __ th President of the United States. Please enter an integer.")
    correct_answer = "45"

    if response == correct_answer:
        print("Correct")
        return 1
    elif response != correct_answer: 
        print("That was incorrect, the correct answer was " + correct_answer)
        return 0







            

#Code to run the quiz
total_score = 0
result = question_one() + question_two() + question_three() + question_four() + question_five()
total_score += result
print("Below is how many questions you got correct out of 5")
print(total_score)        

#Final Message Options
if total_score <= 1:
    print(f"You scored {total_score} out of 5. Now that's not very patriotic of you")

elif total_score <= 4:
    print(f"You scored {total_score} out of 5. You must spend a lot of your time on Facebook")

elif total_score == 5:
    print(f"You scored {total_score} out of 5. You should run for President")
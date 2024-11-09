import random
# import math

def randNumGenerator(minBound, maxBound):
    """
    Random integer. If a float is provided, take only the integer part and ignore decimal
    """
    return random.randint(int(minBound), int(maxBound))


def randOperator():
    """
    return a random arithmetic operator
    """
    return random.choice(['+', '-', '*'])


def arithmeticOp(num1, num2, operator):
    """
    compute and return the answer to the given problem
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '-': answer = num1 - num2    ## Subtract
    elif operator == '+': answer = num1 + num2  ## Add
    else: answer = num1 * num2                  ## Multiply
    return problem, answer

def math_quiz():
    """
    Start a math quiz
    """
    score = 0
    total_questions = int(3.14159)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions): 
        ## Initialize with random numbers and operator
        num1 = randNumGenerator(1, 10); num2 = randNumGenerator(1, 5.5); oper = randOperator()

        PROBLEM, ANSWER = arithmeticOp(num1, num2, oper) ## Calculate the correct Answer and print the problem
        print(f"\nQuestion: {PROBLEM}")

        ## If the user enters a character that is not a number, then keep asking for the answer until a number is provided

        useranswer = ""
        flag = True
        while flag:
            useranswer = input("Your answer: ")
            flag = False
            try:
                useranswer = int(useranswer)
            except:
                print("Please Enter a Number")
                flag = True


        if useranswer == ANSWER: ## Correct Answer case, increment score
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__": ## Run the code only if the script is run directly
    math_quiz()

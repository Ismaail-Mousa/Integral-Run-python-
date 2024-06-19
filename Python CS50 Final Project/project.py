import time
import random

def generate_problem1():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '/':
        num1 = num1 * num2
    
    problem = f"{num1} {operator} {num2}"
    return problem, eval(problem)
    
def generate_problem2():
    integrals = {
        "∫k dx": "kx", "∫x dx": "(1/2)x^2", "∫x^n dx (n ≠ -1)": "1/(n+1)x^(n+1)", 
        "∫1/x dx": "ln(x)", "∫e^x dx": "e^x", "∫sin(x) dx": "-cos(x)", "∫cos(x) dx": "sin(x)",
        "∫sec^2(x) dx": "tan(x)", "∫csc(x) dx": "-cot(x)", "∫sec(x)tan(x) dx": "sec(x)",
        "∫csc(x)cot(x) dx": "-csc(x)", "∫tan(x) dx": "-ln(cos(x))", "∫cot(x) dx": "ln(sin(x))",
        "∫a^x dx": "(a^x)/ln(a)", "∫ln(x) dx": "xln(x)-x", "∫e^(ax) dx": "(1/a)e^(ax)", 
        "∫1/sqrt(1-x^2) dx": "sin^(-1)(x)", "∫1/sqrt(1+x^2) dx": "tan^(-1)(x)", 
        "∫sin^2(x) dx": "x/2 - (sin(2x)/4)", "∫sin(x)cos(x) dx": "(1/2)sin^2(x)", 
        "∫cos^2(x) dx": "(1/2)x+(1/4)sin(2x)", "∫sin^(-1)(x) dx": "xsin^(-1)(x)+sqrt(1-x^2)", 
        "∫1/(ax+b) dx": "(1/a)ln(ax+b)"
    }
    problem = random.choice(list(integrals.keys()))
    return problem, integrals[problem] 

def generate_difficulty():
    while True:
        dif = input("Type 1 if you want easy problems or type 2 if you want integrals: ")
        if dif in ('1', '2'):
            return int(dif)

def get_length():
    while True:
        try:
            l = int(input("How many problems do you want to solve? "))
            if l > 0:
                return l
        except ValueError:
            print("Please enter a valid number.")

def main():
    difficulty = generate_difficulty()
    num_problems = get_length()
    
    start_time = time.time()
    
    for _ in range(num_problems):
        if difficulty == 1:
            problem, solution = generate_problem1()
        else:
            problem, solution = generate_problem2()
        
        print("Solve this problem:")
        print(problem)
        
        user_answer = input("Your answer: ")
        
        if difficulty == 1:
            try:
                user_answer = float(user_answer)
                if user_answer == solution:
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer was {solution}.")
            except ValueError:
                print("Invalid input.")
        else:
            if user_answer.strip() == solution:
                print("Correct!")
            else:
                print(f"Incorrect. The correct answer was {solution}.")
    
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"You took {time_taken:.2f} seconds to solve {num_problems} problems.")

if __name__ == "__main__":
    main()

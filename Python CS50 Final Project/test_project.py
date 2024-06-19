import project

def test_generate_problem1():
    problem, solution = project.generate_problem1()
    assert isinstance(problem, str)
    assert problem.split()[1] in ['+', '-', '*', '/']
    assert eval(problem) == solution

def test_generate_problem2():
    problem, solution = project.generate_problem2()
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
    assert problem in integrals
    assert solution == integrals[problem]

def test_generate_difficulty():
    difficulty = project.generate_difficulty()
    assert difficulty in [1, 2], "Difficulty should be 1 or 2"

def test_get_length():
    length = project.get_length()
    assert isinstance(length, int), "Length should be an integer"
    assert length > 0, "Length should be a positive integer"

if __name__ == "__main__":
    test_generate_problem1()
    test_generate_problem2()
    test_generate_difficulty()
    test_get_length()

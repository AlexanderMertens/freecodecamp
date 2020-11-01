MAX_DIGITS = 4


def parse_problem(problem_string):
    if '+' in problem_string:
        split_string = "+"
    elif '-' in problem_string:
        split_string = "-"
    else:
        raise ValueError("Error: Operator must be '+' or '-'.")

    try:
        operand1, operand2 = map(int, problem_string.split(split_string, 1))
    except ValueError:
        raise ValueError("Error: Numbers must only contain digits.")

    if max(operand1, operand2) >= 10 ** MAX_DIGITS:
        raise ValueError("Error: Numbers cannot be more than four digits.")
    return operand1, operand2, split_string

MAX_DIGITS = 4
SPACING = "    "


def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."

    parsed_problems = []
    for problem in problems:
        try:
            parsed_problems.append(parse_problem(problem))
        except ValueError as e:
            return str(e)

    arranged_problems = ""
    # add the three lines in arranged_problems
    for i in range(0, 3):
        for problem in parsed_problems:
            arranged_problems += ''.join((problem[i], SPACING))
        if i == 2:
            break  # The last line doesn't need a newline character
        arranged_problems = ''.join((arranged_problems.rstrip(), '\n'))
    return arranged_problems


def parse_problem(problem_string):
    if '+' in problem_string:
        split_string = "+"
    elif '-' in problem_string:
        split_string = "-"
    else:
        raise ValueError("Error: Operator must be '+' or '-'.")

    try:
        operand1, operand2 = map(str, map(int, problem_string.split(split_string, 1)))
    except ValueError:
        raise ValueError("Error: Numbers must only contain digits.")

    if max(len(operand1), len(operand2)) > MAX_DIGITS:
        raise ValueError("Error: Numbers cannot be more than four digits.")
    length = 2 + max(len(operand1), len(operand2))
    return [' ' * (length - len(operand1)) + operand1,
            split_string + ' ' * (length - len(operand2) - 1) + operand2,
            '-' * length]

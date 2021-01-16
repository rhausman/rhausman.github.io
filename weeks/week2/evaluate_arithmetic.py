"""
Write a Python function called evaluate_arithmetic that takes a string 
consisting of digits 0-9, operation symbols + - * and /, and parentheses, 
and evaluates its result as a mathematical expression, respecting the usual 
order of operations.  For instance, evaluate_arithmetic("(1+3) * 6 - 4 / 2") 
should return 22.  The challenge is to do this on your own; don't use the built-in 
eval function!  
If the input expression is not valid, you can either return an error 
message or simply None.
"""
# reverse order of operation (evaluated recursively), checked sequentially
operators = ["*", "/", "+", "-"][::-1]


def evaluate_arithmetic(exp):
    # remove spaces
    exp = "".join([c for c in exp if c != " "])
    # print(exp)
    if exp == "":
        print("EMPTY STRING")
        return None

    # First, check for parenthetical
    if "(" in exp:
        opening = exp.find("(")
        # find last occurance of closing paren
        closing = exp.rfind(")")
        # evaluate in context

        return evaluate_arithmetic(
            exp[:opening]
            + str(evaluate_arithmetic(exp[opening + 1 : closing]))
            + exp[closing + 1 :]
        )

    # next, check for operators in the proper order
    for op in operators:
        if op in exp:

            split = exp.split(op)
            if len(split) == 2:
                a, b = evaluate_arithmetic(split[0]), evaluate_arithmetic(split[1])
            else:
                # if the same operation occurs more than once
                a = evaluate_arithmetic(op.join([split[0], split[1]]))
                b = evaluate_arithmetic(split[2:])
            # print("(", op, " ", a, " ", b, ")")
            if op == "+":
                return a + b
            elif op == "-":
                if split[0] == "":
                    # negative number case
                    a = 0
                return a - b
            elif op == "*":
                return a * b
            elif op == "/":
                return a / b
            else:
                print("something went wrong")
                return None
            # break
    # now try to interpret as int

    return float(exp)

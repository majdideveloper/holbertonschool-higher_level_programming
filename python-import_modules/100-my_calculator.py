#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    res = 0
    lengArg = len(sys.argv)
    if lengArg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    validOp = "+-*/"
    valid = validOp.find(sys.argv[2])
    if valid == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if valid == 0:
        res = add(sys.argv[1], sys.argv[3])
        print(f"""{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}""")

    if valid == 1:
        res = sub(sys.argv[1], sys.argv[3])
        print(f"""{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}""")

    if valid == 2:
        res = mul(sys.argv[1], sys.argv[3])
        print(f"""{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}""")

    if valid == 3:
        res = div(sys.argv[1], sys.argv[3])
        print(f"""{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}""")

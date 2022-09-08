#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    lengArg = len(sys.argv)
    if lengArg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    validOp = "+-*/"
    valid = validOp.find(sys.argv[2])
    if valid == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if valid == 0:
        print("{} + {} = {}".format(a, b, add(a, b)))

    if valid == 1:
        print("{} - {} = {}".format(a, b, sub(a, b)))

    if valid == 2:
        print("{} * {} = {}".format(a, b, mul(a, b)))

    if valid == 3:
        print("{} / {} = {}".format(a, b, div(a, b)))

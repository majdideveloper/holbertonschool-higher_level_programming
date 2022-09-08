#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0
    lengArg = len(sys.argv)
    if lengArg <= 1:
        print("0")
    else:
        for item in range(1, lengArg):
            res += int(sys.argv[item])
        print(f"{res}")

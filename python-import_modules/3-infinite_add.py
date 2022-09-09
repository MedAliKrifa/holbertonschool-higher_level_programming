#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    length = len(sys.argv)
    if length <= 1:
        print(0)
    else:
        for x in range(1, length):
            result = result + int(sys.argv[x])
        print(f"{result}")

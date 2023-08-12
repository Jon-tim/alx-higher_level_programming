#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    argc = len(sys.argv) - 1
    if argc == 0:
        print(0)
    else:
        for i in range(1, argc + 1):
            sum += int(sys.argv[i])
    print(sum)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    r = 0
    num_args = len(sys.argv)
    if (num_args > 1):
        for i in range(1, num_args):
            r += (int(sys.argv[i]))
        print("{}".format(r))

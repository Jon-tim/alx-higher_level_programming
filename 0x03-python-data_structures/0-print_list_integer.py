#!/usr/bin/python3
if __name__ == "__main__":
    """Print all integers of a list."""
    def print_list_integer(my_list=[]):
        for i in range(len(my_list)):
            print("{}".format(int(my_list[i])))

#!/usr/bin/python3

import sys

def hello_world(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    hello_world(sys.argv[1])
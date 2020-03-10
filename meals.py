# -*- coding: utf-8 -*-

"""
Learn to use argparse module
https://docs.python.org/zh-cn/3.8/library/argparse.html
Example:
    python3 meals.py -h
    python3 meals.py supper -h
    python3 steps/meals.py plan -h
    python3 meals.py lunch make --food rice -f meat
    python3 meals.py lunch make --food rice meat eggs --drink water juice
"""


import argparse

def main():
    parser = argparse.ArgumentParser(prog='meals', description="food or drink for each meal")
    parser.add_argument('meal', type=str, choices=('breakfast', 'lunch', 'supper'), nargs='?',
                        default='lunch', help='choose mealtime, such as breakfast, lunch or supper ')

    # subparsers用于产生子命令解析器
    subparsers = parser.add_subparsers(help='describe process', dest='behave')
    parser_a = subparsers.add_parser('plan', help='have not made the final decision yet')
    parser_a.add_argument('-f', '--food', type=str, metavar='food', default='rice',
                          nargs='+', action='store', help='the food to eat')
    parser_a.add_argument('-d', '--drink', type=str, metavar='drinks', default='water',
                          nargs='+', action='store',
                          help='drinks')
    parser_b = subparsers.add_parser('make', help='final decision')
    parser_b.add_argument('-f', '--food', type=str, metavar='food', default='rice',
                          nargs='+', action='store', help='the food to eat')
    parser_b.add_argument('-d', '--drink', type=str, metavar='drinks', default='water',
                          nargs='+', action='store',
                          help='drinks')

    args = parser.parse_args()
    print(args, args.behave)


if __name__ == "__main__":
    main()

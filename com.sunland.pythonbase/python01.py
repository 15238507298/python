import sys
import traceback
import pprint
'''
redirect stdout to file
'''


def print1(name):
    # define file
    f = open('log.txt','w')
    # file redirect to stdout
    sys.stdout = f
    print(name)
    # screen print stream to stdout
    sys.stdout = sys.__stdout__
    print(name)


'''
traceback deal Exception
'''


def tt():
    for i in '123456789098765':
        try:
            10.0/int(i)
        except Exception as e:
            traceback.print_exc()
            print(traceback.format_exc())
            continue


'''
[c for c in XXX]
'''


def lambda1():
    s = [int(c)*2 for c in '123456789']
    print(s)


'''
String format print
'''


def parser():
    data = ("this is a string", [1, 2, 3, 4], ("more tuples", 1.0, 2.3, 4.5), "this is yet another string")
    pprint.pprint(data)


if __name__ == '__main__':
    # print1('mary')
    # tt()
    # lambda1()
    parser()




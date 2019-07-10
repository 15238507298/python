import sys
import traceback

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


if __name__ == '__main__':
    # print1('mary')
    tt()

import sys

'''
redirect stdout to file
'''
def print1(name):
    #define file
    f = open('log.txt','w')
    #file redirect to stdout
    sys.stdout = f
    print(name)
    #screen print stream to stdout
    sys.stdout = sys.__stdout__
    print(name)



if __name__=='__main__':
    print1('mary')
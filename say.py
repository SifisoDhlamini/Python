#import cowsay
import sys

from sayings import hello, goodbye

if len(sys.argv) == 2:
    #cowsay.cow("hello, " + sys.argv[1])
    name = sys.argv[1]
    hello(name)
    goodbye(name)


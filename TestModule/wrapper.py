import os.path
from ctypes import *
from numpy.ctypeslib import ndpointer

me = os.path.abspath(os.path.dirname(__file__))
lib = cdll.LoadLibrary(os.path.join(me, "lib", "libtest.so"))

# function
printData = lib.printData
printData.restype = None
printData.argtypes = [ndpointer(c_double), c_int]

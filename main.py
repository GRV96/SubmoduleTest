from os import system

from LoopIndex.loop_index import LoopIndex
from MockSubmodule.astonishing_wonderful_functions import *

index = LoopIndex(7)
while index.iterate():
    i = index.get_value()
    print("i =", i)
    print("Fantastic:", super_ultimate_function(i))
    print("Uninteresting:", dull_function(365.24 * i))
    print()

system("pause")

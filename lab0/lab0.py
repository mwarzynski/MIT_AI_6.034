# This is the file you'll use to submit most of Lab 0.

# Section 1: Problem set logistics ___________________________________________

# What version of Python do we *recommend* (not "require") for this course?
#   1. Python v2.3
#   2. Python v2.5 or Python v2.6
#   3. Python v3.0
# Fill in your answer in the next line of code ("1", "2", or "3"):

ANSWER_1 = '2'


# Section 2: Programming warmup _____________________________________________

# Problem 2.1: Warm-Up Stretch

def cube(x):
    return x*x*x

def factorial(x):
    if x < 0:
        return -1
    ret = 1
    for i in range(1, x+1):
        ret = ret * i
    return ret

def count_pattern(pattern, lst):
    count = 0
    for i in range(0, len(lst)):
        if lst[i:i+len(pattern)] == pattern:
            count += 1
    return count

# Problem 2.2: Expression depth

def depth(expr):
    if not isinstance(expr, (tuple, list)):
        return 0
    d = 1
    for x in expr:
        if isinstance(x, (tuple, list)):
            t = depth(x)
            if t+1 > d:
                d = t+1
    return d


# Problem 2.3: Tree indexing

def tree_ref(tree, index):
    t = tree
    for i in index:
        t = t[i]
    return t


# Section 3: Symbolic algebra

# Your solution to this problem doesn't go in this file.
# Instead, you need to modify 'algebra.py' to complete the distributer.

from algebra import Sum, Product, simplify_if_possible
from algebra_utils import distribution, encode_sumprod, decode_sumprod


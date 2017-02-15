"""
Class ReversePolishNotation

Method run()
    Begins a program that allows you to enter calculations in an
    RPN style. Evaluations will be stored in the stack. The stack
    may be incrementally evaluated.

    Calculator Operators:
        - : subtract
        + : add
        * : multiply
        / : divide
        ^ : exponent
        sqrt: square root (one argument only)
        s : print stack
        c : clear stack
        q : exit
        <blank> : Evaluate and print stack

ops dictionary modified from from Jamal on StackExchange
http://codereview.stackexchange.com/questions/79795/reverse-polish-notation-calculator-in-python
"""
from __future__ import division
from copy import copy
from collections import deque
import math
import operator


# Need to take an input string, split string into list
# input string is iterated over, adding each character to a deque
# when the deque encounters an operator, the operator and
#   the last 2 integers are replaced with the evaluation

class ReversePolishNotation(object):

    def __init__(self, rounding=2):
        self.stack = deque()
        self.ops = {'+':operator.add,
               '-':operator.sub,
               '*':operator.mul,
               '/':operator.div,
               '^':operator.pow,
               'sqrt': math.sqrt} # sqrt takes one argument
        self.r = rounding


    def run(self):

        cin = ""

        while cin != "q":
            cin = raw_input("Operation(s)/Value(s): ")
            if cin == 's':
                self.print_stack()
            elif cin == "":
                self.evaluate()
                self.print_stack()
            elif cin == "c":
                self.stack.clear()
            elif cin != "q":
                self.stack.extend(cin.split())

    def evaluate(self):

        inputstack = copy(self.stack)
        self.stack.clear()

        while len(inputstack) > 0:
            if inputstack[0] not in self.ops.keys():
                self.stack.append(float(inputstack.popleft()))
            elif inputstack[0] in self.ops.keys():
                if inputstack[0] in '+-*/^':
                    op = inputstack.popleft()
                    pop2 = float(self.stack.pop())
                    pop1 = float(self.stack.pop())
                    calc = self.ops[op](pop1, pop2)
                    self.stack.append(calc)
                elif inputstack[0] in 'sqrt':
                    op = inputstack.popleft()
                    pop1 = float(self.stack.pop())
                    calc = self.ops[op](pop1)
                    self.stack.append(calc)

    def print_stack(self):

        for i in self.stack:
            if (str(i) in '+-/*^') or (str(i) == "sqrt"):
                print i,
            elif (float(i) % 1 == 0):
                print int(i),
            elif (float(i) % 1 > 0):
                print round(float(i), 2),
        print ""

if __name__ == "__main__":
    rpn = ReversePolishNotation()
    rpn.run()

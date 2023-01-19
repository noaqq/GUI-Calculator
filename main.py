from decimal import *
from tkinter import *

root = Tk()
root.title("Calculator")

buttons = (
    ("7", "8", "9", "/", "4"),
    ("4", "5", "6", "*", "4"),
    ("1", "2", "3", "-", "4"),
    ("0", ".", "=", "+", "4"),
)

activeStr = ""
stack = []


def logic():
    global label
    global stack
    res = 0
    number1 = Decimal(stack.pop())
    operation = stack.pop
    number2 = Decimal(stack.pop())

    if operation == "+":
        res = number1 + number2
    if operation == "-":
        res = number1 - number2
    if operation == "*":
        res = number1 * number2
    if operation == "/":
        res = number1 / number2

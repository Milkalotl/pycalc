import math
import sys

# add sub mult div
operators = [lambda a,b: a+b, lambda a,b: a-b, lambda a,b: a*b, lambda a,b: a/b, lambda a,b: a**b, lambda a,b: b**(1/a), lambda a,b: a**(1/b)]
# 0: +  sum
# 1: -  sub
# 2: *  mul
# 3: /  div
# 4: ** exp
# 5: rt n-root
# 6_ tr toor-n

def formatio(ilist):
    h_list = []
    for n in range(len(ilist)):
        a = ilist[n]
        match a:
            case "+": a = 0
            case "-": a = 1
            case "x" | "*": a = 2
            case "/": a = 3
            case "xx" | "^": a = 4
            case "rt": a = 5
            case "tr": a = 6
            case "pi": a = math.pi
            case _: a = float(a)
        h_list.append(a)
    return h_list

process_3 = lambda a, b, c: operators[b](a,c)
def process_2(h_list):
    a = process_3(h_list[0], h_list[1], h_list[2])
    #print(a)
    for n in range(3):
        h_list.pop(0)
    h_list.insert(0,a)
    #print(h_list)
    return len(h_list)

def process_1(h_list) -> float:
    while(True):
        if len(h_list) > 2:
            process_2(h_list)
        else:
            return h_list[0]

def main(ilist):
    ilist = formatio(ilist)
    print(process_1(ilist))


if len(sys.argv) > 2:
    h_list = sys.argv
    h_list.pop(0)
    main(h_list)
else:
    print("Please input some parameters!!\nGuide:\n\tParameters spaced out by spaces!! 9 x 4 + 3 - 2 (like that !!)")
    print("Operators:\n\tsum: +\n\tsubtract: -\n\tmultiply: x\n\tdivide: /\n\texponential: xx OR ^\n\troots: rt (3 rt 4 would be ∛4)\n HAVE FUN!!!")
    i = input("\n:")
    if i == "q":
        quit(0)
    h_list = i.split(" ")
    if len(h_list) < 3:
        quit(-1)
    h_list.insert(0, "goobagack")
    main(h_list)


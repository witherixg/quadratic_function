import ast
import json
from fractions import Fraction

from sympy import Symbol, Rational, solve


class Position:
    def __init__(self, s: str):
        lst = s.replace("(", "").replace(")", "").split(",")
        self.x = Rational(lst[0])
        self.y = Rational(lst[1])

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def getPosition(self):
        return self.x, self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y


def newPosition(__prompt=''):
    while True:
        position_string = input(__prompt)
        if len(position_string.split(',')) == 2:
            try:
                p = Position(position_string)
                return p
            except TypeError:
                printError('"x" and "y" should both be numbers.')
        else:
            printError('A position should in the pattern as "(x,y)".')


def getParamWithNothing(p1: Position, p2: Position, p3: Position):

    unknown_a = Symbol("unknown_a")
    unknown_b = Symbol("unknown_b")
    unknown_c = Symbol("unknown_c")
    x_1, y_1 = p1.getPosition()
    x_2, y_2 = p2.getPosition()
    x_3, y_3 = p3.getPosition()
    # check if p1(also p2) is vertex
    if p1 == p2:
        # 2ah + b = 0
        # ah² + k - c = 0
        h = p1.getX()
        k = p1.getY()
        eq = [2 * unknown_a * h + unknown_b,
              unknown_a * h * h + k - unknown_c,
              x_3 * x_3 * unknown_a + x_3 * unknown_b + unknown_c - y_3]
    # else
    else:
        eq = [x_1 * x_1 * unknown_a + x_1 * unknown_b + unknown_c - y_1,
              x_2 * x_2 * unknown_a + x_2 * unknown_b + unknown_c - y_2,
              x_3 * x_3 * unknown_a + x_3 * unknown_b + unknown_c - y_3]
    dic = solve(eq, [unknown_a, unknown_b, unknown_c])
    v = list(dic.values())
    return Fraction(str(v[-3])) if v[-3] is not None else 0, Fraction(str(v[-2])) if v[-2] is not None else 0, Fraction(
        str(v[-1])) if v[-1] is not None else 0


def getParamWithA(a, p1: Position, p2: Position):
    # check if p1(also p2) is vertex
    if p1 == p2:
        # b = -2ah
        # c = ah² + k
        h = p1.getX()
        k = p1.getY()
        b = -2 * a * h
        c = a * h * h + k
        return b, c
    # else
    unknown_b = Symbol("unknown_b")
    unknown_c = Symbol("unknown_c")
    x_1, y_1 = p1.getPosition()
    x_2, y_2 = p2.getPosition()
    eq = [x_1 * x_1 * a + x_1 * unknown_b + unknown_c - y_1,
          x_2 * x_2 * a + x_2 * unknown_b + unknown_c - y_2]
    dic = solve(eq, [unknown_b, unknown_c])
    v = list(dic.values())
    return Fraction(str(v[-2])) if v[-2] is not None else 0, Fraction(str(v[-1])) if v[-1] is not None else 0


def getParamWithB(b, p1: Position, p2: Position):
    # check if p1(also p2) is vertex
    if p1 == p2:
        # a = -b/2h
        # c = ah² + k
        h = p1.getX()
        k = p1.getY()
        a = - b / (2 * h)
        c = a * h * h + k
        return a, c

    # else
    unknown_a = Symbol("unknown_a")
    unknown_c = Symbol("unknown_c")
    x_1, y_1 = p1.getPosition()
    x_2, y_2 = p2.getPosition()
    eq = [x_1 * x_1 * unknown_a + x_1 * b + unknown_c - y_1,
          x_2 * x_2 * unknown_a + x_2 * b + unknown_c - y_2]
    dic = solve(eq, [unknown_a, unknown_c])
    v = list(dic.values())
    return Fraction(str(v[-2])) if v[-2] is not None else 0, Fraction(str(v[-1])) if v[-1] is not None else 0


def getParamWithC(c, p1: Position, p2: Position):
    # check if p1(also p2) is vertex
    if p1 == p2:
        # a = (c-k)/h²
        # b = -2ah
        h = p1.getX()
        k = p1.getY()
        a = (c - k) / (h * h)
        b = -2 * a * h
        return a, b

    # else
    unknown_a = Symbol("unknown_a")
    unknown_b = Symbol("unknown_b")
    x_1, y_1 = p1.getPosition()
    x_2, y_2 = p2.getPosition()
    eq = [x_1 * x_1 * unknown_a + x_1 * unknown_b + c - y_1,
          x_2 * x_2 * unknown_a + x_2 * unknown_b + c - y_2]
    dic = solve(eq, [unknown_a, unknown_b])

    v = list(dic.values())
    return Fraction(str(v[-2])) if v[-2] is not None else 0, Fraction(str(v[-1])) if v[-1] is not None else 0


def getParamWithAB(a, b, p1: Position):
    unknown_c = Symbol("unknown_c")
    x_1, y_1 = p1.getPosition()
    eq = [x_1 * x_1 * a + x_1 * b + unknown_c - y_1]
    dic = solve(eq, [unknown_c])

    v = list(dic.values())
    return Fraction(str(v[-1])) if v[-1] is not None else 0


def getParamWithAC(a, c, p1: Position):
    unknown_b = Symbol("unknown_b")
    x_1, y_1 = p1.getPosition()
    eq = [x_1 * x_1 * a + x_1 * unknown_b + c - y_1]
    dic = solve(eq, [unknown_b])

    v = list(dic.values())
    return Fraction(str(v[-1])) if v[-1] is not None else 0


def getParamWithBC(b, c, p1: Position):
    unknown_a = Symbol("unknown_a")
    x_1, y_1 = p1.getPosition()
    eq = [x_1 * x_1 * unknown_a + x_1 * b + c - y_1]
    dic = solve(eq, [unknown_a])
    v = list(dic.values())
    return Fraction(str(v[-1])) if v[-1] is not None else 0


def isNotNone(*args):
    for i in args:
        if i is None:
            return False
    return True


def constantToStr(n):
    if n == 0:
        return ''
    elif str(n)[0] != '-':
        return '+' + str(n)
    else:
        return str(n)


def numToStrWithoutPositive(n):
    if n == 1:
        return ''
    elif n == -1:
        return '-'
    return str(n)


def numToStr(n):
    if n == 1:
        return '+'
    elif n == -1:
        return '-'
    elif n == 0:
        return ''
    if str(n)[0] != '-':
        return '+' + str(n)
    else:
        return str(n)


def checkRepetition(*args):
    a_set = set(args)
    return len(a_set) == len(args)


def printError(reason: str):
    doubleLine = "=" * 20
    print(f"{doubleLine}\nInvalid input!\nBecause: {reason}\n{doubleLine}")


def main():
    while True:
        reason = ""
        ua = ''
        ub = ''
        uc = ''
        flag = True
        # check if the input is valid
        try:
            s = (('{' + input('Input the value of a, b and c if given:(as a=1, b=2)\n'))
                 .replace('a', "'a'")
                 .replace('b', "'b'")
                 .replace('c', "'c'")
                 .replace('=', ":'")
                 .replace(',', "',") + "'").strip() + '}'
            if s == "{'}":
                s = '{}'
            if test:
                print(f"s={s}")
            param = eval(s)
            if test:
                print(f"param={param}")
            ua = param.get('a')
            ub = param.get('b')
            uc = param.get('c')
        except (SyntaxError, NameError, TypeError, AttributeError):
            reason = "Input is not under syntax."
        try:
            if isNotNone(ua):
                Rational(ua)
            if isNotNone(ub):
                Rational(ub)
            if isNotNone(uc):
                Rational(uc)

        except TypeError:
            reason = "Input is not under syntax."
            pass
        try:
            if Rational(ua) == 0:
                reason = "The parameter \"a\" can not be 0."
        except TypeError:
            pass
        if reason:
            printError(reason)
            continue
        if isNotNone(ua, ub, uc):
            ka = Rational(ua)
            kb = Rational(ub)
            kc = Rational(uc)
        elif isNotNone(ua, ub):
            ka = Rational(ua)
            kb = Rational(ub)
            kc = getParamWithAB(ka, kb, newPosition('First position?\n'))
        elif isNotNone(ua, uc):
            ka = Rational(ua)
            kc = Rational(uc)
            kb = getParamWithAC(ka, kc, newPosition('First position?\n'))
        elif isNotNone(ub, uc):
            kb = Rational(ub)
            kc = Rational(uc)
            ka = getParamWithBC(kb, kc, newPosition('First position?\n'))
        elif ua:
            ka = Rational(ua)
            p1 = newPosition('First position?\n')
            p2 = Position("0, 0")
            while flag:
                p2 = newPosition('Second position?\n')
                if p1.getX() != p2.getX() or p1 == p2:
                    flag = False
            kb, kc = getParamWithA(ka, p1, p2)
        elif ub:
            kb = Rational(ub)
            p1 = newPosition('First position?\n')
            p2 = Position("0, 0")
            while flag:
                p2 = newPosition('Second position?\n')
                if p1.getX() != p2.getX() or p1 == p2:
                    flag = False
            ka, kc = getParamWithB(kb, p1, p2)
        elif uc:
            kc = Rational(uc)
            p1 = newPosition('First position?\n')
            p2 = Position("0, 0")
            while flag:
                p2 = newPosition('Second position?\n')
                if p1.getX() != p2.getX() or p1 == p2:
                    flag = False
            ka, kb = getParamWithC(kc, p1, p2)
        else:
            p1 = newPosition('First position?\n')
            p2 = Position("0, 0")
            p3 = Position("0, 0")
            while flag:
                p2 = newPosition('Second position?\n')
                if p1.getX() != p2.getX() or p1 == p2:
                    flag = False
            flag = True
            while flag:
                p3 = newPosition('Third position?\n')
                if p1.getY() == p2.getY() == p3.getY():
                    flag = True
                elif p1.getX() == p2.getX():
                    if p1.getY() == p2.getY():
                        flag = False
                    else:
                        flag = True
                elif p1.getX() == p3.getX():
                    if p1.getY() == p3.getY():
                        # Make sure that p1 is equals to p2 instead of p3
                        p2, p3 = p3, p2
                        flag = False
                elif p2.getX() == p3.getX():
                    if p2.getY() == p3.getY():
                        # Make sure that p1 is equals to p2 instead of p3
                        p1, p3 = p3, p1
                        flag = False
                else:
                    flag = False
            ka, kb, kc = getParamWithNothing(p1, p2, p3)
        sa = numToStrWithoutPositive(ka)
        x = Symbol("x")
        solutions = solve([ka * x * x + kb * x + kc], [x])
        if 'I' in str(solutions[0][0]):
            s = 'No intersections'
        elif len(solutions) == 1:
            s = f'({solutions[0][0]},0)'
        else:
            s = f'({solutions[0][0]},0)'
            s += f'({solutions[1][0]},0)'
        vertex_x = -kb / (2 * ka)
        vertex_y = kc - kb ** 2 / (4 * ka)
        str_negative_h = constantToStr(-vertex_x)
        print(f"y={sa}x²{numToStr(kb)}{'x' if numToStr(kb) else ''}{constantToStr(kc)}")
        if str_negative_h != '':
            print(f"( also y={sa}(x{str_negative_h})²{constantToStr(vertex_y)} )")
        if 'I' not in str(solutions[0][0]) and len(solutions) == 2:
            if -solutions[0][0] == 0:
                print(f"( also y={sa}x(x{(constantToStr(-solutions[1][0]))}) )")
            elif -solutions[1][0] == 0:
                print(f"( also y={sa}x(x{(constantToStr(-solutions[0][0]))}) )")
            else:
                print(f"( also y={sa}(x{constantToStr(-solutions[0][0])})(x{(constantToStr(-solutions[1][0]))}) )")

        print(f"Vertex ({'Maximum' if ka < 0 else 'Minimum'}) : ({vertex_x}, {vertex_y})")
        print(f"Symmetry: x = {vertex_x}")
        print(f"Intersection with x-axis: {s}")
        print()

test = False
if __name__ == "__main__":
    main()

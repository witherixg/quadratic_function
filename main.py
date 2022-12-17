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
    return Position(input(__prompt))


def getParamWithNothing(p1: Position, p2: Position, p3: Position):
    unknown_a = Symbol("unknown_a")
    unknown_b = Symbol("unknown_b")
    unknown_c = Symbol("unknown_c")
    x_1, y_1 = p1.getPosition()
    x_2, y_2 = p2.getPosition()
    x_3, y_3 = p3.getPosition()
    eq = [x_1 * x_1 * unknown_a + x_1 * unknown_b + unknown_c - y_1,
          x_2 * x_2 * unknown_a + x_2 * unknown_b + unknown_c - y_2,
          x_3 * x_3 * unknown_a + x_3 * unknown_b + unknown_c - y_3]
    dic = solve(eq, [unknown_a, unknown_b, unknown_c])
    v = list(dic.values())
    return Fraction(str(v[-3])) if v[-3] is not None else 0, Fraction(str(v[-2])) if v[-2] is not None else 0, Fraction(
        str(v[-1])) if v[-1] is not None else 0


def getParamWithA(a, p1: Position, p2: Position):
    # check if p1(p2) is vertex
    if p1 == p2:
        # b = -2ah
        # c = ah² + k
        h = p1.getX()
        k = p1.getY()
        return -2 * a * h, a * h * h + k

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


def numToStrForInteger(n):
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


def main():
    while True:
        param = eval(
            ('{' + input('Input the value of a, b and c if given:(as a=1, b=2)\n') + '}').replace('a', "'a'").replace(
                'b', "'b'").replace('c', "'c'").replace('=', ':'))

        ua = param.get('a')
        ub = param.get('b')
        uc = param.get('c')
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
            kb, kc = getParamWithA(ka, newPosition('First position?\n'), newPosition('Second position?\n'))
        elif ub:
            kb = Rational(ub)
            ka, kc = getParamWithB(kb, newPosition('First position?\n'), newPosition('Second position?\n'))
        elif uc:
            kc = Rational(uc)
            ka, kb = getParamWithC(kc, newPosition('First position?\n'), newPosition('Second position?\n'))
        else:
            ka, kb, kc = getParamWithNothing(newPosition('First position?\n'), newPosition('Second position?\n'),
                                             newPosition())
        sa = numToStrWithoutPositive(ka)
        print(f"y={sa}x²{numToStr(kb)}{'x' if numToStr(kb) else ''}{numToStrForInteger(kc)}")
        x = Symbol("x")
        solutions = solve([ka * x * x + kb * x + kc], [x])
        if 'I' in str(solutions[0][0]):
            s = 'No intersections'
        elif len(solutions) == 1:
            s = f'({solutions[0][0]},0)'
        else:
            s = f'({solutions[0][0]},0)'
            s += f'({solutions[1][0]},0)'
        vertex_x = -kb / 2 * ka
        vertex_y = kc - kb ** 2 / (4 * ka)
        str_negative_h = numToStrForInteger(-vertex_x)
        if str_negative_h != '':
            print(f"(also y={sa}(x{str_negative_h})²{numToStrForInteger(vertex_y)} )")
        if 'I' not in str(solutions[0][0]) and -solutions[0][0] != (numToStrForInteger(-solutions[1][0])):
            if -solutions[0][0] == 0:
                print(f"(also y={sa}x(x{(numToStrForInteger(-solutions[1][0]))}) )")
            elif -solutions[1][0] == 0:
                print(f"(also y={sa}x(x{(numToStrForInteger(-solutions[0][0]))}) )")
            else:
                print(f"(also y={sa}(x{numToStrForInteger(-solutions[0][0])})(x{(numToStrForInteger(-solutions[1][0]))}) )")

        print(f"Vertex: ({-kb / 2 * ka},{kc - kb ** 2 / (4 * ka)})")
        print(f"Symmetry: x = {-kb / 2 * ka}")
        print(f"Intersection with X axis: {s}")


if __name__ == "__main__":
    main()

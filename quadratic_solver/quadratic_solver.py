from math import sqrt


class QuadraticEquationsSolver:
    def __init__(self):
        pass

    def discriminant(self, a, b, c):
        return b * b - 4 * a * c

    # We assume all coefficients are nonzero
    # and we will find only real roots
    def solve(self, a, b, c):
        d = self.discriminant(a, b, c)
        if d < 0:
            print("No roots")
        elif d > 0:
            x1 = (-b + sqrt(d)) / (2.0 * a)
            x2 = (-b - sqrt(d)) / (2.0 * a)
            print("x1 = {}, x2 = {}".format(x1, x2))
        else:
            print("x = {}".format((-b) / (2.0 * a)))


if __name__ == "__main__":
    quad = QuadraticEquationsSolver()
    quad.solve(1,4,-4)
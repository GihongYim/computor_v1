import sys


def polynomial(p : str):
    poly = dict
    term = p.split("+")
    print(term)
    pass

def computor(equation: str):
    try:
        if not isinstance(equation, str):
            raise TypeError("equation should be str")
        left_right = equation.split('=')
        if len(left_right) != 2:
            raise ValueError(f"{equation} it not equation")
    except Exception as e:
        print(e)
        exit(1)

    left = left_right[0]
    right = left_right[1]
    print(left)
    print(right)

    left_poly = polynomial(left)
    right_poly = polynomial(right)



if __name__ == "__main__":
    computor(sys.argv[1])

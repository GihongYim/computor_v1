import sys

def is_float(f : str):
    try:
        float(f)
        return True
    except ValueError:
        return False


def polynomial(p : str) -> list:
    poly = {}
    sign = 1.0
    coef = 1.0
    x_pow = 0
    
    for word in p.split():
        if word == '+' or word == '-':
            if x_pow not in poly.keys():
                poly[x_pow] = 0.0
            poly[x_pow] += sign * coef
            if word == '+':
                coef = 1.0
            elif word == '-':
                coef = -1.0
            x_pow = 0
        elif is_float(word):
            coef *= float(word)
        elif word[0:2] == "X^" and is_float(word[2:]):
            x_pow += int(word[2:])
    if x_pow not in poly.keys():
        poly[x_pow] = 0.0
    poly[x_pow] = coef
    # print(poly)
    return poly


def poly_form(poly: dict):
    form_list = []
    for pow_x, coeff in poly.items():
        if coeff == 0.0: continue
        if coeff < 0.0:
            form_list.append('-')
            coeff = -coeff
        elif len(form_list) != 0:
            form_list.append('+')
        form_list.append(str(coeff) + " * X^" + str(pow_x))
    
    if len(form_list) == 0:
        reduced_form = '0'
    else:
        reduced_form = ' '.join(form_list)
    return reduced_form

def get_degree(poly: dict):
    return [key for key in poly.keys()][-1]

def discriminant(poly: dict):
    return poly[1] ** 2 - 4 * poly[2] * poly[0]

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

    left_poly = polynomial(left)
    right_poly = polynomial(right)

    for x_pow, coef in right_poly.items():
        if x_pow not in left_poly.keys():
            left_poly[x_pow] = 0.0
        left_poly[x_pow] -= coef
    poly_degree = get_degree(left_poly)
    left_terms = poly_form(left_poly)
    print(f"Reduced form: {left_terms} = 0")
    print(f"Polynomial degree: {poly_degree}")

    if poly_degree >= 3:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    else:
        D = discriminant(left_poly)
        if D > 0:
            pass
        elif D == 0.0:
            pass
        else:
            pass




if __name__ == "__main__":
    computor(sys.argv[1])

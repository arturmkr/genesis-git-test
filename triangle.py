def is_valid_triangle(side_a, side_b, side_c):
    if side_a + side_b >= side_c and side_b + side_c >= side_a and side_c + side_a >= side_b:
        return True
    else:
        return False


def is_right_angled_triangle(side_a, side_b, side_c):
    return (side_a * side_a + side_b * side_b == side_c * side_c) or \
           (side_c * side_c + side_b * side_b == side_a * side_a) or \
           (side_a * side_a + side_c * side_c == side_b * side_b)


def determine_triangle_type_by_length(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return "Equilateral triangle"
    elif side_a == side_b or side_b == side_c or side_c == side_a:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


def print_triangle_properties(side_a, side_b, side_c):
    if is_valid_triangle(side_a, side_b, side_c):
        print("Triangle is Valid")
        print(f"Triangle type by length: {determine_triangle_type_by_length(side_a, side_b, side_c)}")
        if is_right_angled_triangle(side_a, side_b, side_c):
            print("Triangle is right angled")
        else:
            print("Triangle is not right angled")
    else:
        print("Triangle is Invalid")


if __name__ == "__main__":
    line_1 = float(input("Enter length of line 1: "))
    line_2 = float(input("Enter length of line 2: "))
    line_3 = float(input("Enter length of line 3: "))
    print_triangle_properties(line_1, line_2, line_3)

def sum_two_var(a, b):
    return a + b


def present_result(value):
    # return f'X = {value}' # The website still uses Python 3.4.3...
    return 'X = {}'.format(value)


if __name__ == "__main__":
    A = eval(input())
    B = eval(input())
    print(present_result(sum_two_var(A, B)))

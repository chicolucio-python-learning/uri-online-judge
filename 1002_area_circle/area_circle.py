# pi value as defined in description
PI = 3.14159


def area_circle(radius):
    """Calculates the area of a circle

    Parameters
    ----------
    radius : float
        radius of the circle

    Returns
    -------
    string
        Area value formatted as defined in description
    """
    area = PI * radius**2
    return '{:.4f}'.format(area)


if __name__ == "__main__":
    R = input()
    result = area_circle(eval(R))
    print("A="+result)  # python adds a \n by default so EOL satisfied

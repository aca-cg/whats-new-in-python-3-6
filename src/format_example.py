def compute_sum(a, b, precision):
    """ Returns a string showing the sum of a and b as in the following example:
    Let a = 3.1, b = 2.2 and precision=4, the expected result is "3.1 + 2.2 = 5.3"
    """
    return f"{a} + b} = {a + b:.{precision}}"

print(compute_sum(3.2, 2.2, 2))

import math


def find_order(a, n):
    if (a == 1) & (n == 1):
        return 1
    if math.gcd(a, n) != 1:
        return -1
    for i in range(1, n):
        if pow(a, i) % n == 1:
            return i
    return -1


def euler_totient(n):
    result = n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result


def find_primitive_root(n):
    if n == 1:
        return 0
    phi = euler_totient(n)
    p_root_list = []
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            order = find_order(i, n)
            if order == phi:
                p_root_list.append(i)
    return p_root_list


def get_super(x):
    normal = "0123456789"
    super_s = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

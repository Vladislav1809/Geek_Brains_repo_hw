from functools import wraps


def val_checker(dec_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        def wrapped(x):
            if dec_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)
        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(1)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

# https://docs.python.org/3.7/library/functions.html#breakpoint

try:
    num = 1
    div = 0
    frac = num / div
except ZeroDivisionError:
    # BEFORE 3.7

    import pdb

    pdb.set_trace()

    # AFTER 3.7

    # breakpoint()

    # looks at environment variable PYTHONBREAKPOINT
    # to determine the debugger - pluggable!

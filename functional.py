
do_it = lambda f, *args, **kwargs: f(*args, **kwargs)
# map() - based action sequence
# map(do_it, [f1, f2, f3])  # functions executed in iteration

hello = lambda first, last: print("Hello", first, last)
bye = lambda first, last: print("Bye", first, last)

# _ = list(map(do_it, [hello, bye], ["David", "Jane"], ["Mertz", "Doe"]))

do_all_funcs = lambda fns, *args: [list(map(fn, *args)) for fn in fns]
_ = do_all_funcs([hello, bye], ["David", "Jane"], ["Metz", "Doe"])


# imperative version of "echo()"
def echo_IMP():
    while 1:
        x = input("IMP -- ")
        if x == "quit":
            break
        else:
            print(x)

# functional version
def identity_print(x):
    print(x)
    return x

echo_FP = lambda: identity_print(input("FP -- ")) == 'quit' or echo_FP()  # this is where our python knowledge needs to deepen.
echo_FP()
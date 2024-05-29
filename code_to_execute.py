from sympy import *
def find_f_of_100():
    """A function $f: \mathbb N \to \mathbb N$ satisfies the following two conditions for all positive integers $n$:$f(f(f(n)))=8n-7$ and $f(2n)=2f(n)+1$. Calculate $f(100)$."""

    def f(n):
        return int((8*n - 7)**(1/3))

    f_100 = f(100)
    f_f_100 = f(f_100)
    f_f_f_100 = f(f_f_100)

    # Check if f(f(f(100))) equals 100
    if f_f_f_100 == 100:
        return f_f_100
    else:
        return "Function not found."

result = find_f_of_100()
print(result)

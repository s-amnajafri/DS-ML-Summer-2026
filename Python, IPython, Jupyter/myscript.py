def square(x):
    """square a number"""
    return x ** 2

for n in range(1,4):
    print(f"{n} squared is {square(n)}")

L = [n*2 for n in range(1,6)]

L = []
for n in range(1,6):
    L.append(n*2)

"""
Ipython magic commands:
1.  %run myscript.py   to run the file
2. %timeit or %%timeit to determine execution time (here it proves that list comprehensions are faster..235ns vs 270ns time)
3. %magic? to get description of all magic functions (? is shorthand of help() in IPython)
4. %lsmagic to list magic functions
5. %history to get a batch of previous input commands (for fist 4 inputs: %history -n 1-3)
6. %xmode to get details about exception/error (modes: plain, context (default mdoe), verbose)
7. %debug for debugging
"""

# factor-out temporary contexts
import sys
with open('help1.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout


from contextlib import redirect_stdout
with open('help2.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
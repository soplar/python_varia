from functools import partial

with open('sample.txt') as f:
    blocks = []
    while True:
        block = f.read(32)
        if block == '':
            break
        blocks.append(block)
    f. close()
print(blocks)


with open('sample.txt') as f:
    blocks = []
    # iter moet een functie hebben zonder argument
    # partial maakt van de functie f.read een functie zonder argument (normaal heeft die 1 argument)
    # en hierdoor heb je een iteratie mogelijkheid
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)
    f. close()
print(blocks)


from functools import lru_cache

def move(s):
    return s+1, s+4, s*3

@lru_cache(None)
def game(s):
    if s>=52:
        return 'W'
    if any( game(b) == 'W' for b in move(s) ):
        return 'P1'
    if all( game(b) == 'P1' for b in move(s) ):
        return 'V1'

    if any( game(b) == 'V1' for b in move(s) ):
        return 'P2'
    if all( game(b) == 'P2' or game(b)=='P1' for b in move(s) ):
        return 'V1/V2'

for s in range(1, 52):
    if game(s)=='V1/V2':
        print(s, game(s))




# %%
# stream of token
import re
from collections import namedtuple

# compile those pattern together
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# namedtuple; typename: 'Token'; field_names: 'type', 'value'
Token = namedtuple('Token', ['type', 'value'])


# it's a generator
def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        # 'type': m.lastgroup; 'value': m.group()
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')

# %%

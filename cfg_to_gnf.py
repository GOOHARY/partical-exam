import nltk
from nltk import CFG

def convert_to_gnf(grammar_string):
    # Placeholder function to show parsing a CFG
    grammar = CFG.fromstring(grammar_string)
    print("Rules:")
    for production in grammar.productions():
        print(production)

# Example CFG
cfg = """
S -> 'a' S 'b' | 'a' 'b'
"""

convert_to_gnf(cfg)
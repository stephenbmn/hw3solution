from operator import itemgetter
from itertools import dropwhile
from string import punctuation

def tokenize(s):
    """Break str s into a list of strings according to some procedure 
    tailored for the task at hand."""

    words = s.lower().strip().split()
    twords = [word.strip(punctuation) for word in words]
    return twords #doesn't handle ''' (e.g., "I'll" will be a token), '--' (e.g., "him -- I" will be a token), and word forms ("walking" and "walk" will be separate tokens)

def gutenberg_file_wc(filename):
    """Open the file with name filename, tokenize it with your 
    tokenize function, and return a dict mapping words to their 
    counts in the file.  Tokenize only the material that occurs
    between the two lines given above."""
    alice = open('alice.txt').read()
    a = alice.find("*** START OF THIS PROJECT GUTENBERG EBOOK") 
    z = alice.find("*** END OF THIS PROJECT GUTENBERG EBOOK") 
    alice_new = alice[a:z]
    alice_tokens = tokenize(alice_new)
    gutenberg_file_wc = {x: alice_tokens.count(x) for x in alice_tokens}
    return gutenberg_file_wc

def view_wc(d):
    """The input is a dict d mapping strings to ints. 
    The function should sort d in reverse order and
    return only pairs whose count value (index 1) is
    at least as large as the threshold, set to 10."""

    try:                       
        threshold = input('Please, enter a threshold (by default -- 10): ')       
    except:
        threshold = 10            
    for key, value in d.items():
        if value < threshold:
            del d[key]
    from operator import itemgetter
    dist = sorted(d.items(), key=itemgetter(1), reverse=True)
    for tup in dist:
        print str(tup[0]) + ":" + str(tup[1])

if __name__ == '__main__':

    print(gutenberg_file_wc('alice.txt'))
    print(view_wc(gutenberg_file_wc('alice.txt')))

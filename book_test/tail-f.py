import time

def watch(fn, words):
    fp = open(fn, 'r')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            for word in words:
                if word in new:
                    yield (word, new)
        else:
            time.sleep(0.5)

fn = 'test.py'
words = ['word']
for hit_word, hit_sentence in watch(fn, words):
    print("Found %r in line: %r" % (hit_word, hit_sentence))
"""
    help with (tail-f.py and coroutines.py)
    https://stackoverflow.com/questions/1703640/how-to-implement-a-pythonic-equivalent-of-tail-f?answertab=votes#tab-top 
    
"""

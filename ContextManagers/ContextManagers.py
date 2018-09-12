"""
handle the teardown of resources when we no longer need it
useful for files, database connections, locks 
we can write our own context managers using classes
and decorators 
Its used for managing
"""
from contextlib import contextmanager
class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with OpenFile('sample.txt', 'w') as f:
    f.write('Testting')

print(f.closed)

@contextmanager
def openfile(file, mode):
    f = open(file, mode)
    yield f
    """
    statements after yield behave as the tear down statement
    """
    f.close()

with openfile('secondsample.txt', 'w') as ff:
    ff.write('La Dolce Vita')

print(ff.closed)

import os

@contextmanager
def changedir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
    
with changedir('./ContextManagers/sample-dir-one'):
    print(os.listdir())


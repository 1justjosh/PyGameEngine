
import repackage

repackage.up()
from items.template import *

self = Temp("streetLight")

@self.decorate
def update(tiles):
    exec('''
foo = 1
bar = 2

selamlar = 42
    ''')
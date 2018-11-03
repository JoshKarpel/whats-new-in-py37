# https://www.python.org/dev/peps/pep-0562/

import wrap

print('AFTER IMPORT WRAP, BUT BEFORE USE SLOW')

print(wrap.slow.SlowClass)

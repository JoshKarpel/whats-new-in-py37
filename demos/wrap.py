print('imported wrap')

import slow

# USING MODULE __GETATTR__

# import importlib
#
# imports = ['slow']
#
#
# def __getattr__(name):
#     if name in imports:
#         print(f'importing {name}')
#         return importlib.import_module(f'.{name}', __name__)
#

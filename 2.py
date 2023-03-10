import os
print('Exist:', os.access('/Users/diasyerlan/Downloads/kulpesh.pdf', os.F_OK))
print('Readable:', os.access('/Users/diasyerlan/Downloads/kulpesh.pdf', os.R_OK))
print('Writable:', os.access('/Users/diasyerlan/Downloads/kulpesh.pdf', os.W_OK))
print('Executable:', os.access('/Users/diasyerlan/Downloads/kulpesh.pdf', os.X_OK))

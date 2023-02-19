import os
l=["Hi There","I Hope you are fine","This program will show you"]
print(len(l))
for i,j in enumerate(l):
    os.mkdir(f'{i}. {j}')
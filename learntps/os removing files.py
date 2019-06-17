import os
if os.path.exists('j.txt'):
    os.remove ('j.txt')
else:
    print("doesn't exist")


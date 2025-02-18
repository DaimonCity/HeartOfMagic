from scripts.Menu import *
from test import *

menu()

const = start_params()

new_floor = True
print(new_floor)
while new_floor is True:
    new_floor = test(*const)
    print(new_floor)


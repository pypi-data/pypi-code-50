import copy
import asteval


a = asteval.Interpreter()
a('x = 4')
a('y = 5')
print(a('sqrt(y+x)'))


def copy_asteval(aeval):
    beval = asteval.Interpreter()
    for key in aeval.user_defined_symbols():
        beval.symtable[key] = copy.deepcopy(aeval.symtable[key])
    return beval

b = copy_asteval(a)
print(b('sqrt(y+x)'))

b = a

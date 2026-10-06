from own_ast.types.list import *
from own_ast.types.symbol import *




def exec_load(filename :  str, *args) -> str:
    text = None
    with open(filename, 'r', encoding="utf-8") as file:
        text = file.read()
    return text

def show(value) -> str:
    if type(value) is bool:
        return str(value).lower()
    elif is_symbol(value):
        return symbol_name(value)
    elif type(value) is str:
        return '"'+value+'"'
    elif is_cons_list(value):
        out = "("
        while not is_nil(value):
            out += show(head(value)) + " "
            value = cdr(value)
        #if out[+1] == " ":
        #    out = out[:-1]
        out += ")"
        return out

    return str(value)


'''print(show(1.11), show(5), show("trueef"), show(True))
test = [1, 2, "4555", 'boo', True]
for  (i ,v) in enumerate(test):
    if i == 0:
        l = cons(v, nil)
    else:
        l = cons(v, l)
l = cons(5, l)
#l = cons(l, l) # завершающая ссылка на самого себя, всегда последняя
print(show(l))'''
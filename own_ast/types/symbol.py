#СИМВОЛ
# реализация 1
'''
class Symbol():
    def __init__(self, name):
        self.name = name

def symbol(name):
    return Symbol(name)

def symbol_name(symb):
    return symb.name

def is_symbol(value):
    return type(value) is Symbol
'''
# реализация 2
class Symbol():
    def __init__(self, name):
        self.name = name

def symbol(name):
    return "\0"+name

def symbol_name(symb):
    return symb[1:]

def is_symbol(value):
    return type(value) is str and value and value[0] == "\0"
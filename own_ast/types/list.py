
#СПИСОК

#realization 1
'''class LinkedList():
    def __init__(self, car, cdr):
        self.value = car
        self.next = cdr


def cons(value, next):
    return LinkedList(value, next)

def head(ls):
    return ls.value 

def cdr(ls):
    return ls.next

def is_cons_list(value):
    return type(value) is LinkedList

'''

#realization 2
'''
def cons(value, next):
    return (value, next)

def head(ls):
    return ls[0] 

def cdr(ls):
    return ls[1]

def is_cons_list(value):
    return type(value) is tuple

'''

#realization 3
def cons(value, next):
    return lambda f : f(value, next)

def head(ls):
    return ls(lambda value, next : value)

def cdr(ls):
    return ls(lambda value, next : next)

def is_cons_list(value):
    return callable(value)




#######################################

nil = cons(None, None)
def is_nil(value):
    return value == nil
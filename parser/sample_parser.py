import re
from own_ast.types.symbol import *
from own_ast.types.list import *
from parser.commands import *

def parse_list(text):
    text = strip_trash_left(text)
    if text == "":
        raise ValueError("command can't be empty")

    f = text[0]

    if f == ")":
        return nil, text[1:]
    else:
        value, reminder = parser(text)
        reminder_a, reminder_b = parse_list(reminder)
        return cons(value, reminder_a), reminder_b

def strip_trash_left(text):
    while len(text) > 0:
        if text[0] in ", \n\r\t":
            text = text[1:]
        elif text[0] == ";":
            s = text.find("\n")
            if s == -1:
                return ""
            text = text[s:]
        else:
            return text

    return text

def parse_token(text):
    if text == "true":
        return True
    elif text == "false":
        return False
    try:
        num = int(text)
        return num
    except Exception:
        try:
            return float(text)
        except:
            return symbol(text)

def parser(text):
    #print("parser", text)
    text = strip_trash_left(text)

    if text == "":
        return None, ""
    
    f = text[0]

    if f == '"':
        s = text[1:].find('"')+1
        if s == 0:
            raise ValueError("no ended comma in -> " + s)
        return text[:s + 1][1:-1], text[s + 1:]
    
    elif f == "(":
        return parse_list(text[1:])
    elif f == ")":
        raise ValueError("no open closure '(' in text")
    else:
        i = re.search(r"[, \n\r$\t\"();]|$", text).start()
        return parse_token(text[:i]), text[i:]

def eval_text(text):
    text = strip_trash_left(text)
    while text:
        x, text = parser(text)
        print(show(x))
        text = strip_trash_left(text)
    

def eval_cmd(cmd):
    args = cmd.split()
    if args[0] == "l":
        try:
            with open(args[1], 'r', encoding="utf-8") as file:
                eval_text(file.read())
        except FileNotFoundError:
            print("no such file")
        
def RPL():
    while True:
        print(">> ", end = "")
        try:
            cmd = input()
            if cmd and cmd[0] == ":":
                eval_cmd(cmd[1:])
            else:
                eval_text(cmd)
        except Exception as e:
            print(e)
        

RPL()
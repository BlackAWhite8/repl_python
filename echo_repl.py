import typing
from parser.sample_parser import Parser
def echo_repl() -> None:
    parser = Parser()
    while True:
        print(">>", end="")
        command = input().strip()
        result = parser.main_parser(command)
        print(result)

if __name__ == "__main__":
    echo_repl()

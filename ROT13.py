import sys
import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

def main(argv: list[str]):
    if len(argv) < 2:
        PrintHelp()
        return

    print(Rot13(argv[1]))

def Rot13(s: str) -> str:
    outputString: str = str()
    alphabet: list[str]

    for char in s:
        if lowercase.__contains__(char):
            alphabet = lowercase
        elif uppercase.__contains__(char):
            alphabet = uppercase
        else:
            outputString += char
            continue

        pos: int = alphabet.index(char) + 13
        if pos > 25:
            pos -= 26

        outputString += alphabet[pos]

    return outputString

def PrintHelp():
    print("Provide an input string as an argument.")

if __name__ == "__main__":
    main(sys.argv)
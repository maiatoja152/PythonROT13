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
    isLowercase: bool = bool()

    for char in s:
        if lowercase.__contains__(char):
            isLowercase = True
        elif uppercase.__contains__(char):
            isLowercase = False
        else:
            outputString += char
            continue

        outputString += RotateLetter(char, isLowercase)

    return outputString

def RotateLetter(char: str, isLowercase: bool) -> str:
    alphabet: list[str] = lowercase if isLowercase else uppercase
    pos: int = alphabet.index(char) + 13
    if pos > 25:
        pos -= 26
    
    print(len(alphabet))
    return alphabet[pos]

def PrintHelp():
    print("Provide an input string as an argument.")

if __name__ == "__main__":
    main(sys.argv)
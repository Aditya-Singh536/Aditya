import AsciiToCharacters as atc

if __name__ == '__main__':
    start = input("Give starting Ascii number SC: ")
    print(type(start))
    end = input("Give ending Ascii number SC: ") 
    atc.printCharactersForGivenAsciiRange(start, end)
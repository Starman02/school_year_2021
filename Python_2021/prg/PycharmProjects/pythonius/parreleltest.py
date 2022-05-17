def main():
    nato = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo', 'lima', 'mike', 'november', 'oscar', 'papa', 'quebec', 'romeo', 'sieera', 'tango', 'uniform', 'victor', 'whiskey', 'xray', 'yankee', 'zulu']
    standard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j',"k",'l','m','n','o','p','q','r','s','t','u',"v",'w','x','y','z']
    phrase = input()
    nata_final = ""
    for letter in phrase:
        print(letter, "letter")
        for item in range(0,len(standard)):
            if letter == standard[item]:
                print(item, "shaboing")
                nata_final += nato[item]

    print(nata_final)



main()
